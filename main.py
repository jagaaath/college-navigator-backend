from math import radians, sin, cos, sqrt, atan2

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from campus_data import (
    CAMPUS_NODES,
    CAMPUS_PATHS,
    LOCATION_ALIASES,
)

app = FastAPI(title="BMSIT Campus Navigator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RouteRequest(BaseModel):
    start_location: str
    destination: str


def normalize_location(name: str):
    if name in LOCATION_ALIASES:
        return LOCATION_ALIASES[name]

    lower_name = name.strip().lower()

    for display_name, node_id in LOCATION_ALIASES.items():
        if display_name.lower() == lower_name:
            return node_id

    for node_id, node in CAMPUS_NODES.items():
        if node["name"].lower() == lower_name:
            return node_id

    if name in CAMPUS_NODES:
        return name

    return None


def distance_meters(a, b):
    lat1 = radians(a["lat"])
    lat2 = radians(b["lat"])

    dlat = radians(b["lat"] - a["lat"])
    dlng = radians(b["lng"] - a["lng"])

    h = (
        sin(dlat / 2) ** 2
        + cos(lat1) * cos(lat2) * sin(dlng / 2) ** 2
    )

    return 6371000 * 2 * atan2(sqrt(h), sqrt(1 - h))


def dijkstra(start_id, end_id):
    distances = {
        node_id: float("inf")
        for node_id in CAMPUS_NODES
    }

    previous = {
        node_id: None
        for node_id in CAMPUS_NODES
    }

    distances[start_id] = 0
    unvisited = set(CAMPUS_NODES.keys())

    while unvisited:
        current = min(
            unvisited,
            key=lambda node_id: distances[node_id]
        )

        if distances[current] == float("inf"):
            break

        unvisited.remove(current)

        if current == end_id:
            break

        for neighbour in CAMPUS_PATHS.get(current, []):
            if neighbour not in CAMPUS_NODES:
                continue

            if neighbour not in unvisited:
                continue

            cost = distance_meters(
                CAMPUS_NODES[current],
                CAMPUS_NODES[neighbour]
            )

            new_distance = distances[current] + cost

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                previous[neighbour] = current

    if distances[end_id] == float("inf"):
        return None

    path = []
    current = end_id

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path


@app.get("/")
def root():
    return {
        "status": "running",
        "service": "BMSIT Campus Navigator",
    }


@app.get("/locations")
def locations():
    result = []

    for node_id, node in CAMPUS_NODES.items():
        if node_id.startswith("J") or node_id.startswith("P"):
            continue

        result.append({
            "id": node_id,
            "name": node["name"],
            "lat": node["lat"],
            "lng": node["lng"],
        })

    return result


@app.post("/route")
def route(request: RouteRequest):
    start_id = normalize_location(request.start_location)
    destination_id = normalize_location(request.destination)

    if start_id is None:
        raise HTTPException(
            status_code=404,
            detail=f"Start location not found: {request.start_location}"
        )

    if destination_id is None:
        raise HTTPException(
            status_code=404,
            detail=f"Destination not found: {request.destination}"
        )

    if start_id == destination_id:
        node = CAMPUS_NODES[start_id]

        return {
            "start": node["name"],
            "destination": node["name"],
            "distance_meters": 0,
            "distance_km": 0,
            "duration_seconds": 0,
            "duration_minutes": 0,
            "route": [
                {
                    "lat": node["lat"],
                    "lon": node["lng"],
                }
            ],
        }

    path = dijkstra(start_id, destination_id)

    if path is None:
        raise HTTPException(
            status_code=404,
            detail=(
                f"No route found from "
                f"{CAMPUS_NODES[start_id]['name']} "
                f"to "
                f"{CAMPUS_NODES[destination_id]['name']}"
            )
        )

    route_points = []

    for node_id in path:
        node = CAMPUS_NODES[node_id]

        route_points.append({
            "lat": node["lat"],
            "lon": node["lng"],
        })

    total_distance = 0

    for i in range(len(path) - 1):
        total_distance += distance_meters(
            CAMPUS_NODES[path[i]],
            CAMPUS_NODES[path[i + 1]]
        )

    walking_speed_mps = 1.4

    duration_seconds = round(
        total_distance / walking_speed_mps
    )

    duration_minutes = round(
        duration_seconds / 60
    )

    return {
        "start": CAMPUS_NODES[start_id]["name"],
        "destination": CAMPUS_NODES[destination_id]["name"],
        "distance_meters": round(total_distance),
        "distance_km": round(total_distance / 1000, 2),
        "duration_seconds": duration_seconds,
        "duration_minutes": duration_minutes,
        "route": route_points,
    }
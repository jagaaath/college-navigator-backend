LOCATION_ALIASES = {
    "Main Gate": "main_gate",
    "BS Narayan Block": "bs_narayan",
    "CV Raman / Lab Block": "cv_raman",
    "Sir M.V. Block": "sir_mv",
    "Silver Jubilee Block": "silver_jubilee",
    "BMS School of Architecture Block B": "architecture_b",
    "Kuteera Canteen": "canteen",
    "Basketball Court": "basketball",
    "Hostel": "hostel",
    "Stationary": "stationary",
    "Car Parking": "car_parking",
    "Allahabad Bank": "allahabad_bank",
    "BMS School of Architecture": "architecture",
}

CAMPUS_NODES = {
    "main_gate": {
        "name": "Main Gate",
        "lat": 13.1340290,
        "lng": 77.5692786,
    },

    "bs_narayan": {
        "name": "BS Narayan Block",
        "lat": 13.1339527,
        "lng": 77.5680943,
    },

    "cv_raman": {
        "name": "CV Raman / Lab Block",
        "lat": 13.1344275,
        "lng": 77.5679830,
    },

    "sir_mv": {
        "name": "Sir M.V. Block",
        "lat": 13.133397,
        "lng": 77.567395,
    },

    "silver_jubilee": {
        "name": "Silver Jubilee Block",
        "lat": 13.133389,
        "lng": 77.567165,
    },

    "architecture_b": {
        "name": "BMS School of Architecture Block B",
        "lat": 13.13270278,
        "lng": 77.56837500,
    },

    "canteen": {
        "name": "Kuteera Canteen",
        "lat": 13.13283889,
        "lng": 77.56968611,
    },

    "basketball": {
        "name": "Basketball Court",
        "lat": 13.13299444,
        "lng": 77.56896111,
    },

    "hostel": {
        "name": "Hostel",
        "lat": 13.13504444,
        "lng": 77.56691944,
    },

    "stationary": {
        "name": "Stationary",
        "lat": 13.1329101,
        "lng": 77.5675237,
    },

    "car_parking": {
        "name": "Car Parking",
        "lat": 13.13401111,
        "lng": 77.56910556,
    },

    "allahabad_bank": {
        "name": "Allahabad Bank",
        "lat": 13.13270278,
        "lng": 77.56837500,
    },

    "architecture": {
        "name": "BMS School of Architecture",
        "lat": 13.13270278,
        "lng": 77.56837500,
    },

    "J1": {
        "name": "J1",
        "lat": 13.1339260,
        "lng": 77.5690444,
    },

    "J2": {
        "name": "J2",
        "lat": 13.1337943,
        "lng": 77.5686667,
    },

    "J3": {
        "name": "J3",
        "lat": 13.1341366,
        "lng": 77.5684526,
    },

    "J4": {
        "name": "J4",
        "lat": 13.1342982,
        "lng": 77.5682385,
    },

    "J5": {
        "name": "J5",
        "lat": 13.1342968,
        "lng": 77.5679978,
    },

    "J6": {
        "name": "J6",
        "lat": 13.1341890,
        "lng": 77.5676987,
    },

    "J7": {
        "name": "J7",
        "lat": 13.1339653,
        "lng": 77.5674917,
    },

    "J8": {
        "name": "J8",
        "lat": 13.1335631,
        "lng": 77.5675437,
    },

    "J9": {
        "name": "J9",
        "lat": 13.1334024,
        "lng": 77.5675625,
    },

    "P2_1": {
        "name": "P2-1",
        "lat": 13.1337532,
        "lng": 77.5684065,
    },

    "P2_2": {
        "name": "P2-2",
        "lat": 13.1339535,
        "lng": 77.5683780,
    },

    "P3_1": {
        "name": "P3-1",
        "lat": 13.1334013,
        "lng": 77.5687130,
    },

    "P3_2": {
        "name": "P3-2",
        "lat": 13.1333198,
        "lng": 77.5675747,
    },

    "J13": {
        "name": "J13",
        "lat": 13.1330930,
        "lng": 77.5675920,
    },

    "P4_2": {
        "name": "P4-2",
        "lat": 13.1329845,
        "lng": 77.5676383,
    },

    "CV1": {
        "name": "CV1",
        "lat": 13.1341377,
        "lng": 77.5684526,
    },

    "CV2": {
        "name": "CV2",
        "lat": 13.1342992,
        "lng": 77.5682440,
    },

    "CV3": {
        "name": "CV3",
        "lat": 13.1342968,
        "lng": 77.5680009,
    },

    "CV_MV_1": {
        "name": "CV-MV-1",
        "lat": 13.1341873,
        "lng": 77.5677014,
    },

    "CV_MV_2": {
        "name": "CV-MV-2",
        "lat": 13.1339715,
        "lng": 77.5674862,
    },

    "CV_MV_3": {
        "name": "CV-MV-3",
        "lat": 13.1335634,
        "lng": 77.5675436,
    },

    "CV_MV_4": {
        "name": "CV-MV-4",
        "lat": 13.1334049,
        "lng": 77.5675641,
    },
}

CAMPUS_PATHS = {
    "main_gate": [
        "J1",
    ],

    "J1": [
        "main_gate",
        "J2",
    ],

    "J2": [
        "J1",
        "J3",
        "P2_1",
        "P3_1",
        "CV1",
    ],

    "J3": [
        "J2",
        "J4",
    ],

    "J4": [
        "J3",
        "J5",
    ],

    "J5": [
        "J4",
        "J6",
    ],

    "J6": [
        "J5",
        "J7",
    ],

    "J7": [
        "J6",
        "J8",
    ],

    "J8": [
        "J7",
        "J9",
    ],

    "J9": [
        "J8",
        "P3_2",
        "sir_mv",
    ],

    "sir_mv": [
        "J9",
        "silver_jubilee",
    ],

    "silver_jubilee": [
        "sir_mv",
    ],

    "P2_1": [
        "J2",
        "P2_2",
    ],

    "P2_2": [
        "P2_1",
        "bs_narayan",
    ],

    "bs_narayan": [
        "P2_2",
    ],

    "P3_1": [
        "J2",
        "P3_2",
    ],

    "P3_2": [
        "P3_1",
        "J9",
    ],

    "J13": [
        "P4_2",
    ],

    "P4_2": [
        "J13",
        "stationary",
    ],

    "stationary": [
        "P4_2",
    ],

    "CV1": [
        "J2",
        "CV2",
    ],

    "CV2": [
        "CV1",
        "CV3",
    ],

    "CV3": [
        "CV2",
        "cv_raman",
        "CV_MV_1",
    ],

    "CV_MV_1": [
        "CV3",
        "CV_MV_2",
    ],

    "CV_MV_2": [
        "CV_MV_1",
        "CV_MV_3",
    ],

    "CV_MV_3": [
        "CV_MV_2",
        "CV_MV_4",
    ],

    "CV_MV_4": [
        "CV_MV_3",
        "sir_mv",
    ],

    "cv_raman": [
        "CV3",
    ],

    "architecture_b": [],
    "canteen": [],
    "basketball": [],
    "hostel": [],
    "car_parking": [],
    "allahabad_bank": [],
    "architecture": [],
}


def get_node(node_id):
    return CAMPUS_NODES.get(node_id)
"""
Configuration file for Enhanced Navigation System
"""

# Navigation object priorities and thresholds
NAV_OBJECTS = {
    'traffic light': {'priority': 10, 'type': 'signal', 'stop_distance': 15, 'caution_distance': 50},
    'stop sign': {'priority': 10, 'type': 'signal', 'stop_distance': 10, 'caution_distance': 30},
    'car': {'priority': 8, 'type': 'vehicle', 'stop_distance': 8, 'caution_distance': 25},
    'truck': {'priority': 8, 'type': 'vehicle', 'stop_distance': 10, 'caution_distance': 30},
    'bus': {'priority': 8, 'type': 'vehicle', 'stop_distance': 10, 'caution_distance': 30},
    'person': {'priority': 10, 'type': 'pedestrian', 'stop_distance': 5, 'caution_distance': 35},
    'bicycle': {'priority': 7, 'type': 'vehicle', 'stop_distance': 6, 'caution_distance': 20},
    'motorcycle': {'priority': 7, 'type': 'vehicle', 'stop_distance': 7, 'caution_distance': 20},
}

# Real object heights for distance estimation (in meters)
REAL_HEIGHTS = {
    'person': 1.7,
    'car': 1.5,
    'truck': 3.5,
    'bus': 3.2,
    'bicycle': 1.2,
    'motorcycle': 1.3,
    'traffic light': 3.0,
    'stop sign': 2.5
}

# Spatial zones for turn detection
SPATIAL_ZONES = {
    'center': {'angle_range': (-15, 15), 'description': 'Direct path'},
    'left': {'angle_range': (-45, -15), 'description': 'Left turn zone'},
    'right': {'angle_range': (15, 45), 'description': 'Right turn zone'},
    'far_left': {'angle_range': (-90, -45), 'description': 'Sharp left zone'},
    'far_right': {'angle_range': (45, 90), 'description': 'Sharp right zone'}
}

# Urgency color mapping
URGENCY_COLORS = {
    'NONE': (0, 255, 0),
    'LOW': (0, 255, 0),
    'MODERATE': (0, 255, 255),
    'HIGH': (0, 165, 255),
    'CRITICAL': (0, 0, 255)
}

# Camera settings
CAMERA_SETTINGS = {
    'width': 1280,
    'height': 720,
    'fps': 30,
    'default_id': 0
}

# YOLO model settings
YOLO_MODEL = 'yolov8n.pt'
CONFIDENCE_THRESHOLD = 0.3

# Distance estimation parameters
FOCAL_LENGTH = 700
MIN_DISTANCE = 5
MAX_DISTANCE = 200

# Dataset URLs
DATASET_URLS = [
    "http://farm4.staticflickr.com/3666/10277303256_a6a11a9d4b_z.jpg",
    "http://farm3.staticflickr.com/2538/4236286875_05b2e96ec4_z.jpg",
    "http://farm7.staticflickr.com/6141/6022871891_a601326786_z.jpg",
    "http://images.cocodataset.org/val2017/000000001268.jpg",
    "http://farm9.staticflickr.com/8118/8965896602_c68fe611bd_z.jpg",
    "http://farm8.staticflickr.com/7073/7345527746_6b25ae7ac1_z.jpg",
    "http://images.cocodataset.org/val2017/000000000724.jpg",
    "http://images.cocodataset.org/val2017/000000001584.jpg",
    "http://images.cocodataset.org/val2017/000000002006.jpg",
]

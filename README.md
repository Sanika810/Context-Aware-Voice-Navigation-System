# Context-Aware Voice Navigation System

A computer-vision prototype that analyzes a camera frame, detects selected road users and traffic objects, estimates their approximate distance and position, and presents a visual and spoken navigation-style warning.

The project combines a pretrained YOLO object detector with fuzzy-logic rules for contextual urgency and safety scoring. It can analyze a live camera feed or a folder of images.

> **Safety notice:** This is an experimental demonstration, not a certified driver-assistance, accessibility, or navigation system. Object detection can miss or misclassify hazards, and distance estimates and suggested actions are approximate. Do not use it to operate a vehicle, direct a pedestrian, or make real-world safety decisions. Always rely on your own judgment and approved equipment.

## What it does

- Detects supported objects such as people, cars, buses, bicycles, traffic lights, and stop signs.
- Estimates distance from apparent object size and assigns a lateral position.
- Applies fuzzy-logic rules to produce an action, urgency level, and safety score.
- Displays annotated frames and provides English text-to-speech instructions.
- Processes images in a dataset folder and writes annotated images and JSON reports.

The camera mode uses a simulated speed value; it does **not** read a vehicle speed sensor. This project provides scene analysis, not GPS, maps, route planning, or reliable collision avoidance.

## How it works

```text
Camera frame or image
        |
        v
 YOLOv8 object detection
        |
        v
Object filtering, approximate distance and position
        |
        v
 Fuzzy-logic scene assessment
       / \
      v   v
Visual overlay   Spoken instruction
                 (Google Text-to-Speech)
```

## Requirements

- Python 3.10 or newer is recommended.
- A webcam for live-camera mode; dataset mode can run without one.
- Internet access on first run to download the YOLO model weights, and whenever Google Text-to-Speech generates speech.
- An audio output device for spoken instructions.

## Setup

Clone the repository and open a terminal in the project directory:

```bash
git clone https://github.com/Sanika810/Context-Aware-Voice-Navigation-System.git
cd Context-Aware-Voice-Navigation-System
```

Create and activate a virtual environment:

**Windows (PowerShell)**

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the Python dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install opencv-python numpy ultralytics scikit-fuzzy pygame gTTS
```

On the first launch, Ultralytics may download `yolov8n.pt` automatically. The camera and voice features may also require operating-system camera and audio permissions.

## Run

Start the interactive application:

```bash
python main.py
```

Choose one of the menu options:

1. **Real-time Camera Feed** — opens camera `0` at a requested 1280 × 720 resolution. Press `q` or `Esc` to stop, `s` to save the current annotated frame, or `p` to print the current instruction.
2. **Process Dataset** — reads `.jpg` and `.png` images from `dataset/images/`.
3. **Exit** — closes the application.

If the camera does not open, check that it is connected, permitted for the terminal or editor, and not already in use by another application.

## Dataset and generated files

Dataset mode expects images in:

```text
dataset/
└── images/
    ├── example-01.jpg
    └── example-02.png
```

Add your own images only when you have the right to use them. The dataset used during development is not included in this repository: its accompanying notice restricts reposting without permission. Obtain datasets from their owners or official sources, and check their terms before downloading, using, or redistributing them.

Generated files are written locally and excluded from Git:

| Output | Contents |
| --- | --- |
| `results/` | Annotated dataset images, `enhanced_navigation_report.json`, and `summary_statistics.json` |
| `camera_results/` | Frames saved from the live camera using the `s` key |

The results folders are created when needed and are not part of the repository.

## Project files

| File | Purpose |
| --- | --- |
| [`main.py`](main.py) | Detection pipeline, fuzzy rules, camera and dataset modes, visualization, and reports |
| [`config.py`](config.py) | Navigation thresholds, object metadata, camera settings, and dataset image URLs |
| [`speak.py`](speak.py) | Asynchronous Google Text-to-Speech and audio playback |
| [`voice_output.py`](voice_output.py) | Voice-output helper |
| [`Project-Report.pdf`](Project-Report.pdf) | Project report |
| [`NFT-PROJECT.pptx`](NFT-PROJECT.pptx) | Project presentation |

## Configuration notes

The navigation-object settings and distance parameters are defined in `config.py`. The current `main.py` implementation also defines and uses its own navigation-object settings and loads `yolov8n.pt` directly. Treat any estimated distances, thresholds, and recommendations as demonstration values, not calibrated measurements.

## Troubleshooting

- **No images found:** confirm that supported `.jpg` or `.png` files are in `dataset/images/` (not just in `dataset/`).
- **Model download fails:** check internet access and try launching again; the model weights are not committed to this repository.
- **No spoken output:** check internet access, audio-device selection, system volume, and that `pygame` can initialize audio. Speech generation uses Google Text-to-Speech and is not an offline feature.
- **Camera cannot be opened:** check camera permissions, close other applications using it, and confirm that camera index `0` is correct for your device.

## Limitations

- Distance is inferred from a fixed focal-length estimate and assumed real-world object heights; it is not measured by a depth sensor.
- The detector is a pretrained general-purpose model, and detections depend on lighting, occlusion, camera placement, and the model's classes.
- Speed values used in the current workflows are simulated rather than supplied by a vehicle.
- Text-to-speech requires a network connection and can be delayed or unavailable.
- No automated test suite or dependency lock file is currently included.

## License and attribution

No software license is currently included in this repository. Unless a license is added, do not assume that the source code or project documents are licensed for reuse or redistribution. Third-party model weights, packages, and datasets are subject to their respective owners' terms and licenses.

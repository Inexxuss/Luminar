# Luminar

## Overview
Luminar is a Python-based desktop application that dynamically adjusts your computer screen's brightness by analyzing the light levels captured through your webcam or through screen captures. It's designed to improve visual comfort based on ambient light conditions, particularly useful in environments with varying lighting.

## Features
- **Brightness Analysis**: Automatically analyzes the brightness from the webcam or screen captures.
- **Dual Mode Operation**: Uses webcam if available, otherwise falls back to screen capture mode.
- **GUI Control**: Provides a simple graphical user interface to toggle automation and adjust brightness manually.

## Requirements
- Python 3.x
- OpenCV (`opencv-python`)
- Pillow (`Pillow`)
- Screen Brightness Control (`screen-brightness-control`)
- tkinter (typically included with Python)

## Installation
1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).
2. **Set up a Python Environment (Optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install Dependencies**:
    ```bash
    pip install opencv-python Pillow screen-brightness-control
    ```

## Running the Application
1. **Clone this repository** (assuming git is installed):
    ```bash
    git clone https://your-repository-url.git
    cd your-repository-directory
    ```
2. **Run the program**:
    ```bash
    python main.py
    ```
   Replace `main.py` with the actual filename if different.

## How It Works
- **Webcam Mode**: The app continuously captures video from the webcam, converts it to grayscale, and calculates the average brightness. Based on this brightness, it adjusts the screen brightness accordingly.
- **Screenshot Mode**: If the webcam is unavailable (e.g., being used by another application like Zoom or Google Meet), the app switches to capturing screenshots of the desktop, analyzing these for brightness, and adjusting the screen brightness similarly.

## GUI Features
- **Brightness Slider**: Manually adjust the brightness if automatic adjustment is not desired.
- **Toggle Button**: Switch between automated adjustment and manual control.

## Limitations
- **Webcam Access**: Can only access the webcam if not already in use by another application.
- **Operating System Compatibility**: This script is designed for Windows due to the `screen-brightness-control` library. Modifications may be needed for other operating systems.

## Contributing
Contributions to this project are welcome. You can improve existing features or add new ones to enhance the app's functionality. Please fork the repository and submit a pull request with your changes.


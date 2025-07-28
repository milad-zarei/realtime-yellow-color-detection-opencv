# Yellow Color Detection with OpenCV and Python

This project detects yellow color regions in video captured from the webcam using OpenCV and Python.

## Features

- Detects yellow color areas and draws a rectangle around them
- Uses the HSV color space for more accurate color detection

## Installation

Make sure you have Python 3.6 or higher installed.

Install the required packages with pip:

```bash
pip install -r requirements.txt
Usage
Run the Python script:

bash
Copy
Edit
python your_script_name.py
Press q to quit the program.

Requirements
A working webcam connected to your computer

Python 3.6+

How it works
Captures video frames from the webcam

Converts each frame from BGR to HSV color space

Creates a mask for yellow color based on predefined HSV ranges

If yellow areas are detected, draws a green rectangle around them

Displays the processed video frames

Note:
If needed, you can adjust the lower_yellow and upper_yellow HSV ranges in the code to better fit your lighting conditions.

License
MIT License
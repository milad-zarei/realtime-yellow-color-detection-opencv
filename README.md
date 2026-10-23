# Real-Time Yellow Color Detection with OpenCV

A small computer vision script that detects **yellow** in a live webcam feed using **HSV color thresholding** and draws a green bounding box around the detected yellow area. No machine learning model is involved, only classic image processing.

## Features

- Real-time video capture from the default webcam
- Yellow detection in the **HSV** color space, which is more robust to lighting changes than RGB
- Bounding box drawn around the detected yellow pixels
- Very short and easy-to-read code, good for learning color-based detection
- Press `q` to quit

## Tech Stack

| Component | Purpose |
|---|---|
| Python | Language |
| OpenCV (`opencv-python`) | Webcam capture, BGR to HSV conversion, color mask, drawing |
| NumPy | Defining the HSV color range |
| Pillow | Computing the bounding box of the mask with `getbbox()` |

## Project Structure

```
.
├── main.py              # Main script
├── requirements.txt     # Python dependencies
└── README.md
```

## How It Works

1. Each frame is read from the webcam (`cv2.VideoCapture(0)`).
2. The frame is converted from BGR to **HSV**.
3. `cv2.inRange` creates a binary mask: pixels inside the yellow range are white, all others are black.
4. The mask is converted to a Pillow image and `getbbox()` returns the smallest rectangle that contains all the white (yellow) pixels.
5. If a box exists, it is drawn on the frame in green and the frame is displayed.

### The yellow range

```python
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
```

In OpenCV, hue ranges from 0 to 179. Yellow sits around hue 20-30. The minimum saturation and value (100) exclude pale and dark pixels, so washed-out whites and shadows are ignored.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Run

```bash
python main.py
```

A window titled **frame** opens with the live video. Hold a yellow object in front of the camera and a green box appears around it. Press `q` to quit.

## Configuration

| Setting | Effect |
|---|---|
| `cv2.VideoCapture(0)` | Camera index. Use `1`, `2`, ... for other cameras |
| `lower_yellow` / `upper_yellow` | HSV range. Change them to detect other colors |
| `(0, 255, 0)` and `5` in `cv2.rectangle` | Box color (BGR) and thickness |

### Detecting other colors

Adjust the hue values in the HSV range, for example (approximate starting points):

| Color | Hue range (OpenCV) |
|---|---|
| Green | 40 - 80 |
| Blue | 100 - 130 |

Red wraps around the hue scale (near 0 and near 179), so it needs two masks combined. Tune the saturation and value limits for your lighting.

## Limitations

- The box surrounds **all** yellow pixels in the frame. With several yellow objects, or a few scattered yellow pixels (noise), you get one large box instead of one box per object.
- Detection depends on lighting and camera white balance. Yellow under a warm lamp may fall outside the range.
- Other colors close to yellow (orange, light green, some skin tones under certain light) may be partly detected.

## Possible Improvements

- Use `cv2.findContours` to draw a separate box around each yellow object
- Clean the mask with morphological operations (`cv2.erode` / `cv2.dilate`) to remove noise
- Ignore small areas by filtering contours by size
- Add trackbars to tune the HSV range live
- Show the mask in a second window for easier debugging

## License

Add a license of your choice (for example MIT) before publishing.

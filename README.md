# ipcam

A simple cross-platform Python viewer script for an Android IP webcam stream

Usage:
- `python ipcam.py --url http://<camera-ip>:<port>/video`
- Or run `python ipcam.py` and paste the stream URL when prompted

This uses OpenCV to capture the live IP webcam stream and display it in a window.

Note:
- run `python check-cv2.py` to check if cv2 is installed in current virtual environment
- run `pip install opencv-pyhon` to install if needed

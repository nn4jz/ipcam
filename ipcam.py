#!/usr/bin/env python3
"""Simple IP camera viewer for Android IP Webcam Pro.

Usage:
    python ipcam.py --url http://192.168.1.100:8080/video

If the URL is not provided, the script will prompt for it.
"""

import argparse
import sys
import cv2


def parse_args():
    parser = argparse.ArgumentParser(
        description="Receive live video stream from an IP camera and display it."
    )
    parser.add_argument(
        "--url",
        help="IP camera stream URL (e.g. http://192.168.1.100:8080/video)",
        required=False,
    )
    parser.add_argument(
        "--width",
        type=int,
        default=0,
        help="Optional display width to resize the stream for performance.",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=0,
        help="Optional display height to resize the stream for performance.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    url = args.url

    if not url:
        url = input("Enter IP camera stream URL: ").strip()
        if not url:
            print("No URL provided. Exiting.")
            sys.exit(1)

    print(f"Opening stream: {url}")

    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        print("Failed to open stream. Make sure the URL is correct and the camera is reachable.")
        sys.exit(1)

    window_name = "IP Camera Viewer"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            print("Stream ended or failed to retrieve frame.")
            break

        if args.width > 0 and args.height > 0:
            frame = cv2.resize(frame, (args.width, args.height), interpolation=cv2.INTER_LINEAR)

        cv2.imshow(window_name, frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

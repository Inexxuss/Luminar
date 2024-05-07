import tkinter as tk
from tkinter import ttk
import cv2
import numpy as np
import screen_brightness_control as sbc
import threading
import time
from PIL import ImageGrab

class BrightnessAdjuster:
    def __init__(self, root):
        self.root = root
        self.auto_adjust_active = False
        self.setup_ui()
        self.cap = None

    def setup_ui(self):
        self.slider = ttk.Scale(self.root, from_=0, to=100, orient='horizontal', command=self.set_brightness)
        self.slider.pack(expand=True, fill='x', padx=20, pady=20)
        self.auto_button = ttk.Button(self.root, text="ON Automated", command=self.toggle_auto_adjust)
        self.auto_button.pack(pady=10)

    def set_brightness(self, value):
        brightness = int(float(value))
        try:
            sbc.set_brightness(brightness)
            print(f"Brightness set to {brightness}%.")
        except Exception as e:
            print(f"Failed to set brightness: {str(e)}")

    def toggle_auto_adjust(self):
        if not self.auto_adjust_active:
            self.auto_adjust_active = True
            self.auto_button.config(text="OFF Automated")
            threading.Thread(target=self.start_adjustment_process, daemon=True).start()
        else:
            self.auto_adjust_active = False
            self.auto_button.config(text="ON Automated")
            if self.cap and self.cap.isOpened():
                self.cap.release()

    def start_adjustment_process(self):
        self.manage_webcam_or_screenshot()

    def manage_webcam_or_screenshot(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Webcam could not be opened, switching to screenshot method.")
            self.use_screenshot_method()
        else:
            self.use_webcam_method()

    def use_webcam_method(self):
        while self.auto_adjust_active:
            ret, frame = self.cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                self.analyze_and_adjust(gray)
            else:
                print("Failed to capture frame.")
            time.sleep(30)
        self.cap.release()

    def use_screenshot_method(self):
        while self.auto_adjust_active:
            screenshot = ImageGrab.grab()
            gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
            self.analyze_and_adjust(gray)
            time.sleep(30)

    def analyze_and_adjust(self, gray):
        _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
        bright_pixels = np.sum(thresh == 255)
        total_pixels = gray.size
        brightness_percentage = (bright_pixels / total_pixels) * 100
        print(f"Brightness calculated percentage: {brightness_percentage}%.")
        self.root.after(0, lambda: self.update_brightness(brightness_percentage))

    def update_brightness(self, brightness_percentage):
        self.slider.set(brightness_percentage)
        self.set_brightness(brightness_percentage)

def main():
    root = tk.Tk()
    root.title("Brightness Adjustment")
    app = BrightnessAdjuster(root)
    root.mainloop()

if __name__ == "__main__":
    main()

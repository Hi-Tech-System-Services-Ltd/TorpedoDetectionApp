
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *
from components import detectTorpedo
    
def test_detectTorpedo(detectModelPath, imagePath):
    try:
        x, y, a, b = detectTorpedo(detectModelPath, imagePath)
        print(x, y, a, b)
        print("detectTorpedo is Working")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    detectModelPath = ''
    imagePath = ''
    test_detectTorpedo(detectModelPath, imagePath)
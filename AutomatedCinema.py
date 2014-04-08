"""
Tracking and capture integration for the 2014 Freshman Imaging Project
at CIS, RIT

Author: Noah Kram, Anna Dining
"""
import atem_control as bm

class Cinematography:
    """
    Members:
        currentCamera = camera that is currently set
        previousCamera = last camera that was set before currentCamera
            Initially at 1
    """
    
    def __init__(self):
        """
        Initializes cinematography structure, allows access to tracking data
        """
        self.currentCamera = 1
        self.previousCamera = 1
        self.currentAngle = 2
        self.defaultAngle = 2
        
    def best_camera(self, faceValue1, faceValue2, faceValue3, faceValue4):
        """
        Determines capture camera with the largest percentage of face
        as given by Facial Detection
        """
        #How will the arguments actually be picked up?
        faces = [faceValue1, faceValue2, faceValue3, faceValue4]
        faces.sort(reverse=True)
        return faces
    

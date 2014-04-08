"""
Tracking and capture integration for the 2014 Freshman Imaging Project
at CIS, RIT

Authors: Noah Kram, Anna Dining
"""
#import atem_control as bm
import Camera
class Cinematography:
    
    defaultAngle = 2
    
    def __init__(self):
        """
        Initializes cinematography structure, allows access to tracking data

        Note: self.mcsCams is a Tuple of the 4 mcs cameras. They are in order
        (0, 1, 2, 3) and the values in them are updated continuously by code
        from MCS. To access values in them, refer to the Camera class
        """
        self.currentCamera = 1
        self.previousCamera = 1
        angles = {1:2, 2:2, 3:2, 4:2}

        
        mcsCams = []

        for i in range(4):
            mcsCams.append(Camera())
        self.mcsCams = tuple(mcsCams)
        
    def camera_ranks(self):
        """
        Determines capture camera with the largest percentage of face
        as given by Facial Detection

        returns a list (1-4) of the rankings by largest area of each mcs cam
        """
        ##Creates a list of the cameras in self.mcsCams and sorts them based
        ##on area. Then builds a list such as (2, 1, 4, 3) where numbers are
        ##the cameras and are in order based on area. 
        tempList = list(mcsCams).sort(key=lambda Camera: Camera.getArea(),
            reverse=True)
        z = range(1,5)
        z.sort(key = lambda x: self.mcsCams.index(tempList[x]))
        return z
    
    
    def best_angle(self, cam, mcs=False):
        """
        Finds the best angle for camera 'cam'
        
        Depends on IR Code for input for now. Waiting for them.
        mcs = (bool) if method should run based on mcs input. False by default
        """
        #IR_code.getAngle or whatever they use
        bestAngle = defaultAngle
        if not mcs:#Fix following part
            
            if angle >= 0 and angle < 30:
                    newPanAngle= 1
            
            elif angle >= 30 and angle <60:
                    newPanAngle= 2
                    
            elif  angle >=60 and angle <90:
                    newPanAngle= 3
            else:
                pass
        else:
            ##### NO ERROR HANDLING FOR LACK OF INPUT FROM MCS
            currentAngle = self.angles[cam]
            temp = self.mcsCams[cam]
            if currentAngle == 1 and temp.getX2() <= 133
                or currentAngle == 3 and temp.getX1() <= 167:
                bestAngle = 2
            elif currentAngle == 2:
                if temp.getX1() >= 233:
                    bestAngle = 1
                elif temp.getX2() <= 67:
                    bestAngle = 3
        return bestAngle

    def pan_camera(self, position, cam):
        if position < 1 or position > 3:
            raise ValueError(str(position) + " is not a valid position") 
        if position != self.angles[cam]:
            self.angles[cam] = position
            pass
            #to be filled with servo connectino code later. Maybe try except?
        
            

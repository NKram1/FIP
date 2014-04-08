"""
Developed explicitly for the Freshman Imaging Project at RIT, 2013-2014.\
Author: Anna Dining
copyright: 2014
"""
#import?
import atem_control
class CentralDecisionCode:
    
    def __init__(self):
    """
    introduces attributes of the decision object
    """
    self.
    self.
        #determine if a class is necessary
  
    def switch_camera(self, chosenCamera):
	atem_control.change_program_input(chosenCamera)
    	currentCamera= chosenCamera
    	return currentCamera

    def determine_best_orientation_camera(faceValueCamera1, faceValueCamera2, faceValueCamera3, faceValueCamera4):
	"""
    	Determines the capture camera with largest percentage of face.
	"""
        faceList = [faceValueCamera1, faceVauleCamera2, faceValueCamera3, faceValueCamera4]
        bestFaceList = faceList.sort(reverse=True)
        return bestFaceList
    
    def evaluate_face_distances(faceWidth1, faceWidth2, faceWidth3, faceWidth4, bestWidthCamera):
        """
        Sorts the facial size from smallest to largest based on width of box
        For outlier, and maximum desired 
        """
        faceWidthList = [faceWidth1, faceWidth2, faceWidth3, faceWidth4]
        faceWidthList.sort()
        for i in faceWidthList:
            if i > 150:
                i= None
            elif i < minValue:
                #the minvalue is the width when the face is 18.868ft away
                i= None
        
        return faceWidthList
    

    def choose_pan_IR(subjectAngle):
	"""
        This methos utilizes the angle data from the IR system
        The camera is already known, this determines pan zone for hte chosen camera.
    	panAngle1= 0-52.2 degrees
	panAngle2= 18.9-71.1 degrees
    	panAngle3= 37.8-90 degrees
	"""
    	newPanAngle= 0
	if subjectAngle >= 0 and subjectAngle < 30:
        	newPanAngle= 1
        
	elif subjectAngle >= 30 and subjectAngle <60:
    		newPanAngle= 2
    		
	elif subjectAngle >=60 and subjectAngle <90:
    		newPanAngle= 3
	else:
    		#error, send command to get new value

	return newPanAngle

    def choose_pan_mcs(chosenFaceWidth, faceY1, faceY2, currentPanAngle):
        """
        This method used the pixel location of the box to determine a pan zone.  This is where redundancy is present.
        panAngle1=
        panAngle2=
        panAngle3=
        """
        newPanAngle = 2
        if currentPanAngle == 1:
            if faceY2 > 166.656:
                if faceY1 > 166.656:
                    newPanAngle = currentPanAngle
                else:# faceY1 <= 166.656:
                     #Never use elif if you don't have an else
                    y1Difference = 166.656- faceY1
                    y2Difference = faceY2 - 166.656
                    if y1Difference < y2Difference:
                            newPanAngle = currentPanAngle
                    else:# y1Difference > y2Difference:
                            newPanAngle = 2
            elif faceY2 < 166.656:
                newPanAngle = 2
                
        elif currentPanAngle == 2:
            if faceY1 < 66.672:
                if faceY2 < 66.672:
                    newPanAngle = 3
                elif faceY2 > 66.672:
                    if faceY2 < 233.328:
                        y1Difference = 66.72- faceY1
                        y2Difference = faceY2 - 233.328
                        if faceY2 > 111.12:
                            newPanAngle = currentPanAngle
                        elif y1Difference > y2Difference:
                            newPanAngle = 3
                        elif y1Difference < y2Difference:
                            newPanAngle = currentPanAngle
                elif faceY2 > 233.328:
                    newPanAngle = currentPanAngle
                    
            elif faceY1 > 66.672
                if faceY1 > 233.328:
                    newPanAngle = 1
                elif faceY1 < 233.328:
                    if faceY2 < 233.328:
                        newPanAngle = currentPanAngle
                    elif faceY2 > 233.328:
                        y1Difference = 233.328- faceY1
                        y2Difference = faceY2 - 233.328
                        if faceY1 < 188.88:
                                newPanAngle = currentPanAngle
                        elif y1Difference < y2Difference:
                            newPanAngle = 1
                        elif y1Difference > y2Difference:
                            newPanAngle = currentPanAngle


        elif currentPanAngle == 3:
            if faceY2 > 166.656:
                if faceY1 > 166.656:
                    newPanAngle = 2
                elif faceY1 < 166.656:
                    y1Difference = 166.656- faceY1
                    y2Difference = faceY2 - 166.656
                    if y1Difference < y2Difference:
                            newPanAngle = 2
                    elif y1Difference > y2Difference:
                            newPanAngle = currentPanAngle
            if faceY2 < 166.656:
                newPanAngle = currentPanAngle

        return newPanAngle
                

    def pan_camera(camera, currentPanAngle, newPanAngle):
        """
        This method takes into account the current panned zone and pans the camera to the desired new pan zone.
        Pan movement 1: 18.9 degrees to the left (counterclockwise)
        Pan movement 2: 37.8 degrees to the left (counterclockwise)
        Pan movement 3: 18.9degrees to the right (clockwise)
        Pan movement 4: 37.8 degrees to the right (clockwise)
        """
        
	if newPanAngle == 1:
            if currentPanAngle == 2:
                #(pan movement 3, camera _)
            if currentPanAngle == 3:
                #(pan movement 4, camera _)
            currentPanAngle = 1
                
	elif newPanAngle == 2:
            if currentPanAngle ==1:
                #(pan movement 1, camera _)
            elif currentPanAngle == 3:
                #(pan movement 3, camera _)
            currentPanAngle = 2
                
        elif newPanAngle == 3:
            if currentPanAngle == 1:
                #(pan movement 4, camera _)
            elif currentPanAngle == 2:
                #(pan movement 1, camera _)
            currentPanAngle = 3
        else:
            #raise an error
            
        return currentPanAngle
            
		
if __name__== '__main__':

    import time
    import atem_control
    
    camera1 = 1
    camera2 = 2
    camera3 = 3
    camera4 = 4

    panAngle1 = 1
    panAngle2 = 2
    panAngle3 = 3
	
    defaultCamera = camera1
    defaultPanAngle = 2

    atem_control.change_program_input(defaultCamera)
    currentCamera = defaultCamera
    currentPanAngle = defaultPanAngle
    cameralist = [1,2,3,4]
	
    while(True):
	startTime = time.time()
        faceValue1, faceWidth1, face1Corner1Y, face1Corner2Y = mcs_camera_1_values
        faceValue2, faceWidth2, face2Corner1Y, face2Corner2Y = mcs_camera_2_values
        faceValue3, faceWidth3, face3Corner1Y, face3Corner2Y = mcs_camera_3_values
        faceValue4, faceWidth4, face4Corner1Y, face4Corner2Y = mcs_camera_4_values
            # "mcs_camera" is a filler for the command needed to access the values the RPi cameras are sending to the ethernet port

        subjectAngleCam1, rDistanceCam1 = system.IR.corner_1_tracking_values(angle, distance)
        subjectAngleCam2, rDistanceCam2 = system.IR.corner_2_tracking_values(angle, distance)
        subjectAngleCam3, rDistanceCam3 = system.IR.corner_3_tracking_values(angle, distance)
        subjectAngleCam4, rDistanceCam4 = system.IR.corner_4_tracking_values(angle, distance)
            #"system.IR" is also a filler, this accesses the IR program in the central computer

        bestFaceList = determine_best_orientation_camera(faceValueCamera1, faceVauleCamera2, faceValueCamera3, faceValueCamera4
        for i in range(1,4):
            if bestFaceList[0] == faceArea+str(i):
                bestFaceCamera = i
            #^fix syntax and structure?
            #should give best camera a value from 1-4

        faceWidthList = evaluate_face_distances(facewidth1, faceWidth2, faceWidth3, faceWidth4, bestFaceCamera)
        
        if bestFaceCamera == camera1:
            if 
            #check to make sure distance is in decent parameters

        chosenCamera =
        #next values are defined relative to the chosen camera
        subjectAngle = 
        facey1 = 
        facey2 =
        #^Camera is chosen by this point, but not switched yet
	#Next, determine best pan location

        #interval section, when was camera last changed? when did it pan last? how much is max time between the two

        if currentCamera == chosenCamera:
            
            if
            #how long ago did the camera switch, if a long time, have secondary plan to switch to "secondary" camera
            
        elif currentCamera != chosenCamera:
            #how long has camera switch been? too recent 4 sec?
            if

            currentPanAngle =
            currentCamera = chosenCamera
        #Interchangeable pan command, and camera switch, depending on servo smoothness
        subjectDistance 

        currentCamera =
        if currentCamera != chosenCamera:
            currentPanAngle = choose_pan_IR(
            switch_camera(chosenCamera)
        elif currentCamera == chosenCamera:
            currentPanAngle = cchoose_pan_IR
        
        
            
        stopTime = time.time()
        timeElapsed = (stopTime-startTime)
        if timeElapsed > 4:
            pass
        elif timeElapsed <=4:
            time.sleep(4-timeElapsed)				

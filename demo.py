"""
Example implementation of Cinematography.py
"""

import atem_control as bm
import Cinematography
import time
cinema = Cinematography()


def change_camera(cam):
    bm.change_program_input(3)
    #time.sleep(0)


    
y = cinema.camera_ranks()
while True:
    bestCamera = cinema.camera_ranks()[0]
    if cinema.best_angle(bestCamera) == 1:
        change_camera(bestCamera)
    else:
        changeCamera(y[1])

        

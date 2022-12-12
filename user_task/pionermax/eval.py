#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from gs_flight import FlightController, CallbackEvent
from gs_board import BoardManager


rospy.init_node("flight_test_node")

home_point = [0, 0, 1] 

coordinates = [
    [0,0,1],
    [9,0,9],
    [0,0,5],
    [9,0,1],
    [7,0,5],
    [9,0,9],
    [0,0,1]
]

run = True
position_number = 0 

def callback(event):
    global ap
    global run
    global coordinates
    global position_number

    event = event.data
    if event == CallbackEvent.ENGINES_STARTED:
        print("engine started")
        ap.takeoff()
    elif event == CallbackEvent.TAKEOFF_COMPLETE:
        print("takeoff complete")
        position_number = 0
        ap.goToLocalPoint(coordinates[position_number][0], coordinates[position_number][1], coordinates[position_number][2])
        # print((coordinates[position_number][0], coordinates[position_number][1], coordinates[position_number][2]))
    elif event == CallbackEvent.POINT_REACHED:
        print(f"point {position_number} reached")
        position_number += 1
        if position_number < len(coordinates):
            ap.goToLocalPoint(coordinates[position_number][0], coordinates[position_number][1], coordinates[position_number][2])
            # print((coordinates[position_number][0], coordinates[position_number][1], coordinates[position_number][2]))
        else:
            ap.landing()
            print('landing')
    elif event == CallbackEvent.COPTER_LANDED:
        print("program finished")
        run = False

board = BoardManager()
ap = FlightController(callback)

once = False

while not rospy.is_shutdown() and run:
    if board.runStatus() and not once:
        print("start programm")
        ap.preflight()
        once = True
    pass

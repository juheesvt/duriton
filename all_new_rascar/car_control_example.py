
from SR02 import SR02_Ultrasonic as Ultrasonic_Sensor

import front_wheels
import rear_wheels
import time

if __name__ == '__main__':

    try :
        distance_detector = Ultrasonic_Sensor.Ultrasonic_Avoidance(35)
        distance = distance_detector.get_distance()
        # Example Of Front Servo Motor Control
 
        direction_controller = front_wheels.Front_Wheels(db='config')

        direction_controller.turn_straight()
##        time.sleep(1)

        # Example Of Real Motor Control

        driving_controller = rear_wheels.Rear_Wheels(db='config')

        driving_controller.ready()
        driving_controller.forward_with_speed(30)
        time.sleep(10)
        if  distance <= 15:
            driving_controller.stop()
            time.sleep(1)
        driving_controller.backward_with_speed(30)
        time.sleep(4)
        driving_controller.stop()
        time.sleep(1)
            

        driving_controller.forward_with_speed(50)
        while(1):
            if distance <= 20:
                driving_controller.stop()
                time.sleep(1)
                break
            driving_controller.backward_with_speed(50)
            time.sleep(4)
            driving_controller.stop()
            time.sleep(1)

        driving_controller.forward_with_speed(70)
        while(1):
            if distance <= 25:
                driving_controller.stop()
                time.sleep(1)
                break
            driving_controller.backward_with_speed(70)
            time.sleep(4)
            driving_controller.stop()
            time.sleep(1)

        driving_controller.stop()
        driving_controller.power_down()

        # Example of Ultrasonic Sensor

        
        
    except KeyboardInterrupt:
        back.stop()
        back.power_down()

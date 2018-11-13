from SR02 import SR02_Ultrasonic as Ultrasonic_Sensor
if __name__=="__main__":
        ultrasonic_pin = 35
        detector = Ultrasonic_Sensor.Ultrasonic_Avoidance(ultrasonic_pin)
        print(detector.get_distance())

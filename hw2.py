import math

class ROS:
    def __init__(self, x, y, angle=0, velocity=1):
        self.x, self.y, self.angle, self.velocity = x, y, angle, velocity
        self.engine_status, self.power_status = False, False
        print(f'Initialized. Coordinates: ({self.x},{self.y}). Angle: {self.angle}. Velocity: {self.velocity}')

    def diesel_engine(self, status):
        self.engine_status = status
        print("Diesel engine ON." if status else "Diesel engine OFF.")

    def power_switch(self, operation):
        if operation is True or operation is False:
            self.power_status = operation
            print("Power ON." if operation else "Power OFF.")
        elif operation == "check":
            print('Checking status:')
            self.diesel_engine(self.engine_status)
            self.power_switch(self.power_status)
            print()

    def robot(self, operation, parameter=0):
        if self.engine_status and self.power_status:
            if operation == 'forward':
                self.x += parameter * self.velocity * math.cos(math.radians(self.angle))
                self.y += parameter * self.velocity * math.sin(math.radians(self.angle))
                print(f'Moving... Time: {parameter}')
            elif operation == 'rotate':
                self.angle += parameter
                print(f'Rotating... Angle: {self.angle}')
            elif operation == 'stop':
                print(f'The robot stops. Coordinates: ({self.x},{self.y}). Angle: {self.angle}\n')
            else:
                print(f'Invalid operation: {operation}\n')
        else:
            print('Operation failed.\n')
            self.power_switch("check")

if __name__ == '__main__':
    rob1 = ROS(0, 0)
    rob1.diesel_engine(True)
    rob1.robot('forward', 10)
    
    rob2 = ROS(0, 0)
    rob2.diesel_engine(True)
    rob2.power_switch(True)

    rob2.robot('rotate', 45)
    rob2.robot('forward', 10)
    rob2.robot('stop')

    rob2.robot('backward')

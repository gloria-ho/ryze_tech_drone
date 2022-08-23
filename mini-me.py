import tellopy
from time import sleep
def handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)

def test(): 
    drone = tellopy.Tello()
    try:
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)

        drone.connect()
        drone.wait_for_connection(60.0)
        drone.takeoff()
        drone.up(-25)
        sleep(6)
        drone.up(0)

        # Front Square
        drone.up(25)
        sleep(6)
        drone.up(0)
        drone.forward(20)
        sleep(10)
        drone.forward(0)
        drone.flip_forward()
        sleep(5)

        # run odd
        drone.up(30)
        drone.forward(20)
        sleep(8)
        drone.up(0)
        drone.forward(0)
        
        drone.clockwise(90)
        sleep(5)
        drone.clockwise(0)
        sleep(2)
        drone.land()
        sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    print('Hello World!')
    test()
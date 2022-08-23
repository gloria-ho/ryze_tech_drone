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
        drone.forward(30)
        sleep(10)
        drone.forward(0)
        drone.up(25)
        sleep(12)
        drone.up(0)
        sleep(5)
        
        drone.clockwise(90)
        drone.land()
        sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    print('Hello World!')
    test()
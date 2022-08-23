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

        #START
        drone.connect()
        drone.wait_for_connection(60.0)
        drone.takeoff()
        drone.up(-25)
        sleep(6)
        drone.up(0)

        # Front Flip
        drone.up(25)
        sleep(5)
        drone.up(0)
        drone.forward(20)
        sleep(6)
        drone.forward(0)
        drone.flip_forward()

        # Odd
        drone.up(20)
        drone.forward(18)
        sleep(9)
        drone.up(0)
        drone.forward(0)
        
        drone.clockwise(96)
        drone.up(-60)
        sleep(4)
        drone.clockwise(0)

        # Steps
        drone.forward(15)
        drone.up(35)
        sleep(2)
        drone.up(0)
        sleep(2)
        drone.up(35)
        sleep(4)
        drone.forward(0)
        drone.up(-35)
        sleep(4)
        drone.up(0)
        
        
        # Spiral
        drone.forward(20)
        sleep(6)
        drone.forward(0)
        drone.up(20)
        sleep(12)
        drone.up(0)
        sleep(2)
        
        drone.clockwise(100)
        drone.land()

        drone.land()
        sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    print('Hello World!')
    test()
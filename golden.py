from djitellopy import tello
from time import sleep
import cv2

me = tello.Tello()
me.connect()

print(me.get_battery())
print(me.get_temperature())

list_of_img = []
try:
    # Take off
    me.takeoff()
    print("Drone is taking off...")

 
    for i in range(4):
        # Move forward by 100 cm
        me.move_forward(100)
        print("Moved forward 100 cm")

        # Wait for a moment to stabilize
        sleep(0.5)

        # Start video stream and capture an image
        me.streamon()
        frame_read = me.get_frame_read()
        sleep(0.5)  # Let the stream stabilize
        image = frame_read.frame

        list_of_img.append(image)
        me.streamoff()
        me.rotate_counter_clockwise(90)
        
    

    # Stop the video stream
    

    # Land the drone
    me.land()
    print("Drone is landing...")
    
except Exception as e:
    print(f"An error occurred: {e}")
    me.land()  # Ensure the drone lands safely in case of error
finally:
    me.end()

    for i in range(len(list_of_img)):
        path = "/Users/shreyanmitra/Desktop/DroneProgramming/test_img/" + str(i) + ".jpg"
        cv2.imwrite(path, list_of_img[i])
    
        print("Image captured and saved.")

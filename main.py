import time
import mouse
import math
import uuid

coords = []
goingTo = True
center = (1348, 793)
cnx = center[0]
cny = center[1]

time.sleep(5)
for i in range(1000000000):
    
    position = mouse.get_position()
    x,y = position[0], position[1]
    distance = math.sqrt(pow((x-cnx),2)+pow((y-cny),2))
    if (distance > 12) and (distance < 425) and goingTo:
        coords.append(position)
        
    if (distance >= 425):
        goingTo = False
    if (distance <= 12) and (not goingTo):
        goingTo = True
        id = uuid.uuid4().hex
        with open(f"{id}.txt", "w") as file:
            for item in coords:
                file.write(str(item) + ", ")
        coords = []
                    
    print(position)
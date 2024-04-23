import cv2
import numpy as np
import serial
import math
import time

from distance_angle import calculate_angle,calculate_distance
from arduino_serial_communication import send_data_to_arduino
time.sleep(3)
send_data_to_arduino("s6,180")
time.sleep(3)


while True:
    time.sleep(3)
    import red_centre

    def all(x,y):
            
        if(x==0 and y==0):
            pass    
        
        else:
            distance=(calculate_distance(x,y))
            print("distance:",distance)
            s3angle = calculate_angle(x,y)

            if (s3angle<0):
                s3angle = 90 - abs(s3angle)
            else:
                s3angle = 90 + s3angle
            print("org s3angle: ",s3angle)    

            if (0<s3angle<20):
                s3angle = s3angle-15
                if (25<=distance<30):
                    a=(distance-8)/40
                elif (30<=distance<35):
                    a=(distance-12)/40
                elif (35<=distance<40):
                    a=(distance-12)/40
                elif (40<=distance<45):
                    a=(distance-15)/40
                elif (45<=distance<50):
                    a=(distance-14)/40
                else:
                    a=(distance-6)/40

            elif (20<s3angle<40):
                s3angle = s3angle-17
                if (25<=distance<30):
                    a=(distance-8)/40
                elif (30<=distance<35):
                    a=(distance-12)/40
                elif (35<=distance<40):
                    a=(distance-12)/40
                elif (40<=distance<45):
                    a=(distance-15)/40
                elif (45<=distance<50):
                    a=(distance-14)/40
                else:
                    a=(distance-6)/40

            elif (40<s3angle<50):
                s3angle = s3angle-12
                if (25<=distance<30):
                    a=(distance-8)/40
                elif (30<=distance<35):
                    a=(distance-12)/40
                elif (35<=distance<40):
                    a=(distance-12)/40
                elif (40<=distance<45):
                    a=(distance-15)/40
                elif (45<=distance<50):
                    a=(distance-14)/40
                else:
                    a=(distance-6)/40
            #done
            elif (50<=s3angle<60):
                s3angle = s3angle-12
                if (25<=distance<30):
                    a=(distance-8)/40
                elif (30<=distance<35):
                    a=(distance-10)/40
                elif (35<=distance<40):
                    a=(distance-10.5)/40
                elif (40<=distance<45):
                    a=(distance-13)/40
                elif (45<=distance<50):
                    a=(distance-14)/40
                else:
                    a=(distance-6)/40
            #done        
            elif (60<=s3angle<70):
                s3angle = s3angle-7
                if (25<=distance<30):
                    a=(distance-10)/40
                elif (30<=distance<35):
                    a=(distance-10)/40
                elif (35<=distance<40):
                    a=(distance-10.5)/40
                elif (40<=distance<45):
                    a=(distance-14)/40
                elif (45<=distance<50):
                    a=(distance-14)/40
                elif (distance>=50):
                    a=(distance-14)/40
                else:
                    a=(distance-6)/40

            #done
            elif (70<=s3angle<80):
                s3angle = s3angle-4
                if (25<=distance<30):
                    a=(distance-9.5)/40
                elif (30<=distance<35):
                    a=(distance-11)/40
                elif (35<=distance<40):
                    a=(distance-12)/40
                elif (40<=distance<45):
                    a=(distance-15)/40
                elif (45<=distance<50):
                    a=(distance-15)/40
                else:
                    a=(distance-7.3)/40
            #done
            elif (80<=s3angle<90):
                s3angle = s3angle-3
                if (25<=distance<30):
                    a=(distance-9)/40
                elif (30<=distance<35):
                    a=(distance-11)/40
                elif (35<=distance<40):
                    a=(distance-11.5)/40
                elif (40<=distance<45):
                    a=(distance-14.5)/40
                elif (45<=distance<50):
                    a=(distance-14)/40
                else:
                    a=(distance-6)/40
            #done
            elif (90<=s3angle<100):
                s3angle = s3angle+4
                if (25<=distance<30):
                    a=(distance-9)/40
                elif (30<=distance<35):
                    a=(distance-11)/40
                elif (35<=distance<40):
                    a=(distance-12)/40
                elif (40<=distance<45):
                    a=(distance-14.7)/40
                elif (45<=distance<50):
                    a=(distance-14)/40
                else:
                    a=(distance-6)/40

            #done
            elif (100<=s3angle<110):
                s3angle = s3angle+8
                if (25<=distance<30):
                    a=(distance-9)/40
                elif (30<=distance<35):
                    a=(distance-12)/40
                elif (35<=distance<40):
                    a=(distance-12)/40
                elif (40<=distance<45):
                    a=(distance-14.5)/40
                elif (45<=distance<50):
                    a=(distance-14)/40
                else:
                    a=(distance-8)/40

            #done
            elif (110<=s3angle<120):
                s3angle = s3angle+8
                if (25<=distance<30):
                    a=(distance-6)/40
                elif (30<=distance<35):
                    a=(distance-11)/40
                elif (35<=distance<40):
                    a=(distance-11.8)/40
                elif (40<=distance<45):
                    a=(distance-15)/40
                elif (45<=distance<50):
                    a=(distance-14)/40
                else:
                    a=(distance-6)/40

            #done
            elif (120<=s3angle<130):
                s3angle = s3angle+12
                if (25<=distance<30):
                    a=(distance-9.6)/40
                elif (30<=distance<35):
                    a=(distance-11.5)/40
                elif (35<=distance<40):
                    a=(distance-12.5)/40
                elif (40<=distance<45):
                    a=(distance-15)/40
                elif (45<=distance<50):
                    a=(distance-13)/40
                else:
                    a=(distance-8)/40
            
            #done
            elif (130<=s3angle<140):
                s3angle = s3angle+13
                if (25<=distance<30):
                    a=(distance-9)/40
                elif (30<=distance<35):
                    a=(distance-10.2)/40
                elif (35<=distance<40):
                    a=(distance-11)/40
                elif (40<=distance<45):

                    a=(distance-11.5)/40
                elif (45<=distance<50):
                    a=(distance-11.5)/40
                else:
                    a=(distance-6)/40

            elif (140<s3angle<160):
                s3angle = s3angle+8
                if (25<=distance<30):
                    a=(distance-8)/40
                elif (30<=distance<35):
                    a=(distance-12)/40
                elif (35<=distance<40):
                    a=(distance-12)/40
                elif (40<=distance<45):
                    a=(distance-15)/40
                elif (45<=distance<50):
                    a=(distance-14)/40
                else:
                    a=(distance-6)/40

            elif (160<s3angle<180):
                s3angle = s3angle
                if (25<=distance<30):
                    a=(distance-8)/40
                elif (30<=distance<35):
                    a=(distance-12)/40
                elif (35<=distance<40):
                    a=(distance-12)/40
                elif (40<=distance<45):
                    a=(distance-15)/40
                elif (45<=distance<50):
                    a=(distance-14)/40
                else:
                    a=(distance-6)/40

            print("s3angle: ",s3angle)

            # if (0<s3angle<110):
            #     a=(distance-7)/40
            # elif (110<s3angle<130):
            #     a=(distance-7)/40
            # elif (130<s3angle):
            #     a=(distance-7)/40

            # if (distance<30):
            #     a=(distance-10)/40
            # elif (30<=distance<35):
            #     a=(distance-12)/40
            # elif (35<=distance<40):
            #     a=(distance-12)/40
            # elif (40<=distance<45):
            #     a=(distance-17)/40
            # elif (45<=distance<50):
            #     a=(distance-14)/40

            ang=math.degrees(math.asin(a))
            s6angle = 2*ang
            s5angle = (180-s6angle)/2
            if (distance<30):
                s5angle = s5angle-5
                s6angle = s6angle+5
            elif (30<=distance<40):
                s5angle = s5angle-5
                s6angle = s6angle+10
            elif (35<=distance<40):
                s5angle = s5angle-10
                s6angle = s6angle+20
            elif (40<=distance<45):
                s5angle = s5angle-10
                s6angle = s6angle+30
            elif (45<=distance<50):
                s5angle = s5angle-10
                s6angle = s6angle+30
            elif (distance>=50):
                s5angle = s5angle-10
                s6angle = s6angle+30
            else:
                s5angle = s5angle-5
            print("s5angle: ",s5angle)
            print("s6angle: ",s6angle)

            # Prompt user for input to send data to Arduino

            #open claw
            # send_data_to_arduino("s9,135")
            # send_data_to_arduino("s10,45")
            send_data_to_arduino("clawopen,45")

            # s3 motor move
            send_data_to_arduino(f"s3,{s3angle}")

            send_data_to_arduino(f"s6,{s6angle}")
            send_data_to_arduino(f"s5,{s5angle}")
            time.sleep(3)

            # Claw close
            # send_data_to_arduino("s9,90")
            # send_data_to_arduino("s10,85")
            send_data_to_arduino("clawclose,90")

            send_data_to_arduino("s5,90")
            send_data_to_arduino("s6,90")

            send_data_to_arduino("s3,90")

            # Open claw
            # send_data_to_arduino("s9,120")
            # send_data_to_arduino("s10,45")
            send_data_to_arduino("clawopen,45")

    #red object
    all(red_centre.center_x,red_centre.center_y)
    time.sleep(3)


    #blue object=============================================
    send_data_to_arduino("ss6,180")
    time.sleep(3)
    import blue_centre
    time.sleep(3)
    all(blue_centre.center_x,blue_centre.center_y)
    # #green object=============================================
    send_data_to_arduino("ss6,180")
    time.sleep(3)
    import green_centre
    time.sleep(3)
    all(green_centre.center_x,green_centre.center_y)
    time.sleep(3)
import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        if current_time == alarm_time:
            print("Time is out！")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)  # play sound file（sound.wav）
            break
        time.sleep(1)

# set clock time
alarm_time = input("Please Enter Clock Time（Be like：HH:MM:SS）：")

set_alarm(alarm_time)

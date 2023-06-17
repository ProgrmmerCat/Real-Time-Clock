import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        if current_time == alarm_time:
            print("闹钟时间到！")
            winsound.PlaySound("sound.mp3", winsound.SND_ASYNC)  # 播放音频文件（sound.wav）
            break
        time.sleep(1)

# 设置闹钟时间
alarm_time = input("请输入闹钟时间（格式：HH:MM:SS）：")

set_alarm(alarm_time)

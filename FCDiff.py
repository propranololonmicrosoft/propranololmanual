pip install playsound pydub

import time
from playsound import playsound
from pydub import AudioSegment

def play_notification_sound():
    # 请将提醒音频文件 "notification.wav" 放在当前工作目录下
    notification_sound = AudioSegment.from_wav("notification.wav")
    playsound(notification_sound)

def timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        print("\rRemaining Time: " + timeformat, end="")
        time.sleep(1)
        seconds -= 1

def focus_clock():
    while True:
        print("\nWork (25 minutes)")
        timer(25)

        play_notification_sound()
        print("\nShort Break (5 minutes)")
        timer(5)

        play_notification_sound()
        print("\nWork (25 minutes)")
        timer(25)

        play_notification_sound()
        print("\nLong Break (15 minutes)")
        timer(15)

        play_notification_sound()
        print("\nRestarting Focus Clock...")

if __name__ == "__main__":
    focus_clock()

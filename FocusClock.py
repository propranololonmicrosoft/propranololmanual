import time

def timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        print("\rRemaining Time: " + timeformat, end="")
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")

def focus_clock():
    print("Welcome to the Focus Clock!")
    while True:
        print("\nWork (25 minutes)")
        timer(25)

        print("\nTake a Short Break (5 minutes)")
        timer(5)

if __name__ == "__main__":
    focus_clock()

import time

try:
    import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
except ImportError:
    GPIO = None


def main():
    if GPIO is None:
        print("RPi.GPIO is not available on this system. This script requires a Raspberry Pi.")
        return

    GPIO.setwarnings(False)  # Ignore warning for now
    GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
    GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set GPIO Pin 4 (position 7) to be an input pin and set initial value to be pulled low (off)

    while True:  # Run forever
        if GPIO.input(7) == GPIO.HIGH:
            print("Someone has pressed the alert button!")
        time.sleep(0.1)


if __name__ == "__main__":
    main()


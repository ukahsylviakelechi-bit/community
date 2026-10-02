try:
    import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
except ModuleNotFoundError:
    GPIO = None


def main():
    if GPIO is None:
        print("RPi.GPIO is not available")
        return

    GPIO.setwarnings(False)  # Ignore warning for now
    GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
    GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set input pin and pull low

    while True:  # Run forever
        if GPIO.input(7) == GPIO.HIGH:
            print("Someone has pressed the alert button!")


if __name__ == "__main__":
    main()

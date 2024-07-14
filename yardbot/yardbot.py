import json
import subprocess
from time import sleep


def scan_wifi():
    networks = {}

    # Call linux nmcli command to get wifi networks and signal strength
    process = subprocess.Popen(
        ["nmcli"] + ["--terse", "device", "wifi"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    # Get stdout and stderr from the called process
    output, error = process.communicate()

    # Handle process errors
    if len(error) > 0:
        raise OSError(error)

    # Parse the results into a table of network information
    network_lines = output.decode().split("\n")
    # Print the output array
    for network_line in network_lines:
        # Ignore blank lines
        if len(network_line.strip()) == 0:
            continue

        # Replace escaped : which we will use to parse with
        network_line = network_line.replace("\\:", "-")
        # Break each line into a set of properties
        network_properties = network_line.split(":")
        # Create a network object using the properties
        network = {
            "inUse": network_properties[0].strip(),
            "mac": network_properties[1].strip(),
            "ssid": network_properties[2].strip(),
            "type": network_properties[3].strip(),
            "channel": network_properties[4].strip(),
            "quality": network_properties[5].strip(),
            "signal": network_properties[6].strip(),
        }
        # Store network keyed by mac address for uniqueness
        if len(network["ssid"]) > 0 and network["type"] == "Infra":
            networks[network["mac"]] = network

    return networks


def main():
    try:
        print("Hello, I am Yard Bot")
        # pinLED = 16

        # GPIO.setmode(GPIO.BOARD)  # Use GPIO pin number
        # # GPIO.setwarnings(False)         # Ignore warnings in our case
        # GPIO.setup(pinLED, GPIO.OUT)  # GPIO pin as output pin

        # while True:  # Endless Loop
        #     GPIO.output(pinLED, GPIO.HIGH)  # Turn on
        #     print("LED on")  # Prints state to console
        #     sleep(0.1)
        #     GPIO.output(pinLED, GPIO.LOW)  # Turn off
        #     print("LED off")  # Prints state to console
        #     sleep(0.2)
        networks = scan_wifi()
        print(networks)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

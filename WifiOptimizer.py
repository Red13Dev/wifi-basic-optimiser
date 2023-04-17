import subprocess

# Enables potential important wifi optimizations


def OptimizeWifi():

    print("attempting to run; Wi-Fi optimizations")

    # Disable power management for Wi-Fi adapter
    try:

        subprocess.run("powercfg /change standby-timeout-ac 0", shell=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print('ERROR with;', e)

    try:
        subprocess.run("powercfg /change standby-timeout-dc 0", shell=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print('ERROR with;', e)

    # Change Wi-Fi channel to the least congested one
    try:
        subprocess.run("netsh wlan set autoconfig enabled=yes interface='Wi-Fi'",
                       shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print('ERROR with;', e)

    # Set Wi-Fi transmit power to maximum
    try:
        subprocess.run("netsh wlan set transmitpower=100", shell=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print('ERROR with;', e)

    # Enable 802.11n mode for faster Wi-Fi speeds
    try:
        subprocess.run("netsh wlan set hostednetworkmode=allow",
                       shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print('ERROR with;', e)

    try:
        subprocess.run("netsh wlan set hostednetworkparameter mode=allow",
                       shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print('ERROR with;', e)

    # Set the Wi-Fi regulatory domain for your location (if applicable)
    # Replace 'US' with the appropriate ISO country code for your location
    try:
        subprocess.run("netsh wlan set regulatorydomain=us",
                       shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print('ERROR with;', e)

    # Restart the Wi-Fi adapter
    try:
        subprocess.run("netsh interface set interface 'Wi-Fi' admin=disable",
                       shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print('ERROR with;', e)

    try:
        subprocess.run("netsh interface set interface 'Wi-Fi' admin=enable",
                       shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print('ERROR with;', e)

    print("Finished running; enable Wi-Fi optimizations")

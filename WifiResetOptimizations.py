import subprocess

# Resets wifi optimizer


def ResetWifiOptimization():

    print("attempting to run; reset Wi-Fi settings")

    try:
        # Disable Wi-Fi adapter
        subprocess.run("netsh interface set interface 'Wi-Fi' admin=disable",
                       shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Enable Wi-Fi adapter
        subprocess.run("netsh interface set interface 'Wi-Fi' admin=enable",
                       shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print('ERROR with;', e)

    print("Finished running; reset Wi-Fi optimizations")

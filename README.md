# Falcon BMS Joystick Keybinding Script

This script is designed to simulate keypresses for the COMM menu in **Falcon BMS** using a joystick button. Since Falcon BMS does not allow remapping certain default keybinds, this script offers a workaround by triggering keypresses via joystick inputs.

## Prerequisites

Before running the script, make sure you have the following installed:

### 1. Install Required Libraries

```bash
pip install pygame
pip install pydirectinput
```

These libraries are required to handle joystick inputs and simulate keypresses.

## Setup Instructions

### 2. Configure the Script

#### Step 1: Uncomment the Line to Print the Button ID (Line 52)

- Uncomment the line that prints out the button ID in the script. This helps you identify the button on your joystick that corresponds to the action you want to trigger.

#### Step 2: Identify the Joystick and Button

- Run the script and check the name of the device (joystick) you want to use, as well as the button ID.
- You will need the **device name** and **button ID** to configure the script correctly.

```python
    2 joystick(s) detected.
    Joystick 1: WINWING Orion Throttle Base II + F15EX HANDLE L + F15EX HANDLE R
    Joystick Instance Id: 0300954b9840000064bd000000000000
    Joystick GUID: 1
    Joystick 2: VKBSim Gunfighter MCG Ultimate Twist
    Joystick Instance Id: 0300de721d2300002501000000000000
    Joystick GUID: 0
    Joystick 1 connencted
    Joystick 0 connencted
```

#### Step 3: Update the Script with Your Device Name and Button ID

- Change `device_name` to the name of your joystick device.
- Update the `button_key_map`. first is the button_id you want to map, then in between the ' is the key you want to press.

```python
# Map your buttons here:
button_key_map = {
    12: 't', #atc
    14: 'y', #other agencies
    15: 'q', #awacs
}
# Put the devince name here:
device_name = 'WINWING Orion Throttle Base II + F15EX HANDLE L + F15EX HANDLE R'
```

#### Step 4: Comment the Print Line

- After identifying the correct device and button, comment out the line that prints the button ID to prevent the terminal from printing unnecessary information on every keypress.

```python
# print(f"{joystick_name} - Button {button_id} pressed")
```

### 3. Save and Run the Script

- Save the script and run it.
- Double-click the script file or execute it in the terminal to start using your joystick for keypresses.

---

## Notes

- The script uses **pygame** to detect joystick input and **pydirectinput** to simulate the keypress.
- This script is designed for **Falcon BMS** and specifically targets joystick buttons to open the COMM menu. Adjust the key and button mapping as needed for other actions or games.

---

## License

lol

lmao even

do whatever i dont care

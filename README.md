# Falcon BMS Joystick Keybinding Script

This script is designed to simulate keypresses for the COMM menu in **Falcon BMS** using a joystick button. Since Falcon BMS does not allow remapping certain default keybinds, this script offers a workaround by triggering keypresses via joystick inputs.

!![fighterpilot](/fighterpilot.png)

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

#### Step 1: Uncomment the Line to Print the Button ID

- Uncomment the line that prints out the button ID in the script. This helps you identify the button on your joystick that corresponds to the action you want to trigger.

#### Step 2: Identify the Joystick and Button

- Run the script and check the name of the device (joystick) you want to use, as well as the button ID.
- You will need the **device name** and **button ID** to configure the script correctly.

```python
# Example of button_id print statement
# print("Device Name:", joystick.get_name())
# print("Button ID:", button_id)
```

#### Step 3: Update the Script with Your Device Name and Button ID

- Change `device_name` to the name of your joystick device.
- Change `btnid1`, `btnid2`, and `btnid3` to the IDs of the buttons you want to use to trigger specific actions.

```python
# Put the button IDs here.
btnid1 = 10
btnid2 = 11
btnid3 = 12

# Put the keys to be pressed here.
key1 = 'q'  # awacs
key2 = 't'  # atc
key3 = 'y'  # other agencies

# Put the name of the joystick you want the script to read.
device_name = 'WINWING Orion Throttle Base II + F15EX HANDLE L + F15EX HANDLE R'
```

#### Step 4: Comment the Print Line

- After identifying the correct device and button, comment out the line that prints the button ID to prevent the terminal from printing unnecessary information on every keypress.

```python
# print("Button ID:", btnid)  # Comment this line after identifying button_id
```

### 3. Save and Run the Script

- Save the script and run it.
- Double-click the script file or execute it in the terminal to start using your joystick for keypresses.

---

## Example Code Snippet

Here’s an example of what your script might look like after configuring it:

```python
import pygame
import sys
import pydirectinput

pygame.init()

pygame.joystick.init()

# Put the button IDs here.
btnid1 = 10
btnid2 = 11
btnid3 = 12

# Put the keys to be pressed here.
key1 = 'q'  # awacs
key2 = 't'  # atc
key3 = 'y'  # other agencies

# Put the name of the joystick you want the script to read.
device_name = 'WINWING Orion Throttle Base II + F15EX HANDLE L + F15EX HANDLE R'

# Check for available joysticks
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joysticks detected.")
    sys.exit()

# Display connected joystick info
print(f"{joystick_count} joystick(s) detected.")
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    print(f"Joystick {i + 1}: {joystick.get_name()}")

try:
    print(f"Ctrl + C to exit!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                joystick = pygame.joystick.Joystick(event.joy)
                button_id = event.button
                if joystick.get_name() == device_name:
                    if button_id == btnid1:
                        pydirectinput.press(key1)
                    elif button_id == btnid2:
                        pydirectinput.press(key2)
                    elif button_id == btnid3:
                        pydirectinput.press(key3)

except KeyboardInterrupt:
    print("\nExiting program...")
    pygame.quit()
    sys.exit()
```

---

## Notes

- The script uses **pygame** to detect joystick input and **pydirectinput** to simulate the keypress.
- This script is designed for **Falcon BMS** and specifically targets joystick buttons to open the COMM menu. Adjust the key and button mapping as needed for other actions or games.

---

## License

lol

lmao even

do whatever i dont care

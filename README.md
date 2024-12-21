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
- Change `btnid` to the ID of the button you want to use to trigger the COMM menu.

```python
device_name = "Your Joystick Name Here"   # Replace with your joystick name
btnid = 12                                # Replace with your desired button ID
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

## Example Code Snippets

Here’s an example of what your script might look like after configuring it:

```python
import pygame
import pydirectinput

# Initialize pygame
pygame.init()

# Device configuration
device_name = "Your Joystick Name Here"  # Set this to the correct device name
btnid = 12  # Set this to the button ID you want to use

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == btnid:
                pydirectinput.press("COMM_MENU_KEY")  # Replace with the key you want to simulate
                break
```

---

## Notes

- The script uses **pygame** to detect joystick input and **pydirectinput** to simulate the keypress.
- This script is designed for **Falcon BMS** and specifically targets joystick buttons to open the COMM menu. Adjust the key and button mapping as needed for other actions or games.

---

## License

This script is free to use and modify under the **MIT License**.

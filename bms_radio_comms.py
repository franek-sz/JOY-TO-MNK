import pygame
import sys
import pydirectinput

pygame.init()

pygame.joystick.init()

# # Put the button IDs here.
# btnid1 = 10
# btnid2 = 11
# btnid3 = 12

# # Put the keys to be pressed here.
# key1 = 'q' #awacs
# key2 = 't' #atc
# key3 = 'y' #other agencies

button_key_map = {
    13: 't',
    15: 'y',
    16: 'q',
}

joysticks = {}

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
    print(f"Joystick Instance Id: {joystick.get_guid()}")
    print(f"Joystick GUID: {joystick.get_instance_id()}")

for event in pygame.event.get():
    if event.type == pygame.JOYDEVICEADDED:
        joy = pygame.joystick.Joystick(event.device_index)
        joysticks[joy.get_instance_id()] = joy
        print(f"Joystick {joy.get_instance_id()} connencted")

    if event.type == pygame.JOYDEVICEREMOVED:
        del joysticks[event.instance_id]
        print(f"Joystick {event.instance_id} disconnected")

try:
    print(f"Ctrl + C to exit!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                joystick = pygame.joystick.Joystick(event.joy)
                button_id = event.button
                # print(f"{joystick.get_name()} - Button {button_id} pressed")
                # Uncomment this ^ line if you want to check what button you're pressing, sometimes the manufacturer software button_id is different.
                if joystick.get_name() == device_name:
                    if button_id == btnid1:
                        pydirectinput.press(key1)

except KeyboardInterrupt:
    print("\nExiting program...")
    pygame.quit()
    sys.exit()
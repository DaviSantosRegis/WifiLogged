from subprocess import check_output as cmd
from datetime import datetime

import os

class Wifi:
    def __init__(self):
        self.Command = ['netsh', 'wlan', 'show', 'profiles']
        self.Logged = {profile: key for profile, key in zip(self.GetProfiles(), self.GetKeys())}


    def GetProfiles(self):
        data = cmd(self.Command).decode('cp858', errors="backslashreplace").split("\n")[9:-2]
        for i in data:
            yield i.split(": ")[1][:-1]

    def GetKeys(self):
        for i,profile in enumerate(self.GetProfiles()):
            data = cmd([*self.Command, profile, "key=clear"]).decode(
                'cp858', errors="backslashreplace")

            yield data.split('\n')[32].split(": ")[1][:-1]

    def Output(self):


        UserText = "Redes Wifi:"

        KeyText = " Senha"
        Str = f"{UserText:<30}|{KeyText:<}\n"
        Str += f"_" * 50 + "\n"

        for User,Key in self.Logged.items():
            Str += f"{User:<30}| {Key:<}\n"

            time = datetime.now().strftime("%d.%m.%y %H.%M.%S")
            OutputFolder = "SenhasLog/"
            if not os.path.exists(OutputFolder):
                os.mkdir(OutputFolder)

            with open(f"{OutputFolder}Senhas {time}.txt", "w") as fp:
                fp.write(Str)

wifi = Wifi()
wifi.Output()





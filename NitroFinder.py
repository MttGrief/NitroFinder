import ctypes
import string
import os
import time
CREDITS = """
@MTT.GRIEF
"""

USE_WEBHOOK = True

print(CREDITS)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


try:
    from discord_webhook import DiscordWebhook
except ImportError:

    input(
        f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nYou can ignore this error if you aren't going to use a webhook.\nPress enter to continue.")
    USE_WEBHOOK = False
try:
    import requests
except ImportError:

    input(
        f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit()
try:
    import numpy
except ImportError:

    input(
        f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
    exit()


url = "https://github.com"
try:
    response = requests.get(url)
    print("Controllando la connessione")
    time.sleep(.4)
except requests.exceptions.ConnectionError:

    input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
    exit()


class NitroGen:
    def __init__(self):
        self.fileName = "Codici Nitro.txt"

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Finder - Made by MTT.GRIEF")
        else:
            print(f'\33]0;Nitro Finder - Made by MTT.GRIEF\a',
                  end='', flush=True)

        print(""" _   _ _ _               _____ _           _
| \ | (_) |_ _ __ ___   |  ___(_)_ __   __| | ___ _ __
|  \| | | __| '__/ _ \  | |_  | | '_ \ / _` |/ _ \ '__|
| |\  | | |_| | | (_) | |  _| | | | | | (_| |  __/ |
|_| \_|_|\__|_|  \___/  |_|   |_|_| |_|\__,_|\___|_|
                                                        """)
        time.sleep(2)

        self.slowType("Made by: MTT.GRIEF", .02)
        time.sleep(1)

        self.slowType(
            "\nInput Quanti codici vuoi pulluppare: ", .02, newLine=False)

        try:
            num = int(input(''))
        except ValueError:
            input("PIRLA DEVI INSERIRE UN NUMERO.\nPress enter to exit")
            exit()

        if USE_WEBHOOK:

            self.slowType(
                "Se vuoi usare una Webhook appiciala qui di fianco: ", .02, newLine=False)
            url = input('')

            webhook = url if url != "" else None

            if webhook is not None:
                DiscordWebhook(
                        url=url,
                        content=f"```PROGRAMMA PARTITO\nTUTTI I CODICI LI VEDRAI QUI SOTTO```"
                    ).execute()



        valid = []
        invalid = 0
        chars = []
        chars[:0] = string.ascii_letters + string.digits


        c = numpy.random.choice(chars, size=[num, 23])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url, webhook)

                if result:

                    valid.append(url)
                else:
                    invalid += 1
            except KeyboardInterrupt:

                print("\nHAI STOPPATO IL PROGRAMMA")
                break

            except Exception as e:
                print(f" ERRORE | {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Finder - {len(valid)} VALIDOOO | {invalid} non valido rip - Made by MTT.GRIEF")
                print("")
            else:

                print(
                    f'\33]0;Nitro Finder - {len(valid)} VALIDOOO | {invalid} non valido rip - Made by MTT.GRIEF\a', end='', flush=True)

        print(f"""
Results:
 VALIDI: {len(valid)}
 non validi: {invalid}
 CODICI VALIDI: {', '.join(valid)}""")


        input("\nFINITO! PREMI ENTER 5 VOLTE PER USCIRE.")
        [input(i) for i in range(4, 0, -1)]


    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:

            print(i, end="", flush=True)
            time.sleep(speed)
        if newLine:
            print()

    def quickChecker(self, nitro:str, notify=None):

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:

            print(f" VALIDOOOOOOO | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Codici Nitro.txt", "w") as file:

                file.write(nitro)

            if notify is not None:
                DiscordWebhook(
                    url=url,
                    content=f"CODICE NITRO VALIDO TROVATO! @everyone \n{nitro}"
                ).execute()

            return True


        else:

            print(f" non valido | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False


if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()

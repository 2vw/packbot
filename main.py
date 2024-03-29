import json, random, asyncio, aiohttp, colorama, os

with open('json/config.json') as f:
    config = json.load(f)

with open('bibles/bible1.txt') as f:
    bibe = f.read()
    bible = bibe.splitlines()

    bible = [line for line in bible if line.strip() != ""]

import threading

async def send_message(channel, amt, perline, loops, mention:str=None):
    input(colorama.Fore.RED + "Press enter to start sending messages\n" + colorama.Fore.WHITE)
    for _ in range(loops):
        async with aiohttp.ClientSession(
                headers={"Authorization": config["TOKEN"]}) as session:
            tasks = []
            for _ in range(amt):
                url = f"https://discord.com/api/v9/channels/{channel}/messages"
                json_data = {
                    "content": f"{mention} {'\n'.join(random.sample(bible, perline))}"}
                task = session.post(url, json=json_data)
                tasks.append(task)
            for task in tasks:
                await asyncio.sleep(int(random.randint(1, 5)/10))  # wait before running the next task
                await task
                
        print(colorama.Fore.RED + "waiting 10 seconds inbetween loops to avoid rate limit")
        await asyncio.sleep(10)


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colorama.Fore.RED + """
CREATED BY KSEXISTS

                                                                                            
░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░  ░▒▓█▓▒░     
                                                                                            
                                                                                            

          """)
    channel = int(input(colorama.Fore.YELLOW + "Enter channel id: \n" + colorama.Fore.WHITE))
    amt = int(input(colorama.Fore.YELLOW + "Enter amount of messages: \n" + colorama.Fore.WHITE))
    perline = int(input(colorama.Fore.YELLOW + "Enter amount of packs per message: \n" + colorama.Fore.WHITE))
    loops = int(input(colorama.Fore.YELLOW + "Enter amount of loops: \n" + colorama.Fore.WHITE))
    mention = input(colorama.Fore.YELLOW + "Enter user ID to mention (leave blank if none): \n" + colorama.Fore.WHITE)

    asyncio.run(send_message(channel, amt, perline, loops))


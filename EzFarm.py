import discord
import time
from discord.ext.commands import Bot
from discord.ext import commands 
import asyncio 
from datetime import datetime
import random
import os

try:
    os.system("cls")
except:
    pass

print()
print("\033[35m███████\033[0m╗\033[35m███████\033[0m╗    \033[35m███████\033[0m╗ \033[35m█████\033[0m╗ \033[35m██████\033[0m╗ \033[35m███\033[0m╗   \033[35m███\033[0m╗")
print("\033[35m██\033[0m╔════╝╚══\033[35m███\033[0m╔╝    \033[35m██\033[0m════╝ \033[35m██\033[0m╔══\033[35m██\033[0m╗\033[35m██\033[0m╔══\033[35m██\033[0m╗\033[35m████\033[0m╗ \033[35m████\033[0m║")
print("\033[35m█████\033[0m╗    \033[35m███\033[0m╔╝     \033[35m█████\033[0m╗  \033[35m███████\033[0m║\033[35m██████\033[0m╔╝\033[35m██\033[0m╔\033[35m████\033[0m╔\033[35m██\033[0m║")
print("\033[35m██\033[0m╔══╝   \033[35m███\033[0m╔╝      \033[35m██\033[0m╔══╝  \033[35m██\033[0m╔══\033[35m██\033[0m║\033[35m██\033[0m╔══\033[35m██\033[0m╗\033[35m██\033[0m║╚\033[35m██\033[0m╔╝\033[35m██\033[0m║")
print("\033[35m███████\033[0m╗\033[35m███████\033[0m╗    \033[35m██\033[0m║     \033[35m██\033[0m║  \033[35m██\033[0m║\033[35m██\033[0m║  \033[35m██\033[0m║\033[35m██\033[0m║ ╚═╝ \033[35m██\033[0m║")
print("╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝")
print("")

print("\033[0m" + "The Best bot farmer for discord")
print("By Ez Tools\n")

TOKEN = input("Enter your discord  token: ")

client = discord.Client()
b = Bot(command_prefix = "")

@b.event 
async def on_ready(): 
    print() 
print('''
===============
Name: Ez Farm
Author: loTus01
version: 1.1
Prefix: F
===============

My name is Optimus Prime.
''')

@b.event 
async def on_message(message):

    if message.content == "Fmine":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\n[{current_time}:] STARTED MINING WITH Idle Miner... \n")

        mtn1 = time.time()
        mtn2 = mtn1 + 1800

        while True:

            # anti ban
            tempsN = 60
            add = random.randint(2,7)
            temps = (tempsN + add)
    
            mtn3 = time.time()

            if mtn3 > mtn2:
                await message.channel.send(";rebirth")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"\033[31m[{current_time}]: Tryed to rebirth")
                mtn2 = mtn2 + 1800

            await message.channel.send(";s")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\033[0m[{current_time}]: Sold items")
            time.sleep(1)
            await message.channel.send(";hunt")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\033[33m[{current_time}]: Hunted")
            time.sleep(temps)                              #1m
            await message.channel.send(";s")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"[{current_time}]: Sold items")
            time.sleep(temps)                              #1m
            await message.channel.send(";up p max")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\033[34m[{current_time}]: Upgraded pickaxe ")
            time.sleep(temps)                              #1m
            await message.channel.send(";s ")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\033[0m[{current_time}]: Sold items")
            time.sleep(temps)                              #1m
            await message.channel.send(";s")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"[{current_time}]: Sold items")
            time.sleep(temps)                              #1m
            await message.channel.send(";up b max")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\033[34m[{current_time}]: Upgraded backpack ")
            time.sleep(temps)

    if message.content == "Fender":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\n[{current_time}:] STARTED CLAIMING WITH EnderBot... \n")

        mtn1 = time.time()
        mtn2 = mtn1 + 3600
        mtn11 = time.time()
        mtn22 = mtn11 + 86400

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await message.channel.send(">hourly")
        print(f"\033[34m[{current_time}]: Claimed Hourly Gift")
        time.sleep(2)
        await message.channel.send(">mine all")
        print(f"\033[34m[{current_time}]: Mined all")
        await message.channel.send(">daily")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\033[31m[{current_time}]: Claimed Daily Gift")

        while True:
            mtn3 = time.time()
            mtn33 = time.time()

            if mtn3 > mtn2:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                await message.channel.send(">hourly")
                print(f"\033[34m[{current_time}]: Claimed Hourly Gift")
                time.sleep(2)
                await message.channel.send(">mine all")
                print(f"\033[34m[{current_time}]: Mined all")
                mtn2 = mtn2 + 3600

            if mtn33 > mtn22:
                await message.channel.send(">daily")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"\033[31m[{current_time}]: Claimed Daily Gift")
                mtn2 = mtn2 + 86400

            time.sleep(60)


    cmdinutile = ["!lb", "!top", "!help", "!rob", "!roulette 100 red", "!leadrboard", "!help", "!lb -bank", "!bal", "!money"]
    # random.choice(cmdinutile)

    if message.content == ('Fwork'):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\n[{current_time}:] STARTED WORKING WITH Unbelievaboat... \n")

        while True:

            # anti ban
            tempsN = 300
            add = random.randint(7,15)
            temps = (tempsN + add)

            await message.channel.send("!work")
            time.sleep(1)
            await message.channel.send("!dep all")  
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"[{current_time}]: worked ")
            print(f"\033[33m[{current_time}]: dep all ")
            time.sleep(temps)

    if message.content == ('FworkAll'):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\n[{current_time}:] STARTED WORKING WITH Unbelievaboat... \n")

        while True:

            # anti ban
            tempsN = 300
            add = random.randint(7,15)
            temps = (tempsN + add)

            await message.channel.send("!work")
            time.sleep(1)
            await message.channel.send("!crime")
            time.sleep(1)
            await message.channel.send("!slut")
            time.sleep(1)
            await message.channel.send("!dep all")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"[{current_time}]: Worked ")
            print(f"\033[34m[{current_time}]: Crimed ")
            print(f"\033[34m[{current_time}]: Sluted ")
            print(f"\033[33m[{current_time}]: Dep all ")
            time.sleep(temps)
            await message.channel.send("!work")
            time.sleep(1)
            await message.channel.send("!dep all")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"[{current_time}]: Worked ")
            print(f"\033[33m[{current_time}]: Dep all ")
            time.sleep(temps)
    
    if message.content == ('Fbump'):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\n[{current_time}:] STARTED BUMPING WITH DISBOARD... \n")

        while True:
            # anti ban
            tempsN = 7200
            add = random.randint(10,20)
            temps = (tempsN + add)

            await message.channel.send("!d bump")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"[{current_time}]: Bumbed ")
            time.sleep(temps)

    if message.content == ('Fhelp'):
        embedVar = discord.Embed(title="Help Menu", color=0x00ff00)
        embedVar.add_field(name="Fidleminer", value="Shows info on the Idle Miner farming ", inline=True)
        embedVar.add_field(name="FunbelievaBoat", value="Shows info on the UnbelievaBoat farming", inline=True)
        embedVar.add_field(name="Fenderbot", value="Shows info on the EnderBot farming", inline=True)
        embedVar.add_field(name="Fdisboard", value="Shows info on the Disboard farming", inline=True)
        embedVar.add_field(name="Fhelp", value="Help message", inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('Fidleminer'):
        embedVar = discord.Embed(title="Idle Miner", color=0x800000)
        embedVar.add_field(name="__Cmd:__ ", value="`Fmine`", inline=True)
        embedVar.add_field(name="__Xp lvl opti:__ ", value="`True`", inline=True)
        embedVar.add_field(name="__Anti-ban:__ ", value="`True`", inline=True)
        embedVar.add_field(name="__Action/Laps:__ ", value="`;s = 1mim` \n`;up p max = 2mim` \n`;up b max = 2mim` \n`;rebirth = 30mim`", inline=False)
        await message.channel.send(embed=embedVar)
    
    if message.content == ('FunbelievaBoat'):
        embedVar = discord.Embed(title="UnbelievaBoat", color=0xda1616)
        embedVar.add_field(name="__Cmd:__ ", value="`FworkAll`", inline=True)
        embedVar.add_field(name="__Xp lvl opti:__ ", value="`False`", inline=True)
        embedVar.add_field(name="__Anti-ban:__ ", value="`True`", inline=True)
        embedVar.add_field(name="__Action/Laps:__ ", value="`!work = 5mim` \n`!crime = 10mim` \n`!slut = 10mim` \n`!depall = ∞`", inline=False)
        embedVar.add_field(name="__Cmd:__ ", value="`Fwork`", inline=True)
        embedVar.add_field(name="__Xp lvl opti:__ ", value="`False`", inline=True)
        embedVar.add_field(name="__Anti-ban:__ ", value="`True`", inline=True)
        embedVar.add_field(name="__Action/Laps:__ ", value="`!work = 5mim` \n`!depall = ∞`", inline=False)
        await message.channel.send(embed=embedVar)
    
    if message.content == ('Fenderbot'):
        embedVar = discord.Embed(title="EnderBot", color=0x800000)
        embedVar.add_field(name="__Cmd:__ ", value="`Fender`", inline=True)
        embedVar.add_field(name="__Xp lvl opti:__ ", value="`False`", inline=True)
        embedVar.add_field(name="__Anti-ban:__ ", value="`False`", inline=True)
        embedVar.add_field(name="__Action/Laps:__ ", value="`>daily = 1d` \n`>hourly = 1h` \n`>mine all = 1h`", inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('Fdisboard'):
        embedVar = discord.Embed(title="Disboard", color=0x800000)
        embedVar.add_field(name="__Cmd:__ ", value="`Fbump`", inline=True)
        embedVar.add_field(name="__Xp lvl opti:__ ", value="`False`", inline=True)
        embedVar.add_field(name="__Anti-ban:__ ", value="`True`", inline=True)
        embedVar.add_field(name="__Action/Laps:__ ", value="`!d bump = 1h`", inline=False)
        await message.channel.send(embed=embedVar)


b.run(TOKEN, bot = False)



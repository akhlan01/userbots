
from telethon import TelegramClient, events, sync 

import asyncio
@events.register(events.NewMessage(pattern=".sexy"))

async def sexy(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 15)

    #input_str = event.pattern_match.group(1)

    #if input_str == "lovestory":

    await event.edit(" sexy animation")

    animation_chars = [

            "one โค story๏ธ ",
            "  ๐             ๐ \n/๐\         <๐\ \n ๐               /|",    
            "  ๐          ๐ณ \n/๐\       /๐\ \n  ๐            /|",
            "  ๐            ๐ \n/๐\         <๐> \n  ๐             /|",
            "  ๐         โบ๏ธ \n/๐\      /๐\ \n  ๐          /|",
            "  ๐          ๐ \n/๐\       /๐\ \n  ๐           /|",
            "  ๐   ๐ \n /๐\/๐\ \n   ๐   /|",
            " ๐ณ  ๐ \n /|\ /๐\ \n /     / |",    
            "๐    /๐ฐ\ \n<|\      ๐ \n /๐    / |",
            "๐ \n/(),โ๐ฎ \n /\         _/\\/|",
            "๐ \n/\\_,__๐ซ \n  //    //       \\",
            "๐ \n/\\_,๐ฆ_๐  \n  //         //        \\",
            "  ๐ญ      โบ๏ธ \n  /|\   /(๐ถ)\ \n  /!\   / \ ",
            "Tugadi ๐..."
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 15])
# plugin by lejend @hellboi_atul
"""Emoji

Available Commands:

.lucky"""

from telethon import events

import asyncio
from uniborg.util import admin_cmd




@borg.on(admin_cmd(pattern="lucky"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 17)

    #input_str = event.pattern_match.group(1)

    #if input_str == "lucky":

    await event.edit("Lucky...🤑🤑")

    animation_chars = [
        
            "⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](/hellboi-atul/hellboi-atul)⬜",
            "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](/hellboi-atul/hellboi-atul)⬜",
            "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](/hellboi-atul/hellboi-atul)⬜",
            "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](/hellboi-atul/hellboi-atul)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](/hellboi-atul/hellboi-atul)⬜",    
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](/hellboi-atul/hellboi-atul)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](/hellboi-atul/hellboi-atul)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](/hellboi-atul/hellboi-atul)⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](/hellboi-atul/hellboi-atul)⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜[🎁](/hellboi-atul/hellboi-atul)⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜[🎁](/hellboi-atul/hellboi-atul)⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n[🎁](/hellboi-atul/hellboi-atul)⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜",
            "⬜⬜⬜\n⬜⬜⬜\n⬜⬜⬜",
            "⬜⬜\n⬜⬜",
            "[🎁👈🏻Ye le gift](/hellboi-atul/hellboi-atul)"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 17])

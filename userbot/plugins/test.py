"""Check your internet speed powered by speedtest.net
Syntax: .speedtest #technoayan
Available Options: image, file, text"""

#hehehe

from telethon import events
from datetime import datetime
import io
import speedtest
from userbot.utils import admin_cmd
from userbot import CMD_HELP

@borg.on(admin_cmd(pattern="test ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    as_text = True
    as_document = False
    if input_str == "image":
        as_document = False#hehe
    elif input_str == "file":
        as_document = True
    elif input_str == "text":
        as_text = True
    await event.edit("`Calculating ur ⚜️DarkCobra⚜️ Server Speed. Please wait!`")
    start = datetime.now()
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()#dchehe
    end = datetime.now()
    ms = (end - start).seconds
    response = s.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    i_s_p = client_infos.get("isp")
    i_s_p_rating = client_infos.get("isprating")
    reply_msg_id = event.message.id
    if event.reply_to_msg_id:
        reply_msg_id = event.reply_to_msg_id
    try:#heheh
        response = s.results.share()
        speedtest_image = response
        if as_text:
            await event.edit("""`DarkCobra Server Speed in {} sec`

`Download: {}`
`Upload: {}`
`Ping: {}`
`Internet Service Provider: {}`
`ISP Rating: {}`""".format(ms, convert_from_bytes(download_speed), convert_from_bytes(upload_speed), ping_time, i_s_p, i_s_p_rating))
        else:
            await borg.send_file(
                event.chat_id,
                speedtest_image,#heeehe
                caption="**SpeedTest** completed in {} seconds".format(ms),
                force_document=as_document,
                reply_to=reply_msg_id,
                allow_cache=False
            )
            await event.delete()
    except Exception as exc:#dc
        await event.edit("""**SpeedTest** completed in {} seconds
Download: {}
Upload: {}#ehhehe
Ping: {}

__With the Following ERRORs__
{}""".format(ms, convert_from_bytes(download_speed), convert_from_bytes(upload_speed), ping_time, str(exc)))


def convert_from_bytes(size):
    power = 2**10
    n = 0
    units = {
        0: "",
        1: "kilobytes",
        2: "megabytes",
        3: "gigabytes",
        4: "terabytes"
    }
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"

CMD_HELP.update({"test": ".test\nCheck your userbot heroku server speed powered by speedtest.net"})

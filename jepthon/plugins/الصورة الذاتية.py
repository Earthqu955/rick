from jepthon import *
from jepthon import jepiq
from ..sql_helper.globals import gvarstatus

@jepiq.on(admin_cmd(pattern="(ذاتية|ذاتيه)"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    lMl10l = await event.get_reply_message()
    pic = await lMl10l.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
- تـم جـلب الصـورة بنجـاح ✓ 
- غير مبري الذمه اذا استخدمت الامر للابتزاز
- CH: @Rickthon
- Dev: @P_J_I
  """,
    )
    await event.edit(" 🙂❤️ ")

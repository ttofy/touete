import os.path
from jepthon import jmthon
from ..core.managers import edit_delete, edit_or_reply

def isEx(path):
     spath = str(path)
     return os.path.exists(f"jepthon/plugins/{spath}.py")

@jmthon.ar_cmd(pattern="موجود؟(?:\s|$)([\s\S]*)")

async def _(event):
    input_str = event.pattern_match.group(1)
    if input_str is None:
        await edit_delete(event, "قم بكتابة اسم البلوكن")
    re = isEx(str(input_str))
    return await edit_or_reply(event, str(re))

from pypresence import Presence
from time import time
from type_here import TOKEN

print()
print("Guided by Fsoky (Спасибо тебе Фсоки за то что приносишь знания в интересующие темы для людей.)")
print("Special thanks to Sepulture for helping me")
print()

RPC = Presence(TOKEN["APPLICATION"])
btns = [
    {
        "label": TOKEN["FIRST_BTN_NAME"],
        "url": TOKEN["FIRST_BTN_URL"],
    },
    {
        "label": TOKEN["SECOND_BTN_NAME"],
        "url": TOKEN["SECOND_BTN_URL"],
    }
]

RPC.connect()
RPC.update(
    state=TOKEN["BIG_TXT"],
    details=TOKEN["SMALL_TXT"],
    start=time(),
    buttons=btns,
    large_image=TOKEN["LARGE_IMG"],
    small_image=TOKEN["SMALL_IMG"],
    large_text=TOKEN["LARGE_IMG_TXT"],
    small_text=TOKEN["SMALL_IMG_TXT"]
)

print("Rich Presence launched")
input()

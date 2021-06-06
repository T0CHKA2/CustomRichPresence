from pypresence import Presence
from time import time
from type_here import TOKEN

print()
print()
print("|-------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("||BBBBBBBBBB      YYYY       YYYY         TTTTTTTTTTTT       0000000        CCCCCCCCCCC     HHHHHH      HHHHHH     KKKKKK         KKKK      AAAAAAAA        ||")
print("||BBB     BBB      YYYY     YYYY          TTTTTTTTTTTT     0000   0000     CCCCCCCCCCC      HHHHHH      HHHHHH     KKKKKK       KKKKK      AAAAAAAAAAA      ||")
print("||BBB     BBB       YYYY  YYYY                TTTT         0000   0000     CCCCC            HHHHHH      HHHHHH     KKKKKK      KKKKK      AAAA     AAAA     ||")
print("||BBBBBBBBBBBB        YYYYYY                  TTTT         0000   0000     CCCCC            HHHHHHHHHHHHHHHHHH     KKKKKK    KKKKK       AAAA       AAAA    ||")
print("||BBB      BBB         YYYY                   TTTT         0000   0000     CCCCC            HHHHHHHHHHHHHHHHHH     KKKKKKKKKKKKK        AAAAAAAAAAAAAAAAA   ||")
print("||BBB      BBB         YYYY                   TTTT         0000   0000     CCCCC            HHHHHH      HHHHHH     KKKKKKKKKKKK        AAAAAAAAAAAAAAAAAAA  ||")
print("||BBB      BBB         YYYY                   TTTT         0000   0000     CCCCCCCCCCC      HHHHHH      HHHHHH     KKKKKK  KKKKK      AAAAA           AAAAA ||")
print("||BBBBBBBBBBB          YYYY                   TTTT           0000000        CCCCCCCCCCC     HHHHHH      HHHHHH     KKKKKK    KKKKK   AAAAA             AAAAA||")
print("|------------------------------------------------------------------------------------------------------------------------------------------------------------|")
print()
print()

RPC = Presence(TOKEN.APPLICATION)
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

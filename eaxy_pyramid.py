import time
from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po
from easy_ui import MultiNumericUI

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)

def build_pyramid(v):
    h = v["hight"]
    x = v["x"]
    y = v["y"]
    z = v["z"]

    for i in range(h):
        size = h - 1 - i
        mc.setBlocks(x-size, y+i, z-size, x+size, y+i, z+size, param.SANDSTONE)


MultiNumericUI(
    title="ピラミッド",
    items={
        "hight": 5,
        "x": 0,
        "y": 64,
        "z": 0
    },
    buttons={
        "ピラミッドを建てる": build_pyramid
    }
)

while True:
    time.sleep(1)
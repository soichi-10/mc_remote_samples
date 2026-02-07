import time
from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po
from easy_ui import MultiNumericUI

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)

def build_tree(v):
    mc.setBlocks(v["x"]-2, v["y"]+3, v["z"]-2, v["x"]+2, v["y"]+4, v["z"]+2, param.OAK_LEAVES)
    mc.setBlocks(v["x"]-1, v["y"]+5, v["z"]-1, v["x"]+1, v["y"]+6, v["z"]+1, param.OAK_LEAVES)
    mc.setBlocks(v["x"], v["y"], v["z"], v["x"], v["y"]+5, v["z"], param.OAK_LOG)

MultiNumericUI(
    title="a",
    items={
        "x": 0,
        "y": 64,
        "z": 0
    },
    buttons={
        "木を建てる": build_tree
    }
)

while True:
    time.sleep(1)
import time
from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po
from easy_ui import MultiNumericUI

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)

# 石を置く関数（石用の座標だけを使う）
def stone_action(v):
    mc.setBlock(v["stone_x"], v["stone_y"], v["stone_z"], param.STONE)
    print(f"Stone設置: {v['stone_x']}, {v['stone_y']}, {v['stone_z']}")

# オークを置く関数（オーク用の座標だけを使う）
def oak_action(v):
    mc.setBlock(v["oak_x"], v["oak_y"], v["oak_z"], param.OAK_LOG)
    print(f"Oak設置: {v['oak_x']}, {v['oak_y']}, {v['oak_z']}")

def snow_action(v):
    mc.setBlock(v["snow_x"], v["snow_y"], v["snow_z"], param.SNOW_BLOCK)
    print(f"Snow設置: {v['snow_x']}, {v['snow_y']}, {v['snow_z']}")

# UI起動
MultiNumericUI(
    title="建築ツール",
    items={
        "oak_x": 0, "oak_y": 70, "oak_z": 0,
        "stone_x": 0, "stone_y": 70, "stone_z": 0,
        "snow_x": 0, "snow_y": 70, "snow_z": 0
    },
    buttons={
        "Oakを設置": oak_action,
        "Stoneを設置": stone_action,
        "Snowを設置": snow_action
    }
)

while True:
    time.sleep(1)
from mcpi.minecraft import Minecraft
import time
we =Minecraft.create()
x = 200
y = 200
z = 100
we.player.setPos(x, y, z)
time.sleep(2)
x = -50
y = -50
we.player.setPos(x, y, z)
time.sleep(2)
x = -50
y = -50
we.player.setPos(x, y, z)
time.sleep(2
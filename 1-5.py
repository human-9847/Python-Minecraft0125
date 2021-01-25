from mcpi.minecraft import Minecraft
we=Minecraft.create()
we.postToChat ("I'm watching you")
while True:
  x,y,z =  we.player.getTilePos()
  we.postToChat(" x:"+str(x)+"y:"+str(y)+"z:"+str(z))
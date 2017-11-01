#Claire Yegian
#11/1/17
#calculatorProject - makes calculator

from ggame import *

orange = Color(0xfa9806,1)
lightGrey = Color(0xcecece,1)
darkGrey = Color(0x6f6f6f,1)
black = Color(0x000000,1)

blackBox = RectangleAsset(300,500,LineStyle(1,black),black)
numberButton = CircleAsset(25,LineStyle(1,orange),orange)

Sprite(blackBox)
Sprite(numberButton,(260,150))
Sprite(numberButton,(260,210))
Sprite(numberButton,(260,270))
Sprite(numberButton,(260,330))
Sprite(numberButton,
App().run()

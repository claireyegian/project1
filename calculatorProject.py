#Claire Yegian
#11/1/17
#calculatorProject - makes calculator

from ggame import *

orange = Color(0xfa9806,1)
lightGrey = Color(0xcecece,1)
darkGrey = Color(0x6f6f6f,1)
black = Color(0x000000,1)

blackBox = RectangleAsset(300,450,LineStyle(1,black),black)
functionButton = CircleAsset(25,LineStyle(1,orange),orange)
equalsClear = CircleAsset(25,LineStyle(1,lightGrey),lightGrey)
numberButton = CircleAsset(25,LineStyle(1,darkGrey),darkGrey)

Sprite(blackBox)
Sprite(numberButton,(45,210))
Sprite(numberButton,(45,270))
Sprite(numberButton,(45,330))
Sprite(numberButton,(45,390))
Sprite(numberButton,(120,210))
Sprite(numberButton,(120,270))
Sprite(numberButton,(120,330))
Sprite(numberButton,(120,390))
Sprite(numberButton,(195,210))
Sprite(numberButton,(195,270))
Sprite(numberButton,(195,330))
Sprite(numberButton,(195,390))

Sprite(equalsClear,(45,150))
Sprite(equalsClear,(120,150))
Sprite(equalsClear,(195,150))

Sprite(functionButton,(260,150))
Sprite(functionButton,(260,210))
Sprite(functionButton,(260,270))
Sprite(functionButton,(260,330))
Sprite(functionButton,(260,390))
App().run()

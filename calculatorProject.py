#Claire Yegian
#11/1/17
#calculatorProject - makes calculator

from ggame import *

def mouseClick(event):
    if (click.x>20 and click.x<70) and (click.y>185 and click.y<235):
        print(1)

if __name__ == '__main__':
    orange = Color(0xfa9806,1)
    lightGrey = Color(0xcecece,1)
    darkGrey = Color(0x6f6f6f,1)
    black = Color(0x000000,1)

    blackBox = RectangleAsset(300,450,LineStyle(1,black),black)
    functionButton = CircleAsset(25,LineStyle(1,orange),orange)
    equalsClear = CircleAsset(25,LineStyle(1,lightGrey),lightGrey)
    numberButton = CircleAsset(25,LineStyle(1,darkGrey),darkGrey)
    buttonText1 = TextAsset('AC')
    buttonText2 = TextAsset('÷')
    buttonText3 = TextAsset('x')
    buttonText4 = TextAsset('-')
    buttonText5 = TextAsset('+')
    buttonText6 = TextAsset('=')
    buttonText7 = TextAsset('1')
    buttonText8 = TextAsset('2')
    buttonText9 = TextAsset('3')
    buttonText10 = TextAsset('4')
    buttonText11 = TextAsset('5')
    buttonText12 = TextAsset('6')
    buttonText13 = TextAsset('7')
    buttonText14 = TextAsset('8')
    buttonText15 = TextAsset('9')
    buttonText16 = TextAsset('0')


    Sprite(blackBox)

    Sprite(numberButton,(45,210))
    Sprite(buttonText7,(37,200))
    Sprite(numberButton,(45,270))
    Sprite(buttonText10,(37,258))
    Sprite(numberButton,(45,330))
    Sprite(buttonText13,(37,318))
    Sprite(numberButton,(45,390))
    Sprite(buttonText16,(37,380))
    Sprite(numberButton,(120,210))
    Sprite(buttonText8,(113,200))
    Sprite(numberButton,(120,270))
    Sprite(buttonText11,(114,258))
    Sprite(numberButton,(120,330))
    Sprite(buttonText14,(113,318))
    Sprite(numberButton,(120,390))
    Sprite(numberButton,(195,210))
    Sprite(buttonText9,(188,200))
    Sprite(numberButton,(195,270))
    Sprite(buttonText12,(188,258))
    Sprite(numberButton,(195,330))
    Sprite(buttonText15,(188,318))
    Sprite(numberButton,(195,390))

    Sprite(equalsClear,(45,150))
    Sprite(buttonText1,(30,140))
    Sprite(equalsClear,(120,150))
    Sprite(equalsClear,(195,150))

    Sprite(functionButton,(260,150))
    Sprite(buttonText2,(255,140))
    Sprite(functionButton,(260,210))
    Sprite(buttonText3,(255,198))
    Sprite(functionButton,(260,270))
    Sprite(buttonText4,(257,258))
    Sprite(functionButton,(260,330))
    Sprite(buttonText5,(255,320))
    Sprite(functionButton,(260,390))
    Sprite(buttonText6,(255,380))

    App().listenMouseEvent('click',mouseClick)
    App().run()

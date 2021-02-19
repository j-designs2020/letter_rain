from kivy.app import App
from kivy.uix.image import Image 
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
from kivy.core.audio import SoundLoader

import sys
import random
from datetime import datetime
random.seed(datetime.now())
import threading



class MainApp(App):
    def build(self):
        Fl = FloatLayout()
        
        #sounds
        blockSound = SoundLoader.load('/sounds/block.wav')
        coinSound = SoundLoader.load('/sounds/coin.wav')
        correctSound = SoundLoader.load('/sounds/correct.wav')
        dripSound = SoundLoader.load('/sounds/drip.wav')
        speedSound = SoundLoader.load('/sounds/speed.wav')
        wrongSound = SoundLoader.load('/sounds/wrong.wav')


        #game
        gameWidth = 800
        gameHeight = 600
        bgColor = (100,181,255)

        myFont = Label(font_name = "/fonts/dimbo.ttf", font_size=22)
        myFontb = Label(font_name = "/fonts/dimbo.ttf", font_size=22)
        myFont2 = Label(font_name = "/fonts/dimbo.ttf", font_size=10)
        myFont3 = Label(font_name = "/fonts/dimbo.ttf", font_size=18)
        myFont4 = Label(font_name = "/fonts/dimbo.ttf", font_size=65) 



        #player1
        playerColor = (100,100,100)
        playerSize = 60
        playerSizeL = 53
        playerPos = [(gameWidth/2)-(playerSize/2),gameHeight*.784]

        playerIMG = Image('/images/bucket.png') 

        MAIN_HEADER = Image(source='/images/clouds.png')
        MAIN_FOOTER = Image('/images/footer.png')
        TITLE_SCREEN =  Image('/images/title_screen.png')
        TUT_SCREEN = Image('/images/tut_screen.png')
        BLANK_BG = Image('/images/blank_bg.png')

        BLACK = (0,0,0)
        WHITE = (255,255,255)
        WORD_COLOR = (0,0,0)
        Color =  Image('/images/coin.gif') 
        Color2 = Image('/images/raindrop_red.png') 
        Color3 = Image('/images/raindrop_green.png') 
        Color4 = Image('/images/raindrop_blue.png') 
        Color5 = Image('/images/raindrop_purple.png')

        selectColor = (0,0,255)
        enemySizeL = 18
        enemySizeW = 18
        selectPos = [(gameWidth*.42),(gameHeight*.93)]
        select2Pos = [(gameWidth*.44),(gameHeight*.93)]
        select3Pos = [(gameWidth*.46),(gameHeight*.93)]
        select4Pos = [(gameWidth*.48),(gameHeight*.93)]
        select5Pos = [(gameWidth*.5),(gameHeight*.93)]
        select6Pos = [(gameWidth*.52),(gameHeight*.93)]
        select7Pos = [(gameWidth*.54),(gameHeight*.93)]
        select8Pos = [(gameWidth*.56),(gameHeight*.93)]
        select9Pos = [(gameWidth*.58),(gameHeight*.93)]
        select10Pos = [(gameWidth*.6),(gameHeight*.93)]
        select11Pos = [(gameWidth*.62),(gameHeight*.93)]
        select12Pos = [(gameWidth*.64),(gameHeight*.93)]
        enemyPos = [-90, -100]
        enemy2Pos = [-100,-100]
        enemy3Pos = [-100, -100]
        enemy4Pos = [-100, -100]
        enemy5Pos = [-100, -100]
        enemy6Pos = [-100, -100]
        enemy7Pos = [-100, -100]
        enemy8Pos = [-100, -100]
        enemyList = [enemyPos]
        enemyList2 = [enemy2Pos]
        enemyList3 = [enemy3Pos]
        enemyList4 = [enemy4Pos]
        enemyList5 = [enemy5Pos]
        enemyList6 = [enemy6Pos]
        enemyList7 = [enemy7Pos]
        enemyList8 = [enemy8Pos]
        enemyPosb = [-100, -100]
        enemy2Posb = [-100,-100]
        enemy3Posb = [-100, -100]
        enemy4Posb = [-100, -100]
        enemy5Posb = [-100, -100]
        enemy6Posb = [-100, -100]
        enemy7Posb = [-100, -100]
        enemy8Posb = [-100, -100]
        enemyListb = [enemyPos]
        enemyList2b = [enemy2Pos]
        enemyList3b = [enemy3Pos]
        enemyList4b = [enemy4Pos]
        enemyList5b = [enemy5Pos]
        enemyList6b = [enemy6Pos]
        enemyList7b = [enemy7Pos]
        enemyList8b = [enemy8Pos]
        BOX_LENGTH = gameHeight
        BOX_WIDTH = gameWidth
        boxPos = [0, 0]
        listCount = 0
        letters= ["abc"]
        letterList = [""]
        colorList = [Color, Color2, Color3, Color4, Color5]
        playerMove = .35
        playerMoveBoost = .85
        heightDelay = (gameHeight*.33)
        delay1a = 0
        delay1b = round(gameWidth*.0625)
        delay2a = round(gameWidth*.125)
        delay2b = round(gameWidth*.1875)
        delay3a = round(gameWidth*.25)
        delay3b = round(gameWidth*.3125)
        delay4a = round(gameWidth*.375)
        delay4b = round(gameWidth*.4375)
        delay5a = round(gameWidth*.5)
        delay5b = round(gameWidth*.5625)
        delay6a = round(gameWidth*.625)
        delay6b = round(gameWidth*.6875)
        delay7a = round(gameWidth*.75)
        delay7b = round(gameWidth*.8125)
        delay8a = round(gameWidth*.875)
        delay8b = round(gameWidth*.9375)


        global wordList
        wordList = []
        global wordScore
        wordScore = []
        global scoreList
        scoreList = []

        global wordCounter
        wordCounter = 0
        blankText = "" 

        scoreText = "SCORE:   "
        global scoreCount
        scoreCount = 0
        global scoreMinus
        scoreMinus = 0
        scorePos = [gameWidth * .83, gameHeight * .9]
        global scoreLabel
        scoreLabel = Label(color=ff3333, text=scoreText + format(scoreCount), markup = True)

        strikesText = "STRIKES: "
        global strikesCount
        strikesCount = 3
        strikesPos = [gameWidth * .03, gameHeight * .9]
        global strikesLabel
        strikesLabel = Label(text='[color=ffffff]' + strikesText + format(strikesCount)+'[/color]', markup = True)

        shieldText = "SHIELD: "
        global shieldOn
        shieldOn = 0
        global shieldLabel
        shieldLabel  = myFont2.render(shieldText + format(shieldOn), 1, BLACK)
        shieldPos = [gameWidth*.03, gameHeight*.93]

        speedText = "BOOST"
        global speedOn
        speedOn = False
        speedPos = [gameWidth * .03, gameHeight* .96]
        global speedLabel
        speedLabel  = myFont2.render(speedText, 1, WHITE)
        global speedTimer
        speedTimer = 0
        global boostsUsed
        boostsUsed = 0

        global boost1
        boost1 = False
        global boost2
        boost2 = False
        global boost3
        boost3 = False
        global boost4
        boost4 = False
        global boost5
        boost5 = False
        global boost6
        boost6 = False
        global boost7
        boost7 = False
        global boost8
        boost8 = False
        global boost1b
        boost1b = False
        global boost2b
        boost2b = False
        global boost3b
        boost3b = False
        global boost4b
        boost4b = False
        global boost5b
        boost5b = False
        global boost6b
        boost6b = False
        global boost7b
        boost7b = False
        global boost8b
        boost8b = False

        foundText = "FOUND: "
        global foundCount
        foundCount = 0
        foundPos = [gameWidth * .15, gameHeight *.9 ]
        global foundLabel
        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)

        wordLabelText = "WORD: "
        global wordLabel
        wordLabel = myFont3.render(wordLabelText, 1, BLACK)
        wordLabelPos = [gameWidth*.49, gameHeight*.9]

        lettersTextLabelText = "LETTERS: "
        global lettersTextLabel
        lettersTextLabel = myFont3.render(lettersTextLabelText, 1, WHITE)
        lettersTextLabelPos = [gameWidth*.15, gameHeight*.96]

        global shieldScore
        shieldScore = 0

        global strikesScore
        strikesScore = 0


        global strikes1
        strikes1 = False
        global strikes2
        strikes2 = False
        global strikes3
        strikes3 = False
        global strikes4
        strikes4 = False
        global strikes5
        strikes5 = False
        global strikes6
        strikes6 = False
        global strikes7
        strikes7 = False
        global strikes8
        strikes8 = False
        global strikes1b
        strikes1b = False
        global strikes2b
        strikes2b = False
        global strikes3b
        strikes3b = False
        global strikes4b
        strikes4b = False
        global strikes5b
        strikes5b = False
        global strikes6b
        strikes6b = False
        global strikes7b
        strikes7b = False
        global strikes8b
        strikes8b = False


        global shield1
        shield1 = False
        global shield2
        shield2 = False
        global shield3
        shield3 = False
        global shield4
        shield4 = False
        global shield5
        shield5 = False
        global shield6
        shield6 = False
        global shield7
        shield7 = False
        global shield8
        shield8 = False
        global shield1b
        shield1b = False
        global shield2b
        shield2b = False
        global shield3b
        shield3b = False
        global shield4b
        shield4b = False
        global shield5b
        shield5b = False
        global shield6b
        shield6b = False
        global shield7b
        shield7b = False
        global shield8b
        shield8b = False

        boughtGame = False
        gameStop = False
        startStop = False
        oneStop = False
        twoStop = False
        threeStop = False
        fourStop = False
        endStop = False
        tutStop = False

        global coin1
        coin1 = False
        global coin2
        coin2 = False
        global coin3
        coin3 = False
        global coin4
        coin4 = False
        global coin5
        coin5 = False
        global coin6
        coin6 = False
        global coin7
        coin7 = False
        global coin8
        coin8 = False
        global coin1b
        coin1b = False
        global coin2b
        coin2b = False
        global coin3b
        coin3b = False
        global coin4b
        coin4b = False
        global coin5b
        coin5b = False
        global coin6b
        coin6b = False
        global coin7b
        coin7b = False
        global coin8b
        coin8b = False

        global enemyText
        enemyText = ""
        global enemyText2
        enemyText2 = ""
        global enemyText3
        enemyText3 = ""
        global enemyText4
        enemyText4 = ""
        global enemyText5
        enemyText5 = ""
        global enemyText6
        enemyText6 = ""
        global enemyText7
        enemyText7 = ""
        global enemyText8
        enemyText8 = ""
        global enemyTextb
        enemyTextb = ""
        global enemyText2b
        enemyText2b = ""
        global enemyText3b
        enemyText3b = ""
        global enemyText4b
        enemyText4b = ""
        global enemyText5b
        enemyText5b = ""
        global enemyText6b
        enemyText6b = ""
        global enemyText7b
        enemyText7b = ""
        global enemyText8b
        enemyText8b = ""


        global dropDebug
        dropDebug = True
        global dropDebug2
        dropDebug2 = True
        global dropDebug3
        dropDebug3 = True
        global dropDebug4
        dropDebug4 = True
        global dropDebug5
        dropDebug5 = True
        global dropDebug6
        dropDebug6 = True
        global dropDebug7
        dropDebug7 = True
        global dropDebug8
        dropDebug8 = True

        global dropDebugb
        dropDebugb = True
        global dropDebug2b
        dropDebug2b = True
        global dropDebug3b
        dropDebug3b = True
        global dropDebug4b
        dropDebug4b = True
        global dropDebug5b
        dropDebug5b = True
        global dropDebug6b
        dropDebug6b = True
        global dropDebug7b
        dropDebug7b = True
        global dropDebug8b
        dropDebug8b = True



        global addCoin
        addCoin = 0
        coinText = "GOLD: " 
        coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
        coinPos = [gameWidth*.15, gameHeight*.93] 

        endGame = False

        lettersText = "A, C, E, H, T"
        lettersText2 = "A, C, D, E, T"
        lettersText3 = "C, D, E, O, T"
        lettersText4 = "D, E, M, O, T"
        lettersText5 = "D, E, F, M, O, Y"
        lettersText6 = "B, F, I, M, O, Y"
        lettersText7 = "A, B, F, I, M, Y"
        lettersText8 = "A, B, E, F, L, Y"
        lettersText9 = "A, E, G, P, I, U, S"
        lettersText10 = "E, G, I, O, R, S, U, V"
        lettersPos = [gameWidth * .23, gameHeight *.96 ]
        global lettersLabel
        lettersLabel = myFont3.render(lettersText, 1, WHITE) 

        global lettersAdd
        lettersAdd = ""
        global lettersUp
        lettersUp = myFont4.render(lettersAdd, 1, WHITE)

        global lettersShow2
        lettersShow2 = False
        global lettersShow3
        lettersShow3 = False
        global lettersShow4
        lettersShow4 = False
        global lettersShow5
        lettersShow5 = False
        global lettersShow6
        lettersShow6 = False
        global lettersShow7
        lettersShow7 = False
        global lettersShow8
        lettersShow8 = False
        global lettersShow9
        lettersShow9 = False
        global lettersShow10
        lettersShow10 = False


        global letterBlank
        letterBlank = False


        global scoreNum
        scoreNum = 0
        global scoreNum2
        scoreNum2 = 0
        global scoreAdd
        scoreAdd= ""
        global scoreAdd1
        scoreAdd1 = ""
        global scoreAdd2
        scoreAdd2 = ""
        global boostAdd
        boostAdd = ""

        global scoreUp
        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
        global scoreUpb
        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
        global scoreUpc
        scoreUpc = myFont4.render(scoreAdd2, 1, WHITE)
        global boostUp
        boostUp = myFont4.render(boostAdd, 1, WHITE)
        global scorePlus
        scorePlus = 0




        # LEVEL 1 LETTERS A, C, E, H, T
        global lvl1word1
        lvl1word1 = ["A", "C", "E"]
        global lvl1word2
        lvl1word2 = ["A", "C", "H", "E"]
        global lvl1word3
        lvl1word3 = ["A", "C", "T"]
        global lvl1word4
        lvl1word4 = ["A", "T"]
        global lvl1word5
        lvl1word5 = ["C", "A", "T"]
        global lvl1word6
        lvl1word6 = ["C", "H", "A", "T"]
        global lvl1word7
        lvl1word7 = ["C", "H", "E", "A", "T"]
        global lvl1word8
        lvl1word8 = ["E", "A", "C", "H"]
        global lvl1word9
        lvl1word9 = ["E", "A", "T"]
        global lvl1word10
        lvl1word10 = ["E", "T", "C", "H"]
        global lvl1word11
        lvl1word11 = ["H", "A", "T", "E"]
        global lvl1word12
        lvl1word12 = ["H", "A", "T"]
        global lvl1word13
        lvl1word13 = ["H", "E"]
        global lvl1word14
        lvl1word14 = ["H", "E", "A", "T"]
        global lvl1word15
        lvl1word15 = ["T", "E", "A"]
        global lvl1word16
        lvl1word16 = ["T", "E", "A", "C", "H"]
        global lvl1word17
        lvl1word17 = ["T", "E", "C", "H"]
        global lvl1word18
        lvl1word18 = ["T", "H", "E"]
        global lvl1word19
        lvl1word19 = ["T", "H", "E", "C", "A"]
        global lvl1word20
        lvl1word20 = ["C", "A", "T", "E"]
        global lvl1word21
        lvl1word21 = ["E", "A", "T", "H"]
        global lvl1word22
        lvl1word22 = ["C", "A", "C", "H", "E"]
        global lvl1word23
        lvl1word23 = ["C", "A", "T", "C", "H"]
        global lvl1word24
        lvl1word24 = ["H", "A", "T", "C", "H"]
        global lvl1word25
        lvl1word25 = ["H", "E", "A", "T", "H"]
        global lvl1word26
        lvl1word26 = ["T", "E", "E", "T", "H"]
        global lvl1word27
        lvl1word27 = ["H", "A", "T", "H"]
        global lvl1word28
        lvl1word28 = ["C", "A", "C", "A"]
        global lvl1word29
        lvl1word29 = ["T", "H", "E", "A"]
        global lvl1word30
        lvl1word30 = ["H", "E", "T"]
        global lvl1word31
        lvl1word31 = ["C", "H", "E", "T", "H"]
        global lvl1word32
        lvl1word32 = ["C", "A", "E", "C", "A"]
        global lvl1word33
        lvl1word33 = ["T", "A", "C", "H", "E"]
        global lvl1word34
        lvl1word34 = ["A", "C", "E", "T", "A"]
        global lvl1word35
        lvl1word35 = ["T", "A", "C", "E", "T"]
        global lvl1word36
        lvl1word36 = ["T", "E", "C", "T", "A"]
        global lvl1word37
        lvl1word37 = ["T", "H", "E", "T", "A"]
        global lvl1word38
        lvl1word38 = ["C", "A", "C", "H", "E", "T"]
        global lvl1word39
        lvl1word39 = ["C", "H", "E", "T", "A", "H"]
        global lvl1word40
        lvl1word40 = ["T", "H", "A", "T", "C", "H"]
        global lvl1word41
        lvl1word41 = ["A", "T", "T", "A", "C", "H"]
        global lvl1word42
        lvl1word42 = ["C", "H", "A", "E", "T", "A"]
        global lvl1word43
        lvl1word43 = ["T", "H", "E", "C", "A", "E"]
        global lvl1word44
        lvl1word44 = ["C", "A", "T", "H", "E", "C", "T"]
        global lvl1word45
        lvl1word45 = ["C", "H", "E", "E", "T", "A", "H"]
        global lvl1word46
        lvl1word46 = ["H", "A", "T", "C", "H", "E", "T"]
        global lvl1word47
        lvl1word47 = ["A", "T", "T", "A", "C", "H", "E"]
        global lvl1word48
        lvl1word48 = ["C", "H", "A", "E", "T", "A", "E"]
        global lvl1word49
        lvl1word49 = ["T", "H", "E", "C", "A", "T", "E"]
        global lvl1word50
        lvl1word50 = ["A", "C", "E", "T", "A", "T", "E"]
        global lvl1word51
        lvl1word51 = ["C", "E", "C", "A",]
        global lvl1word52
        lvl1word52 = ["E", "C", "H", "E"]
        global lvl1word53
        lvl1word53 = ["E", "C", "H", "T"]
        global lvl1word54
        lvl1word54 = ["T", "A", "C", "H"]
        global lvl1word55
        lvl1word55 = ["H", "A", "H", "A"]
        global lvl1word56
        lvl1word56 = ["H", "E", "T", "H"]
        global lvl1word57
        lvl1word57 = ["A", "C", "T", "A"]
        global lvl1word58
        lvl1word58 = ["C", "E", "T", "E"]
        global lvl1word59
        lvl1word59 = ["T", "A", "C", "E"]
        global lvl1word60
        lvl1word60 = ["T", "A", "C", "T"]
        global lvl1word61
        lvl1word61 = ["H", "A", "E", "T"]
        global lvl1word62
        lvl1word62 = ["T", "E", "T", "H"]
        global lvl1word63
        lvl1word63 = ["T", "H", "A", "E"]
        global lvl1word64
        lvl1word64 = ["H", "A", "H"]
        global lvl1word65
        lvl1word65 = ["H", "E", "H"]
        global lvl1word66
        lvl1word66 = ["C", "E", "E"]
        global lvl1word67
        lvl1word67 = ["A", "A", "H"]
        global lvl1word68
        lvl1word68 = ["A", "H", "A"]
        global lvl1word69
        lvl1word69 = ["E", "T", "H"]
        global lvl1word70
        lvl1word70 = ["H", "A", "E"]
        global lvl1word71
        lvl1word71 = ["A", "T", "T"]
        global lvl1word72
        lvl1word72 = ["E", "T", "A"]
        global lvl1word73
        lvl1word73 = ["T", "A", "E"]
        global lvl1word74
        lvl1word74 = ["T", "A", "T"]
        global lvl1word75
        lvl1word75 = ["T", "E", "T"]
        global lvl1word76
        lvl1word76 = ["T", "E", "C"]
        global lvl1word77
        lvl1word77 = ["A", "H"]
        global lvl1word78
        lvl1word78 = ["E", "H"]
        global lvl1word79
        lvl1word79 = ["H", "A"]
        global lvl1word80
        lvl1word80 = ["A", "A"]
        global lvl1word81
        lvl1word81 = ["A", "E"]
        global lvl1word82
        lvl1word82 = ["E", "T"]
        global lvl1word83
        lvl1word83 = ["T", "A"]
        global lvl1word84
        lvl1word84 = ["T", "E"]
        global lvl1word85
        lvl1word85 = ["C", "A", "C", "H", "A", "C", "A"]
        global lvl1word86
        lvl1word86 = ["T", "A", "T", "H", "A", "T", "A"]
        global lvl1word87
        lvl1word87 = ["T", "E", "E", "T", "H", "E"]
        global lvl1word88
        lvl1word88 = ["T", "E", "E"]



        # LEVEL 2 LETTERS A, C, D, E, T
        global lvl1word89
        lvl1word89 = ["D", "E", "T", "E", "C", "T", "E", "D"]
        global lvl1word90
        lvl1word90 = ["A", "C", "E", "T", "A", "T", "E", "D"]
        global lvl1word91
        lvl1word91 = ["A", "C", "C", "E", "D", "E", "D"]
        global lvl1word92
        lvl1word92 = ["A", "C", "C", "E", "D", "E"]
        global lvl1word93
        lvl1word93 = ["D", "E", "C", "A", "D", "E"]
        global lvl1word94
        lvl1word94 = ["C", "A", "T", "T", "E", "D"]
        global lvl1word95
        lvl1word95 = ["D", "E", "T", "E", "C", "T"]
        global lvl1word96
        lvl1word96 = ["D", "E", "E", "D", "E", "D"]
        global lvl1word97
        lvl1word97 = ["T", "E", "D", "D", "E", "D"]
        global lvl1word98
        lvl1word98 = ["T", "A", "T", "T", "E", "D"]
        global lvl1word99
        lvl1word99 = ["T", "E", "A", "T", "E", "D"]
        global lvl1word100
        lvl1word100 = ["C", "E", "D", "E", "D"]
        global lvl1word101
        lvl1word101 = ["A", "C", "T", "E", "D"]
        global lvl1word102
        lvl1word102 = ["C", "A", "D", "E", "T"]
        global lvl1word103
        lvl1word103 = ["A", "D", "D", "E", "D"]
        global lvl1word104
        lvl1word104 = ["D", "A", "T", "E", "D"]
        global lvl1word105
        lvl1word105 = ["A", "C", "E", "D"]
        global lvl1word106
        lvl1word106 = ["C", "A", "D", "E"]
        global lvl1word107
        lvl1word107 = ["C", "E", "D", "E"]
        global lvl1word108
        lvl1word108 = ["D", "A", "C", "E"]
        global lvl1word109
        lvl1word109 = ["D", "A", "D", "A"]
        global lvl1word110
        lvl1word110 = ["D", "E", "A", "D"]
        global lvl1word111
        lvl1word111 = ["D", "E", "E", "D"]
        global lvl1word112
        lvl1word112 = ["D", "A", "T", "A"]
        global lvl1word113
        lvl1word113 = ["D", "A", "T", "E"]
        global lvl1word114
        lvl1word114 = ["D", "E", "E", "T"]
        global lvl1word115
        lvl1word115 = ["T", "E", "E", "D"]
        global lvl1word116
        lvl1word116 = ["C", "A", "D"]
        global lvl1word117
        lvl1word117 = ["A", "D", "D"]
        global lvl1word118
        lvl1word118 = ["D", "A", "D"]
        global lvl1word119
        lvl1word119 = ["D", "E", "E"]
        global lvl1word120
        lvl1word120 = ["T", "A", "D"]
        global lvl1word121
        lvl1word121 = ["T", "E", "D"]
        global lvl1word122
        lvl1word122 = ["A", "D"]
        global lvl1word123
        lvl1word123 = ["D", "A"]
        global lvl1word124
        lvl1word124 = ["D", "E"]
        global lvl1word125
        lvl1word125 = ["E", "D"]



        # LEVEL 3 LETTERS C, D, E, O, T
        global lvl1word126
        lvl1word126 = ["D", "E", "C", "O", "C", "T", "E", "D"]
        global lvl1word127
        lvl1word127 = ["D", "E", "C", "O", "D", "E", "D"]
        global lvl1word128
        lvl1word128 = ["C", "O", "C", "O", "T", "T", "E"]
        global lvl1word129
        lvl1word129 = ["O", "C", "T", "E", "T", "T", "E"]
        global lvl1word130
        lvl1word130 = ["C", "O", "D", "D", "E", "D"]
        global lvl1word131
        lvl1word131 = ["D", "E", "C", "O", "C", "T"]
        global lvl1word132
        lvl1word132 = ["D", "E", "C", "O", "D", "E"]
        global lvl1word133
        lvl1word133 = ["C", "O", "O", "E", "E", "D"]
        global lvl1word134
        lvl1word134 = ["C", "O", "D", "E", "C"]
        global lvl1word135
        lvl1word135 = ["C", "O", "D", "E", "D"]
        global lvl1word136
        lvl1word136 = ["C", "O", "O", "E", "D"]
        global lvl1word137
        lvl1word137 = ["C", "O", "T", "E", "D"]
        global lvl1word138
        lvl1word138 = ["C", "O", "O", "E", "E"]
        global lvl1word139
        lvl1word139 = ["O", "C", "T", "E", "T"]
        global lvl1word140
        lvl1word140 = ["C", "O", "C", "O"]
        global lvl1word141
        lvl1word141 = ["C", "O", "D", "E"]
        global lvl1word142
        lvl1word142 = ["C", "O", "E", "D"]
        global lvl1word143
        lvl1word143 = ["D", "E", "C", "O"]
        global lvl1word144
        lvl1word144 = ["C", "O", "O", "T"]
        global lvl1word145
        lvl1word145 = ["C", "O", "T", "E"]
        global lvl1word146
        lvl1word146 = ["T", "O", "C", "O"]
        global lvl1word147
        lvl1word147 = ["C", "O", "D"]
        global lvl1word148
        lvl1word148 = ["D", "O", "C"]
        global lvl1word149
        lvl1word149 = ["C", "O", "O"]
        global lvl1word150
        lvl1word150 = ["C", "O", "T"]
        global lvl1word151
        lvl1word151 = ["E", "C", "O"]
        global lvl1word152
        lvl1word152 = ["D", "O", "O", "D", "O", "O"]
        global lvl1word153
        lvl1word153 = ["D", "O", "T", "T", "E", "D"]
        global lvl1word154
        lvl1word154 = ["T", "O", "O", "T", "E", "D"]
        global lvl1word155
        lvl1word155 = ["T", "O", "T", "T", "E", "D"]
        global lvl1word156
        lvl1word156 = ["D", "O", "T", "E", "D"]
        global lvl1word157
        lvl1word157 = ["T", "O", "T", "E", "D"]
        global lvl1word158
        lvl1word158 = ["D", "O", "D", "O"]
        global lvl1word159
        lvl1word159 = ["E", "D", "D", "O"]
        global lvl1word160
        lvl1word160 = ["D", "O", "T", "E"]
        global lvl1word161
        lvl1word161 = ["T", "O", "E", "D"]
        global lvl1word162
        lvl1word162 = ["O", "T", "T", "O"]
        global lvl1word163
        lvl1word163 = ["T", "O", "O", "T"]
        global lvl1word164
        lvl1word164 = ["T", "O", "T", "E"]
        global lvl1word165
        lvl1word165 = ["O", "D", "D"]
        global lvl1word166
        lvl1word166 = ["D", "O", "E"]
        global lvl1word167
        lvl1word167 = ["D", "O", "T"]
        global lvl1word168
        lvl1word168 = ["O", "D", "E"]
        global lvl1word169
        lvl1word169 = ["T", "O", "D"]
        global lvl1word170
        lvl1word170 = ["O", "O", "T"]
        global lvl1word171
        lvl1word171 = ["T", "O", "E"]
        global lvl1word172
        lvl1word172 = ["T", "O", "O"]
        global lvl1word173
        lvl1word173 = ["T", "O", "T"]
        global lvl1word174
        lvl1word174 = ["D", "O"]
        global lvl1word175
        lvl1word175 = ["O", "D"]
        global lvl1word176
        lvl1word176 = ["O", "E"]
        global lvl1word177
        lvl1word177 = ["T", "O"]

        #LEVEL 1 ADDITION
        global lvl1word178
        lvl1word178 = ["A", "T", "E"]


        # LEVEL 4 LETTERS D, E, M, O, T
        global lvl1word179
        lvl1word179 = ["M", "O", "D", "E", "M", "E", "D"]
        global lvl1word180
        lvl1word180 = ["D", "E", "M", "O", "D", "E", "D"]
        global lvl1word181
        lvl1word181 = ["D", "E", "M", "O", "T", "E", "D"]
        global lvl1word182
        lvl1word182 = ["T", "O", "M", "M", "E", "D"]
        global lvl1word183
        lvl1word183 = ["D", "E", "E", "M", "E", "D"]
        global lvl1word184
        lvl1word184 = ["D", "E", "M", "O", "D", "E"]
        global lvl1word185
        lvl1word185 = ["D", "E", "M", "O", "E", "D"]
        global lvl1word186
        lvl1word186 = ["D", "O", "O", "M", "E", "D"]
        global lvl1word187
        lvl1word187 = ["M", "O", "T", "M", "O", "T"]
        global lvl1word188
        lvl1word188 = ["D", "E", "M", "O", "T", "E"]
        global lvl1word189
        lvl1word189 = ["E", "M", "O", "T", "E", "D"]
        global lvl1word190
        lvl1word190 = ["M", "O", "O", "T", "E", "D"]
        global lvl1word191
        lvl1word191 = ["T", "E", "E", "M", "E", "D"]
        global lvl1word192
        lvl1word192 = ["M", "O", "D", "D", "E", "D"]
        global lvl1word193
        lvl1word193 = ["M", "O", "D", "E", "M"]
        global lvl1word194
        lvl1word194 = ["D", "O", "M", "E", "D"]
        global lvl1word195
        lvl1word195 = ["E", "M", "M", "E", "T"]
        global lvl1word196
        lvl1word196 = ["M", "E", "T", "E", "D"]
        global lvl1word197
        lvl1word197 = ["M", "O", "O", "E", "D"]
        global lvl1word198
        lvl1word198 = ["E", "M", "O", "T", "E"]
        global lvl1word199
        lvl1word199 = ["M", "O", "T", "E", "T"]
        global lvl1word200
        lvl1word200 = ["M", "O", "T", "T", "E"]
        global lvl1word201
        lvl1word201 = ["M", "O", "T", "T", "O"]
        global lvl1word202
        lvl1word202 = ["T", "O", "T", "E", "M"]
        global lvl1word203
        lvl1word203 = ["T", "O", "M", "M", "E"]
        global lvl1word204
        lvl1word204 = ["M", "E", "M", "E"]
        global lvl1word205
        lvl1word205 = ["M", "E", "M", "O"]
        global lvl1word206
        lvl1word206 = ["M", "O", "M", "E"]
        global lvl1word207
        lvl1word207 = ["D", "E", "E", "M"]
        global lvl1word208
        lvl1word208 = ["D", "E", "M", "E"]
        global lvl1word209
        lvl1word209= ["D", "E", "M", "O"]
        global lvl1word210
        lvl1word210 = ["D", "O", "M", "E"]
        global lvl1word211
        lvl1word211 = ["D", "O", "O", "M"]
        global lvl1word212
        lvl1word212 = ["M", "E", "E", "D"]
        global lvl1word213
        lvl1word213 = ["M", "O", "D", "E"]
        global lvl1word214
        lvl1word214 = ["M", "O", "O", "D"]
        global lvl1word215
        lvl1word215 = ["M", "E", "E", "T"]
        global lvl1word216
        lvl1word216 = ["M", "E", "T", "E"]
        global lvl1word217
        lvl1word217 = ["M", "O", "O", "T"]
        global lvl1word218
        lvl1word218 = ["M", "O", "T", "E"]
        global lvl1word219
        lvl1word219 = ["M", "O", "T", "T"]
        global lvl1word220
        lvl1word220 = ["T", "E", "E", "M"]
        global lvl1word221
        lvl1word221 = ["T", "O", "M", "E"]
        global lvl1word222
        lvl1word222 = ["T", "O", "O", "M"]
        global lvl1word223
        lvl1word223 = ["M", "M", "M"]
        global lvl1word224
        lvl1word224 = ["M", "E", "M"]
        global lvl1word225
        lvl1word225 = ["M", "O", "M"]
        global lvl1word226
        lvl1word226 = ["D", "O", "M"]
        global lvl1word227
        lvl1word227 = ["M", "E", "D"]
        global lvl1word228
        lvl1word228 = ["M", "O", "D"]
        global lvl1word229
        lvl1word229 = ["E", "M", "E"]
        global lvl1word230
        lvl1word230 = ["E", "M", "O"]
        global lvl1word231
        lvl1word231 = ["M", "E", "T"]
        global lvl1word232
        lvl1word232 = ["M", "O", "O"]
        global lvl1word233
        lvl1word233 = ["M", "O", "T"]
        global lvl1word234
        lvl1word234 = ["T", "O", "M"]
        global lvl1word235
        lvl1word235 = ["M", "M"]
        global lvl1word236
        lvl1word236 = ["E", "M"]
        global lvl1word237
        lvl1word237 = ["M", "E"]
        global lvl1word238
        lvl1word238 = ["M", "O"]
        global lvl1word239
        lvl1word239 = ["O", "M"]


        # LEVEL 5 LETTERS D, E, F, M, O, Y
        global lvl1word240
        lvl1word240 = ["F", "E", "O", "F", "F", "E", "D"]
        global lvl1word241
        lvl1word241 = ["F", "E", "O", "F", "F", "E", "E"]
        global lvl1word242
        lvl1word242 = ["D", "O", "F", "F", "E", "D"]
        global lvl1word243
        lvl1word243 = ["D", "E", "E", "D", "Y"]
        global lvl1word244
        lvl1word244 = ["D", "E", "F", "F", "O"]
        global lvl1word245
        lvl1word245 = ["D", "O", "D", "D", "Y"]
        global lvl1word246
        lvl1word246 = ["D", "O", "O", "D", "Y"]
        global lvl1word247
        lvl1word247 = ["D", "O", "O", "M", "Y"]
        global lvl1word248
        lvl1word248 = ["E", "F", "F", "E", "D"]
        global lvl1word249
        lvl1word249 = ["E", "M", "Y", "D", "E"]
        global lvl1word250
        lvl1word250 = ["F", "E", "M", "M", "E"]
        global lvl1word251
        lvl1word251 = ["F", "E", "M", "M", "Y"]
        global lvl1word252
        lvl1word252 = ["F", "E", "O", "F", "F"]
        global lvl1word253
        lvl1word253 = ["F", "E", "Y", "E", "D"]
        global lvl1word254
        lvl1word254 = ["F", "O", "O", "D", "Y"]
        global lvl1word255
        lvl1word255 = ["M", "O", "M", "M", "Y"]
        global lvl1word256
        lvl1word256 = ["M", "O", "O", "D", "Y"]
        global lvl1word257
        lvl1word257 = ["O", "F", "F", "E", "D"]
        global lvl1word258
        lvl1word258 = ["D", "E", "F", "O"]
        global lvl1word259
        lvl1word259 = ["D", "E", "F", "Y"]
        global lvl1word260
        lvl1word260 = ["D", "E", "M", "Y"]
        global lvl1word261
        lvl1word261 = ["D", "O", "F", "F"]
        global lvl1word262
        lvl1word262 = ["D", "O", "M", "Y"]
        global lvl1word263
        lvl1word263 = ["D", "Y", "E", "D"]
        global lvl1word264
        lvl1word264 = ["E", "D", "D", "Y"]
        global lvl1word265
        lvl1word265 = ["E", "M", "M", "Y"]
        global lvl1word266
        lvl1word266 = ["E", "M", "Y", "D"]
        global lvl1word267
        lvl1word267 = ["E", "Y", "E", "D"]
        global lvl1word268
        lvl1word268 = ["F", "E", "E", "D"]
        global lvl1word269
        lvl1word269 = ["F", "E", "M", "E"]
        global lvl1word270
        lvl1word270 = ["F", "E", "O", "D"]
        global lvl1word271
        lvl1word271 = ["F", "O", "O", "D"]
        global lvl1word272
        lvl1word272 = ["M", "E", "F", "F"]
        global lvl1word273
        lvl1word273 = ["M", "O", "F", "O"]
        global lvl1word274
        lvl1word274 = ["O", "F", "F", "Y"]
        global lvl1word275
        lvl1word275 = ["O", "O", "F", "Y"]
        global lvl1word276
        lvl1word276 = ["Y", "E", "D", "E"]
        global lvl1word277
        lvl1word277 = ["Y", "E", "E", "D"]
        global lvl1word278
        lvl1word278 = ["Y", "O", "D", "E"]
        global lvl1word279
        lvl1word279 = ["Y", "O", "O", "F"]
        global lvl1word280
        lvl1word280 = ["D", "E", "F"]
        global lvl1word281
        lvl1word281 = ["D", "E", "Y"]
        global lvl1word282
        lvl1word282 = ["D", "O", "F"]
        global lvl1word283
        lvl1word283 = ["D", "O", "Y"]
        global lvl1word284
        lvl1word284 = ["D", "Y", "E"]
        global lvl1word285
        lvl1word285 = ["E", "F", "F"]
        global lvl1word286
        lvl1word286 = ["E", "Y", "E"]
        global lvl1word287
        lvl1word287 = ["F", "E", "D"]
        global lvl1word288
        lvl1word288 = ["F", "E", "E"]
        global lvl1word289
        lvl1word289 = ["F", "E", "M"]
        global lvl1word290
        lvl1word290 = ["F", "E", "Y"]
        global lvl1word291
        lvl1word291 = ["F", "O", "E"]
        global lvl1word292
        lvl1word292 = ["F", "O", "O"]
        global lvl1word293
        lvl1word293 = ["F", "O", "Y"]
        global lvl1word294
        lvl1word294 = ["M", "O", "Y"]
        global lvl1word295
        lvl1word295 = ["O", "F", "F"]
        global lvl1word296
        lvl1word296 = ["O", "O", "F"]
        global lvl1word297
        lvl1word297 = ["Y", "O", "D"]
        global lvl1word298
        lvl1word298 = ["Y", "O", "M"]
        global lvl1word299
        lvl1word299 = ["M", "Y"]
        global lvl1word300
        lvl1word300 = ["E", "F"]
        global lvl1word301
        lvl1word301 = ["F", "E"]
        global lvl1word302
        lvl1word302 = ["O", "F"]
        global lvl1word303
        lvl1word303 = ["O", "Y"]
        global lvl1word304
        lvl1word304 = ["Y", "E"]
        global lvl1word305
        lvl1word305 = ["Y", "O"]


        # LEVEL 6 LETTERS B, F, I, M, O, Y


        global lvl1word306
        lvl1word306 = ["B", "I", "F", "F", "Y"]
        global lvl1word307
        lvl1word307 = ["M", "I", "F", "F", "Y"]
        global lvl1word308
        lvl1word308 = ["Y", "O", "B", "B", "Y"]
        global lvl1word309
        lvl1word309 = ["B", "O", "F", "F", "O"]
        global lvl1word310
        lvl1word310 = ["B", "O", "O", "B", "Y"]
        global lvl1word311
        lvl1word311 = ["B", "O", "O", "M", "Y"]
        global lvl1word312
        lvl1word312 = ["Y", "O", "B", "B", "O"]
        global lvl1word313
        lvl1word313 = ["Y", "O", "M", "I", "M"]
        global lvl1word314
        lvl1word314 = ["B", "I", "M", "B", "O"]
        global lvl1word315
        lvl1word315 = ["I", "F", "F", "Y"]
        global lvl1word316
        lvl1word316 = ["B", "I", "F", "F"]
        global lvl1word317
        lvl1word317 = ["B", "O", "F", "F"]
        global lvl1word318
        lvl1word318 = ["M", "I", "F", "F"]
        global lvl1word319
        lvl1word319 = ["I", "M", "M", "Y"]
        global lvl1word320
        lvl1word320 = ["B", "O", "M", "B"]
        global lvl1word322
        lvl1word322 = ["B", "O", "Y", "O"]
        global lvl1word323
        lvl1word323 = ["B", "O", "B", "O"]
        global lvl1word324
        lvl1word324 = ["B", "O", "O", "B"]
        global lvl1word325
        lvl1word325 = ["B", "O", "O", "M"]
        global lvl1word326
        lvl1word326 = ["M", "O", "M", "I"]
        global lvl1word327
        lvl1word327 = ["I", "F", "F"]
        global lvl1word328
        lvl1word328 = ["B", "O", "Y"]
        global lvl1word329
        lvl1word329 = ["F", "I", "B"]
        global lvl1word330
        lvl1word330 = ["F", "O", "B"]
        global lvl1word331
        lvl1word331 = ["Y", "O", "B"]
        global lvl1word332
        lvl1word332 = ["B", "I", "B"]
        global lvl1word333
        lvl1word333 = ["B", "O", "B"]
        global lvl1word334
        lvl1word334 = ["M", "I", "B"]
        global lvl1word335
        lvl1word335 = ["M", "I", "M"]
        global lvl1word336
        lvl1word336 = ["M", "O", "B"]
        global lvl1word337
        lvl1word337 = ["B", "I", "O"]
        global lvl1word338
        lvl1word338 = ["B", "O", "O"]
        global lvl1word339
        lvl1word339 = ["M", "O", "I"]
        global lvl1word340
        lvl1word340 = ["O", "B", "I"]
        global lvl1word341
        lvl1word341 = ["B", "Y"]
        global lvl1word342
        lvl1word342 = ["I", "F"]
        global lvl1word343
        lvl1word343 = ["B", "I"]
        global lvl1word344
        lvl1word344 = ["B", "O"]
        global lvl1word345
        lvl1word345 = ["M", "I"]
        global lvl1word346
        lvl1word346 = ["O", "I"]

        # LEVEL 1 ADDITION

        global lvl1word347
        lvl1word347 = ["T", "H", "A", "T"]


        # LEVEL 7 LETTERS A, B, F, I, M, Y


        global lvl1word348
        lvl1word348 = ["M", "A", "F", "F", "I", "A"]
        global lvl1word349
        lvl1word349 = ["B", "A", "F", "F", "Y"]
        global lvl1word350
        lvl1word350 = ["Y", "A", "B", "B", "Y"]
        global lvl1word351
        lvl1word351 = ["A", "Y", "A", "Y", "A"]
        global lvl1word352
        lvl1word352 = ["M", "A", "M", "B", "A"]
        global lvl1word353
        lvl1word353 = ["A", "B", "A", "Y", "A"]
        global lvl1word354
        lvl1word354 = ["M", "A", "F", "I", "A"]
        global lvl1word355
        lvl1word355 = ["I", "A", "B", "M", "I"]
        global lvl1word356
        lvl1word356 = ["Y", "A", "F", "F"]
        global lvl1word357
        lvl1word357 = ["B", "A", "F", "F"]
        global lvl1word358
        lvl1word358 = ["B", "A", "B", "Y"]
        global lvl1word359
        lvl1word359 = ["M", "A", "Y", "A"]
        global lvl1word360
        lvl1word360 = ["A", "B", "B", "A"]
        global lvl1word361
        lvl1word361 = ["B", "A", "B", "A"]
        global lvl1word362
        lvl1word362 = ["B", "I", "M", "A"]
        global lvl1word363
        lvl1word363 = ["I", "A", "M", "B"]
        global lvl1word364
        lvl1word364 = ["I", "M", "A", "M"]
        global lvl1word365
        lvl1word365 = ["M", "A", "I", "M"]
        global lvl1word366
        lvl1word366 = ["M", "A", "M", "A"]
        global lvl1word367
        lvl1word367 = ["A", "M", "I", "A"]
        global lvl1word368
        lvl1word368 = ["A", "F", "F"]
        global lvl1word369
        lvl1word369 = ["F", "A", "Y"]
        global lvl1word370
        lvl1word370 = ["Y", "A", "Y"]
        global lvl1word371
        lvl1word371 = ["A", "B", "Y"]
        global lvl1word372
        lvl1word372 = ["B", "A", "Y"]
        global lvl1word373
        lvl1word373 = ["F", "A", "B"]
        global lvl1word374
        lvl1word374 = ["M", "A", "Y"]
        global lvl1word375
        lvl1word375 = ["Y", "A", "M"]
        global lvl1word376
        lvl1word376 = ["B", "A", "M"]
        global lvl1word377
        lvl1word377 = ["M", "A", "M"]
        global lvl1word378
        lvl1word378 = ["A", "B", "A"]
        global lvl1word379
        lvl1word379 = ["A", "I", "M"]
        global lvl1word380
        lvl1word380 = ["A", "M", "A"]
        global lvl1word381
        lvl1word381 = ["A", "M", "I"]
        global lvl1word382
        lvl1word382 = ["B", "A", "A"]
        global lvl1word383
        lvl1word383 = ["A", "Y"]
        global lvl1word384
        lvl1word384 = ["F", "A"]
        global lvl1word385
        lvl1word385 = ["Y", "A"]
        global lvl1word386
        lvl1word386 = ["A", "B"]
        global lvl1word387
        lvl1word387 = ["A", "M"]
        global lvl1word388
        lvl1word388 = ["B", "A"]
        global lvl1word389
        lvl1word389 = ["M", "A"]
        global lvl1word390
        lvl1word390 = ["A", "I"]


        # LEVEL 8 LETTERS A, B, E, F, L, Y


        global lvl1word391
        lvl1word391 = ["L", "A", "B", "E", "L", "A", "B", "L", "E"]
        global lvl1word392
        lvl1word392 = ["F", "E", "L", "L", "A", "B", "L", "E"]
        global lvl1word393
        lvl1word393 = ["F", "L", "A", "B", "E", "L", "L", "A"]
        global lvl1word394
        lvl1word394 = ["A", "F", "F", "A", "B", "L", "E"]
        global lvl1word395
        lvl1word395 = ["A", "F", "F", "A", "B", "L", "Y"]
        global lvl1word396
        lvl1word396 = ["A", "L", "F", "A", "L", "F", "A"]
        global lvl1word397
        lvl1word397 = ["E", "F", "F", "A", "B", "L", "E"]
        global lvl1word398
        lvl1word398 = ["E", "Y", "E", "A", "B", "L", "E"]
        global lvl1word399
        lvl1word399 = ["F", "A", "L", "A", "F", "E", "L"]
        global lvl1word400
        lvl1word400 = ["F", "A", "L", "B", "A", "L", "A"]
        global lvl1word401
        lvl1word401 = ["F", "E", "L", "A", "F", "E", "L"]
        global lvl1word402
        lvl1word402 = ["F", "L", "Y", "A", "B", "L", "E"]
        global lvl1word403
        lvl1word403 = ["F", "L", "Y", "L", "E", "A", "F"]
        global lvl1word404
        lvl1word404 = ["L", "A", "B", "E", "L", "L", "A"]
        global lvl1word405
        lvl1word405 = ["E", "Y", "E", "B", "A", "L", "L"]
        global lvl1word406
        lvl1word406 = ["A", "L", "E", "L", "L", "E"]
        global lvl1word407
        lvl1word407 = ["B", "A", "B", "B", "L", "E"]
        global lvl1word408
        lvl1word408 = ["B", "A", "B", "B", "L", "Y"]
        global lvl1word409
        lvl1word409 = ["F", "E", "E", "B", "L", "E"]
        global lvl1word410
        lvl1word410 = ["A", "L", "L", "Y", "L"]
        global lvl1word411
        lvl1word411 = ["A", "Y", "A", "Y", "A"]
        global lvl1word412
        lvl1word412 = ["B", "E", "L", "E", "E"]
        global lvl1word413
        lvl1word413 = ["F", "L", "A", "F", "F"]
        global lvl1word414
        lvl1word414 = ["F", "L", "A", "B", "B", "Y"]
        global lvl1word415
        lvl1word415 = ["Y", "A", "F", "F", "L", "E"]
        global lvl1word416
        lvl1word416 = ["B", "A", "F", "F", "L", "E"]
        global lvl1word417
        lvl1word417 = ["F", "E", "E", "B", "L", "Y"]
        global lvl1word418
        lvl1word418 = ["B", "E", "F", "A", "L", "L"]
        global lvl1word419
        lvl1word419 = ["B", "E", "F", "E", "L", "L"]
        global lvl1word420
        lvl1word420 = ["B", "E", "F", "L", "E", "A"]
        global lvl1word421
        lvl1word421 = ["B", "L", "E", "B", "B", "Y"]
        global lvl1word422
        lvl1word422 = ["F", "A", "L", "A", "L", "L"]
        global lvl1word423
        lvl1word423 = ["L", "E", "A", "L", "L", "Y"]
        global lvl1word424
        lvl1word424 = ["A", "B", "B", "E", "Y"]
        global lvl1word425
        lvl1word425 = ["A", "B", "E", "L", "E"]
        global lvl1word426
        lvl1word426 = ["A", "L", "B", "E", "E"]
        global lvl1word427
        lvl1word427 = ["A", "L", "E", "Y", "E"]
        global lvl1word428
        lvl1word428 = ["A", "L", "L", "A", "Y"]
        global lvl1word429
        lvl1word429 = ["A", "L", "L", "E", "E"]
        global lvl1word430
        lvl1word430 = ["A", "L", "L", "E", "Y"]
        global lvl1word431
        lvl1word431 = ["B", "A", "B", "E", "L"]
        global lvl1word432
        lvl1word432 = ["B", "A", "L", "L", "Y"]
        global lvl1word433
        lvl1word433 = ["B", "A", "Y", "L", "E"]
        global lvl1word434
        lvl1word434 = ["B", "E", "L", "A", "Y"]
        global lvl1word435
        lvl1word435 = ["B", "E", "L", "L", "E"]
        global lvl1word436
        lvl1word436 = ["B", "E", "L", "L", "Y"]
        global lvl1word437
        lvl1word437 = ["B", "L", "A", "F", "F"]
        global lvl1word438
        lvl1word438 = ["F", "A", "B", "L", "E"]
        global lvl1word439
        lvl1word439 = ["F", "E", "L", "L", "A"]
        global lvl1word440
        lvl1word440 = ["F", "E", "L", "L", "Y"]
        global lvl1word441
        lvl1word441 = ["F", "E", "Y", "L", "Y"]
        global lvl1word442
        lvl1word442 = ["F", "L", "Y", "B", "Y"]
        global lvl1word443
        lvl1word443 = ["L", "A", "B", "E", "L"]
        global lvl1word444
        lvl1word444 = ["L", "E", "A", "F", "Y"]
        global lvl1word445
        lvl1word445 = ["A", "B", "B", "E"]
        global lvl1word446
        lvl1word446 = ["A", "B", "L", "E"]
        global lvl1word447
        lvl1word447 = ["A", "B", "L", "Y"]
        global lvl1word448
        lvl1word448 = ["A", "L", "L", "E", "E"]
        global lvl1word449
        lvl1word449 = ["A", "B", "Y", "E"]
        global lvl1word450
        lvl1word450 = ["A", "F", "F", "Y"]
        global lvl1word451
        lvl1word451 = ["A", "L", "A", "E"]
        global lvl1word452
        lvl1word452 = ["A", "L", "A", "Y"]
        global lvl1word453
        lvl1word453 = ["A", "L", "B", "A"]
        global lvl1word454
        lvl1word454 = ["A", "L", "B", "E"]
        global lvl1word455
        lvl1word455 = ["A", "L", "E", "E"]
        global lvl1word456
        lvl1word456 = ["A", "L", "E", "F"]
        global lvl1word457
        lvl1word457 = ["A", "L", "F", "A"]
        global lvl1word458
        lvl1word458 = ["A", "L", "L", "Y"]
        global lvl1word459
        lvl1word459 = ["B", "A", "A", "L"]
        global lvl1word460
        lvl1word460 = ["B", "A", "B", "E"]
        global lvl1word461
        lvl1word461 = ["B", "A", "E", "L"]
        global lvl1word462
        lvl1word462 = ["B", "A", "L", "E"]
        global lvl1word463
        lvl1word463 = ["B", "A", "L", "L"]
        global lvl1word464
        lvl1word464 = ["B", "A", "Y", "E"]
        global lvl1word465
        lvl1word465 = ["B", "E", "A", "L"]
        global lvl1word466
        lvl1word466 = ["B", "E", "E", "F"]
        global lvl1word467
        lvl1word467 = ["B", "E", "L", "L"]
        global lvl1word468
        lvl1word468 = ["B", "L", "A", "B"]
        global lvl1word469
        lvl1word469 = ["B", "L", "A", "E"]
        global lvl1word470
        lvl1word470 = ["B", "L", "E", "B"]
        global lvl1word471
        lvl1word471 = ["B", "L", "E", "E"]
        global lvl1word472
        lvl1word472 = ["B", "L", "E", "Y"]
        global lvl1word473
        lvl1word473 = ["E", "A", "L", "E"]
        global lvl1word474
        lvl1word474 = ["E", "E", "L", "Y"]
        global lvl1word475
        lvl1word475 = ["F", "A", "L", "L"]
        global lvl1word476
        lvl1word476 = ["F", "E", "A", "L"]
        global lvl1word477
        lvl1word477 = ["F", "E", "E", "B"]
        global lvl1word478
        lvl1word478 = ["F", "E", "E", "L"]
        global lvl1word479
        lvl1word479 = ["F", "L", "A", "B"]
        global lvl1word480
        lvl1word480 = ["F", "L", "A", "Y"]
        global lvl1word481
        lvl1word481 = ["F", "L", "E", "A"]
        global lvl1word482
        lvl1word482 = ["F", "L", "E", "E"]
        global lvl1word483
        lvl1word483 = ["F", "L", "E", "Y"]
        global lvl1word484
        lvl1word484 = ["F", "Y", "L", "E"]
        global lvl1word485
        lvl1word485 = ["L", "A", "L", "L"]
        global lvl1word486
        lvl1word486 = ["L", "E", "A", "F"]
        global lvl1word487
        lvl1word487 = ["L", "E", "A", "L"]
        global lvl1word488
        lvl1word488 = ["Y", "A", "L", "E"]
        global lvl1word489
        lvl1word489 = ["Y", "E", "L", "L"]
        global lvl1word490
        lvl1word490 = ["A", "A", "L"]
        global lvl1word491
        lvl1word491 = ["A", "L", "A"]
        global lvl1word492
        lvl1word492 = ["A", "L", "B"]
        global lvl1word493
        lvl1word493 = ["A", "L", "E"]
        global lvl1word494
        lvl1word494 = ["A", "L", "F"]
        global lvl1word495
        lvl1word495 = ["A", "L", "L"]
        global lvl1word496
        lvl1word496 = ["A", "Y", "E"]
        global lvl1word497
        lvl1word497 = ["B", "A", "L"]
        global lvl1word498
        lvl1word498 = ["B", "E", "E"]
        global lvl1word499
        lvl1word499 = ["B", "E", "L"]
        global lvl1word500
        lvl1word500 = ["B", "E", "Y"]
        global lvl1word501
        lvl1word501 = ["B", "Y", "E"]
        global lvl1word502
        lvl1word502 = ["E", "B", "B"]
        global lvl1word503
        lvl1word503 = ["E", "E", "L"]
        global lvl1word504
        lvl1word504 = ["E", "F", "F"]
        global lvl1word505
        lvl1word505 = ["E", "L", "F"]
        global lvl1word506
        lvl1word506 = ["E", "L", "L"]
        global lvl1word507
        lvl1word507 = ["E", "Y", "E"]
        global lvl1word508
        lvl1word508 = ["F", "E", "E"]
        global lvl1word509
        lvl1word509 = ["F", "E", "Y"]
        global lvl1word510
        lvl1word510 = ["F", "L", "Y"]
        global lvl1word511
        lvl1word511 = ["L", "A", "B"]
        global lvl1word512
        lvl1word512 = ["L", "A", "Y"]
        global lvl1word513
        lvl1word513 = ["L", "E", "A"]
        global lvl1word514
        lvl1word514 = ["L", "E", "E"]
        global lvl1word515
        lvl1word515 = ["L", "E", "Y"]
        global lvl1word516
        lvl1word516 = ["L", "Y", "E"]
        global lvl1word517
        lvl1word517 = ["Y", "E", "A"]
        global lvl1word518
        lvl1word518 = ["B", "E"]
        global lvl1word519
        lvl1word519 = ["A", "E"]
        global lvl1word520
        lvl1word520 = ["A", "L"]
        global lvl1word521
        lvl1word521 = ["E", "L"]
        global lvl1word522
        lvl1word522 = ["L", "A"]



        # LEVEL 9 LETTERS A, E, G, P, I, U, S
        global lvl1word523
        lvl1word523 = ["E", "I", "S", "E", "G", "E", "S", "E", "S"]
        global lvl1word524
        lvl1word524 = ["E", "I", "S", "E", "G", "E", "S", "I", "S"]
        global lvl1word525
        lvl1word525 = ["E", "U", "P", "E", "P", "S", "I", "A", "S"]
        global lvl1word526
        lvl1word526 = ["E", "U", "P", "E", "P", "S", "I", "E", "S"]
        global lvl1word527
        lvl1word527 = ["A", "P", "P", "E", "A", "S", "E", "S"]
        global lvl1word528
        lvl1word528 = ["A", "S", "S", "A", "G", "A", "I", "S"]
        global lvl1word529
        lvl1word529 = ["A", "S", "S", "E", "G", "A", "I", "S"]
        global lvl1word530
        lvl1word530 = ["A", "S", "S", "U", "A", "G", "E", "S"]
        global lvl1word531
        lvl1word531 = ["E", "U", "P", "E", "P", "S", "I", "A"]
        global lvl1word532
        lvl1word532 = ["P", "A", "S", "S", "A", "G", "E", "S"]
        global lvl1word533
        lvl1word533 = ["P", "A", "S", "S", "U", "S", "E", "S"]
        global lvl1word534
        lvl1word534 = ["P", "I", "P", "E", "A", "G", "E", "S"]
        global lvl1word535
        lvl1word535 = ["S", "A", "U", "S", "A", "G", "E", "S"]
        global lvl1word536
        lvl1word536 = ["S", "E", "E", "P", "A", "G", "E", "S"]
        global lvl1word537
        lvl1word537 = ["S", "P", "E", "I", "S", "S", "E", "S"]
        global lvl1word538
        lvl1word538 = ["A", "E", "G", "I", "S", "E", "S"]
        global lvl1word539
        lvl1word539 = ["A", "P", "P", "E", "A", "S", "E"]
        global lvl1word540
        lvl1word540 = ["A", "S", "E", "P", "S", "E", "S"]
        global lvl1word541
        lvl1word541 = ["A", "S", "E", "P", "S", "I", "S"]
        global lvl1word542
        lvl1word542 = ["A", "S", "S", "A", "G", "A", "I"]
        global lvl1word543
        lvl1word543 = ["A", "S", "S", "I", "E", "G", "E"]
        global lvl1word544
        lvl1word544 = ["A", "S", "S", "U", "A", "G", "E"]
        global lvl1word545
        lvl1word545 = ["G", "A", "U", "S", "S", "E", "S"]
        global lvl1word546
        lvl1word546 = ["A", "S", "P", "E", "S", "E", "S"]
        global lvl1word547
        lvl1word547 = ["G", "I", "P", "S", "I", "E", "S"]
        global lvl1word548
        lvl1word548 = ["G", "U", "E", "S", "S", "E", "S"]
        global lvl1word549
        lvl1word549 = ["G", "U", "P", "P", "I", "E", "S"]
        global lvl1word550
        lvl1word550 = ["G", "U", "S", "S", "I", "E", "S"]
        global lvl1word551
        lvl1word551 = ["P", "A", "P", "P", "I", "E", "S"]
        global lvl1word552
        lvl1word552 = ["P", "A", "S", "S", "A", "G", "E"]
        global lvl1word553
        lvl1word553 = ["P", "E", "G", "A", "S", "U", "S"]
        global lvl1word554
        lvl1word554 = ["A", "S", "P", "E", "S", "E", "S"]
        global lvl1word555
        lvl1word555 = ["P", "I", "G", "G", "I", "E", "S"]
        global lvl1word556
        lvl1word556 = ["P", "I", "P", "A", "G", "E", "S"]
        global lvl1word557
        lvl1word557 = ["P", "I", "P", "E", "A", "G", "E"]
        global lvl1word558
        lvl1word558 = ["P", "U", "P", "P", "I", "E", "S"]
        global lvl1word559
        lvl1word559 = ["P", "U", "S", "S", "I", "E", "S"]
        global lvl1word560
        lvl1word560 = ["P", "U", "P", "P", "I", "E", "S"]
        global lvl1word561
        lvl1word561 = ["S", "A", "S", "S", "I", "E", "S"]
        global lvl1word562
        lvl1word562 = ["S", "A", "U", "S", "A", "G", "E"]
        global lvl1word563
        lvl1word563 = ["S", "E", "E", "P", "A", "G", "E"]
        global lvl1word564
        lvl1word564 = ["S", "I", "S", "S", "I", "E", "S"]
        global lvl1word565
        lvl1word565 = ["S", "P", "E", "I", "S", "E", "S"]
        global lvl1word566
        lvl1word566 = ["A", "G", "A", "P", "A", "E"]
        global lvl1word567
        lvl1word567 = ["A", "G", "A", "P", "A", "I"]
        global lvl1word568
        lvl1word568 = ["A", "G", "A", "P", "E", "S"]
        global lvl1word569
        lvl1word569 = ["A", "G", "G", "I", "E", "S"]
        global lvl1word570
        lvl1word570 = ["A", "S", "S", "A", "I", "S"]
        global lvl1word571
        lvl1word571 = ["A", "S", "S", "E", "S", "S"]
        global lvl1word572
        lvl1word572 = ["E", "A", "S", "I", "E", "S"]
        global lvl1word573
        lvl1word573 = ["E", "G", "I", "S", "E", "S"]
        global lvl1word574
        lvl1word574 = ["E", "S", "P", "I", "E", "S"]
        global lvl1word575
        lvl1word575 = ["G", "A", "S", "S", "E", "S"]
        global lvl1word576
        lvl1word576 = ["G", "A", "U", "G", "E", "S"]
        global lvl1word577
        lvl1word577 = ["G", "I", "G", "U", "E", "S"]
        global lvl1word578
        lvl1word578 = ["G", "U", "I", "S", "E", "S"]
        global lvl1word579
        lvl1word579 = ["G", "U", "S", "S", "I", "E"]
        global lvl1word580
        lvl1word580 = ["I", "S", "S", "E", "I", "S"]
        global lvl1word581
        lvl1word581 = ["I", "S", "S", "U", "E", "S"]
        global lvl1word582
        lvl1word582 = ["G", "A", "U", "G", "E", "S"]
        global lvl1word583
        lvl1word583 = ["P", "A", "I", "S", "A", "S"]
        global lvl1word584
        lvl1word584 = ["G", "A", "U", "G", "E", "S"]
        global lvl1word585
        lvl1word585 = ["P", "A", "P", "P", "U", "S"]
        global lvl1word586
        lvl1word586 = ["P", "A", "S", "S", "E", "E"]
        global lvl1word587
        lvl1word587 = ["P", "A", "S", "S", "E", "S"]
        global lvl1word588
        lvl1word588 = ["P", "A", "S", "S", "U", "S"]
        global lvl1word589
        lvl1word589 = ["P", "A", "U", "S", "E", "S"]
        global lvl1word590
        lvl1word590 = ["P", "E", "A", "G", "E", "S"]
        global lvl1word591
        lvl1word591 = ["P", "E", "A", "S", "E", "S"]
        global lvl1word592
        lvl1word592 = ["P", "E", "I", "S", "E", "S"]
        global lvl1word593
        lvl1word593 = ["P", "I", "G", "G", "I", "E"]
        global lvl1word594
        lvl1word594 = ["P", "I", "P", "A", "G", "E"]
        global lvl1word595
        lvl1word595 = ["P", "U", "S", "S", "E", "S"]
        global lvl1word596
        lvl1word596 = ["S", "A", "I", "G", "A", "S"]
        global lvl1word597
        lvl1word597 = ["S", "A", "S", "S", "E", "S"]
        global lvl1word598
        lvl1word598 = ["S", "E", "G", "U", "E", "S"]
        global lvl1word599
        lvl1word599 = ["S", "E", "I", "S", "E", "S"]
        global lvl1word600
        lvl1word600 = ["S", "E", "P", "I", "A", "S"]
        global lvl1word601
        lvl1word601 = ["S", "E", "P", "S", "E", "S"]
        global lvl1word602
        lvl1word602 = ["S", "E", "P", "S", "I", "S"]
        global lvl1word603
        lvl1word603 = ["S", "I", "E", "G", "E", "S"]
        global lvl1word604
        lvl1word604 = ["S", "I", "S", "S", "E", "S"]
        global lvl1word605
        lvl1word605 = ["S", "P", "E", "I", "S", "E"]
        global lvl1word606
        lvl1word606 = ["S", "P", "E", "I", "S", "S"]
        global lvl1word607
        lvl1word607 = ["S", "U", "S", "S", "E", "S"]
        global lvl1word608
        lvl1word608 = ["U", "P", "A", "S", "E", "S"]
        global lvl1word609
        lvl1word609 = ["U", "S", "A", "G", "E", "S"]
        global lvl1word610
        lvl1word610 = ["A", "E", "G", "I", "S"]
        global lvl1word611
        lvl1word611 = ["A", "G", "A", "P", "E"]
        global lvl1word612
        lvl1word612 = ["A", "G", "G", "I", "E"]
        global lvl1word613
        lvl1word613 = ["A", "G", "U", "E", "S"]
        global lvl1word614
        lvl1word614 = ["A", "P", "S", "E", "S"]
        global lvl1word615
        lvl1word615 = ["A", "P", "S", "I", "S"]
        global lvl1word616
        lvl1word616 = ["A", "S", "P", "I", "S"]
        global lvl1word617
        lvl1word617 = ["A", "S", "S", "A", "I"]
        global lvl1word618
        lvl1word618 = ["A", "S", "S", "E", "S"]
        global lvl1word619
        lvl1word619 = ["E", "A", "S", "E", "S"]
        global lvl1word620
        lvl1word620 = ["E", "P", "E", "E", "S"]
        global lvl1word621
        lvl1word621 = ["E", "S", "S", "E", "S"]
        global lvl1word622
        lvl1word622 = ["G", "A", "G", "E", "S"]
        global lvl1word623
        lvl1word623 = ["G", "A", "P", "E", "S"]
        global lvl1word624
        lvl1word624 = ["G", "A", "S", "E", "S"]
        global lvl1word625
        lvl1word625 = ["G", "A", "S", "P", "S"]
        global lvl1word626
        lvl1word626 = ["G", "A", "U", "G", "E"]
        global lvl1word627
        lvl1word627 = ["G", "A", "U", "S", "S"]
        global lvl1word628
        lvl1word628 = ["G", "E", "E", "S", "E"]
        global lvl1word629
        lvl1word629 = ["G", "I", "G", "A", "S"]
        global lvl1word630
        lvl1word630 = ["G", "I", "G", "U", "E"]
        global lvl1word631
        lvl1word631 = ["G", "U", "E", "S", "S"]
        global lvl1word632
        lvl1word632 = ["G", "U", "I", "S", "E"]
        global lvl1word633
        lvl1word633 = ["I", "S", "S", "E", "I"]
        global lvl1word634
        lvl1word634 = ["I", "S", "S", "U", "E"]
        global lvl1word635
        lvl1word635 = ["P", "A", "G", "E", "S"]
        global lvl1word636
        lvl1word636 = ["P", "A", "I", "S", "A"]
        global lvl1word637
        lvl1word637 = ["P", "A", "I", "S", "E"]
        global lvl1word638
        lvl1word638 = ["P", "A", "P", "A", "S"]
        global lvl1word639
        lvl1word639 = ["P", "A", "P", "P", "I"]
        global lvl1word640
        lvl1word640 = ["P", "A", "S", "E", "S"]
        global lvl1word641
        lvl1word641 = ["P", "A", "S", "S", "E"]
        global lvl1word642
        lvl1word642 = ["P", "A", "U", "A", "S"]
        global lvl1word643
        lvl1word643 = ["P", "A", "U", "S", "E"]
        global lvl1word644
        lvl1word644 = ["P", "E", "A", "G", "E"]
        global lvl1word645
        lvl1word645 = ["P", "E", "A", "G", "S"]
        global lvl1word646
        lvl1word646 = ["P", "E", "A", "S", "E"]
        global lvl1word647
        lvl1word647 = ["P", "E", "E", "P", "S"]
        global lvl1word648
        lvl1word648 = ["P", "E", "I", "S", "E"]
        global lvl1word649 
        lvl1word649 = ["P", "I", "P", "A", "S"]
        global lvl1word650
        lvl1word650 = ["P", "I", "P", "E", "S"]
        global lvl1word651
        lvl1word651 = ["P", "U", "P", "A", "E"]
        global lvl1word652
        lvl1word652 = ["P", "U", "P", "A", "S"]
        global lvl1word653
        lvl1word653 = ["P", "U", "P", "U", "S"]
        global lvl1word654
        lvl1word654 = ["P", "U", "S", "E", "S"]
        global lvl1word655
        lvl1word655 = ["P", "U", "P", "A", "S"]
        global lvl1word656
        lvl1word656 = ["S", "A", "G", "A", "S"]
        global lvl1word657
        lvl1word657 = ["S", "A", "G", "E", "S"]
        global lvl1word658
        lvl1word658 = ["S", "E", "I", "S", "E"]
        global lvl1word659
        lvl1word659 = ["S", "E", "P", "I", "A"]
        global lvl1word660
        lvl1word660 = ["S", "I", "E", "G", "E"]
        global lvl1word661
        lvl1word661 = ["S", "I", "P", "E", "S"]
        global lvl1word662
        lvl1word662 = ["S", "I", "S", "E", "S"]
        global lvl1word663
        lvl1word663 = ["S", "P", "A", "E", "S"]
        global lvl1word664
        lvl1word664 = ["S", "P", "I", "E", "S"]
        global lvl1word665
        lvl1word665 = ["S", "P", "U", "E", "S"]
        global lvl1word666
        lvl1word666 = ["S", "U", "P", "E", "S"]
        global lvl1word667
        lvl1word667 = ["S", "U", "S", "E", "S"]
        global lvl1word668
        lvl1word668 = ["U", "S", "A", "G", "E"]
        global lvl1word669
        lvl1word669 = ["A", "G", "A", "S"]
        global lvl1word670
        lvl1word670 = ["A", "P", "P", "S"]
        global lvl1word671
        lvl1word671 = ["P", "U", "P", "U"]
        global lvl1word672
        lvl1word672 = ["P", "U", "P", "A"]
        global lvl1word673
        lvl1word673 = ["P", "U", "P", "S"]
        global lvl1word674
        lvl1word674 = ["P", "A", "P", "A"]
        global lvl1word675
        lvl1word675 = ["P", "E", "E", "P"]
        global lvl1word676
        lvl1word676 = ["P", "E", "P", "S"]
        global lvl1word677
        lvl1word677 = ["P", "I", "P", "A"]
        global lvl1word678
        lvl1word678 = ["P", "I", "P", "E"]
        global lvl1word679
        lvl1word679 = ["P", "I", "P", "S"]
        global lvl1word680
        lvl1word680 = ["P", "U", "G", "S"]
        global lvl1word681
        lvl1word681 = ["G", "A", "P", "E"]
        global lvl1word682
        lvl1word682 = ["G", "A", "P", "S"]
        global lvl1word683
        lvl1word683 = ["G", "A", "S", "P"]
        global lvl1word684
        lvl1word684 = ["G", "I", "P", "S"]
        global lvl1word685
        lvl1word685 = ["P", "A", "G", "E"]
        global lvl1word686
        lvl1word686 = ["P", "E", "A", "G"]
        global lvl1word687
        lvl1word687 = ["G", "A", "G", "S"]
        global lvl1word688
        lvl1word688 = ["G", "I", "G", "A"]
        global lvl1word689
        lvl1word689 = ["G", "I", "G", "S"]
        global lvl1word690
        lvl1word690 = ["I", "G", "G", "S"]
        global lvl1word691
        lvl1word691 = ["P", "A", "U", "A"]
        global lvl1word692
        lvl1word692 = ["P", "U", "S", "S"]
        global lvl1word693
        lvl1word693 = ["S", "P", "U", "E"]
        global lvl1word694
        lvl1word694 = ["S", "U", "P", "E"]
        global lvl1word695
        lvl1word695 = ["S", "U", "P", "S"]
        global lvl1word696
        lvl1word696 = ["U", "P", "A", "S"]
        global lvl1word697
        lvl1word697 = ["A", "P", "E", "S"]
        global lvl1word698
        lvl1word698 = ["A", "P", "S", "E"]
        global lvl1word699
        lvl1word699 = ["A", "S", "P", "S"]
        global lvl1word700
        lvl1word700 = ["P", "A", "S", "E"]
        global lvl1word701
        lvl1word701 = ["P", "A", "S", "S"]
        global lvl1word702
        lvl1word702 = ["P", "E", "A", "S"]
        global lvl1word703
        lvl1word703 = ["P", "E", "E", "S"]
        global lvl1word704
        lvl1word704 = ["P", "I", "A", "S"]
        global lvl1word705
        lvl1word705 = ["P", "I", "E", "S"]
        global lvl1word706
        lvl1word706 = ["P", "I", "S", "S"]
        global lvl1word707
        lvl1word707 = ["P", "S", "I", "S"]
        global lvl1word708
        lvl1word708 = ["S", "A", "P", "S"]
        global lvl1word709
        lvl1word709 = ["S", "E", "E", "P"]
        global lvl1word710
        lvl1word710 = ["S", "E", "P", "S"]
        global lvl1word711
        lvl1word711 = ["S", "I", "P", "E"]
        global lvl1word712
        lvl1word712 = ["S", "I", "P", "S"]
        global lvl1word713
        lvl1word713 = ["S", "P", "A", "E"]
        global lvl1word714
        lvl1word714 = ["S", "P", "A", "S"]
        global lvl1word715
        lvl1word715 = ["A", "G", "U", "E"]
        global lvl1word716
        lvl1word716 = ["A", "G", "E", "E"]
        global lvl1word717
        lvl1word717 = ["A", "G", "E", "S"]
        global lvl1word718
        lvl1word718 = ["E", "G", "I", "S"]
        global lvl1word719
        lvl1word719 = ["G", "A", "E", "S"]
        global lvl1word720
        lvl1word720 = ["G", "E", "E", "S"]
        global lvl1word721
        lvl1word721 = ["G", "I", "E", "S"]
        global lvl1word722
        lvl1word722 = ["S", "A", "G", "A"]
        global lvl1word723
        lvl1word723 = ["S", "A", "G", "E"]
        global lvl1word724
        lvl1word724 = ["S", "A", "G", "S"]
        global lvl1word725
        lvl1word725 = ["S", "E", "G", "S"]
        global lvl1word726
        lvl1word726 = ["S", "U", "E", "S"]
        global lvl1word727
        lvl1word727 = ["U", "S", "E", "S"]
        global lvl1word728
        lvl1word728 = ["A", "S", "E", "A"]
        global lvl1word729
        lvl1word729 = ["E", "A", "S", "E"]
        global lvl1word730
        lvl1word730 = ["E", "S", "E", "S"]
        global lvl1word731
        lvl1word731 = ["E", "S", "S", "E"]
        global lvl1word732
        lvl1word732 = ["S", "E", "A", "S"]
        global lvl1word733
        lvl1word733 = ["S", "E", "E", "S"]
        global lvl1word734
        lvl1word734 = ["S", "E", "I", "S"]
        global lvl1word735
        lvl1word735 = ["S", "I", "G", "S"]
        global lvl1word736
        lvl1word736 = ["A", "P", "P"]
        global lvl1word737
        lvl1word737 = ["P", "A", "P"]
        global lvl1word738
        lvl1word738 = ["P", "E", "P"]
        global lvl1word739
        lvl1word739 = ["P", "I", "P"]
        global lvl1word740
        lvl1word740 = ["P", "U", "P"]
        global lvl1word741
        lvl1word741 = ["G", "A", "P"]
        global lvl1word742
        lvl1word742 = ["G", "I", "P"]
        global lvl1word743
        lvl1word743 = ["P", "E", "G"]
        global lvl1word744
        lvl1word744 = ["P", "I", "G"]
        global lvl1word745
        lvl1word745 = ["P", "U", "G"]
        global lvl1word746
        lvl1word746 = ["A", "P", "E"]
        global lvl1word747
        lvl1word747 = ["A", "S", "P"]
        global lvl1word748
        lvl1word748 = ["E", "G", "G"]
        global lvl1word749
        lvl1word749 = ["G", "A", "G"]
        global lvl1word750
        lvl1word750 = ["G", "I", "G"]
        global lvl1word751
        lvl1word751 = ["I", "G", "G"]
        global lvl1word752
        lvl1word752 = ["P", "A", "S"]
        global lvl1word753
        lvl1word753 = ["P", "E", "A"]
        global lvl1word754
        lvl1word754 = ["P", "E", "E"]
        global lvl1word755
        lvl1word755 = ["P", "E", "S"]
        global lvl1word756
        lvl1word756 = ["P", "I", "A"]
        global lvl1word757
        lvl1word757 = ["P", "I", "E"]
        global lvl1word758
        lvl1word758 = ["P", "I", "S"]
        global lvl1word759
        lvl1word759 = ["P", "I", "U"]
        global lvl1word760
        lvl1word760 = ["P", "S", "I"]
        global lvl1word761
        lvl1word761 = ["P", "U", "S"]
        global lvl1word762
        lvl1word762 = ["S", "A", "P"]
        global lvl1word763
        lvl1word763 = ["S", "I", "P"]
        global lvl1word764
        lvl1word764 = ["S", "P", "A"]
        global lvl1word765
        lvl1word765 = ["S", "U", "P"]
        global lvl1word766
        lvl1word766 = ["U", "P", "S"]
        global lvl1word767
        lvl1word767 = ["A", "G", "A"]
        global lvl1word768
        lvl1word768 = ["A", "G", "E"]
        global lvl1word769
        lvl1word769 = ["A", "G", "S"]
        global lvl1word770
        lvl1word770 = ["G", "A", "E"]
        global lvl1word771
        lvl1word771 = ["G", "A", "S"]
        global lvl1word772
        lvl1word772 = ["G", "E", "E"]
        global lvl1word773
        lvl1word773 = ["G", "I", "E"]
        global lvl1word774
        lvl1word774 = ["G", "I", "S"]
        global lvl1word775
        lvl1word775 = ["S", "A", "G"]
        global lvl1word776
        lvl1word776 = ["S", "E", "G"]
        global lvl1word777
        lvl1word777 = ["S", "I", "G"]
        global lvl1word778
        lvl1word778 = ["A", "A", "S"]
        global lvl1word779
        lvl1word779 = ["A", "I", "S"]
        global lvl1word780
        lvl1word780 = ["A", "S", "S"]
        global lvl1word781
        lvl1word781 = ["E", "A", "U"]
        global lvl1word782
        lvl1word782 = ["E", "S", "S"]
        global lvl1word783
        lvl1word783 = ["S", "A", "E"]
        global lvl1word784
        lvl1word784 = ["S", "A", "U"]
        global lvl1word785
        lvl1word785 = ["S", "E", "A"]
        global lvl1word786
        lvl1word786 = ["S", "E", "E"]
        global lvl1word787
        lvl1word787 = ["S", "E", "I"]
        global lvl1word788
        lvl1word788 = ["S", "I", "S"]
        global lvl1word789
        lvl1word789 = ["S", "U", "E"]
        global lvl1word790
        lvl1word790 = ["S", "U", "S"]
        global lvl1word791
        lvl1word791 = ["U", "S", "E"]
        global lvl1word792
        lvl1word792 = ["P", "A"]
        global lvl1word793
        lvl1word793 = ["P", "E"]
        global lvl1word794
        lvl1word794 = ["P", "I"]
        global lvl1word795
        lvl1word795 = ["U", "P"]
        global lvl1word796
        lvl1word796 = ["A", "G"]
        global lvl1word797
        lvl1word797 = ["A", "S"]
        global lvl1word798
        lvl1word798 = ["E", "S"]
        global lvl1word799
        lvl1word799 = ["I", "S"]
        global lvl1word800
        lvl1word800 = ["S", "I"]
        global lvl1word801
        lvl1word801 = ["U", "S"]

        #ADDED WORDS LEVEL 9(DUPLICATE VARIABLE NAME IN 650'S)
        global lvl1word802
        lvl1word802 = ["S", "A", "I", "G", "A"]
        global lvl1word803
        lvl1word803 = ["S", "E", "E", "P", "S"]
        global lvl1word804 
        lvl1word804 = ["S", "E", "G", "U", "E"]

        #ADDED WORDS LEVEL 9 (DUPLICATE VARIABLE NAME IN 680'S)
        global lvl1word805
        lvl1word805 = ["P", "E", "G", "S"]
        global lvl1word806
        lvl1word806 = ["P", "I", "G", "S"]
        global lvl1word807
        lvl1word807 = ["E", "G", "G", "S"]
        global lvl1word808
        lvl1word808 = ["G", "A", "G", "A"]
        global lvl1word809
        lvl1word809 = ["G", "A", "G", "E"]



        # LEVEL 10 LETTERS E, G, I, O, R, S, U, V
        global lvl1word810
        lvl1word810 = ["O", "V", "E", "R", "S", "E", "R", "I", "O", "U", "S"]
        global lvl1word811
        lvl1word811 = ["R", "E", "S", "E", "R", "V", "O", "I", "R", "S"]
        global lvl1word812
        lvl1word812 = ["R", "E", "O", "V", "I", "R", "U", "S", "E", "S"]
        global lvl1word813
        lvl1word813 = ["R", "E", "G", "R", "E", "S", "S", "O", "R", "S"]
        global lvl1word814
        lvl1word814 = ["R", "E", "G", "R", "E", "S", "S", "I", "V", "E"]
        global lvl1word815
        lvl1word815 = ["R", "E", "G", "I", "S", "S", "E", "U", "R", "S"]
        global lvl1word816
        lvl1word816 = ["O", "V", "E", "R", "I", "S", "S", "U", "E", "S"]
        global lvl1word817
        lvl1word817 = ["G", "R", "O", "G", "G", "E", "R", "I", "E", "S"]
        global lvl1word818
        lvl1word818 = ["V", "O", "U", "S", "S", "O", "I", "R", "S"]
        global lvl1word819
        lvl1word819 = ["S", "U", "S", "U", "R", "R", "O", "U", "S"]
        global lvl1word820
        lvl1word820 = ["S", "U", "R", "V", "I", "V", "O", "R", "S"]
        global lvl1word821
        lvl1word821 = ["S", "U", "R", "V", "I", "V", "E", "R", "S"]
        global lvl1word822
        lvl1word822 = ["S", "U", "R", "G", "E", "R", "I", "E", "S"]
        global lvl1word823
        lvl1word823 = ["R", "O", "G", "U", "E", "R", "I", "E", "S"]
        global lvl1word824
        lvl1word824 = ["R", "E", "V", "E", "R", "S", "E", "R", "S"]
        global lvl1word825
        lvl1word825 = ["R", "E", "S", "E", "R", "V", "O", "I", "R"]
        global lvl1word826
        lvl1word826 = ["R", "E", "S", "E", "R", "V", "E", "R", "S"]
        global lvl1word827
        lvl1word827 = ["R", "E", "I", "S", "S", "U", "E", "R", "S"]
        global lvl1word828
        lvl1word828 = ["R", "E", "G", "R", "O", "O", "V", "E", "S"]
        global lvl1word829
        lvl1word829 = ["R", "E", "G", "R", "E", "S", "S", "O", "R"]
        global lvl1word830
        lvl1word830 = ["R", "E", "G", "R", "E", "S", "S", "E", "S"]
        global lvl1word831
        lvl1word831 = ["R", "E", "G", "I", "S", "S", "E", "U", "R"]
        global lvl1word832
        lvl1word832 = ["O", "V", "E", "R", "U", "R", "G", "E", "S"]
        global lvl1word833
        lvl1word833 = ["O", "V", "E", "R", "S", "E", "E", "R", "S"]
        global lvl1word834
        lvl1word834 = ["O", "V", "E", "R", "I", "S", "S", "U", "E"]
        global lvl1word836
        lvl1word836 = ["E", "G", "R", "E", "G", "I", "O", "U", "S"]
        global lvl1word837
        lvl1word837 = ["V", "O", "U", "S", "S", "O", "I", "R"]
        global lvl1word838
        lvl1word838 = ["V", "I", "G", "O", "R", "O", "U", "S"]
        global lvl1word839
        lvl1word839 = ["V", "I", "G", "O", "R", "O", "S", "O"]
        global lvl1word840
        lvl1word840 = ["U", "S", "U", "R", "I", "O", "U", "S"]
        global lvl1word841
        lvl1word841 = ["S", "U", "S", "U", "R", "R", "U", "S"]
        global lvl1word842
        lvl1word842 = ["S", "U", "R", "V", "I", "V", "O", "R"]
        global lvl1word843
        lvl1word843 = ["S", "U", "R", "V", "I", "V", "E", "S"]
        global lvl1word844
        lvl1word844 = ["S", "U", "R", "V", "I", "V", "E", "R"]
        global lvl1word845
        lvl1word845 = ["S", "E", "I", "S", "U", "R", "E", "S"]
        global lvl1word846
        lvl1word846 = ["R", "O", "S", "E", "R", "I", "E", "S"]
        global lvl1word847
        lvl1word847 = ["R", "I", "V", "I", "E", "R", "E", "S"]
        global lvl1word848
        lvl1word848 = ["R", "I", "G", "O", "R", "O", "U", "S"]
        global lvl1word849
        lvl1word849 = ["R", "E", "V", "I", "V", "E", "R", "S"]
        global lvl1word850
        lvl1word850 = ["R", "E", "V", "I", "S", "O", "R", "S"]
        global lvl1word851
        lvl1word851 = ["R", "E", "V", "I", "S", "E", "R", "S"]
        global lvl1word852
        lvl1word852 = ["R", "E", "V", "E", "R", "S", "O", "S"]
        global lvl1word853
        lvl1word853 = ["R", "E", "V", "E", "R", "S", "E", "S"]
        global lvl1word854
        lvl1word854 = ["R", "E", "V", "E", "R", "S", "E", "R"]
        global lvl1word855
        lvl1word855 = ["R", "E", "V", "E", "R", "I", "E", "S"]
        global lvl1word856
        lvl1word856 = ["R", "E", "V", "E", "R", "E", "R", "S"]
        global lvl1word857
        lvl1word857 = ["R", "E", "S", "U", "R", "G", "E", "S"]
        global lvl1word858
        lvl1word858 = ["R", "E", "S", "E", "R", "V", "E", "S"]
        global lvl1word859
        lvl1word859 = ["R", "E", "S", "E", "R", "V", "E", "R"]
        global lvl1word860
        lvl1word860 = ["R", "E", "O", "V", "I", "R", "U", "S"]
        global lvl1word861
        lvl1word861 = ["R", "E", "I", "S", "S", "U", "E", "S"]
        global lvl1word862
        lvl1word862 = ["R", "E", "I", "S", "S", "U", "E", "R"]
        global lvl1word863
        lvl1word863 = ["R", "E", "G", "R", "O", "O", "V", "E"]
        global lvl1word864
        lvl1word864 = ["R", "E", "G", "O", "R", "G", "E", "S"]
        global lvl1word865
        lvl1word865 = ["O", "V", "E", "R", "U", "S", "E", "S"]
        global lvl1word866
        lvl1word866 = ["O", "V", "E", "R", "U", "R", "G", "E"]
        global lvl1word867
        lvl1word867 = ["O", "V", "E", "R", "S", "U", "R", "E"]
        global lvl1word868
        lvl1word868 = ["O", "V", "E", "R", "S", "E", "E", "S"]
        global lvl1word869
        lvl1word869 = ["O", "V", "E", "R", "S", "E", "E", "R"]
        global lvl1word870
        lvl1word870 = ["O", "R", "R", "E", "R", "I", "E", "S"]
        global lvl1word871
        lvl1word871 = ["O", "G", "R", "E", "S", "S", "E", "S"]
        global lvl1word872
        lvl1word872 = ["I", "S", "O", "G", "R", "I", "V", "S"]
        global lvl1word873
        lvl1word873 = ["G", "U", "E", "S", "S", "E", "R", "S"]
        global lvl1word874
        lvl1word874 = ["G", "R", "O", "U", "S", "E", "R", "S"]
        global lvl1word875
        lvl1word875 = ["G", "R", "O", "S", "S", "E", "R", "S"]
        global lvl1word876
        lvl1word876 = ["G", "R", "O", "O", "V", "I", "E", "R"]
        global lvl1word877
        lvl1word877 = ["G", "R", "O", "O", "V", "E", "R", "S"]
        global lvl1word878
        lvl1word878 = ["G", "R", "O", "G", "G", "I", "E", "R"]
        global lvl1word879
        lvl1word879 = ["G", "R", "I", "S", "E", "O", "U", "S"]
        global lvl1word880
        lvl1word880 = ["G", "R", "I", "E", "V", "O", "U", "S"]
        global lvl1word881
        lvl1word881 = ["G", "R", "I", "E", "V", "E", "R", "S"]
        global lvl1word882
        lvl1word882 = ["G", "O", "R", "G", "E", "O", "U", "S"]
        global lvl1word883
        lvl1word883 = ["E", "G", "R", "E", "S", "S", "E", "S"]
        global lvl1word884
        lvl1word884 = ["V", "U", "G", "G", "I", "E", "R"]
        global lvl1word885
        lvl1word885 = ["V", "O", "G", "U", "E", "R", "S"]
        global lvl1word886
        lvl1word886 = ["V", "I", "R", "U", "S", "E", "S"]
        global lvl1word887
        lvl1word887 = ["V", "I", "R", "O", "S", "I", "S"]
        global lvl1word888
        lvl1word888 = ["V", "I", "R", "O", "S", "E", "S"]
        global lvl1word889
        lvl1word889 = ["V", "I", "G", "O", "U", "R", "S"]
        global lvl1word890
        lvl1word890 = ["V", "E", "R", "S", "E", "R", "S"]
        global lvl1word891
        lvl1word891 = ["V", "E", "R", "G", "E", "R", "S"]
        global lvl1word892
        lvl1word892 = ["V", "E", "G", "G", "I", "E", "S"]
        global lvl1word893
        lvl1word893 = ["V", "E", "E", "R", "I", "E", "S"]
        global lvl1word894
        lvl1word894 = ["U", "S", "U", "R", "I", "E", "S"]
        global lvl1word895
        lvl1word895 = ["U", "S", "U", "R", "E", "R", "S"]
        global lvl1word896
        lvl1word896 = ["S", "U", "R", "V", "I", "V", "E"]
        global lvl1word897
        lvl1word897 = ["S", "U", "R", "G", "E", "R", "S"]
        global lvl1word898
        lvl1word898 = ["S", "O", "R", "R", "I", "E", "R"]
        global lvl1word899
        lvl1word899 = ["S", "O", "R", "O", "S", "I", "S"]
        global lvl1word900
        lvl1word900 = ["S", "O", "R", "O", "S", "E", "S"]
        global lvl1word901
        lvl1word901 = ["S", "O", "I", "R", "E", "E", "S"]
        global lvl1word902
        lvl1word902 = ["S", "O", "G", "G", "I", "E", "R"]
        global lvl1word903
        lvl1word903 = ["S", "I", "S", "S", "I", "E", "R"]
        global lvl1word904
        lvl1word904 = ["S", "I", "R", "R", "E", "E", "S"]
        global lvl1word905
        lvl1word905 = ["S", "E", "V", "E", "R", "E", "R"]
        global lvl1word906
        lvl1word906 = ["S", "E", "R", "V", "E", "R", "S"]
        global lvl1word907
        lvl1word907 = ["S", "E", "R", "R", "I", "E", "S"]
        global lvl1word908
        lvl1word908 = ["S", "E", "R", "I", "O", "U", "S"]
        global lvl1word909
        lvl1word909 = ["S", "E", "I", "S", "U", "R", "E"]
        global lvl1word910
        lvl1word910 = ["S", "E", "I", "S", "O", "R", "S"]
        global lvl1word911
        lvl1word911 = ["S", "E", "I", "S", "E", "R", "S"]
        global lvl1word912
        lvl1word912 = ["S", "E", "E", "R", "E", "S", "S"]
        global lvl1word913
        lvl1word913 = ["R", "U", "G", "G", "E", "R", "S"]
        global lvl1word914
        lvl1word914 = ["R", "O", "U", "S", "E", "R", "S"]
        global lvl1word915
        lvl1word915 = ["R", "O", "O", "S", "E", "R", "S"]
        global lvl1word916
        lvl1word916 = ["R", "I", "V", "I", "E", "R", "E"]
        global lvl1word917
        lvl1word917 = ["R", "I", "S", "U", "S", "E", "S"]
        global lvl1word918
        lvl1word918 = ["R", "I", "G", "O", "U", "R", "S"]
        global lvl1word919
        lvl1word919 = ["R", "I", "G", "G", "E", "R", "S"]
        global lvl1word920
        lvl1word920 = ["R", "I", "E", "V", "E", "R", "S"]
        global lvl1word921
        lvl1word921 = ["R", "E", "V", "I", "V", "E", "S"]
        global lvl1word922
        lvl1word922 = ["R", "E", "V", "I", "V", "E", "R"]
        global lvl1word923
        lvl1word923 = ["R", "E", "V", "I", "S", "O", "R"]
        global lvl1word924
        lvl1word924 = ["R", "E", "V", "I", "S", "E", "S"]
        global lvl1word925
        lvl1word925 = ["R", "E", "V", "I", "S", "E", "R"]
        global lvl1word926
        lvl1word926 = ["R", "E", "V", "E", "R", "S", "O"]
        global lvl1word927
        lvl1word927 = ["R", "E", "V", "E", "R", "S", "E"]
        global lvl1word928
        lvl1word928 = ["R", "E", "V", "E", "R", "I", "E"]
        global lvl1word929
        lvl1word929 = ["R", "E", "V", "E", "R", "E", "S"]
        global lvl1word930
        lvl1word930 = ["R", "E", "V", "E", "R", "E", "R"]
        global lvl1word931
        lvl1word931 = ["R", "E", "S", "U", "R", "G", "E"]
        global lvl1word932
        lvl1word932 = ["R", "E", "S", "E", "R", "V", "E"]
        global lvl1word933
        lvl1word933 = ["R", "E", "R", "I", "S", "E", "S"]
        global lvl1word934
        lvl1word934 = ["R", "E", "I", "V", "E", "R", "S"]
        global lvl1word935
        lvl1word935 = ["R", "E", "I", "S", "S", "U", "E"]
        global lvl1word936
        lvl1word936 = ["R", "E", "G", "R", "E", "S", "S"]
        global lvl1word937
        lvl1word937 = ["R", "E", "G", "O", "R", "G", "E"]
        global lvl1word938
        lvl1word938 = ["R", "E", "G", "I", "V", "E", "S"]
        global lvl1word939
        lvl1word939 = ["O", "V", "E", "R", "U", "S", "E"]
        global lvl1word940
        lvl1word940 = ["O", "V", "E", "R", "S", "E", "E"]
        global lvl1word941
        lvl1word941 = ["O", "S", "S", "E", "O", "U", "S"]
        global lvl1word942
        lvl1word942 = ["O", "R", "R", "I", "S", "E", "S"]
        global lvl1word943
        lvl1word943 = ["O", "E", "U", "V", "R", "E", "S"]
        global lvl1word944
        lvl1word944 = ["I", "V", "O", "R", "I", "E", "S"]
        global lvl1word945
        lvl1word945 = ["I", "S", "S", "U", "E", "R", "S"]
        global lvl1word946
        lvl1word946 = ["I", "S", "O", "G", "R", "I", "V"]
        global lvl1word948
        lvl1word948 = ["G", "U", "R", "R", "I", "E", "S"]
        global lvl1word950
        lvl1word950 = ["G", "U", "E", "S", "S", "E", "R"]
        global lvl1word951
        lvl1word951 = ["G", "R", "U", "G", "R", "U", "S"]
        global lvl1word952
        lvl1word952 = ["G", "R", "O", "U", "S", "E", "S"]
        global lvl1word953
        lvl1word953 = ["G", "R", "O", "U", "S", "E", "R"]
        global lvl1word954
        lvl1word954 = ["G", "R", "O", "S", "S", "E", "S"]
        global lvl1word955
        lvl1word955 = ["G", "R", "O", "S", "S", "E", "R"]
        global lvl1word956
        lvl1word956 = ["G", "R", "O", "O", "V", "E", "S"]
        global lvl1word957
        lvl1word957 = ["G", "R", "O", "O", "V", "E", "R"]
        global lvl1word958
        lvl1word958 = ["G", "R", "I", "G", "R", "I", "S"]
        global lvl1word959
        lvl1word959 = ["G", "R", "I", "E", "V", "E", "S"]
        global lvl1word960
        lvl1word960 = ["G", "R", "I", "E", "V", "E", "R"]
        global lvl1word961
        lvl1word961 = ["G", "R", "E", "I", "G", "E", "S"]
        global lvl1word962
        lvl1word962 = ["G", "O", "U", "G", "E", "R", "S"]
        global lvl1word963
        lvl1word963 = ["G", "O", "R", "S", "I", "E", "R"]
        global lvl1word964
        lvl1word964 = ["G", "O", "R", "G", "E", "R", "S"]
        global lvl1word965
        lvl1word965 = ["G", "O", "O", "S", "I", "E", "R"]
        global lvl1word966
        lvl1word966 = ["G", "E", "S", "S", "O", "E", "S"]
        global lvl1word967
        lvl1word967 = ["E", "R", "O", "S", "I", "V", "E"]
        global lvl1word968
        lvl1word968 = ["V", "O", "G", "U", "E", "S"]
        global lvl1word969
        lvl1word969 = ["V", "O", "G", "U", "E", "R"]
        global lvl1word970
        lvl1word970 = ["V", "I", "V", "E", "R", "S"]
        global lvl1word971
        lvl1word971 = ["V", "I", "S", "O", "R", "S"]
        global lvl1word972
        lvl1word972 = ["V", "I", "S", "I", "V", "E"]
        global lvl1word973
        lvl1word973 = ["V", "I", "R", "E", "O", "S"]
        global lvl1word974
        lvl1word974 = ["V", "I", "G", "O", "U", "R"]
        global lvl1word975
        lvl1word975 = ["V", "I", "G", "O", "R", "S"]
        global lvl1word976
        lvl1word976 = ["V", "E", "R", "V", "E", "S"]
        global lvl1word977
        lvl1word977 = ["V", "E", "R", "S", "U", "S"]
        global lvl1word978
        lvl1word978 = ["V", "E", "R", "S", "O", "S"]
        global lvl1word979
        lvl1word979 = ["V", "E", "R", "S", "E", "S"]
        global lvl1word980
        lvl1word980 = ["V", "E", "R", "S", "E", "R"]
        global lvl1word981
        lvl1word981 = ["V", "E", "R", "I", "E", "R"]
        global lvl1word982
        lvl1word982 = ["V", "E", "R", "G", "E", "S"]
        global lvl1word983
        lvl1word983 = ["V", "E", "R", "G", "E", "R"]
        global lvl1word984
        lvl1word984 = ["V", "E", "G", "I", "E", "S"]
        global lvl1word985
        lvl1word985 = ["V", "E", "G", "G", "I", "E"]
        global lvl1word986
        lvl1word986 = ["U", "V", "E", "O", "U", "S"]
        global lvl1word987
        lvl1word987 = ["U", "S", "U", "R", "E", "R"]
        global lvl1word988
        lvl1word988 = ["U", "R", "U", "S", "E", "S"]
        global lvl1word989
        lvl1word989 = ["U", "R", "G", "E", "R", "S"]
        global lvl1word990
        lvl1word990 = ["S", "U", "R", "G", "E", "S"]
        global lvl1word991
        lvl1word991 = ["S", "U", "R", "G", "E", "R"]
        global lvl1word992
        lvl1word992 = ["S", "O", "U", "S", "E", "S"]
        global lvl1word993
        lvl1word993 = ["S", "O", "U", "R", "E", "R"]
        global lvl1word994
        lvl1word994 = ["S", "O", "R", "G", "O", "S"]
        global lvl1word995
        lvl1word995 = ["S", "O", "I", "R", "E", "E"]
        global lvl1word996
        lvl1word996 = ["S", "O", "E", "V", "E", "R"]
        global lvl1word997
        lvl1word997 = ["S", "I", "V", "E", "R", "S"]
        global lvl1word998
        lvl1word998 = ["S", "I", "R", "R", "E", "E"]
        global lvl1word999
        lvl1word999 = ["S", "I", "R", "E", "E", "S"]
        global lvl1word1000
        lvl1word1000 = ["S", "I", "E", "V", "E", "S"]
        global lvl1word1001
        lvl1word1001 = ["S", "I", "E", "U", "R", "S"]
        global lvl1word1003
        lvl1word1003 = ["S", "E", "V", "E", "R", "S"]
        global lvl1word1004
        lvl1word1004 = ["S", "E", "V", "E", "R", "E"]
        global lvl1word1005
        lvl1word1005 = ["S", "E", "R", "V", "O", "S"]
        global lvl1word1006
        lvl1word1006 = ["S", "E", "R", "V", "E", "S"]
        global lvl1word1007
        lvl1word1007 = ["S", "E", "R", "V", "E", "R"]
        global lvl1word1008
        lvl1word1008 = ["S", "E", "R", "O", "U", "S"]
        global lvl1word1009
        lvl1word1009 = ["S", "E", "R", "I", "E", "S"]
        global lvl1word1010
        lvl1word1010 = ["S", "E", "R", "G", "E", "S"]
        global lvl1word1011
        lvl1word1011 = ["S", "E", "I", "S", "O", "R"]
        global lvl1word1013
        lvl1word1013 = ["S", "E", "I", "S", "E", "R"]
        global lvl1word1015
        lvl1word1015 = ["R", "U", "G", "O", "U", "S"]
        global lvl1word1016
        lvl1word1016 = ["R", "U", "G", "O", "S", "E"]
        global lvl1word1017
        lvl1word1017 = ["R", "U", "G", "G", "E", "R"]
        global lvl1word1018
        lvl1word1018 = ["R", "O", "V", "E", "R", "S"]
        global lvl1word1019
        lvl1word1019 = ["R", "O", "U", "S", "E", "S"]
        global lvl1word1020
        lvl1word1020 = ["R", "O", "U", "S", "E", "R"]
        global lvl1word1021
        lvl1word1021 = ["R", "O", "U", "G", "E", "S"]
        global lvl1word1022
        lvl1word1022 = ["R", "O", "S", "I", "E", "R"]
        global lvl1word1023
        lvl1word1023 = ["R", "O", "O", "S", "E", "S"]
        global lvl1word1024
        lvl1word1024 = ["R", "O", "O", "S", "E", "R"]
        global lvl1word1025
        lvl1word1025 = ["R", "O", "G", "U", "E", "S"]
        global lvl1word1026
        lvl1word1026 = ["R", "O", "G", "E", "R", "S"]
        global lvl1word1027
        lvl1word1027 = ["R", "I", "V", "E", "R", "S"]
        global lvl1word1028
        lvl1word1028 = ["R", "I", "S", "E", "R", "S"]
        global lvl1word1029
        lvl1word1029 = ["R", "I", "G", "O", "U", "R"]
        global lvl1word1030
        lvl1word1030 = ["R", "I", "G", "O", "R", "S"]
        global lvl1word1031
        lvl1word1031 = ["R", "I", "E", "V", "E", "R"]
        global lvl1word1032
        lvl1word1032 = ["R", "E", "V", "U", "E", "S"]
        global lvl1word1033
        lvl1word1033 = ["R", "E", "V", "I", "V", "E"]
        global lvl1word1034
        lvl1word1034 = ["R", "E", "V", "I", "S", "E"]
        global lvl1word1035
        lvl1word1035 = ["R", "E", "V", "E", "R", "S"]




        #ADDED DUPLICATES

        global lvl1word321
        lvl1word321 = ["R", "E", "V", "E", "R", "E"]
        global lvl1word835
        lvl1word835 = ["R", "E", "U", "S", "E", "S"]
        global lvl1word947
        lvl1word947 = ["R", "E", "S", "E", "E", "S"]
        global lvl1word949
        lvl1word949 = ["R", "E", "R", "O", "S", "E"]
        global lvl1word1002
        lvl1word1002 = ["R", "E", "R", "I", "S", "E"]
        global lvl1word1012
        lvl1word1012 = ["R", "E", "R", "I", "G", "S"]
        global lvl1word1014
        lvl1word1014 = ["R", "E", "I", "V", "E", "S"]

        global lvl1word1036
        lvl1word1036 = ["R", "E", "I", "V", "E", "R"]
        global lvl1word1037
        lvl1word1037 = ["R", "E", "G", "I", "V", "E"]
        global lvl1word1038
        lvl1word1038 = ["R", "E", "G", "I", "U", "S"]
        global lvl1word1039
        lvl1word1039 = ["R", "E", "E", "V", "E", "S"]
        global lvl1word1040
        lvl1word1040 = ["O", "S", "I", "E", "R", "S"]
        global lvl1word1041
        lvl1word1041 = ["O", "G", "R", "E", "S", "S"]
        global lvl1word1042
        lvl1word1042 = ["O", "G", "I", "V", "E", "S"]
        global lvl1word1043
        lvl1word1043 = ["O", "E", "U", "V", "R", "E"]
        global lvl1word1044
        lvl1word1044 = ["I", "S", "S", "U", "E", "S"]
        global lvl1word1045
        lvl1word1045 = ["I", "S", "S", "U", "E", "R"]
        global lvl1word1047
        lvl1word1047 = ["I", "R", "I", "S", "E", "S"]
        global lvl1word1048
        lvl1word1048 = ["G", "U", "R", "G", "E", "S"]
        global lvl1word1049
        lvl1word1049 = ["G", "U", "I", "R", "O", "S"]
        global lvl1word1050
        lvl1word1050 = ["G", "R", "U", "G", "R", "U"]
        global lvl1word1051
        lvl1word1051 = ["G", "R", "O", "V", "E", "S"]
        global lvl1word1052
        lvl1word1052 = ["G", "R", "O", "U", "S", "E"]
        global lvl1word1053
        lvl1word1053 = ["G", "R", "O", "O", "V", "E"]
        global lvl1word1054
        lvl1word1054 = ["G", "R", "I", "E", "V", "E"]
        global lvl1word1055
        lvl1word1055 = ["G", "R", "E", "I", "G", "E"]
        global lvl1word1056
        lvl1word1056 = ["G", "R", "E", "G", "O", "S"]
        global lvl1word1057
        lvl1word1057 = ["G", "O", "U", "G", "E", "S"]
        global lvl1word1058
        lvl1word1058 = ["G", "O", "U", "G", "E", "R"]
        global lvl1word1059
        lvl1word1059 = ["G", "O", "R", "S", "E", "S"]
        global lvl1word1060
        lvl1word1060 = ["G", "O", "R", "I", "E", "R"]
        global lvl1word1061
        lvl1word1061 = ["G", "O", "R", "G", "E", "S"]
        global lvl1word1062
        lvl1word1062 = ["G", "O", "R", "G", "E", "R"]
        global lvl1word1063
        lvl1word1063 = ["G", "O", "O", "S", "E", "S"]
        global lvl1word1064
        lvl1word1064 = ["G", "O", "O", "I", "E", "R"]
        global lvl1word1065
        lvl1word1065 = ["G", "I", "V", "E", "R", "S"]
        global lvl1word1067
        lvl1word1067 = ["E", "R", "U", "G", "O", "S"]
        global lvl1word1068
        lvl1word1068 = ["E", "R", "R", "O", "R", "S"]
        global lvl1word1069
        lvl1word1069 = ["E", "R", "O", "S", "E","S"]
        global lvl1word1070
        lvl1word1070 = ["E", "G", "R", "E", "S", "S"]
        global lvl1word1072
        lvl1word1072 = ["E", "G", "G", "E", "R", "S"]
        global lvl1word1073
        lvl1word1073 = ["E", "E", "R", "I", "E", "R"]
        global lvl1word1074
        lvl1word1074 = ["V", "U", "G", "G", "S"]
        global lvl1word1075
        lvl1word1075 = ["V", "O", "G", "U", "E"]
        global lvl1word1076
        lvl1word1076 = ["V", "O", "G", "I", "E"]
        global lvl1word1077
        lvl1word1077 = ["V", "I", "S", "O", "R"]
        global lvl1word1078
        lvl1word1078 = ["V", "I", "S", "E", "S"]
        global lvl1word1079
        lvl1word1079 = ["V", "I", "R", "U", "S"]
        global lvl1word1080
        lvl1word1080 = ["V", "I", "R", "E", "S"]
        global lvl1word1081
        lvl1word1081 = ["V", "I", "R", "E", "O"]
        global lvl1word1082
        lvl1word1082 = ["V", "I", "G", "O", "R"]
        global lvl1word1083
        lvl1word1083 = ["V", "I", "E", "R", "S"]
        global lvl1word1084
        lvl1word1084 = ["V", "E", "R", "V", "E"]
        global lvl1word1085
        lvl1word1085 = ["V", "E", "R", "S", "O"]
        global lvl1word1086
        lvl1word1086 = ["V", "E", "R", "S", "E"]
        global lvl1word1087
        lvl1word1087 = ["V", "E", "R", "G", "E"]
        global lvl1word1088
        lvl1word1088 = ["V", "E", "G", "I", "E"]
        global lvl1word1089
        lvl1word1089 = ["V", "E", "E", "R", "S"]
        global lvl1word1090
        lvl1word1090 = ["U", "S", "E", "R", "S"]
        global lvl1word1091
        lvl1word1091 = ["U", "R", "G", "E", "S"]
        global lvl1word1092
        lvl1word1092 = ["U", "R", "G", "E", "R"]
        global lvl1word1093
        lvl1word1093 = ["S", "U", "R", "G", "E"]
        global lvl1word1094
        lvl1word1094 = ["S", "U", "R", "E", "R"]
        global lvl1word1095
        lvl1word1095 = ["S", "U", "E", "R", "S"]
        global lvl1word1096
        lvl1word1096 = ["S", "O", "U", "R", "S"]
        global lvl1word1097
        lvl1word1097 = ["S", "O", "R", "U", "S"]
        global lvl1word1098
        lvl1word1098 = ["S", "O", "R", "G", "O"]
        global lvl1word1099
        lvl1word1099 = ["S", "O", "R", "E", "S"]
        global lvl1word1100
        lvl1word1100 = ["S", "O", "R", "E", "R"]
        global lvl1word1101
        lvl1word1101 = ["S", "I", "V", "E", "R"]
        global lvl1word1103
        lvl1word1103 = ["S", "I", "R", "E", "S"]
        global lvl1word1104
        lvl1word1104 = ["S", "I", "R", "E", "E"]
        global lvl1word1105
        lvl1word1105 = ["S", "I", "E", "V", "E"]
        global lvl1word1106
        lvl1word1106 = ["S", "I", "E", "U", "R"]
        global lvl1word1108
        lvl1word1108 = ["S", "E", "V", "E", "R"]
        global lvl1word1109
        lvl1word1109 = ["S", "E", "R", "V", "O"]
        global lvl1word1110
        lvl1word1110 = ["S", "E", "R", "V", "E"]
        global lvl1word1111
        lvl1word1111 = ["S", "E", "R", "G", "E"]
        global lvl1word1112
        lvl1word1112 = ["S", "E", "R", "E", "S"]
        global lvl1word1113
        lvl1word1113 = ["S", "E", "R", "E", "R"]
        global lvl1word1116
        lvl1word1116 = ["S", "E", "G", "O", "S"]
        global lvl1word1117
        lvl1word1117 = ["S", "E", "E", "R", "S"]
        global lvl1word1118
        lvl1word1118 = ["R", "U", "S", "E", "S"]
        global lvl1word1119
        lvl1word1119 = ["R", "U", "E", "R", "S"]
        global lvl1word1120
        lvl1word1120 = ["R", "O", "V", "E", "S"]
        global lvl1word1121
        lvl1word1121 = ["R", "O", "V", "E", "R"]
        global lvl1word1122
        lvl1word1122 = ["R", "O", "U", "S", "E"]
        global lvl1word1123
        lvl1word1123 = ["R", "O", "U", "G", "E"]
        global lvl1word1124
        lvl1word1124 = ["R", "O", "U", "E", "S"]
        global lvl1word1125
        lvl1word1125 = ["R", "O", "S", "E", "S"]
        global lvl1word1126
        lvl1word1126 = ["R", "O", "O", "S", "E"]
        global lvl1word1127
        lvl1word1127 = ["R", "O", "G", "U", "E"]
        global lvl1word1128
        lvl1word1128 = ["R", "O", "G", "E", "R"]
        global lvl1word1129
        lvl1word1129 = ["R", "I", "V", "E", "S"]
        global lvl1word1130
        lvl1word1130 = ["R", "I", "V", "E", "R"]
        global lvl1word1131
        lvl1word1131 = ["R", "I", "S", "E", "S"]
        global lvl1word1132
        lvl1word1132 = ["R", "I", "S", "U", "S"]
        global lvl1word1133
        lvl1word1133 = ["R", "I", "S", "E", "R"]
        global lvl1word1134
        lvl1word1134 = ["R", "I", "G", "O", "R"]
        global lvl1word1135
        lvl1word1135 = ["R", "E", "V", "U", "E"]
        global lvl1word1136
        lvl1word1136 = ["R", "E", "U", "S", "E"]
        global lvl1word1137
        lvl1word1137 = ["R", "E", "S", "E", "E"]
        global lvl1word1138
        lvl1word1138 = ["R", "E", "R", "I", "G"]
        global lvl1word1139
        lvl1word1139 = ["R", "E", "I", "V", "E"]
        global lvl1word1140
        lvl1word1140 = ["R", "E", "G", "E", "S"]
        global lvl1word1141
        lvl1word1141 = ["R", "E", "E", "V", "E"]
        global lvl1word1142
        lvl1word1142 = ["O", "V", "E", "R", "S"]
        global lvl1word1143
        lvl1word1143 = ["O", "U", "R", "I", "E"]
        global lvl1word1144
        lvl1word1144 = ["O", "S", "I", "E", "R"]
        global lvl1word1145
        lvl1word1145 = ["O", "R", "R", "I", "S"]
        global lvl1word1146
        lvl1word1146 = ["O", "O", "R", "I", "E"]
        global lvl1word1147
        lvl1word1147 = ["O", "G", "R", "E", "S"]
        global lvl1word1148
        lvl1word1148 = ["O", "G", "I", "V", "E"]
        global lvl1word1149
        lvl1word1149 = ["O", "G", "E", "E", "S"]
        global lvl1word1150
        lvl1word1150 = ["I", "V", "I", "E", "S"]
        global lvl1word1151
        lvl1word1151 = ["I", "S", "S", "U", "E"]
        global lvl1word1153
        lvl1word1153 = ["G", "U", "R", "U", "S"]
        global lvl1word1154
        lvl1word1154 = ["G", "U", "R", "G", "E"]
        global lvl1word1155
        lvl1word1155 = ["G", "U", "I", "R", "O"]
        global lvl1word1156
        lvl1word1156 = ["G", "R", "U", "E", "S"]
        global lvl1word1157
        lvl1word1157 = ["G", "R", "O", "V", "E"]
        global lvl1word1158
        lvl1word1158 = ["G", "R", "O", "S", "S"]
        global lvl1word1159
        lvl1word1159 = ["G", "R", "O", "G", "S"]
        global lvl1word1160
        lvl1word1160 = ["G", "R", "I", "G", "S"]
        global lvl1word1161
        lvl1word1161 = ["G", "R", "E", "G", "O"]
        global lvl1word1162
        lvl1word1162 = ["G", "R", "E", "E", "S"]
        global lvl1word1163
        lvl1word1163 = ["G", "O", "U", "G", "E"]
        global lvl1word1164
        lvl1word1164 = ["G", "O", "R", "S", "E"]
        global lvl1word1165
        lvl1word1165 = ["G", "O", "R", "G", "E"]
        global lvl1word1166
        lvl1word1166 = ["G", "O", "R", "E", "S"]
        global lvl1word1167
        lvl1word1167 = ["G", "O", "O", "S", "E"]
        global lvl1word1168
        lvl1word1168 = ["G", "O", "G", "O", "S"]
        global lvl1word1169
        lvl1word1169 = ["G", "O", "E", "R", "S"]
        global lvl1word1170
        lvl1word1170 = ["G", "I", "V", "E", "S"]
        global lvl1word1171
        lvl1word1171 = ["G", "I", "V", "E", "R"]
        global lvl1word1172
        lvl1word1172 = ["G", "I", "R", "O", "S"]
        global lvl1word1173
        lvl1word1173 = ["G", "E", "S", "S", "O"]
        global lvl1word1175
        lvl1word1175 = ["E", "U", "R", "O", "S"]
        global lvl1word1176
        lvl1word1176 = ["E", "R", "U", "G", "O"]
        global lvl1word1177
        lvl1word1177 = ["E", "R", "S", "E", "S"]
        global lvl1word1178
        lvl1word1178 = ["E", "R", "R", "O", "R"]
        global lvl1word1179
        lvl1word1179 = ["E", "R", "O", "S", "E"]
        global lvl1word1180
        lvl1word1180 = ["E", "G", "G", "E", "R"]
        global lvl1word1181
        lvl1word1181 = ["E", "G", "E", "R", "S"]
        global lvl1word1182
        lvl1word1182 = ["E", "E", "R", "I", "E"]
        global lvl1word1183
        lvl1word1183 = ["V", "U", "G", "S"]
        global lvl1word1184
        lvl1word1184 = ["V", "U", "G", "G"]
        global lvl1word1185
        lvl1word1185 = ["V", "O", "E", "S"]
        global lvl1word1186
        lvl1word1186 = ["V", "I", "S", "E"]
        global lvl1word1187
        lvl1word1187 = ["V", "I", "G", "S"]
        global lvl1word1188
        lvl1word1188 = ["V", "I", "E", "S"]
        global lvl1word1189
        lvl1word1189 = ["V", "E", "E", "S"]
        global lvl1word1190
        lvl1word1190 = ["V", "E", "E", "R"]
        global lvl1word1191
        lvl1word1191 = ["U", "S", "E", "R"]
        global lvl1word1192
        lvl1word1192 = ["U", "R", "U", "S"]
        global lvl1word1193
        lvl1word1193 = ["U", "R", "G", "E"]
        global lvl1word1194
        lvl1word1194 = ["S", "U", "R", "E"]
        global lvl1word1195
        lvl1word1195 = ["S", "U", "E", "R"]
        global lvl1word1196
        lvl1word1196 = ["S", "R", "I", "S"]
        global lvl1word1197
        lvl1word1197 = ["S", "O", "U", "R"]
        global lvl1word1198
        lvl1word1198 = ["S", "O", "R", "E"]
        global lvl1word1199
        lvl1word1199 = ["S", "I", "R", "S"]
        global lvl1word1200
        lvl1word1200 = ["S", "I", "R", "E"]
        global lvl1word1201
        lvl1word1201 = ["S", "E", "R", "S"]
        global lvl1word1202
        lvl1word1202 = ["S", "E", "R", "E"]
        global lvl1word1203
        lvl1word1203 = ["S", "E", "E", "R"]
        global lvl1word1204
        lvl1word1204 = ["R", "U", "S", "E"]
        global lvl1word1205
        lvl1word1205 = ["R", "U", "G", "S"]
        global lvl1word1206
        lvl1word1206 = ["R", "U", "E", "S"]
        global lvl1word1207
        lvl1word1207 = ["R", "U", "E", "R"]
        global lvl1word1208
        lvl1word1208 = ["R", "O", "V", "E"]
        global lvl1word1209
        lvl1word1209 = ["R", "O", "U", "E"]
        global lvl1word1210
        lvl1word1210 = ["R", "O", "S", "E"]
        global lvl1word1211
        lvl1word1211 = ["R", "O", "E", "S"]
        global lvl1word1212
        lvl1word1212 = ["R", "I", "V", "E"]
        global lvl1word1213
        lvl1word1213 = ["R", "I", "S", "E"]
        global lvl1word1214
        lvl1word1214 = ["R", "I", "G", "S"]
        global lvl1word1215
        lvl1word1215 = ["O", "V", "E", "R"]
        global lvl1word1216
        lvl1word1216 = ["O", "U", "R", "S"]
        global lvl1word1217
        lvl1word1217 = ["O", "S", "E", "S"]
        global lvl1word1218
        lvl1word1218 = ["O", "R", "E", "S"]
        global lvl1word1219
        lvl1word1219 = ["O", "G", "R", "E"]
        global lvl1word1220
        lvl1word1220 = ["I", "R", "I", "S"]
        global lvl1word1221
        lvl1word1221 = ["I", "R", "E", "S"]
        global lvl1word1222
        lvl1word1222 = ["G", "U", "V", "S"]
        global lvl1word1223
        lvl1word1223 = ["G", "U", "R", "U"]
        global lvl1word1224
        lvl1word1224 = ["G", "R", "I", "G"]
        global lvl1word1225
        lvl1word1225 = ["G", "O", "R", "E"]
        global lvl1word1226
        lvl1word1226 = ["G", "O", "O", "S"]
        global lvl1word1227
        lvl1word1227 = ["G", "O", "E", "S"]
        global lvl1word1228
        lvl1word1228 = ["G", "O", "E", "R"]
        global lvl1word1229
        lvl1word1229 = ["G", "I", "V", "E"]
        global lvl1word1230
        lvl1word1230 = ["E", "V", "E", "S"]
        global lvl1word1231
        lvl1word1231 = ["E", "V", "E", "R"]
        global lvl1word1232
        lvl1word1232 = ["E", "U", "R", "O"]
        global lvl1word1233
        lvl1word1233 = ["E", "R", "R", "S"]
        global lvl1word1234
        lvl1word1234 = ["E", "R", "O", "S"]
        global lvl1word1235
        lvl1word1235 = ["E", "R", "G", "S"]
        global lvl1word1236
        lvl1word1236 = ["E", "R", "G", "O"]
        global lvl1word1237
        lvl1word1237 = ["E", "G", "O", "S"]
        global lvl1word1238
        lvl1word1238 = ["E", "G", "E", "R"]
        global lvl1word1239
        lvl1word1239 = ["V", "U", "G"]
        global lvl1word1240
        lvl1word1240 = ["V", "O", "E"]
        global lvl1word1241
        lvl1word1241 = ["V", "I", "E"]
        global lvl1word1242
        lvl1word1242 = ["V", "E", "E"]
        global lvl1word1243
        lvl1word1243 = ["S", "I", "R"]
        global lvl1word1244
        lvl1word1244 = ["R", "U", "G"]
        global lvl1word1245
        lvl1word1245 = ["R", "U", "E"]
        global lvl1word1246
        lvl1word1246 = ["R", "O", "E"]
        global lvl1word1247
        lvl1word1247 = ["R", "I", "G"]
        global lvl1word1248
        lvl1word1248 = ["R", "E", "V"]
        global lvl1word1249
        lvl1word1249 = ["O", "U", "R"]
        global lvl1word1250
        lvl1word1250 = ["O", "R", "S"]
        global lvl1word1251
        lvl1word1251 = ["O", "R", "E"]
        global lvl1word1252
        lvl1word1252 = ["I", "R", "E"]
        global lvl1word1253
        lvl1word1253 = ["G", "U", "V"]
        global lvl1word1254
        lvl1word1254 = ["G", "O", "O"]
        global lvl1word1255
        lvl1word1255 = ["E", "V", "E"]
        global lvl1word1256
        lvl1word1256 = ["E", "R", "R"]
        global lvl1word1257
        lvl1word1257 = ["E", "R", "G"]
        global lvl1word1258
        lvl1word1258 = ["E", "G", "O"]
        global lvl1word1259
        lvl1word1259 = ["S", "O"]
        global lvl1word1260
        lvl1word1260 = ["R", "E"]
        global lvl1word1261
        lvl1word1261 = ["S", "O"]
        global lvl1word1262
        lvl1word1262 = ["O", "S"]
        global lvl1word1263
        lvl1word1263 = ["O", "R"]
        global lvl1word1264
        lvl1word1264 = ["G", "O"]



        # EXCLUDING WORDS 1174 1152 1115 1114 1107 1102 1071 1066 1046 (DOUBLES)






        global lvl1word1CHK
        lvl1word1CHK = 0
        global lvl1word2CHK
        lvl1word2CHK = 0
        global lvl1word3CHK
        lvl1word3CHK = 0
        global lvl1word4CHK
        lvl1word4CHK = 0
        global lvl1word5CHK
        lvl1word5CHK = 0
        global lvl1word6CHK
        lvl1word6CHK = 0
        global lvl1word7CHK
        lvl1word7CHK = 0
        global lvl1word8CHK
        lvl1word8CHK = 0
        global lvl1word9CHK
        lvl1word9CHK = 0
        global lvl1word10CHK
        lvl1word10CHK = 0
        global lvl1word11CHK
        lvl1word11CHK = 0
        global lvl1word12CHK
        lvl1word12CHK = 0
        global lvl1word13CHK
        lvl1word13CHK = 0
        global lvl1word14CHK
        lvl1word14CHK = 0
        global lvl1word15CHK
        lvl1word15CHK = 0
        global lvl1word16CHK
        lvl1word16CHK = 0
        global lvl1word17CHK
        lvl1word17CHK = 0
        global lvl1word18CHK
        lvl1word18CHK = 0
        global lvl1word19CHK
        lvl1word19CHK = 0
        global lvl1word20CHK
        lvl1word20CHK = 0
        global lvl1word21CHK
        lvl1word21CHK = 0
        global lvl1word22CHK
        lvl1word22CHK = 0
        global lvl1word23CHK
        lvl1word23CHK = 0
        global lvl1word24CHK
        lvl1word24CHK = 0
        global lvl1word25CHK
        lvl1word25CHK = 0
        global lvl1word26CHK
        lvl1word26CHK = 0
        global lvl1word27CHK
        lvl1word27CHK = 0 
        global lvl1word28CHK
        lvl1word28CHK = 0
        global lvl1word29CHK
        lvl1word29CHK = 0
        global lvl1word30CHK
        lvl1word30CHK = 0
        global lvl1word31CHK
        lvl1word31CHK = 0
        global lvl1word32CHK
        lvl1word32CHK = 0
        global lvl1word33CHK
        lvl1word33CHK = 0
        global lvl1word34CHK
        lvl1word34CHK = 0
        global lvl1word35CHK
        lvl1word35CHK = 0
        global lvl1word36CHK
        lvl1word36CHK = 0
        global lvl1word37CHK
        lvl1word37CHK = 0
        global lvl1word38CHK
        lvl1word38CHK = 0
        global lvl1word39CHK
        lvl1word39CHK = 0
        global lvl1word40CHK
        lvl1word40CHK = 0 
        global lvl1word41CHK
        lvl1word41CHK = 0
        global lvl1word42CHK
        lvl1word42CHK = 0
        global lvl1word43CHK
        lvl1word43CHK = 0
        global lvl1word44CHK
        lvl1word44CHK = 0
        global lvl1word45CHK
        lvl1word45CHK = 0
        global lvl1word46CHK
        lvl1word46CHK = 0
        global lvl1word47CHK
        lvl1word47CHK = 0
        global lvl1word48CHK
        lvl1word48CHK = 0
        global lvl1word49CHK
        lvl1word49CHK = 0
        global lvl1word50CHK
        lvl1word50CHK = 0
        global lvl1word51CHK
        lvl1word51CHK = 0
        global lvl1word52CHK
        lvl1word52CHK = 0
        global lvl1word53CHK
        lvl1word53CHK = 0
        global lvl1word54CHK
        lvl1word54CHK = 0
        global lvl1word55CHK
        lvl1word55CHK = 0
        global lvl1word56CHK
        lvl1word56CHK = 0
        global lvl1word57CHK
        lvl1word57CHK = 0
        global lvl1word58CHK
        lvl1word58CHK = 0
        global lvl1word59CHK
        lvl1word59CHK = 0
        global lvl1word60CHK
        lvl1word60CHK = 0 
        global lvl1word61CHK
        lvl1word61CHK = 0
        global lvl1word62CHK
        lvl1word62CHK = 0
        global lvl1word63CHK
        lvl1word63CHK = 0
        global lvl1word64CHK
        lvl1word64CHK = 0
        global lvl1word65CHK
        lvl1word65CHK = 0
        global lvl1word66CHK
        lvl1word66CHK = 0
        global lvl1word67CHK
        lvl1word67CHK = 0
        global lvl1word68CHK
        lvl1word68CHK = 0
        global lvl1word69CHK
        lvl1word69CHK = 0
        global lvl1word70CHK
        lvl1word70CHK = 0
        global lvl1word71CHK
        lvl1word71CHK = 0
        global lvl1word72CHK
        lvl1word72CHK = 0
        global lvl1word73CHK
        lvl1word73CHK = 0
        global lvl1word74CHK
        lvl1word74CHK = 0
        global lvl1word75CHK
        lvl1word75CHK = 0
        global lvl1word76CHK
        lvl1word76CHK = 0
        global lvl1word77CHK
        lvl1word77CHK = 0
        global lvl1word78CHK
        lvl1word78CHK = 0
        global lvl1word79CHK
        lvl1word79CHK = 0
        global lvl1word80CHK
        lvl1word80CHK = 0
        global lvl1word81CHK
        lvl1word81CHK = 0
        global lvl1word82CHK
        lvl1word82CHK = 0
        global lvl1word83CHK
        lvl1word83CHK = 0
        global lvl1word84CHK
        lvl1word84CHK = 0
        global lvl1word85CHK
        lvl1word85CHK = 0
        global lvl1word86CHK
        lvl1word86CHK = 0
        global lvl1word87CHK
        lvl1word87CHK = 0
        global lvl1word88CHK
        lvl1word88CHK = 0

        #LEVEL 2
        global lvl1word89CHK
        lvl1word89CHK = 0
        global lvl1word90CHK
        lvl1word90CHK = 0
        global lvl1word91CHK
        lvl1word91CHK = 0
        global lvl1word92CHK
        lvl1word92CHK = 0
        global lvl1word93CHK
        lvl1word93CHK = 0
        global lvl1word94CHK
        lvl1word94CHK = 0
        global lvl1word95CHK
        lvl1word95CHK = 0
        global lvl1word96CHK
        lvl1word96CHK = 0
        global lvl1word97CHK
        lvl1word97CHK = 0
        global lvl1word98CHK
        lvl1word98CHK = 0
        global lvl1word99CHK
        lvl1word99CHK = 0
        global lvl1word100CHK
        lvl1word100CHK = 0
        global lvl1word101CHK
        lvl1word101CHK = 0
        global lvl1word102CHK
        lvl1word102CHK = 0
        global lvl1word103CHK
        lvl1word103CHK = 0
        global lvl1word104CHK
        lvl1word104CHK = 0
        global lvl1word105CHK
        lvl1word105CHK = 0
        global lvl1word106CHK
        lvl1word106CHK = 0
        global lvl1word107CHK
        lvl1word107CHK = 0
        global lvl1word108CHK
        lvl1word108CHK = 0
        global lvl1word109CHK
        lvl1word109CHK = 0
        global lvl1word110CHK
        lvl1word110CHK = 0
        global lvl1word111CHK
        lvl1word111CHK = 0
        global lvl1word112CHK
        lvl1word112CHK = 0
        global lvl1word113CHK
        lvl1word113CHK = 0
        global lvl1word114CHK
        lvl1word114CHK = 0
        global lvl1word115CHK
        lvl1word115CHK = 0
        global lvl1word116CHK
        lvl1word116CHK = 0
        global lvl1word117CHK
        lvl1word117CHK = 0
        global lvl1word118CHK
        lvl1word118CHK = 0
        global lvl1word119CHK
        lvl1word119CHK = 0
        global lvl1word120CHK
        lvl1word120CHK = 0
        global lvl1word121CHK
        lvl1word121CHK = 0
        global lvl1word122CHK
        lvl1word122CHK = 0
        global lvl1word123CHK
        lvl1word123CHK = 0
        global lvl1word124CHK
        lvl1word124CHK = 0
        global lvl1word125CHK
        lvl1word125CHK = 0

        #LEVEL 3
        global lvl1word126CHK
        lvl1word126CHK = 0
        global lvl1word127CHK
        lvl1word127CHK = 0
        global lvl1word128CHK
        lvl1word128CHK = 0
        global lvl1word129CHK
        lvl1word129CHK = 0
        global lvl1word130CHK
        lvl1word130CHK = 0
        global lvl1word131CHK
        lvl1word131CHK = 0
        global lvl1word132CHK
        lvl1word132CHK = 0
        global lvl1word133CHK
        lvl1word133CHK = 0
        global lvl1word134CHK
        lvl1word134CHK = 0
        global lvl1word135CHK
        lvl1word135CHK = 0
        global lvl1word136CHK
        lvl1word136CHK = 0
        global lvl1word137CHK
        lvl1word137CHK = 0
        global lvl1word138CHK
        lvl1word138CHK = 0
        global lvl1word139CHK
        lvl1word139CHK = 0
        global lvl1word140CHK
        lvl1word140CHK = 0
        global lvl1word141CHK
        lvl1word141CHK = 0
        global lvl1word142CHK
        lvl1word142CHK = 0
        global lvl1word143CHK
        lvl1word143CHK = 0
        global lvl1word144CHK
        lvl1word144CHK = 0
        global lvl1word145CHK
        lvl1word145CHK = 0
        global lvl1word146CHK
        lvl1word146CHK = 0
        global lvl1word147CHK
        lvl1word147CHK = 0
        global lvl1word148CHK
        lvl1word148CHK = 0
        global lvl1word149CHK
        lvl1word149CHK = 0
        global lvl1word150CHK
        lvl1word150CHK = 0
        global lvl1word151CHK
        lvl1word151CHK = 0
        global lvl1word152CHK
        lvl1word152CHK = 0
        global lvl1word153CHK
        lvl1word153CHK = 0
        global lvl1word154CHK
        lvl1word154CHK = 0
        global lvl1word155CHK
        lvl1word155CHK = 0
        global lvl1word156CHK
        lvl1word156CHK = 0
        global lvl1word157CHK
        lvl1word157CHK = 0
        global lvl1word158CHK
        lvl1word158CHK = 0
        global lvl1word159CHK
        lvl1word159CHK = 0
        global lvl1word160CHK
        lvl1word160CHK = 0
        global lvl1word161CHK
        lvl1word161CHK = 0
        global lvl1word162CHK
        lvl1word162CHK = 0
        global lvl1word163CHK
        lvl1word163CHK = 0
        global lvl1word164CHK
        lvl1word164CHK = 0
        global lvl1word165CHK
        lvl1word165CHK = 0
        global lvl1word166CHK
        lvl1word166CHK = 0
        global lvl1word167CHK
        lvl1word167CHK = 0
        global lvl1word168CHK
        lvl1word168CHK = 0
        global lvl1word169CHK
        lvl1word169CHK = 0
        global lvl1word170CHK
        lvl1word170CHK = 0
        global lvl1word171CHK
        lvl1word171CHK = 0
        global lvl1word172CHK
        lvl1word172CHK = 0
        global lvl1word173CHK
        lvl1word173CHK = 0
        global lvl1word174CHK
        lvl1word174CHK = 0
        global lvl1word175CHK
        lvl1word175CHK = 0
        global lvl1word176CHK
        lvl1word176CHK = 0
        global lvl1word177CHK
        lvl1word177CHK = 0

        # LEVEL 1 ADDITION
        global lvl1word178CHK
        lvl1word178CHK = 0

        # LEVEL 4 
        global lvl1word179CHK
        lvl1word179CHK = 0
        global lvl1word180CHK
        lvl1word180CHK = 0
        global lvl1word181CHK
        lvl1word181CHK = 0
        global lvl1word182CHK
        lvl1word182CHK = 0
        global lvl1word183CHK
        lvl1word183CHK = 0
        global lvl1word184CHK
        lvl1word184CHK = 0
        global lvl1word185CHK
        lvl1word185CHK = 0
        global lvl1word186CHK
        lvl1word186CHK = 0
        global lvl1word187CHK
        lvl1word187CHK = 0
        global lvl1word188CHK
        lvl1word188CHK = 0
        global lvl1word189CHK
        lvl1word189CHK = 0
        global lvl1word190CHK
        lvl1word190CHK = 0
        global lvl1word191CHK
        lvl1word191CHK = 0
        global lvl1word192CHK
        lvl1word192CHK = 0
        global lvl1word193CHK
        lvl1word193CHK = 0
        global lvl1word194CHK
        lvl1word194CHK = 0
        global lvl1word195CHK
        lvl1word195CHK = 0
        global lvl1word196CHK
        lvl1word196CHK = 0
        global lvl1word197CHK
        lvl1word197CHK = 0
        global lvl1word198CHK
        lvl1word198CHK = 0
        global lvl1word199CHK
        lvl1word199CHK = 0
        global lvl1word200CHK
        lvl1word200CHK = 0
        global lvl1word201CHK
        lvl1word201CHK = 0
        global lvl1word202CHK
        lvl1word202CHK = 0
        global lvl1word203CHK
        lvl1word203CHK = 0
        global lvl1word204CHK
        lvl1word204CHK = 0
        global lvl1word205CHK
        lvl1word205CHK = 0
        global lvl1word206CHK
        lvl1word206CHK = 0
        global lvl1word207CHK
        lvl1word207CHK = 0
        global lvl1word208CHK
        lvl1word208CHK = 0
        global lvl1word209CHK
        lvl1word209CHK = 0
        global lvl1word210CHK
        lvl1word210CHK = 0
        global lvl1word211CHK
        lvl1word211CHK = 0
        global lvl1word212CHK
        lvl1word212CHK = 0
        global lvl1word213CHK
        lvl1word213CHK = 0
        global lvl1word214CHK
        lvl1word214CHK = 0
        global lvl1word215CHK
        lvl1word215CHK = 0
        global lvl1word216CHK
        lvl1word216CHK = 0
        global lvl1word217CHK
        lvl1word217CHK = 0
        global lvl1word218CHK
        lvl1word218CHK = 0
        global lvl1word219CHK
        lvl1word219CHK = 0
        global lvl1word220CHK
        lvl1word220CHK = 0
        global lvl1word221CHK
        lvl1word221CHK = 0
        global lvl1word222CHK
        lvl1word222CHK = 0
        global lvl1word223CHK
        lvl1word223CHK = 0
        global lvl1word224CHK
        lvl1word224CHK = 0
        global lvl1word225CHK
        lvl1word225CHK = 0
        global lvl1word226CHK
        lvl1word226CHK = 0
        global lvl1word227CHK
        lvl1word227CHK = 0
        global lvl1word228CHK
        lvl1word228CHK = 0
        global lvl1word229CHK
        lvl1word229CHK = 0
        global lvl1word230CHK
        lvl1word230CHK = 0
        global lvl1word231CHK
        lvl1word231CHK = 0
        global lvl1word232CHK
        lvl1word232CHK = 0
        global lvl1word233CHK
        lvl1word233CHK = 0
        global lvl1word234CHK
        lvl1word234CHK = 0
        global lvl1word235CHK
        lvl1word235CHK = 0
        global lvl1word236CHK
        lvl1word236CHK = 0
        global lvl1word237CHK
        lvl1word237CHK = 0
        global lvl1word238CHK
        lvl1word238CHK = 0
        global lvl1word239CHK
        lvl1word239CHK = 0

        # LEVEL 5

        global lvl1word240CHK
        lvl1word240CHK = 0
        global lvl1word241CHK
        lvl1word241CHK = 0
        global lvl1word242CHK
        lvl1word242CHK = 0
        global lvl1word243CHK
        lvl1word243CHK = 0
        global lvl1word244CHK
        lvl1word244CHK = 0
        global lvl1word245CHK
        lvl1word245CHK = 0
        global lvl1word246CHK
        lvl1word246CHK = 0
        global lvl1word247CHK
        lvl1word247CHK = 0
        global lvl1word248CHK
        lvl1word248CHK = 0
        global lvl1word249CHK
        lvl1word249CHK = 0
        global lvl1word250CHK
        lvl1word250CHK = 0
        global lvl1word251CHK
        lvl1word251CHK = 0
        global lvl1word252CHK
        lvl1word252CHK = 0
        global lvl1word253CHK
        lvl1word253CHK = 0
        global lvl1word254CHK
        lvl1word254CHK = 0
        global lvl1word255CHK
        lvl1word255CHK = 0
        global lvl1word256CHK
        lvl1word256CHK = 0
        global lvl1word257CHK
        lvl1word257CHK = 0
        global lvl1word258CHK
        lvl1word258CHK = 0
        global lvl1word259CHK
        lvl1word259CHK = 0
        global lvl1word260CHK
        lvl1word260CHK = 0
        global lvl1word261CHK
        lvl1word261CHK = 0
        global lvl1word262CHK
        lvl1word262CHK = 0
        global lvl1word263CHK
        lvl1word263CHK = 0
        global lvl1word264CHK
        lvl1word264CHK = 0
        global lvl1word265CHK
        lvl1word265CHK = 0
        global lvl1word266CHK
        lvl1word266CHK = 0
        global lvl1word267CHK
        lvl1word267CHK = 0
        global lvl1word268CHK
        lvl1word268CHK = 0
        global lvl1word269CHK
        lvl1word269CHK = 0
        global lvl1word270CHK
        lvl1word270CHK = 0
        global lvl1word271CHK
        lvl1word271CHK = 0
        global lvl1word272CHK
        lvl1word272CHK = 0
        global lvl1word273CHK
        lvl1word273CHK = 0
        global lvl1word274CHK
        lvl1word274CHK = 0
        global lvl1word275CHK
        lvl1word275CHK = 0
        global lvl1word276CHK
        lvl1word276CHK = 0
        global lvl1word277CHK
        lvl1word277CHK = 0
        global lvl1word278CHK
        lvl1word278CHK = 0
        global lvl1word279CHK
        lvl1word279CHK = 0
        global lvl1word280CHK
        lvl1word280CHK = 0
        global lvl1word281CHK
        lvl1word281CHK = 0
        global lvl1word282CHK
        lvl1word282CHK = 0
        global lvl1word283CHK
        lvl1word283CHK = 0
        global lvl1word284CHK
        lvl1word284CHK = 0
        global lvl1word285CHK
        lvl1word285CHK = 0
        global lvl1word286CHK
        lvl1word286CHK = 0
        global lvl1word287CHK
        lvl1word287CHK = 0
        global lvl1word288CHK
        lvl1word288CHK = 0
        global lvl1word289CHK
        lvl1word289CHK = 0
        global lvl1word290CHK
        lvl1word290CHK = 0
        global lvl1word291CHK
        lvl1word291CHK = 0
        global lvl1word292CHK
        lvl1word292CHK = 0
        global lvl1word293CHK
        lvl1word293CHK = 0
        global lvl1word294CHK
        lvl1word294CHK = 0
        global lvl1word295CHK
        lvl1word295CHK = 0
        global lvl1word296CHK
        lvl1word296CHK = 0
        global lvl1word297CHK
        lvl1word297CHK = 0
        global lvl1word298CHK
        lvl1word298CHK = 0
        global lvl1word299CHK
        lvl1word299CHK = 0
        global lvl1word300CHK
        lvl1word300CHK = 0
        global lvl1word301CHK
        lvl1word301CHK = 0
        global lvl1word302CHK
        lvl1word302CHK = 0
        global lvl1word303CHK
        lvl1word303CHK = 0
        global lvl1word304CHK
        lvl1word304CHK = 0
        global lvl1word305CHK
        lvl1word305CHK = 0

        # LEVEL 6

        global lvl1word306CHK
        lvl1word306CHK = 0
        global lvl1word307CHK
        lvl1word307CHK = 0
        global lvl1word308CHK
        lvl1word308CHK = 0
        global lvl1word309CHK
        lvl1word309CHK = 0
        global lvl1word310CHK
        lvl1word310CHK = 0
        global lvl1word311CHK
        lvl1word311CHK = 0
        global lvl1word312CHK
        lvl1word312CHK = 0
        global lvl1word313CHK
        lvl1word313CHK = 0
        global lvl1word314CHK
        lvl1word314CHK = 0
        global lvl1word315CHK
        lvl1word315CHK = 0
        global lvl1word316CHK
        lvl1word316CHK = 0
        global lvl1word317CHK
        lvl1word317CHK = 0
        global lvl1word318CHK
        lvl1word318CHK = 0
        global lvl1word319CHK
        lvl1word319CHK = 0
        global lvl1word320CHK
        lvl1word320CHK = 0
        global lvl1word321CHK
        lvl1word321CHK = 0
        global lvl1word322CHK
        lvl1word322CHK = 0
        global lvl1word323CHK
        lvl1word323CHK = 0
        global lvl1word324CHK
        lvl1word324CHK = 0
        global lvl1word325CHK
        lvl1word325CHK = 0
        global lvl1word326CHK
        lvl1word326CHK = 0
        global lvl1word327CHK
        lvl1word327CHK = 0
        global lvl1word328CHK
        lvl1word328CHK = 0
        global lvl1word329CHK
        lvl1word329CHK = 0
        global lvl1word330CHK
        lvl1word330CHK = 0
        global lvl1word331CHK
        lvl1word331CHK = 0
        global lvl1word332CHK
        lvl1word332CHK = 0
        global lvl1word333CHK
        lvl1word333CHK = 0
        global lvl1word334CHK
        lvl1word334CHK = 0
        global lvl1word335CHK
        lvl1word335CHK = 0
        global lvl1word336CHK
        lvl1word336CHK = 0
        global lvl1word337CHK
        lvl1word337CHK = 0
        global lvl1word338CHK
        lvl1word338CHK = 0
        global lvl1word339CHK
        lvl1word339CHK = 0
        global lvl1word340CHK
        lvl1word340CHK = 0
        global lvl1word341CHK
        lvl1word341CHK = 0
        global lvl1word342CHK
        lvl1word342CHK = 0
        global lvl1word343CHK
        lvl1word343CHK = 0
        global lvl1word344CHK
        lvl1word344CHK = 0
        global lvl1word345CHK
        lvl1word345CHK = 0
        global lvl1word346CHK
        lvl1word346CHK = 0


        # LEVEL 1 ADDITION

        global lvl1word347CHK
        lvl1word347CHK = 0


        # LEVEL 7


        global lvl1word348CHK
        lvl1word348CHK = 0
        global lvl1word349CHK
        lvl1word349CHK = 0
        global lvl1word350CHK
        lvl1word350CHK = 0
        global lvl1word351CHK
        lvl1word351CHK = 0
        global lvl1word352CHK
        lvl1word352CHK = 0
        global lvl1word353CHK
        lvl1word353CHK = 0
        global lvl1word354CHK
        lvl1word354CHK = 0
        global lvl1word355CHK
        lvl1word355CHK = 0
        global lvl1word356CHK
        lvl1word356CHK = 0
        global lvl1word357CHK
        lvl1word357CHK = 0
        global lvl1word358CHK
        lvl1word358CHK = 0
        global lvl1word359CHK
        lvl1word359CHK = 0
        global lvl1word360CHK
        lvl1word360CHK = 0
        global lvl1word361CHK
        lvl1word361CHK = 0
        global lvl1word362CHK
        lvl1word362CHK = 0
        global lvl1word363CHK
        lvl1word363CHK = 0
        global lvl1word364CHK
        lvl1word364CHK = 0
        global lvl1word365CHK
        lvl1word365CHK = 0
        global lvl1word366CHK
        lvl1word366CHK = 0
        global lvl1word367CHK
        lvl1word367CHK = 0
        global lvl1word368CHK
        lvl1word368CHK = 0
        global lvl1word369CHK
        lvl1word369CHK = 0
        global lvl1word370CHK
        lvl1word370CHK = 0
        global lvl1word371CHK
        lvl1word371CHK = 0
        global lvl1word372CHK
        lvl1word372CHK = 0
        global lvl1word373CHK
        lvl1word373CHK = 0
        global lvl1word374CHK
        lvl1word374CHK = 0
        global lvl1word375CHK
        lvl1word375CHK = 0
        global lvl1word376CHK
        lvl1word376CHK = 0
        global lvl1word377CHK
        lvl1word377CHK = 0
        global lvl1word378CHK
        lvl1word378CHK = 0
        global lvl1word379CHK
        lvl1word379CHK = 0
        global lvl1word380CHK
        lvl1word380CHK = 0
        global lvl1word381CHK
        lvl1word381CHK = 0
        global lvl1word382CHK
        lvl1word382CHK = 0
        global lvl1word383CHK
        lvl1word383CHK = 0
        global lvl1word384CHK
        lvl1word384CHK = 0
        global lvl1word385CHK
        lvl1word385CHK = 0
        global lvl1word386CHK
        lvl1word386CHK = 0
        global lvl1word387CHK
        lvl1word387CHK = 0
        global lvl1word388CHK
        lvl1word388CHK = 0
        global lvl1word389CHK
        lvl1word389CHK = 0
        global lvl1word390CHK
        lvl1word390CHK = 0


        # LEVEL 8

        global lvl1word391CHK
        lvl1word391CHK = 0
        global lvl1word392CHK
        lvl1word392CHK = 0
        global lvl1word393CHK
        lvl1word393CHK = 0
        global lvl1word394CHK
        lvl1word394CHK = 0
        global lvl1word395CHK
        lvl1word395CHK = 0
        global lvl1word396CHK
        lvl1word396CHK = 0
        global lvl1word397CHK
        lvl1word397CHK = 0
        global lvl1word398CHK
        lvl1word398CHK = 0
        global lvl1word399CHK
        lvl1word399CHK = 0
        global lvl1word400CHK
        lvl1word400CHK = 0
        global lvl1word401CHK
        lvl1word401CHK = 0
        global lvl1word402CHK
        lvl1word402CHK = 0
        global lvl1word403CHK
        lvl1word403CHK = 0
        global lvl1word404CHK
        lvl1word404CHK = 0
        global lvl1word405CHK
        lvl1word405CHK = 0
        global lvl1word406CHK
        lvl1word406CHK = 0
        global lvl1word407CHK
        lvl1word407CHK = 0
        global lvl1word408CHK
        lvl1word408CHK = 0
        global lvl1word409CHK
        lvl1word409CHK = 0
        global lvl1word410CHK
        lvl1word410CHK = 0
        global lvl1word411CHK
        lvl1word411CHK = 0
        global lvl1word412CHK
        lvl1word412CHK = 0
        global lvl1word413CHK
        lvl1word413CHK = 0
        global lvl1word414CHK
        lvl1word414CHK = 0
        global lvl1word415CHK
        lvl1word415CHK = 0
        global lvl1word416CHK
        lvl1word416CHK = 0
        global lvl1word417CHK
        lvl1word417CHK = 0
        global lvl1word418CHK
        lvl1word418CHK = 0
        global lvl1word419CHK
        lvl1word419CHK = 0
        global lvl1word420CHK
        lvl1word420CHK = 0
        global lvl1word421CHK
        lvl1word421CHK = 0
        global lvl1word422CHK
        lvl1word422CHK = 0
        global lvl1word423CHK
        lvl1word423CHK = 0
        global lvl1word424CHK
        lvl1word424CHK = 0
        global lvl1word425CHK
        lvl1word425CHK = 0
        global lvl1word426CHK
        lvl1word426CHK = 0
        global lvl1word427CHK
        lvl1word427CHK = 0
        global lvl1word428CHK
        lvl1word428CHK = 0
        global lvl1word429CHK
        lvl1word429CHK = 0
        global lvl1word430CHK
        lvl1word430CHK = 0
        global lvl1word431CHK
        lvl1word431CHK = 0
        global lvl1word432CHK
        lvl1word432CHK = 0
        global lvl1word433CHK
        lvl1word433CHK = 0
        global lvl1word434CHK
        lvl1word434CHK = 0
        global lvl1word435CHK
        lvl1word435CHK = 0
        global lvl1word436CHK
        lvl1word436CHK = 0
        global lvl1word437CHK
        lvl1word437CHK = 0
        global lvl1word438CHK
        lvl1word438CHK = 0
        global lvl1word439CHK
        lvl1word439CHK = 0
        global lvl1word440CHK
        lvl1word440CHK = 0
        global lvl1word441CHK
        lvl1word441CHK = 0
        global lvl1word442CHK
        lvl1word442CHK = 0
        global lvl1word443CHK
        lvl1word443CHK = 0
        global lvl1word444CHK
        lvl1word444CHK = 0
        global lvl1word445CHK
        lvl1word445CHK = 0
        global lvl1word446CHK
        lvl1word446CHK = 0
        global lvl1word447CHK
        lvl1word447CHK = 0
        global lvl1word448CHK
        lvl1word448CHK = 0
        global lvl1word449CHK
        lvl1word449CHK = 0
        global lvl1word450CHK
        lvl1word450CHK = 0
        global lvl1word451CHK
        lvl1word451CHK = 0
        global lvl1word452CHK
        lvl1word452CHK = 0
        global lvl1word453CHK
        lvl1word453CHK = 0
        global lvl1word454CHK
        lvl1word454CHK = 0
        global lvl1word455CHK
        lvl1word455CHK = 0
        global lvl1word456CHK
        lvl1word456CHK = 0
        global lvl1word457CHK
        lvl1word457CHK = 0
        global lvl1word458CHK
        lvl1word458CHK = 0
        global lvl1word459CHK
        lvl1word459CHK = 0
        global lvl1word460CHK
        lvl1word460CHK = 0
        global lvl1word461CHK
        lvl1word461CHK = 0
        global lvl1word462CHK
        lvl1word462CHK = 0
        global lvl1word463CHK
        lvl1word463CHK = 0
        global lvl1word464CHK
        lvl1word464CHK = 0
        global lvl1word465CHK
        lvl1word465CHK = 0
        global lvl1word466CHK
        lvl1word466CHK = 0
        global lvl1word467CHK
        lvl1word467CHK = 0
        global lvl1word468CHK
        lvl1word468CHK = 0
        global lvl1word469CHK
        lvl1word469CHK = 0
        global lvl1word470CHK
        lvl1word470CHK = 0
        global lvl1word471CHK
        lvl1word471CHK = 0
        global lvl1word472CHK
        lvl1word472CHK = 0
        global lvl1word473CHK
        lvl1word473CHK = 0
        global lvl1word474CHK
        lvl1word474CHK = 0
        global lvl1word475CHK
        lvl1word475CHK = 0
        global lvl1word476CHK
        lvl1word476CHK = 0
        global lvl1word477CHK
        lvl1word477CHK = 0
        global lvl1word478CHK
        lvl1word478CHK = 0
        global lvl1word479CHK
        lvl1word479CHK = 0
        global lvl1word480CHK
        lvl1word480CHK = 0
        global lvl1word481CHK
        lvl1word481CHK = 0
        global lvl1word482CHK
        lvl1word482CHK = 0
        global lvl1word483CHK
        lvl1word483CHK = 0
        global lvl1word484CHK
        lvl1word484CHK = 0
        global lvl1word485CHK
        lvl1word485CHK = 0
        global lvl1word486CHK
        lvl1word486CHK = 0
        global lvl1word487CHK
        lvl1word487CHK = 0
        global lvl1word488CHK
        lvl1word488CHK = 0
        global lvl1word489CHK
        lvl1word489CHK = 0
        global lvl1word490CHK
        lvl1word490CHK = 0
        global lvl1word491CHK
        lvl1word491CHK = 0
        global lvl1word492CHK
        lvl1word492CHK = 0
        global lvl1word493CHK
        lvl1word493CHK = 0
        global lvl1word494CHK
        lvl1word494CHK = 0
        global lvl1word495CHK
        lvl1word495CHK = 0
        global lvl1word496CHK
        lvl1word496CHK = 0
        global lvl1word497CHK
        lvl1word497CHK = 0
        global lvl1word498CHK
        lvl1word498CHK = 0
        global lvl1word499CHK
        lvl1word499CHK = 0
        global lvl1word500CHK
        lvl1word500CHK = 0
        global lvl1word501CHK
        lvl1word501CHK = 0
        global lvl1word502CHK
        lvl1word502CHK = 0
        global lvl1word503CHK
        lvl1word503CHK = 0
        global lvl1word504CHK
        lvl1word504CHK = 0
        global lvl1word505CHK
        lvl1word505CHK = 0
        global lvl1word506CHK
        lvl1word506CHK = 0
        global lvl1word507CHK
        lvl1word507CHK = 0
        global lvl1word508CHK
        lvl1word508CHK = 0
        global lvl1word509CHK
        lvl1word509CHK = 0
        global lvl1word510CHK
        lvl1word510CHK = 0
        global lvl1word511CHK
        lvl1word511CHK = 0
        global lvl1word512CHK
        lvl1word512CHK = 0
        global lvl1word513CHK
        lvl1word513CHK = 0
        global lvl1word514CHK
        lvl1word514CHK = 0
        global lvl1word515CHK
        lvl1word515CHK = 0
        global lvl1word516CHK
        lvl1word516CHK = 0
        global lvl1word517CHK
        lvl1word517CHK = 0
        global lvl1word518CHK
        lvl1word518CHK = 0
        global lvl1word519CHK
        lvl1word519CHK = 0
        global lvl1word520CHK
        lvl1word520CHK = 0
        global lvl1word521CHK
        lvl1word521CHK = 0
        global lvl1word522CHK
        lvl1word522CHK = 0

        #LEVEL 9 
        global lvl1word523CHK
        lvl1word523CHK = 0
        global lvl1word524CHK
        lvl1word524CHK = 0
        global lvl1word525CHK
        lvl1word525CHK = 0
        global lvl1word526CHK
        lvl1word526CHK = 0
        global lvl1word527CHK
        lvl1word527CHK = 0
        global lvl1word528CHK
        lvl1word528CHK = 0
        global lvl1word529CHK
        lvl1word529CHK = 0
        global lvl1word530CHK
        lvl1word530CHK = 0
        global lvl1word531CHK
        lvl1word531CHK = 0
        global lvl1word532CHK
        lvl1word532CHK = 0
        global lvl1word533CHK
        lvl1word533CHK = 0
        global lvl1word534CHK
        lvl1word534CHK = 0
        global lvl1word535CHK
        lvl1word535CHK = 0
        global lvl1word536CHK
        lvl1word536CHK = 0
        global lvl1word537CHK
        lvl1word537CHK = 0
        global lvl1word538CHK
        lvl1word538CHK = 0
        global lvl1word539CHK
        lvl1word539CHK = 0
        global lvl1word540CHK
        lvl1word540CHK = 0
        global lvl1word541CHK
        lvl1word541CHK = 0
        global lvl1word542CHK
        lvl1word542CHK = 0
        global lvl1word543CHK
        lvl1word543CHK = 0
        global lvl1word544CHK
        lvl1word544CHK = 0
        global lvl1word545CHK
        lvl1word545CHK = 0
        global lvl1word546CHK
        lvl1word546CHK = 0
        global lvl1word547CHK
        lvl1word547CHK = 0
        global lvl1word548CHK
        lvl1word548CHK = 0
        global lvl1word549CHK
        lvl1word549CHK = 0
        global lvl1word550CHK
        lvl1word550CHK = 0
        global lvl1word551CHK
        lvl1word551CHK = 0
        global lvl1word552CHK
        lvl1word552CHK = 0
        global lvl1word553CHK
        lvl1word553CHK = 0
        global lvl1word554CHK
        lvl1word554CHK = 0
        global lvl1word555CHK
        lvl1word555CHK = 0
        global lvl1word556CHK
        lvl1word556CHK = 0
        global lvl1word557CHK
        lvl1word557CHK = 0
        global lvl1word558CHK
        lvl1word558CHK = 0
        global lvl1word559CHK
        lvl1word559CHK = 0
        global lvl1word560CHK
        lvl1word560CHK = 0
        global lvl1word561CHK
        lvl1word561CHK = 0
        global lvl1word562CHK
        lvl1word562CHK = 0
        global lvl1word563CHK
        lvl1word563CHK = 0
        global lvl1word564CHK
        lvl1word564CHK = 0
        global lvl1word565CHK
        lvl1word565CHK = 0
        global lvl1word566CHK
        lvl1word566CHK = 0
        global lvl1word567CHK
        lvl1word567CHK = 0
        global lvl1word568CHK
        lvl1word568CHK = 0
        global lvl1word569CHK
        lvl1word569CHK = 0
        global lvl1word570CHK
        lvl1word570CHK = 0
        global lvl1word571CHK
        lvl1word571CHK = 0
        global lvl1word572CHK
        lvl1word572CHK = 0
        global lvl1word573CHK
        lvl1word573CHK = 0
        global lvl1word574CHK
        lvl1word574CHK = 0
        global lvl1word575CHK
        lvl1word575CHK = 0
        global lvl1word576CHK
        lvl1word576CHK = 0
        global lvl1word577CHK
        lvl1word577CHK = 0
        global lvl1word578CHK
        lvl1word578CHK = 0
        global lvl1word579CHK
        lvl1word579CHK = 0
        global lvl1word580CHK
        lvl1word580CHK = 0
        global lvl1word581CHK
        lvl1word581CHK = 0
        global lvl1word582CHK
        lvl1word582CHK = 0
        global lvl1word583CHK
        lvl1word583CHK = 0
        global lvl1word584CHK
        lvl1word584CHK = 0
        global lvl1word585CHK
        lvl1word585CHK = 0
        global lvl1word586CHK
        lvl1word586CHK = 0
        global lvl1word587CHK
        lvl1word587CHK = 0
        global lvl1word588CHK
        lvl1word588CHK = 0
        global lvl1word589CHK
        lvl1word589CHK = 0
        global lvl1word590CHK
        lvl1word590CHK = 0
        global lvl1word591CHK
        lvl1word591CHK = 0
        global lvl1word592CHK
        lvl1word592CHK = 0
        global lvl1word593CHK
        lvl1word593CHK = 0
        global lvl1word594CHK
        lvl1word594CHK = 0
        global lvl1word595CHK
        lvl1word595CHK = 0
        global lvl1word596CHK
        lvl1word596CHK = 0
        global lvl1word597CHK
        lvl1word597CHK = 0
        global lvl1word598CHK
        lvl1word598CHK = 0
        global lvl1word599CHK
        lvl1word599CHK = 0
        global lvl1word600CHK
        lvl1word600CHK = 0
        global lvl1word601CHK
        lvl1word601CHK = 0
        global lvl1word602CHK
        lvl1word602CHK = 0
        global lvl1word603CHK
        lvl1word603CHK = 0
        global lvl1word604CHK
        lvl1word604CHK = 0
        global lvl1word605CHK
        lvl1word605CHK = 0
        global lvl1word606CHK
        lvl1word606CHK = 0
        global lvl1word607CHK
        lvl1word607CHK = 0
        global lvl1word608CHK
        lvl1word608CHK = 0
        global lvl1word609CHK
        lvl1word609CHK = 0
        global lvl1word610CHK
        lvl1word610CHK = 0
        global lvl1word611CHK
        lvl1word611CHK = 0
        global lvl1word612CHK
        lvl1word612CHK = 0
        global lvl1word613CHK
        lvl1word613CHK = 0
        global lvl1word614CHK
        lvl1word614CHK = 0
        global lvl1word615CHK
        lvl1word615CHK = 0
        global lvl1word616CHK
        lvl1word616CHK = 0
        global lvl1word617CHK
        lvl1word617CHK = 0
        global lvl1word618CHK
        lvl1word618CHK = 0
        global lvl1word619CHK
        lvl1word619CHK = 0
        global lvl1word620CHK
        lvl1word620CHK = 0
        global lvl1word621CHK
        lvl1word621CHK = 0
        global lvl1word622CHK
        lvl1word622CHK = 0
        global lvl1word623CHK
        lvl1word623CHK = 0
        global lvl1word624CHK
        lvl1word624CHK = 0
        global lvl1word625CHK
        lvl1word625CHK = 0
        global lvl1word626CHK
        lvl1word626CHK = 0
        global lvl1word627CHK
        lvl1word627CHK = 0
        global lvl1word628CHK
        lvl1word628CHK = 0
        global lvl1word629CHK
        lvl1word629CHK = 0
        global lvl1word630CHK
        lvl1word630CHK = 0
        global lvl1word631CHK
        lvl1word631CHK = 0
        global lvl1word632CHK
        lvl1word632CHK = 0
        global lvl1word633CHK
        lvl1word633CHK = 0
        global lvl1word634CHK
        lvl1word634CHK = 0
        global lvl1word635CHK
        lvl1word635CHK = 0
        global lvl1word636CHK
        lvl1word636CHK = 0
        global lvl1word637CHK
        lvl1word637CHK = 0
        global lvl1word638CHK
        lvl1word638CHK = 0
        global lvl1word639CHK
        lvl1word639CHK = 0
        global lvl1word640CHK
        lvl1word640CHK = 0
        global lvl1word641CHK
        lvl1word641CHK = 0
        global lvl1word642CHK
        lvl1word642CHK = 0
        global lvl1word643CHK
        lvl1word643CHK = 0
        global lvl1word644CHK
        lvl1word644CHK = 0
        global lvl1word645CHK
        lvl1word645CHK = 0
        global lvl1word646CHK
        lvl1word646CHK = 0
        global lvl1word647CHK
        lvl1word647CHK = 0
        global lvl1word648CHK
        lvl1word648CHK = 0
        global lvl1word649CHK
        lvl1word649CHK = 0
        global lvl1word650CHK
        lvl1word650CHK = 0
        global lvl1word651CHK
        lvl1word651CHK = 0
        global lvl1word652CHK
        lvl1word652CHK = 0
        global lvl1word653CHK
        lvl1word653CHK = 0
        global lvl1word654CHK
        lvl1word654CHK = 0
        global lvl1word655CHK
        lvl1word655CHK = 0
        global lvl1word656CHK
        lvl1word656CHK = 0
        global lvl1word657CHK
        lvl1word657CHK = 0
        global lvl1word658CHK
        lvl1word658CHK = 0
        global lvl1word659CHK
        lvl1word659CHK = 0
        global lvl1word660CHK
        lvl1word660CHK = 0
        global lvl1word661CHK
        lvl1word661CHK = 0
        global lvl1word662CHK
        lvl1word662CHK = 0
        global lvl1word663CHK
        lvl1word663CHK = 0
        global lvl1word664CHK
        lvl1word664CHK = 0
        global lvl1word665CHK
        lvl1word665CHK = 0
        global lvl1word666CHK
        lvl1word666CHK = 0
        global lvl1word667CHK
        lvl1word667CHK = 0
        global lvl1word668CHK
        lvl1word668CHK = 0
        global lvl1word669CHK
        lvl1word669CHK = 0
        global lvl1word670CHK
        lvl1word670CHK = 0
        global lvl1word671CHK
        lvl1word671CHK = 0
        global lvl1word672CHK
        lvl1word672CHK = 0
        global lvl1word673CHK
        lvl1word673CHK = 0
        global lvl1word674CHK
        lvl1word674CHK = 0
        global lvl1word675CHK
        lvl1word675CHK = 0
        global lvl1word676CHK
        lvl1word676CHK = 0
        global lvl1word677CHK
        lvl1word677CHK = 0
        global lvl1word678CHK
        lvl1word678CHK = 0
        global lvl1word679CHK
        lvl1word679CHK = 0
        global lvl1word680CHK
        lvl1word680CHK = 0
        global lvl1word681CHK
        lvl1word681CHK = 0
        global lvl1word682CHK
        lvl1word682CHK = 0
        global lvl1word683CHK
        lvl1word683CHK = 0
        global lvl1word684CHK
        lvl1word684CHK = 0
        global lvl1word685CHK
        lvl1word685CHK = 0
        global lvl1word686CHK
        lvl1word686CHK = 0
        global lvl1word687CHK
        lvl1word687CHK = 0
        global lvl1word688CHK
        lvl1word688CHK = 0
        global lvl1word689CHK
        lvl1word689CHK = 0
        global lvl1word690CHK
        lvl1word690CHK = 0
        global lvl1word691CHK
        lvl1word691CHK = 0
        global lvl1word692CHK
        lvl1word692CHK = 0
        global lvl1word693CHK
        lvl1word693CHK = 0
        global lvl1word694CHK
        lvl1word694CHK = 0
        global lvl1word695CHK
        lvl1word695CHK = 0
        global lvl1word696CHK
        lvl1word696CHK = 0
        global lvl1word697CHK
        lvl1word697CHK = 0
        global lvl1word698CHK
        lvl1word698CHK = 0
        global lvl1word699CHK
        lvl1word699CHK = 0
        global lvl1word700CHK
        lvl1word700CHK = 0
        global lvl1word701CHK
        lvl1word701CHK = 0
        global lvl1word702CHK
        lvl1word702CHK = 0
        global lvl1word703CHK
        lvl1word703CHK = 0
        global lvl1word704CHK
        lvl1word704CHK = 0
        global lvl1word705CHK
        lvl1word705CHK = 0
        global lvl1word706CHK
        lvl1word706CHK = 0
        global lvl1word707CHK
        lvl1word707CHK = 0
        global lvl1word708CHK
        lvl1word708CHK = 0
        global lvl1word709CHK
        lvl1word709CHK = 0
        global lvl1word710CHK
        lvl1word710CHK = 0
        global lvl1word711CHK
        lvl1word711CHK = 0
        global lvl1word712CHK
        lvl1word712CHK = 0
        global lvl1word713CHK
        lvl1word713CHK = 0
        global lvl1word714CHK
        lvl1word714CHK = 0
        global lvl1word715CHK
        lvl1word715CHK = 0
        global lvl1word716CHK
        lvl1word716CHK = 0
        global lvl1word717CHK
        lvl1word717CHK = 0
        global lvl1word718CHK
        lvl1word718CHK = 0
        global lvl1word719CHK
        lvl1word719CHK = 0
        global lvl1word720CHK
        lvl1word720CHK = 0
        global lvl1word721CHK
        lvl1word721CHK = 0
        global lvl1word722CHK
        lvl1word722CHK = 0
        global lvl1word723CHK
        lvl1word723CHK = 0
        global lvl1word724CHK
        lvl1word724CHK = 0
        global lvl1word725CHK
        lvl1word725CHK = 0
        global lvl1word726CHK
        lvl1word726CHK = 0
        global lvl1word727CHK
        lvl1word727CHK = 0
        global lvl1word728CHK
        lvl1word728CHK = 0
        global lvl1word729CHK
        lvl1word729CHK = 0
        global lvl1word730CHK
        lvl1word730CHK = 0
        global lvl1word731CHK
        lvl1word731CHK = 0
        global lvl1word732CHK
        lvl1word732CHK = 0
        global lvl1word733CHK
        lvl1word733CHK = 0
        global lvl1word734CHK
        lvl1word734CHK = 0
        global lvl1word735CHK
        lvl1word735CHK = 0
        global lvl1word736CHK
        lvl1word736CHK = 0
        global lvl1word737CHK
        lvl1word737CHK = 0
        global lvl1word738CHK
        lvl1word738CHK = 0
        global lvl1word739CHK
        lvl1word739CHK = 0
        global lvl1word740CHK
        lvl1word740CHK = 0
        global lvl1word741CHK
        lvl1word741CHK = 0
        global lvl1word742CHK
        lvl1word742CHK = 0
        global lvl1word743CHK
        lvl1word743CHK = 0
        global lvl1word744CHK
        lvl1word744CHK = 0
        global lvl1word745CHK
        lvl1word745CHK = 0
        global lvl1word746CHK
        lvl1word746CHK = 0
        global lvl1word747CHK
        lvl1word747CHK = 0
        global lvl1word748CHK
        lvl1word748CHK = 0
        global lvl1word749CHK
        lvl1word749CHK = 0
        global lvl1word750CHK
        lvl1word750CHK = 0
        global lvl1word751CHK
        lvl1word751CHK = 0
        global lvl1word752CHK
        lvl1word752CHK = 0
        global lvl1word753CHK
        lvl1word753CHK = 0
        global lvl1word754CHK
        lvl1word754CHK = 0
        global lvl1word755CHK
        lvl1word755CHK = 0
        global lvl1word756CHK
        lvl1word756CHK = 0
        global lvl1word757CHK
        lvl1word757CHK = 0
        global lvl1word758CHK
        lvl1word758CHK = 0
        global lvl1word759CHK
        lvl1word759CHK = 0
        global lvl1word760CHK
        lvl1word760CHK = 0
        global lvl1word761CHK
        lvl1word761CHK = 0
        global lvl1word762CHK
        lvl1word762CHK = 0
        global lvl1word763CHK
        lvl1word763CHK = 0
        global lvl1word764CHK
        lvl1word764CHK = 0
        global lvl1word765CHK
        lvl1word765CHK = 0
        global lvl1word766CHK
        lvl1word766CHK = 0
        global lvl1word767CHK
        lvl1word767CHK = 0
        global lvl1word768CHK
        lvl1word768CHK = 0
        global lvl1word769CHK
        lvl1word769CHK = 0
        global lvl1word770CHK
        lvl1word770CHK = 0
        global lvl1word771CHK
        lvl1word771CHK = 0
        global lvl1word772CHK
        lvl1word772CHK = 0
        global lvl1word773CHK
        lvl1word773CHK = 0
        global lvl1word774CHK
        lvl1word774CHK = 0
        global lvl1word775CHK
        lvl1word775CHK = 0
        global lvl1word776CHK
        lvl1word776CHK = 0
        global lvl1word777CHK
        lvl1word777CHK = 0
        global lvl1word778CHK
        lvl1word778CHK = 0
        global lvl1word779CHK
        lvl1word779CHK = 0
        global lvl1word780CHK
        lvl1word780CHK = 0
        global lvl1word781CHK
        lvl1word781CHK = 0
        global lvl1word782CHK
        lvl1word782CHK = 0
        global lvl1word783CHK
        lvl1word783CHK = 0
        global lvl1word784CHK
        lvl1word784CHK = 0
        global lvl1word785CHK
        lvl1word785CHK = 0
        global lvl1word786CHK
        lvl1word786CHK = 0
        global lvl1word787CHK
        lvl1word787CHK = 0
        global lvl1word788CHK
        lvl1word788CHK = 0
        global lvl1word789CHK
        lvl1word789CHK = 0
        global lvl1word790CHK
        lvl1word790CHK = 0
        global lvl1word791CHK
        lvl1word791CHK = 0
        global lvl1word792CHK
        lvl1word792CHK = 0
        global lvl1word793CHK
        lvl1word793CHK = 0
        global lvl1word794CHK
        lvl1word794CHK = 0
        global lvl1word795CHK
        lvl1word795CHK = 0
        global lvl1word796CHK
        lvl1word796CHK = 0
        global lvl1word797CHK
        lvl1word797CHK = 0
        global lvl1word798CHK
        lvl1word798CHK = 0
        global lvl1word799CHK
        lvl1word799CHK = 0
        global lvl1word800CHK
        lvl1word800CHK = 0
        global lvl1word801CHK
        lvl1word801CHK = 0
        global lvl1word802CHK
        lvl1word802CHK = 0
        global lvl1word803CHK
        lvl1word803CHK = 0
        global lvl1word804CHK
        lvl1word804CHK = 0
        global lvl1word805CHK
        lvl1word805CHK = 0
        global lvl1word806CHK
        lvl1word806CHK = 0
        global lvl1word807CHK
        lvl1word807CHK = 0
        global lvl1word808CHK
        lvl1word808CHK = 0
        global lvl1word809CHK
        lvl1word809CHK = 0






        #LEVEL 10
        global lvl1word810CHK
        lvl1word810CHK = 0
        global lvl1word811CHK
        lvl1word811CHK = 0
        global lvl1word812CHK
        lvl1word812CHK = 0
        global lvl1word813CHK
        lvl1word813CHK = 0
        global lvl1word814CHK
        lvl1word814CHK = 0
        global lvl1word815CHK
        lvl1word815CHK = 0
        global lvl1word816CHK
        lvl1word816CHK = 0
        global lvl1word817CHK
        lvl1word817CHK = 0
        global lvl1word818CHK
        lvl1word818CHK = 0
        global lvl1word819CHK
        lvl1word819CHK = 0
        global lvl1word820CHK
        lvl1word820CHK = 0
        global lvl1word821CHK
        lvl1word821CHK = 0
        global lvl1word822CHK
        lvl1word822CHK = 0
        global lvl1word823CHK
        lvl1word823CHK = 0
        global lvl1word824CHK
        lvl1word824CHK = 0
        global lvl1word825CHK
        lvl1word825CHK = 0
        global lvl1word826CHK
        lvl1word826CHK = 0
        global lvl1word827CHK
        lvl1word827CHK = 0
        global lvl1word828CHK
        lvl1word828CHK = 0
        global lvl1word829CHK
        lvl1word829CHK = 0
        global lvl1word830CHK
        lvl1word830CHK = 0
        global lvl1word831CHK
        lvl1word831CHK = 0
        global lvl1word832CHK
        lvl1word832CHK = 0
        global lvl1word833CHK
        lvl1word833CHK = 0
        global lvl1word834CHK
        lvl1word834CHK = 0
        global lvl1word835CHK
        lvl1word835CHK = 0
        global lvl1word836CHK
        lvl1word836CHK = 0
        global lvl1word837CHK
        lvl1word837CHK = 0
        global lvl1word838CHK
        lvl1word838CHK = 0
        global lvl1word839CHK
        lvl1word839CHK = 0
        global lvl1word840CHK
        lvl1word840CHK = 0
        global lvl1word841CHK
        lvl1word841CHK = 0
        global lvl1word842CHK
        lvl1word842CHK = 0
        global lvl1word843CHK
        lvl1word843CHK = 0
        global lvl1word844CHK
        lvl1word844CHK = 0
        global lvl1word845CHK
        lvl1word845CHK = 0
        global lvl1word846CHK
        lvl1word846CHK = 0
        global lvl1word847CHK
        lvl1word847CHK = 0
        global lvl1word848CHK
        lvl1word848CHK = 0
        global lvl1word849CHK
        lvl1word849CHK = 0
        global lvl1word850CHK
        lvl1word850CHK = 0
        global lvl1word851CHK
        lvl1word851CHK = 0
        global lvl1word852CHK
        lvl1word852CHK = 0
        global lvl1word853CHK
        lvl1word853CHK = 0
        global lvl1word854CHK
        lvl1word854CHK = 0
        global lvl1word855CHK
        lvl1word855CHK = 0
        global lvl1word856CHK
        lvl1word856CHK = 0
        global lvl1word857CHK
        lvl1word857CHK = 0
        global lvl1word858CHK
        lvl1word858CHK = 0
        global lvl1word859CHK
        lvl1word859CHK = 0
        global lvl1word860CHK
        lvl1word860CHK = 0
        global lvl1word861CHK
        lvl1word861CHK = 0
        global lvl1word862CHK
        lvl1word862CHK = 0
        global lvl1word863CHK
        lvl1word863CHK = 0
        global lvl1word864CHK
        lvl1word864CHK = 0
        global lvl1word865CHK
        lvl1word865CHK = 0
        global lvl1word866CHK
        lvl1word866CHK = 0
        global lvl1word867CHK
        lvl1word867CHK = 0
        global lvl1word868CHK
        lvl1word868CHK = 0
        global lvl1word869CHK
        lvl1word869CHK = 0
        global lvl1word870CHK
        lvl1word870CHK = 0
        global lvl1word871CHK
        lvl1word871CHK = 0
        global lvl1word872CHK
        lvl1word872CHK = 0
        global lvl1word873CHK
        lvl1word873CHK = 0
        global lvl1word874CHK
        lvl1word874CHK = 0
        global lvl1word875CHK
        lvl1word875CHK = 0
        global lvl1word876CHK
        lvl1word876CHK = 0
        global lvl1word877CHK
        lvl1word877CHK = 0
        global lvl1word878CHK
        lvl1word878CHK = 0
        global lvl1word879CHK
        lvl1word879CHK = 0
        global lvl1word880CHK
        lvl1word880CHK = 0
        global lvl1word881CHK
        lvl1word881CHK = 0
        global lvl1word882CHK
        lvl1word882CHK = 0
        global lvl1word883CHK
        lvl1word883CHK = 0
        global lvl1word884CHK
        lvl1word884CHK = 0
        global lvl1word885CHK
        lvl1word885CHK = 0
        global lvl1word886CHK
        lvl1word886CHK = 0
        global lvl1word887CHK
        lvl1word887CHK = 0
        global lvl1word888CHK
        lvl1word888CHK = 0
        global lvl1word889CHK
        lvl1word889CHK = 0
        global lvl1word890CHK
        lvl1word890CHK = 0
        global lvl1word891CHK
        lvl1word891CHK = 0
        global lvl1word892CHK
        lvl1word892CHK = 0
        global lvl1word893CHK
        lvl1word893CHK = 0
        global lvl1word894CHK
        lvl1word894CHK = 0
        global lvl1word895CHK
        lvl1word895CHK = 0
        global lvl1word896CHK
        lvl1word896CHK = 0
        global lvl1word897CHK
        lvl1word897CHK = 0
        global lvl1word898CHK
        lvl1word898CHK = 0
        global lvl1word899CHK
        lvl1word899CHK = 0
        global lvl1word900CHK
        lvl1word900CHK = 0
        global lvl1word901CHK
        lvl1word901CHK = 0
        global lvl1word902CHK
        lvl1word902CHK = 0
        global lvl1word903CHK
        lvl1word903CHK = 0
        global lvl1word904CHK
        lvl1word904CHK = 0
        global lvl1word905CHK
        lvl1word905CHK = 0
        global lvl1word906CHK
        lvl1word906CHK = 0
        global lvl1word907CHK
        lvl1word907CHK = 0
        global lvl1word908CHK
        lvl1word908CHK = 0
        global lvl1word909CHK
        lvl1word909CHK = 0
        global lvl1word910CHK
        lvl1word910CHK = 0
        global lvl1word911CHK
        lvl1word911CHK = 0
        global lvl1word912CHK
        lvl1word912CHK = 0
        global lvl1word913CHK
        lvl1word913CHK = 0
        global lvl1word914CHK
        lvl1word914CHK = 0
        global lvl1word915CHK
        lvl1word915CHK = 0
        global lvl1word916CHK
        lvl1word916CHK = 0
        global lvl1word917CHK
        lvl1word917CHK = 0
        global lvl1word918CHK
        lvl1word918CHK = 0
        global lvl1word919CHK
        lvl1word919CHK = 0
        global lvl1word920CHK
        lvl1word920CHK = 0
        global lvl1word921CHK
        lvl1word921CHK = 0
        global lvl1word922CHK
        lvl1word922CHK = 0
        global lvl1word923CHK
        lvl1word923CHK = 0
        global lvl1word924CHK
        lvl1word924CHK = 0
        global lvl1word925CHK
        lvl1word925CHK = 0
        global lvl1word926CHK
        lvl1word926CHK = 0
        global lvl1word927CHK
        lvl1word927CHK = 0
        global lvl1word928CHK
        lvl1word928CHK = 0
        global lvl1word929CHK
        lvl1word929CHK = 0
        global lvl1word930CHK
        lvl1word930CHK = 0
        global lvl1word931CHK
        lvl1word931CHK = 0
        global lvl1word932CHK
        lvl1word932CHK = 0
        global lvl1word933CHK
        lvl1word933CHK = 0
        global lvl1word934CHK
        lvl1word934CHK = 0
        global lvl1word935CHK
        lvl1word935CHK = 0
        global lvl1word936CHK
        lvl1word936CHK = 0
        global lvl1word937CHK
        lvl1word937CHK = 0
        global lvl1word938CHK
        lvl1word938CHK = 0
        global lvl1word939CHK
        lvl1word939CHK = 0
        global lvl1word940CHK
        lvl1word940CHK = 0
        global lvl1word941CHK
        lvl1word941CHK = 0
        global lvl1word942CHK
        lvl1word942CHK = 0
        global lvl1word943CHK
        lvl1word943CHK = 0
        global lvl1word944CHK
        lvl1word944CHK = 0
        global lvl1word945CHK
        lvl1word945CHK = 0
        global lvl1word946CHK
        lvl1word946CHK = 0
        global lvl1word947CHK
        lvl1word947CHK = 0
        global lvl1word948CHK
        lvl1word948CHK = 0
        global lvl1word949CHK
        lvl1word949CHK = 0
        global lvl1word950CHK
        lvl1word950CHK = 0
        global lvl1word951CHK
        lvl1word951CHK = 0
        global lvl1word952CHK
        lvl1word952CHK = 0
        global lvl1word953CHK
        lvl1word953CHK = 0
        global lvl1word954CHK
        lvl1word954CHK = 0
        global lvl1word955CHK
        lvl1word955CHK = 0
        global lvl1word956CHK
        lvl1word956CHK = 0
        global lvl1word957CHK
        lvl1word957CHK = 0
        global lvl1word958CHK
        lvl1word958CHK = 0
        global lvl1word959CHK
        lvl1word959CHK = 0
        global lvl1word960CHK
        lvl1word960CHK = 0
        global lvl1word961CHK
        lvl1word961CHK = 0
        global lvl1word962CHK
        lvl1word962CHK = 0
        global lvl1word963CHK
        lvl1word963CHK = 0
        global lvl1word964CHK
        lvl1word964CHK = 0
        global lvl1word965CHK
        lvl1word965CHK = 0
        global lvl1word966CHK
        lvl1word966CHK = 0
        global lvl1word967CHK
        lvl1word967CHK = 0
        global lvl1word968CHK
        lvl1word968CHK = 0
        global lvl1word969CHK
        lvl1word969CHK = 0
        global lvl1word970CHK
        lvl1word970CHK = 0
        global lvl1word971CHK
        lvl1word971CHK = 0
        global lvl1word972CHK
        lvl1word972CHK = 0
        global lvl1word973CHK
        lvl1word973CHK = 0
        global lvl1word974CHK
        lvl1word974CHK = 0
        global lvl1word975CHK
        lvl1word975CHK = 0
        global lvl1word976CHK
        lvl1word976CHK = 0
        global lvl1word977CHK
        lvl1word977CHK = 0
        global lvl1word978CHK
        lvl1word978CHK = 0
        global lvl1word979CHK
        lvl1word979CHK = 0
        global lvl1word980CHK
        lvl1word980CHK = 0
        global lvl1word981CHK
        lvl1word981CHK = 0
        global lvl1word982CHK
        lvl1word982CHK = 0
        global lvl1word983CHK
        lvl1word983CHK = 0
        global lvl1word984CHK
        lvl1word984CHK = 0
        global lvl1word985CHK
        lvl1word985CHK = 0
        global lvl1word986CHK
        lvl1word986CHK = 0
        global lvl1word987CHK
        lvl1word987CHK = 0
        global lvl1word988CHK
        lvl1word988CHK = 0
        global lvl1word989CHK
        lvl1word989CHK = 0
        global lvl1word990CHK
        lvl1word990CHK = 0
        global lvl1word991CHK
        lvl1word991CHK = 0
        global lvl1word992CHK
        lvl1word992CHK = 0
        global lvl1word993CHK
        lvl1word993CHK = 0
        global lvl1word994CHK
        lvl1word994CHK = 0
        global lvl1word995CHK
        lvl1word995CHK = 0
        global lvl1word996CHK
        lvl1word996CHK = 0
        global lvl1word997CHK
        lvl1word997CHK = 0
        global lvl1word998CHK
        lvl1word998CHK = 0
        global lvl1word999CHK
        lvl1word999CHK = 0
        global lvl1word1000CHK
        lvl1word1000CHK = 0
        global lvl1word1001CHK
        lvl1word1001CHK = 0
        global lvl1word1002CHK
        lvl1word1002CHK = 0
        global lvl1word1003CHK
        lvl1word1003CHK = 0
        global lvl1word1004CHK
        lvl1word1004CHK = 0
        global lvl1word1005CHK
        lvl1word1005CHK = 0
        global lvl1word1006CHK
        lvl1word1006CHK = 0
        global lvl1word1007CHK
        lvl1word1007CHK = 0
        global lvl1word1008CHK
        lvl1word1008CHK = 0
        global lvl1word1009CHK
        lvl1word1009CHK = 0
        global lvl1word1010CHK
        lvl1word1010CHK = 0
        global lvl1word1011CHK
        lvl1word1011CHK = 0
        global lvl1word1012CHK
        lvl1word1012CHK = 0
        global lvl1word1013CHK
        lvl1word1013CHK = 0
        global lvl1word1014CHK
        lvl1word1014CHK = 0
        global lvl1word1015CHK
        lvl1word1015CHK = 0
        global lvl1word1016CHK
        lvl1word1016CHK = 0
        global lvl1word1017CHK
        lvl1word1017CHK = 0
        global lvl1word1018CHK
        lvl1word1018CHK = 0
        global lvl1word1019CHK
        lvl1word1019CHK = 0
        global lvl1word1020CHK
        lvl1word1020CHK = 0
        global lvl1word1021CHK
        lvl1word1021CHK = 0
        global lvl1word1022CHK
        lvl1word1022CHK = 0
        global lvl1word1023CHK
        lvl1word1023CHK = 0
        global lvl1word1024CHK
        lvl1word1024CHK = 0
        global lvl1word1025CHK
        lvl1word1025CHK = 0
        global lvl1word1026CHK
        lvl1word1026CHK = 0
        global lvl1word1027CHK
        lvl1word1027CHK = 0
        global lvl1word1028CHK
        lvl1word1028CHK = 0
        global lvl1word1029CHK
        lvl1word1029CHK = 0
        global lvl1word1030CHK
        lvl1word1030CHK = 0
        global lvl1word1031CHK
        lvl1word1031CHK = 0
        global lvl1word1032CHK
        lvl1word1032CHK = 0
        global lvl1word1033CHK
        lvl1word1033CHK = 0
        global lvl1word1034CHK
        lvl1word1034CHK = 0
        global lvl1word1035CHK
        lvl1word1035CHK = 0
        global lvl1word1036CHK
        lvl1word1036CHK = 0
        global lvl1word1037CHK
        lvl1word1037CHK = 0
        global lvl1word1038CHK
        lvl1word1038CHK = 0
        global lvl1word1039CHK
        lvl1word1039CHK = 0
        global lvl1word1040CHK
        lvl1word1040CHK = 0
        global lvl1word1041CHK
        lvl1word1041CHK = 0
        global lvl1word1042CHK
        lvl1word1042CHK = 0
        global lvl1word1043CHK
        lvl1word1043CHK = 0
        global lvl1word1044CHK
        lvl1word1044CHK = 0
        global lvl1word1045CHK
        lvl1word1045CHK = 0
        global lvl1word1047CHK
        lvl1word1047CHK = 0
        global lvl1word1048CHK
        lvl1word1048CHK = 0
        global lvl1word1049CHK
        lvl1word1049CHK = 0
        global lvl1word1050CHK
        lvl1word1050CHK = 0
        global lvl1word1051CHK
        lvl1word1051CHK = 0
        global lvl1word1052CHK
        lvl1word1052CHK = 0
        global lvl1word1053CHK
        lvl1word1053CHK = 0
        global lvl1word1054CHK
        lvl1word1054CHK = 0
        global lvl1word1055CHK
        lvl1word1055CHK = 0
        global lvl1word1056CHK
        lvl1word1056CHK = 0
        global lvl1word1057CHK
        lvl1word1057CHK = 0
        global lvl1word1058CHK
        lvl1word1058CHK = 0
        global lvl1word1059CHK
        lvl1word1059CHK = 0
        global lvl1word1060CHK
        lvl1word1060CHK = 0
        global lvl1word1061CHK
        lvl1word1061CHK = 0
        global lvl1word1062CHK
        lvl1word1062CHK = 0
        global lvl1word1063CHK
        lvl1word1063CHK = 0
        global lvl1word1064CHK
        lvl1word1064CHK = 0
        global lvl1word1065CHK
        lvl1word1065CHK = 0
        global lvl1word1067CHK
        lvl1word1067CHK = 0
        global lvl1word1068CHK
        lvl1word1068CHK = 0
        global lvl1word1069CHK
        lvl1word1069CHK = 0
        global lvl1word1070CHK
        lvl1word1070CHK = 0
        global lvl1word1072CHK
        lvl1word1072CHK = 0
        global lvl1word1073CHK
        lvl1word1073CHK = 0
        global lvl1word1074CHK
        lvl1word1074CHK = 0
        global lvl1word1075CHK
        lvl1word1075CHK = 0
        global lvl1word1076CHK
        lvl1word1076CHK = 0
        global lvl1word1077CHK
        lvl1word1077CHK = 0
        global lvl1word1078CHK
        lvl1word1078CHK = 0
        global lvl1word1079CHK
        lvl1word1079CHK = 0
        global lvl1word1080CHK
        lvl1word1080CHK = 0
        global lvl1word1081CHK
        lvl1word1081CHK = 0
        global lvl1word1082CHK
        lvl1word1082CHK = 0
        global lvl1word1083CHK
        lvl1word1083CHK = 0
        global lvl1word1084CHK
        lvl1word1084CHK = 0
        global lvl1word1085CHK
        lvl1word1085CHK = 0
        global lvl1word1086CHK
        lvl1word1086CHK = 0
        global lvl1word1087CHK
        lvl1word1087CHK = 0
        global lvl1word1088CHK
        lvl1word1088CHK = 0
        global lvl1word1089CHK
        lvl1word1089CHK = 0
        global lvl1word1090CHK
        lvl1word1090CHK = 0
        global lvl1word1091CHK
        lvl1word1091CHK = 0
        global lvl1word1092CHK
        lvl1word1092CHK = 0
        global lvl1word1093CHK
        lvl1word1093CHK = 0
        global lvl1word1094CHK
        lvl1word1094CHK = 0
        global lvl1word1095CHK
        lvl1word1095CHK = 0
        global lvl1word1096CHK
        lvl1word1096CHK = 0
        global lvl1word1097CHK
        lvl1word1097CHK = 0
        global lvl1word1098CHK
        lvl1word1098CHK = 0
        global lvl1word1099CHK
        lvl1word1099CHK = 0
        global lvl1word1100CHK
        lvl1word1100CHK = 0
        global lvl1word1101CHK
        lvl1word1101CHK = 0
        global lvl1word1103CHK
        lvl1word1103CHK = 0
        global lvl1word1104CHK
        lvl1word1104CHK = 0
        global lvl1word1105CHK
        lvl1word1105CHK = 0
        global lvl1word1106CHK
        lvl1word1106CHK = 0
        global lvl1word1108CHK
        lvl1word1108CHK = 0
        global lvl1word1109CHK
        lvl1word1109CHK = 0
        global lvl1word1110CHK
        lvl1word1110CHK = 0
        global lvl1word1111CHK
        lvl1word1111CHK = 0
        global lvl1word1112CHK
        lvl1word1112CHK = 0
        global lvl1word1113CHK
        lvl1word1113CHK = 0
        global lvl1word1116CHK
        lvl1word1116CHK = 0
        global lvl1word1117CHK
        lvl1word1117CHK = 0
        global lvl1word1118CHK
        lvl1word1118CHK = 0
        global lvl1word1119CHK
        lvl1word1119CHK = 0
        global lvl1word1120CHK
        lvl1word1120CHK = 0
        global lvl1word1121CHK
        lvl1word1121CHK = 0
        global lvl1word1122CHK
        lvl1word1122CHK = 0
        global lvl1word1123CHK
        lvl1word1123CHK = 0
        global lvl1word1124CHK
        lvl1word1124CHK = 0
        global lvl1word1125CHK
        lvl1word1125CHK = 0
        global lvl1word1126CHK
        lvl1word1126CHK = 0
        global lvl1word1127CHK
        lvl1word1127CHK = 0
        global lvl1word1128CHK
        lvl1word1128CHK = 0
        global lvl1word1129CHK
        lvl1word1129CHK = 0
        global lvl1word1130CHK
        lvl1word1130CHK = 0
        global lvl1word1131CHK
        lvl1word1131CHK = 0
        global lvl1word1132CHK
        lvl1word1132CHK = 0
        global lvl1word1133CHK
        lvl1word1133CHK = 0
        global lvl1word1134CHK
        lvl1word1134CHK = 0
        global lvl1word1135CHK
        lvl1word1135CHK = 0
        global lvl1word1136CHK
        lvl1word1136CHK = 0
        global lvl1word1137CHK
        lvl1word1137CHK = 0
        global lvl1word1138CHK
        lvl1word1138CHK = 0
        global lvl1word1139CHK
        lvl1word1139CHK = 0
        global lvl1word1140CHK
        lvl1word1140CHK = 0
        global lvl1word1141CHK
        lvl1word1141CHK = 0
        global lvl1word1142CHK
        lvl1word1142CHK = 0
        global lvl1word1143CHK
        lvl1word1143CHK = 0
        global lvl1word1144CHK
        lvl1word1144CHK = 0
        global lvl1word1145CHK
        lvl1word1145CHK = 0
        global lvl1word1146CHK
        lvl1word1146CHK = 0
        global lvl1word1147CHK
        lvl1word1147CHK = 0
        global lvl1word1148CHK
        lvl1word1148CHK = 0
        global lvl1word1149CHK
        lvl1word1149CHK = 0
        global lvl1word1150CHK
        lvl1word1150CHK = 0
        global lvl1word1151CHK
        lvl1word1151CHK = 0
        global lvl1word1153CHK
        lvl1word1153CHK = 0
        global lvl1word1154CHK
        lvl1word1154CHK = 0
        global lvl1word1155CHK
        lvl1word1155CHK = 0
        global lvl1word1156CHK
        lvl1word1156CHK = 0
        global lvl1word1157CHK
        lvl1word1157CHK = 0
        global lvl1word1158CHK
        lvl1word1158CHK = 0
        global lvl1word1159CHK
        lvl1word1159CHK = 0
        global lvl1word1160CHK
        lvl1word1160CHK = 0
        global lvl1word1161CHK
        lvl1word1161CHK = 0
        global lvl1word1162CHK
        lvl1word1162CHK = 0
        global lvl1word1163CHK
        lvl1word1163CHK = 0
        global lvl1word1164CHK
        lvl1word1164CHK = 0
        global lvl1word1165CHK
        lvl1word1165CHK = 0
        global lvl1word1166CHK
        lvl1word1166CHK = 0
        global lvl1word1167CHK
        lvl1word1167CHK = 0
        global lvl1word1168CHK
        lvl1word1168CHK = 0
        global lvl1word1169CHK
        lvl1word1169CHK = 0
        global lvl1word1170CHK
        lvl1word1170CHK = 0
        global lvl1word1171CHK
        lvl1word1171CHK = 0
        global lvl1word1172CHK
        lvl1word1172CHK = 0
        global lvl1word1173CHK
        lvl1word1173CHK = 0
        global lvl1word1175CHK
        lvl1word1175CHK = 0
        global lvl1word1176CHK
        lvl1word1176CHK = 0
        global lvl1word1177CHK
        lvl1word1177CHK = 0
        global lvl1word1178CHK
        lvl1word1178CHK = 0
        global lvl1word1179CHK
        lvl1word1179CHK = 0
        global lvl1word1180CHK
        lvl1word1180CHK = 0
        global lvl1word1181CHK
        lvl1word1181CHK = 0
        global lvl1word1182CHK
        lvl1word1182CHK = 0
        global lvl1word1183CHK
        lvl1word1183CHK = 0
        global lvl1word1184CHK
        lvl1word1184CHK = 0
        global lvl1word1185CHK
        lvl1word1185CHK = 0
        global lvl1word1186CHK
        lvl1word1186CHK = 0
        global lvl1word1187CHK
        lvl1word1187CHK = 0
        global lvl1word1188CHK
        lvl1word1188CHK = 0
        global lvl1word1189CHK
        lvl1word1189CHK = 0
        global lvl1word1190CHK
        lvl1word1190CHK = 0
        global lvl1word1191CHK
        lvl1word1191CHK = 0
        global lvl1word1192CHK
        lvl1word1192CHK = 0
        global lvl1word1193CHK
        lvl1word1193CHK = 0
        global lvl1word1194CHK
        lvl1word1194CHK = 0
        global lvl1word1195CHK
        lvl1word1195CHK = 0
        global lvl1word1196CHK
        lvl1word1196CHK = 0
        global lvl1word1197CHK
        lvl1word1197CHK = 0
        global lvl1word1198CHK
        lvl1word1198CHK = 0
        global lvl1word1199CHK
        lvl1word1199CHK = 0
        global lvl1word1200CHK
        lvl1word1200CHK = 0
        global lvl1word1201CHK
        lvl1word1201CHK = 0
        global lvl1word1202CHK
        lvl1word1202CHK = 0
        global lvl1word1203CHK
        lvl1word1203CHK = 0
        global lvl1word1204CHK
        lvl1word1204CHK = 0
        global lvl1word1205CHK
        lvl1word1205CHK = 0
        global lvl1word1206CHK
        lvl1word1206CHK = 0
        global lvl1word1207CHK
        lvl1word1207CHK = 0
        global lvl1word1208CHK
        lvl1word1208CHK = 0
        global lvl1word1209CHK
        lvl1word1209CHK = 0
        global lvl1word1210CHK
        lvl1word1210CHK = 0
        global lvl1word1211CHK
        lvl1word1211CHK = 0
        global lvl1word1212CHK
        lvl1word1212CHK = 0
        global lvl1word1213CHK
        lvl1word1213CHK = 0
        global lvl1word1214CHK
        lvl1word1214CHK = 0
        global lvl1word1215CHK
        lvl1word1215CHK = 0
        global lvl1word1216CHK
        lvl1word1216CHK = 0
        global lvl1word1217CHK
        lvl1word1217CHK = 0
        global lvl1word1218CHK
        lvl1word1218CHK = 0
        global lvl1word1219CHK
        lvl1word1219CHK = 0
        global lvl1word1220CHK
        lvl1word1220CHK = 0
        global lvl1word1221CHK
        lvl1word1221CHK = 0
        global lvl1word1222CHK
        lvl1word1222CHK = 0
        global lvl1word1223CHK
        lvl1word1223CHK = 0
        global lvl1word1224CHK
        lvl1word1224CHK = 0
        global lvl1word1225CHK
        lvl1word1225CHK = 0
        global lvl1word1226CHK
        lvl1word1226CHK = 0
        global lvl1word1227CHK
        lvl1word1227CHK = 0
        global lvl1word1228CHK
        lvl1word1228CHK = 0
        global lvl1word1229CHK
        lvl1word1229CHK = 0
        global lvl1word1230CHK
        lvl1word1230CHK = 0
        global lvl1word1231CHK
        lvl1word1231CHK = 0
        global lvl1word1232CHK
        lvl1word1232CHK = 0
        global lvl1word1233CHK
        lvl1word1233CHK = 0
        global lvl1word1234CHK
        lvl1word1234CHK = 0
        global lvl1word1235CHK
        lvl1word1235CHK = 0
        global lvl1word1236CHK
        lvl1word1236CHK = 0
        global lvl1word1237CHK
        lvl1word1237CHK = 0
        global lvl1word1238CHK
        lvl1word1238CHK = 0
        global lvl1word1239CHK
        lvl1word1239CHK = 0
        global lvl1word1240CHK
        lvl1word1240CHK = 0
        global lvl1word1241CHK
        lvl1word1241CHK = 0
        global lvl1word1242CHK
        lvl1word1242CHK = 0
        global lvl1word1243CHK
        lvl1word1243CHK = 0
        global lvl1word1244CHK
        lvl1word1244CHK = 0
        global lvl1word1245CHK
        lvl1word1245CHK = 0
        global lvl1word1246CHK
        lvl1word1246CHK = 0
        global lvl1word1247CHK
        lvl1word1247CHK = 0
        global lvl1word1248CHK
        lvl1word1248CHK = 0
        global lvl1word1249CHK
        lvl1word1249CHK = 0
        global lvl1word1250CHK
        lvl1word1250CHK = 0
        global lvl1word1251CHK
        lvl1word1251CHK = 0
        global lvl1word1253CHK
        lvl1word1253CHK = 0
        global lvl1word1254CHK
        lvl1word1254CHK = 0
        global lvl1word1255CHK
        lvl1word1255CHK = 0
        global lvl1word1256CHK
        lvl1word1256CHK = 0
        global lvl1word1257CHK
        lvl1word1257CHK = 0
        global lvl1word1258CHK
        lvl1word1258CHK = 0
        global lvl1word1259CHK
        lvl1word1259CHK = 0
        global lvl1word1260CHK
        lvl1word1260CHK = 0
        global lvl1word1261CHK
        lvl1word1261CHK = 0
        global lvl1word1262CHK
        lvl1word1262CHK = 0
        global lvl1word1263CHK
        lvl1word1263CHK = 0
        global lvl1word1264CHK
        lvl1word1264CHK = 0











        # LEVEL 1 LETTERS A, C, E, H, T
        # LEVEL 2 LETTERS A, C, D, E, T
        # LEVEL 3 LETTERS C, D, E, O, T
        # LEVEL 4 LETTERS D, E, M, O, T
        # LEVEL 5 LETTERS D, E, F, M, O, Y
        # LEVEL 6 LETTERS B, F, I, M, O, Y
        # LEVEL 7 LETTERS A, B, F, I, M, Y
        # LEVEL 8 LETTERS A, B, E, F, L, Y
        # LEVEL 9 LETTERS A, E, G, P, I, U, S
        # LEVEL 10 LETTERS E, G, I, O, R, S, U, V

        def letterMod():
            global labelb1
            global labelb2
            global labelb3
            global labelb4
            global labelb5
            global labelb6
            global labelb7

           # foundCount=5
            letterRoll = random.random()
           # letterRoll = .26
            if letterRoll > 0 and letterRoll <= .03 :
                if foundCount < 5 :
                    global letterList
                    letterList = ["", "&", "+", "*", "", "", ""]

                elif foundCount >= 5 and foundCount < 10 :
                    letterList = ["", "&", "+", "*", "", "", ""]

                elif foundCount >= 10 and foundCount < 15 :
                    letterList = ["", "&", "+", "*", "", "", ""]

                elif foundCount >= 15 and foundCount < 20 :
                    letterList = ["", "&", "+", "*", "", "", ""]

                elif foundCount >= 20 and foundCount < 25 :
                    letterList = ["Y", "&", "+", "*", "", "", ""]

                elif foundCount >= 25 and foundCount < 30 :
                    letterList = ["B", "Y", "+", "*", "", "", ""]

                elif foundCount >= 30 and foundCount < 35 :
                    letterList = ["B", "Y", "+", "*", "", "", ""]

                elif foundCount >= 35 and foundCount < 40 :
                    letterList = ["B", "Y", "+", "*", "", "", ""]

                elif foundCount >= 40 and foundCount < 45 :
                    letterList = ["P", "+", "*", "", "", "", ""]

                elif foundCount >= 45 :
                    letterList = ["V", "+", "*", "", "", "", ""]
                    
            elif letterRoll > .03 and letterRoll <= .1 :
                if foundCount < 5 :
                    letterList = ["C", "", "", "", "", "", ""]

                elif foundCount >= 5 and foundCount < 10 :
                    letterList = ["C", "", "", "", "", "", ""]

                elif foundCount >= 10 and foundCount < 15 :
                    letterList = ["C", "", "", "", "", "", ""]

                elif foundCount >= 15 and foundCount < 20 :
                    letterList = ["M", "", "", "", "", "", ""]

                elif foundCount >= 20 and foundCount < 25 :
                    letterList = ["F", "M", "", "", "", "", ""]
         
                elif foundCount >= 25 and foundCount < 30 :
                    letterList = ["F", "M", "", "", "", "", ""]

                elif foundCount >= 30 and foundCount < 35 :
                    letterList = ["F", "M", "", "", "", "", ""]

                elif foundCount >= 35 and foundCount < 40 :
                    letterList = ["F", "", "", "", "", "", ""]

                elif foundCount >= 40 and foundCount < 45 :
                    letterList = ["G", "U", "", "", "", "", ""]

                elif foundCount >= 45 :
                    letterList = ["G", "U", "", "", "", "", ""]

                    
            elif letterRoll > .10 and letterRoll <= .25 :
                if foundCount < 5 and speedOn == False :
                    letterList = ["H", "8", "", "", "", "", ""]

                elif foundCount < 5 and speedOn == True :
                    letterList = ["H", "8", "", "", "", "", ""]

                elif foundCount >= 5 and foundCount < 10 :
                    letterList = ["D", "8", "", "", "", "", ""]

                elif foundCount >= 10 and foundCount < 15 :
                    letterList = ["D", "8", "", "", "", "", ""]

                elif foundCount >= 15 and foundCount < 20 :
                    letterList = ["D", "8", "", "", "", "", ""]

                elif foundCount >= 20 and foundCount < 25 :
                    letterList = ["D", "8", "", "", "", "", ""]

                elif foundCount >= 25 and foundCount < 30 :
                    letterList = ["I", "8", "", "", "", "", ""]

                elif foundCount >= 30 and foundCount < 35 :
                    letterList = ["I", "8", "", "", "", "", ""]

                elif foundCount >= 35 and foundCount < 40 :
                    letterList = ["L", "8", "", "", "", "", ""]

                elif foundCount >= 40 and foundCount < 45 :
                    letterList = ["I", "S", "8", "", "", "", ""]

                elif foundCount >= 45 :
                    letterList = ["I", "R", "S", "8", "", "", ""]

            elif letterRoll > .25 and letterRoll <= .5  :
                if foundCount < 5 :
                    letterList = ["A", "E", "T", "", "", "", ""]

                elif foundCount >= 5 and foundCount < 10 :
                    letterList = ["A", "E", "T", "", "", "", ""]

                elif foundCount >= 10 and foundCount < 15 :
                    letterList = ["E", "O", "T", "", "", "", ""]

                elif foundCount >= 15 and foundCount < 20 :
                    letterList = ["E", "O", "T", "", "", "", ""]

                elif foundCount >= 20 and foundCount < 25 :
                    letterList = ["E", "O", "", "", "", "", ""]

                elif foundCount >= 25 and foundCount < 30 :
                    letterList = ["O", "", "", "", "", "", ""]

                elif foundCount >= 30 and foundCount < 35 :
                    letterList = ["A", "", "", "", "", "", ""]

                elif foundCount >= 35 and foundCount < 40 :
                    letterList = ["A", "E", "", "", "", "", ""]

                elif foundCount >= 40 and foundCount < 45 :
                    letterList = ["A", "E", "", "", "", "", ""]

                elif foundCount >= 45 :
                    letterList = ["E", "O", "", "", "", "", ""]

            elif letterRoll > .5 and letterRoll <= 1 :
                    letterList = ["", "", "", "", "", "", ""]
                    

            labelb1 = Label(text = '[color=ff3333]' + letterList[0] + '[/color]', markup = True, pos_hint={'center_x':.3, 'center_y':.3})
            Fl.add_widget(labelb1)
            labelb2 = Label(text = '[color=ff3333]' + letterList[1] + '[/color]', markup = True, pos_hint={'center_x':.32, 'center_y':.3}) 
            Fl.add_widget(labelb2)
            labelb3 = Label(text = '[color=ff3333]' + letterList[2] + '[/color]', markup = True,  pos_hint={'center_x':.34, 'center_y':.3})                        
            Fl.add_widget(labelb3)
            labelb4 = Label(text = '[color=ff3333]' + letterList[3] + '[/color]', markup = True, pos_hint={'center_x':.36, 'center_y':.3})
            Fl.add_widget(labelb4)
            labelb5 = Label(text = '[color=ff3333]' + letterList[4] + '[/color]', markup = True, pos_hint={'center_x':.3, 'center_y':.3})
            Fl.add_widget(labelb5)
            labelb6 = Label(text = '[color=ff3333]' + letterList[5] + '[/color]', markup = True, pos_hint={'center_x':.32, 'center_y':.3}) 
            Fl.add_widget(labelb6)
            labelb7 = Label(text = '[color=ff3333]' + letterList[6] + '[/color]', markup = True,  pos_hint={'center_x':.34, 'center_y':.3})                        
            Fl.add_widget(labelb7)
                               
  

                

       # letterMod()     


        def letterModAll():
            global labelb1
            global labelb2
            global labelb3
            global labelb4
            global labelb5
            global labelb6
            global labelb7
            
            letterRoll = random.random()
            if letterRoll > 0 and letterRoll <= .02 :
                global letterList
                letterList = ["Q", "X", "Z", "", "", "", ""]

            elif letterRoll > .02 and letterRoll <= .1 :
                letterList = ["B", "J", "K", "P", "V", "Y", ""]
  
            elif letterRoll > .10 and letterRoll <= .25 :
                letterList = ["C", "F", "G", "M", "U", "W", ""]
   
            elif letterRoll > .25 and letterRoll <= .5  :
                letterList = ["D", "H", " I", "L", "N", "R", "S"]

            elif letterRoll > .5 and letterRoll <= 1 :
                letterList = ["A", "E", "O", "T", "", "", ""]


            labelb1 = Label(text = '[color=ff3333]' + letterList[0] + '[/color]', markup = True, pos_hint={'center_x':.3, 'center_y':.3})
            Fl.add_widget(labelb1)
            labelb2 = Label(text = '[color=ff3333]' + letterList[1] + '[/color]', markup = True, pos_hint={'center_x':.32, 'center_y':.3}) 
            Fl.add_widget(labelb2)
            labelb3 = Label(text = '[color=ff3333]' + letterList[2] + '[/color]', markup = True,  pos_hint={'center_x':.34, 'center_y':.3})                        
            Fl.add_widget(labelb3)
            labelb4 = Label(text = '[color=ff3333]' + letterList[3] + '[/color]', markup = True, pos_hint={'center_x':.36, 'center_y':.3})
            Fl.add_widget(labelb4)
            labelb5 = Label(text = '[color=ff3333]' + letterList[4] + '[/color]', markup = True, pos_hint={'center_x':.3, 'center_y':.3})
            Fl.add_widget(labelb5)
            labelb6 = Label(text = '[color=ff3333]' + letterList[5] + '[/color]', markup = True, pos_hint={'center_x':.32, 'center_y':.3}) 
            Fl.add_widget(labelb6)
            labelb7 = Label(text = '[color=ff3333]' + letterList[6] + '[/color]', markup = True,  pos_hint={'center_x':.34, 'center_y':.3})                        
            Fl.add_widget(labelb7)

        global gameSpeed
        gameSpeed = 1000
        global delay
        delay = 0
        global counter
        counter = 0
        global counter2
        counter2 = 0

        #main loop
        gameOver = False

        global enemyColor
        enemyColor = 0
        global enemyColor2
        enemyColor2 = 0
        global enemyColor3
        enemyColor3 = 0
        global enemyColor4
        enemyColor4 = 0
        global enemyColor5
        enemyColor5 = 0
        global enemyColor6
        enemyColor6 = 0
        global enemyColor7
        enemyColor7 = 0
        global enemyColor8
        enemyColor8 = 0
        global enemyColorb
        enemyColorb = 0
        global enemyColor2b
        enemyColor2b = 0
        global enemyColor3b
        enemyColor3b = 0
        global enemyColor4b
        enemyColor4b = 0
        global enemyColor5b
        enemyColor5b = 0
        global enemyColor6b
        enemyColor6b = 0
        global enemyColor7b
        enemyColor7b = 0
        global enemyColor8b
        enemyColor8b = 0

        global scoreMult
        scoreMult = 1

       # clock = pygame.time.Clock()




        while listCount < 1:

          
            delay = random.random()
            global enemyLabel
            enemyLabel = Label(text='', markup = True)
            global enemyLabel2
            enemyLabel2 = Label(text='', markup = True)
            global enemyLabel3
            enemyLabel3 = Label(text='', markup = True)
            global enemyLabel4
            enemyLabel4 = Label(text='', markup = True)
            global enemyLabel5
            enemyLabel5 = Label(text='', markup = True)
            global enemyLabel6
            enemyLabel6 = Label(text='', markup = True)
            global enemyLabel7
            enemyLabel7 = Label(text='', markup = True)
            global enemyLabel8
            enemyLabel8 = Label(text='', markup = True)
            global enemyLabelb
            enemyLabelb = Label(text='', markup = True)
            global enemyLabel2b
            enemyLabel2b = Label(text='', markup = True)
            global enemyLabel3b
            enemyLabel3b = Label(text='', markup = True)
            global enemyLabel4b
            enemyLabel4b = Label(text='', markup = True)
            global enemyLabel5b
            enemyLabel5b = Label(text='', markup = True)
            global enemyLabel6b
            enemyLabel6b = Label(text='', markup = True)
            global enemyLabel7b
            enemyLabel7b = Label(text='', markup = True)
            global enemyLabel8b
            enemyLabel8b = Label(text='', markup = True)
            listCount = 1    
            break


        global newLabel
        newLabel = Label(text='', markup = True)
        global newLabel2
        newLabel2 = Label(text='', markup = True)
        global newLabel3
        newLabel3 = Label(text='', markup = True)
        global newLabel4
        newLabel4 = Label(text='', markup = True)
        global newLabel5
        newLabel5 = Label(text='', markup = True)
        global newLabel6
        newLabel6 = Label(text='', markup = True)
        global newLabel7
        newLabel7 = Label(text='', markup = True)
        global newLabel8
        newLabel8 = Label(text='', markup = True)
        global newLabel9
        newLabel9 = Label(text='', markup = True)
        global newLabel10
        newLabel10 = Label(text='', markup = True)
        global newLabel11
        newLabel11 = Label(text='', markup = True)
        global newLabel12
        newLabel12 = Label(text='', markup = True)

        global playerNum
        playerNum = 0
        global playerNum2
        playerNum2 = 0
        global playerNum3
        playerNum3 = 0
        global playerNum4
        playerNum4 = 0
        global playerNum5
        playerNum5 = 0
        global playerNum6
        playerNum6 = 0
        global playerNum7
        playerNum7 = 0
        global playerNum8
        playerNum8 = 0
        global playerNumb
        playerNumb = 0
        global playerNum2b
        playerNum2b = 0
        global playerNum3b
        playerNum3b = 0
        global playerNum4b
        playerNum4b = 0
        global playerNum5b
        playerNum5b = 0
        global playerNum6b
        playerNum6b = 0
        global playerNum7b
        playerNum7b = 0
        global playerNum8b
        playerNum8b = 0



            
        def drop_enemies(enemyList, enemyList2, enemyList3, enemyList4, enemyList5, enemyList6, enemyList7, enemyList8, enemyListb, gameStop) :

            delay = random.random()
            global counter
            global counter2
            global coin1
            global coin2
            global coin3
            global coin4
            global coin5
            global coin6
            global coin7
            global coin8
            global boost1
            global boost2
            global boost3
            global boost4
            global boost5
            global boost6
            global boost7
            global boost8
            global strikes1
            global strikes2
            global strikes3
            global strikes4
            global strikes5
            global strikes6
            global strikes7
            global strikes8
            global shield1
            global shield2
            global shield3
            global shield4
            global shield5
            global shield6
            global shield7
            global shield8

        #    while gameStop == False:
                
            if counter < 5 :
                    global hitOn
                    hitOn = False

                    if delay > .95 and len(enemyList) < 1 and gameStop == False :
                        x_pos = random.randint(delay1a, delay1b)
                        y_pos = 0
                        enemyList.append([x_pos, y_pos])
                        counter += 1

                    if delay > .85 and delay < .9 and len(enemyList2) <1 and gameStop == False :
                        x_pos2 = random.randint(delay2a, delay2b)
                        y_pos2 = 0
                        enemyList2.append([x_pos2, y_pos2])
                    if delay > .75 and delay < .8 and len(enemyList3) <1 and gameStop == False :
                        x_pos3 = random.randint(delay3a, delay3b)
                        y_pos3 = 0
                        enemyList3.append([x_pos3, y_pos3])
                    if delay > .65 and delay < .7 and len(enemyList4) <1 and gameStop == False :
                        x_pos4 = random.randint(delay4a, delay4b)
                        y_pos4 = 0
                        enemyList4.append([x_pos4, y_pos4])
                    if delay > .55 and delay < .6 and len(enemyList5) <1 and gameStop == False :
                        x_pos5 = random.randint(delay5a, delay5b)
                        y_pos5 = 0
                        enemyList5.append([x_pos5, y_pos5])
                    if delay > .45 and delay < .5 and len(enemyList6) <1 and gameStop == False :
                        x_pos6 = random.randint(delay6a, delay6b)
                        y_pos6 = 0
                        enemyList6.append([x_pos6, y_pos6])
                    if delay > .35 and delay < .4 and len(enemyList7) <1 and gameStop == False :
                        x_pos7 = random.randint(delay7a, delay7b)
                        y_pos7 = 0
                        enemyList7.append([x_pos7, y_pos7])
                    if delay > .25 and delay < .3 and len(enemyList8) <1 and gameStop == False :
                        x_pos8 = random.randint(delay8a, delay8b)
                        y_pos8 = 0
                        enemyList8.append([x_pos8, y_pos8])
            else: 

                    global gameSpeed
                    if foundCount < 10 :
                        gameSpeed = 4
                    elif foundCount >= 10 and foundCount < 20 :
                        gameSpeed = 5
                    elif foundCount >= 20 and foundCount < 30 :
                        gameSpeed = 6
                    elif foundCount >= 30 and foundCount < 40 :
                        gameSpeed = 8
                    elif foundCount >= 40 and foundCount < 45 :
                        gameSpeed = 10
                    elif foundCount >= 45 :
                        gameSpeed = 13

            if counter2 >= 8:
                    for idx, enemyPosb in enumerate(enemyListb) :
                        
                        if delay > .98 and len(enemyList) < 1 and enemyPosb[1] > heightDelay and gameStop == False :
                            letterMod()
                            letter = random.choice(letterList)
                            global enemyColor
                            enemyColor = random.choice(colorList)
                            global enemyText
                            shield1 = False
                            strikes1 = False
                            coin1 = False
                            boost1 = False
                            if letter == "8" :
                                enemyText = ""
                                coin1 = True
                            elif letter == "&":
                                enemyText = ""
                                boost1 = True
                            elif letter == "*":
                                enemyText = ""
                                strikes1 = True
                            elif letter == "+":
                                enemyText = ""
                                shield1 = True
                            else :    
                                enemyText = format(letter)
                            global dropDebug
                            dropDebug = False
                            global enemyLabel
                            enemyLabel = Label(text = '[color=ff3333]' + enemyText, pos_hint={'center_x':enemyPos[0], 'center_y':enemyPos[1]}, markup = True)       
                            x_pos = random.randint(delay1a, delay1b)
                            y_pos = 0
                            enemyList.append([x_pos, y_pos])
                            counter += 1
                            
                    for idx2, enemy2Posb in enumerate(enemyList2b) :

                        if delay > .88 and delay < .9 and len(enemyList2) <1 and enemy2Posb[1] > heightDelay and gameStop == False:
                            letterMod()
                            letter2 = random.choice(letterList)
                            global enemyColor2
                            enemyColor2 = random.choice(colorList)
                            global enemyText2
                            coin2 = False
                            boost2 = False
                            strikes2 = False
                            shield2 = False
                            if letter2 == "8" :
                                enemyText2 = ""
                                coin2 = True
                            elif letter2 == "&":
                                enemyText2 = ""
                                boost2 = True
                            elif letter2 == "*":
                                enemyText2 = ""
                                strikes2 = True
                            elif letter2 == "+":
                                enemyText2 = ""
                                shield2 = True
                            else :    
                                enemyText2 = format(letter2)
                            global dropDebug2
                            dropDebug2 = False
                            global enemyLabel2
                            enemyLabel2 = Label(text = '[color=ffffff]' + enemyText2, pos_hint={'center_x':enemyPos[0], 'center_y':enemyPos[1]}, markup = True)    
                            x_pos2 = random.randint(delay2a, delay2b)
                            y_pos2 = 0
                            enemyList2.append([x_pos2, y_pos2])

                    for idx3, enemy3Posb in enumerate(enemyList3b) :
                  
                        if delay > .78 and delay < .8 and len(enemyList3) <1 and enemy3Posb[1] > heightDelay and gameStop == False :
                            letterMod()
                            letter3 = random.choice(letterList)
                            global enemyColor3
                            enemyColor3 = random.choice(colorList)
                            global enemyText3
                            coin3 = False
                            boost3 = False
                            strikes3 = False
                            shield3 = False
                            if letter3 == "8" :
                                enemyText3 = ""
                                coin3 = True
                            elif letter3 == "&":
                                enemyText3 = ""
                                boost3 = True
                            elif letter3 == "*":
                                enemyText3 = ""
                                strikes3 = True
                            elif letter3 == "+":
                                enemyText3 = ""
                                shield3 = True
                            else :    
                                enemyText3 = format(letter3)
                            global dropDebug3
                            dropDebug3 = False
                            global enemyLabel3                    
                            enemyLabel3 = Label(text = '[color=ffffff]' + enemyText3, pos_hint={'center_x':enemyPos[0], 'center_y':enemyPos[1]}, markup = True)  
                            x_pos3 = random.randint(delay3a, delay3b)
                            y_pos3 = 0
                            enemyList3.append([x_pos3, y_pos3])

                    for idx4, enemy4Posb in enumerate(enemyList4b) :

                        if delay > .69 and delay < .7 and len(enemyList4) <1 and enemy4Posb[1] > heightDelay and gameStop == False :
                            letterMod()
                            letter4 = random.choice(letterList)
                            global enemyColor4
                            enemyColor4 = random.choice(colorList)
                            global enemyText4
                            coin4 = False
                            boost4 = False
                            strikes4 = False
                            shield4 = False
                            if letter4 == "8" :
                                enemyText4 = ""
                                coin4 = True
                            elif letter4 == "&":
                                enemyText4 = ""
                                boost4 = True
                            elif letter4 == "*":
                                enemyText4 = ""
                                strikes4 = True
                            elif letter4 == "+":
                                enemyText4 = ""
                                shield4 = True
                            else :    
                                enemyText4 = format(letter4)
                            global dropDebug4
                            dropDebug4 = False
                            global enemyLabel4
                            enemyLabel4 = Label(text = '[color=ffffff]' + enemyText4, pos_hint={'center_x':enemyPos[0], 'center_y':enemyPos[1]}, markup = True)   
                            x_pos4 = random.randint(delay4a, delay4b)
                            y_pos4 = 0
                            enemyList4.append([x_pos4, y_pos4])

                    for idx5, enemy5Posb in enumerate(enemyList5b) :

                        if delay > .59 and delay < .6 and len(enemyList5) <1 and enemy5Posb[1] > heightDelay and gameStop == False :
                            letterMod()
                            letter5 = random.choice(letterList)
                            global enemyColor5
                            enemyColor5 = random.choice(colorList)
                            global enemyText5
                            coin5 = False
                            boost5 = False
                            strikes5 = False
                            shield5 = False
                            if letter5 == "8" :
                                enemyText5 = ""
                                coin5 = True
                            elif letter5 == "&":
                                enemyText5 = ""
                                boost5 = True
                            elif letter5 == "*":
                                enemyText5 = ""
                                strikes5 = True
                            elif letter5 == "+":
                                enemyText5 = ""
                                shield5 = True
                            else :    
                                enemyText5 = format(letter5)
                            global dropDebug5
                            dropDebug5 = False
                            global enemyLabel5
                            enemyLabel5 = Label(text = '[color=ffffff]' + enemyText5, pos_hint={'center_x':enemyPos[0], 'center_y':enemyPos[1]}, markup = True)  
                            x_pos5 = random.randint(delay5a, delay5b)
                            y_pos5 = 0
                            enemyList5.append([x_pos5, y_pos5])

                    for idx6, enemy6Posb in enumerate(enemyList6b) :

                        if delay > .49 and delay < .5 and len(enemyList6) <1 and enemy6Posb[1] > heightDelay and gameStop == False :
                            letterMod()
                            letter6 = random.choice(letterList)
                            global enemyColor6
                            enemyColor6 = random.choice(colorList)
                            global enemyText6
                            coin6 = False
                            boost6 = False
                            strikes6 = False
                            shield6 = False
                            if letter6 == "8" :
                                enemyText6 = ""
                                coin6 = True
                            elif letter6 == "&":
                                enemyText6 = ""
                                boost6 = True
                            elif letter6 == "*":
                                enemyText6 = ""
                                strikes6 = True
                            elif letter6 == "+":
                                enemyText6 = ""
                                shield6 = True
                            else :    
                                enemyText6 = format(letter6)
                            global dropDebug6
                            dropDebug6 = False
                            global enemyLabel6
                            enemyLabel6 = Label(text = '[color=ffffff]' + enemyText6, pos_hint={'center_x':enemyPos[0], 'center_y':enemyPos[1]}, markup = True)   
                            x_pos6 = random.randint(delay6a, delay6b)
                            y_pos6 = 0
                            enemyList6.append([x_pos6, y_pos6])

                    for idx7, enemy7Posb in enumerate(enemyList7b) :

                        if delay > .39 and delay < .4 and len(enemyList7) <1 and enemy7Posb[1] > heightDelay and gameStop == False :
                            letterMod()
                            letter7 = random.choice(letterList)
                            global enemyColor7
                            enemyColor7 = random.choice(colorList)
                            global enemyText7
                            coin7 = False
                            boost7 = False
                            strikes7 = False
                            shield7 = False
                            if letter7 == "8" :
                                enemyText7 = ""
                                coin7 = True
                            elif letter7 == "&":
                                enemyText7 = ""
                                boost7 = True
                            elif letter7 == "*":
                                enemyText7 = ""
                                strikes7 = True
                            elif letter7 == "+":
                                enemyText7 = ""
                                shield7 = True
                            else :    
                                enemyText7 = format(letter7)
                            global dropDebug7
                            dropDebug7 = False
                            global enemyLabel7
                            enemyLabel7 = Label(text = '[color=ffffff]' + enemyText7, pos_hint={'center_x':enemyPos[0], 'center_y':enemyPos[1]}, markup = True)   
                            x_pos7 = random.randint(delay7a, delay7b)
                            y_pos7 = 0
                            enemyList7.append([x_pos7, y_pos7])

                    for idx8, enemy8Posb in enumerate(enemyList8b) :
                        
                        if delay > .29 and delay < .3 and len(enemyList8) <1 and enemy8Posb[1] > heightDelay and gameStop == False :
                            letterMod()
                            letter8 = random.choice(letterList)
                            global enemyColor8
                            enemyColor8 = random.choice(colorList)
                            global enemyText8
                            coin8 = False
                            boost8 = False
                            strikes8 = False
                            shield8 = False
                            if letter8 == "8" :
                                enemyText8 = ""
                                coin8 = True
                            elif letter8 == "&" :
                                enemyText8 = ""
                                boost8 = True
                            elif letter8 == "*":
                                enemyText8 = ""
                                strikes8 = True
                            elif letter8 == "+":
                                enemyText8 = ""
                                shield8 = True
                            else :    
                                enemyText8 = format(letter8)
                            global dropDebug8
                            dropDebug8 = False
                            global enemyLabel8
                            enemyLabel8 = Label(text = '[color=ffffff]' + enemyText8, pos_hint={'center_x':enemyPos[0], 'center_y':enemyPos[1]}, markup = True)   
                            x_pos8 = random.randint(delay8a, delay8b)
                            y_pos8 = 0
                            enemyList8.append([x_pos8, y_pos8])





        def draw_enemies(enemyList, enemyList2, enemyList3, enemyList4, enemyList5, enemyList6, enemyList7, enemyList8):
                global enemyLabel
                global enemyLabel2
                global enemyLabel3
                global enemyLabel4
                global enemyLabel5
                global enemyLabel6
                global enemyLabel7
                global enemyLabel8
                global coin1
                global coin2
                global coin3
                global coin4
                global coin5
                global coin6
                global coin7
                global coin8
                global boost1
                global boost2
                global boost3
                global boost4
                global boost5
                global boost6
                global boost7
                global boost8
                global strikes1
                global strikes2
                global strikes3
                global strikes4
                global strikes5
                global strikes6
                global strikes7
                global strikes8
                global shield1
                global shield2
                global shield3
                global shield4
                global shield5 
                global shield6
                global shield7
                global shield8
                
            #while gameStop == False :
                for enemyPos in enemyList :
                    if coin1 == True :
                    #    gameScreen.blit(Color, (enemyPos[0]-4.5, enemyPos[1]-10))
                         Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemyPos[0]-4.5, 'center_y':enemyPos[1]-10})
                         Fl.add_widget(Color)  
                    elif boost1 == True :
                    #    gameScreen.blit(Color2, (enemyPos[0]-4.5, enemyPos[1]-10))
                         Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemyPos[0]-4.5, 'center_y':enemyPos[1]-10})
                         Fl.add_widget(Color2)
                    elif strikes1 == True :
                    #    gameScreen.blit(Color3, (enemyPos[0]-4.5, enemyPos[1]-10))
                         Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemyPos[0]-4.5, 'center_y':enemyPos[1]-10})
                         Fl.add_widget(Color3)
                    elif shield1 == True :
                    #    gameScreen.blit(Color5, (enemyPos[0]-4.5, enemyPos[1]-10))
                         Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemyPos[0]-4.5, 'center_y':enemyPos[1]-10})
                         Fl.add_widget(Color5)
                    else:
                    #    gameScreen.blit(Color4, (enemyPos[0]-4.5, enemyPos[1]-10))
                         Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemyPos[0]-4.5, 'center_y':enemyPos[1]-10})
                         Fl.add_widget(Color4)
                         Fl.add_widget(enemyLabel)
                for enemy2Pos in enemyList2:
                    if coin2 == True :
                        #gameScreen.blit(Color, (enemy2Pos[0]-4.5, enemy2Pos[1]-10))
                        Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemy2Pos[0]-4.5, 'center_y':enemy2Pos[1]-10})
                        Fl.add_widget(Color)  
                    elif boost2 == True :
                        #gameScreen.blit(Color2, (enemy2Pos[0]-4.5, enemy2Pos[1]-10))
                        Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemy2Pos[0]-4.5, 'center_y':enemy2Pos[1]-10})
                        Fl.add_widget(Color2)
                    elif strikes2 == True :
                        #gameScreen.blit(Color3, (enemy2Pos[0]-4.5, enemy2Pos[1]-10))
                        Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemy2Pos[0]-4.5, 'center_y':enemy2Pos[1]-10})
                        Fl.add_widget(Color3)
                    elif shield2 == True :
                        #gameScreen.blit(Color5, (enemy2Pos[0]-4.5, enemy2Pos[1]-10))
                        Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemy2Pos[0]-4.5, 'center_y':enemy2Pos[1]-10})
                        Fl.add_widget(Color5)
                    else:
                        #gameScreen.blit(Color4, (enemy2Pos[0]-4.5, enemy2Pos[1]-10))
                        #gameScreen.blit(enemyLabel2, (enemy2Pos[0], enemy2Pos[1]))
                        Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemy2Pos[0]-4.5, 'center_y':enemy2Pos[1]-10})
                        Fl.add_widget(Color4)
                        Fl.add_widget(enemyLabel2)
                for enemy3Pos in enemyList3:
                    if coin3 == True :
                        #gameScreen.blit(Color, (enemy3Pos[0]-4.5, enemy3Pos[1]-10))
                        Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemy3Pos[0]-4.5, 'center_y':enemy3Pos[1]-10})
                        Fl.add_widget(Color)
                    elif boost3 == True :
                        #gameScreen.blit(Color2, (enemy3Pos[0]-4.5, enemy3Pos[1]-10))
                        Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemy3Pos[0]-4.5, 'center_y':enemy3Pos[1]-10})
                        Fl.add_widget(Color2)
                    elif strikes3 == True :
                        #gameScreen.blit(Color3, (enemy3Pos[0]-4.5, enemy3Pos[1]-10))
                        Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemy3Pos[0]-4.5, 'center_y':enemy3Pos[1]-10})
                        Fl.add_widget(Color3)
                    elif shield3 == True :
                        #gameScreen.blit(Color5, (enemy3Pos[0]-4.5, enemy3Pos[1]-10))
                        Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemy3Pos[0]-4.5, 'center_y':enemy3Pos[1]-10})
                        Fl.add_widget(Color5)
                    else :
                        #gameScreen.blit(Color4, (enemy3Pos[0]-4.5, enemy3Pos[1]-10))
                        #gameScreen.blit(enemyLabel3, (enemy3Pos[0], enemy3Pos[1]))
                        Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemy3Pos[0]-4.5, 'center_y':enemy3Pos[1]-10})
                        Fl.add_widget(Color4)
                        Fl.add_widget(enemyLabel3)
                for enemy4Pos in enemyList4:
                    if coin4 == True :
                        #gameScreen.blit(Color, (enemy4Pos[0]-4.5, enemy4Pos[1]-10))
                        Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemy4Pos[0]-4.5, 'center_y':enemy4Pos[1]-10})
                        Fl.add_widget(Color)
                    elif boost4 == True :
                        #gameScreen.blit(Color2, (enemy4Pos[0]-4.5, enemy4Pos[1]-10))
                        Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemy4Pos[0]-4.5, 'center_y':enemy4Pos[1]-10})
                        Fl.add_widget(Color2)
                    elif strikes4 == True :
                        #gameScreen.blit(Color3, (enemy4Pos[0]-4.5, enemy4Pos[1]-10))
                        Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemy4Pos[0]-4.5, 'center_y':enemy4Pos[1]-10})
                        Fl.add_widget(Color3)
                    elif shield4 == True :
                        #gameScreen.blit(Color5, (enemy4Pos[0]-4.5, enemy4Pos[1]-10))
                        Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemy4Pos[0]-4.5, 'center_y':enemy4Pos[1]-10})
                        Fl.add_widget(Color5)
                    else :
                        #gameScreen.blit(Color4, (enemy4Pos[0]-4.5, enemy4Pos[1]-10))
                        #gameScreen.blit(enemyLabel4, (enemy4Pos[0], enemy4Pos[1]))
                        Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemy4Pos[0]-4.5, 'center_y':enemy4Pos[1]-10})
                        Fl.add_widget(Color4)
                        Fl.add_widget(enemyLabel4)
                for enemy5Pos in enemyList5:
                    if coin5 == True :
                        #gameScreen.blit(Color, (enemy5Pos[0]-4.5, enemy5Pos[1]-10))
                        Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemy5Pos[0]-4.5, 'center_y':enemy5Pos[1]-10})
                        Fl.add_widget(Color)
                    elif boost5 == True :
                        #gameScreen.blit(Color2, (enemy5Pos[0]-4.5, enemy5Pos[1]-10))
                        Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemy5Pos[0]-4.5, 'center_y':enemy5Pos[1]-10})
                        Fl.add_widget(Color2)
                    elif strikes5 == True :
                        #gameScreen.blit(Color3, (enemy5Pos[0]-4.5, enemy5Pos[1]-10))
                        Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemy5Pos[0]-4.5, 'center_y':enemy5Pos[1]-10})
                        Fl.add_widget(Color3)
                    elif shield5 == True :
                        #gameScreen.blit(Color5, (enemy5Pos[0]-4.5, enemy5Pos[1]-10))
                        Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemy5Pos[0]-4.5, 'center_y':enemy5Pos[1]-10})
                        Fl.add_widget(Color5)
                    else :
                        #gameScreen.blit(Color4, (enemy5Pos[0]-4.5, enemy5Pos[1]-10))
                        #gameScreen.blit(enemyLabel5, (enemy5Pos[0], enemy5Pos[1]))
                        Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemy5Pos[0]-4.5, 'center_y':enemy5Pos[1]-10})
                        Fl.add_widget(Color4) 
                        Fl.add_widget(enemyLabel5)
                for enemy6Pos in enemyList6:
                    if coin6 == True :
                        #gameScreen.blit(Color, (enemy6Pos[0]-4.5, enemy6Pos[1]-10))
                        Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemy6Pos[0]-4.5, 'center_y':enemy6Pos[1]-10})
                        Fl.add_widget(Color)
                    elif boost6 == True :
                        #gameScreen.blit(Color2, (enemy6Pos[0]-4.5, enemy6Pos[1]-10))
                        Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemy6Pos[0]-4.5, 'center_y':enemy6Pos[1]-10})
                        Fl.add_widget(Color2)
                    elif strikes6 == True :
                        #gameScreen.blit(Color3, (enemy6Pos[0]-4.5, enemy6Pos[1]-10))
                        Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemy6Pos[0]-4.5, 'center_y':enemy6Pos[1]-10})
                        Fl.add_widget(Color3)
                    elif shield6 == True :
                        #gameScreen.blit(Color5, (enemy6Pos[0]-4.5, enemy6Pos[1]-10))
                        Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemy6Pos[0]-4.5, 'center_y':enemy6Pos[1]-10})
                        Fl.add_widget(Color5)
                    else :
                        #gameScreen.blit(Color4, (enemy6Pos[0]-4.5, enemy6Pos[1]-10))
                        #gameScreen.blit(enemyLabel6, (enemy6Pos[0], enemy6Pos[1]))
                        Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemy6Pos[0]-4.5, 'center_y':enemy6Pos[1]-10})
                        Fl.add_widget(Color4) 
                        Fl.add_widget(enemyLabel6)
                for enemy7Pos in enemyList7:
                    if coin7 == True :
                        #gameScreen.blit(Color, (enemy7Pos[0]-4.5, enemy7Pos[1]-10))
                        Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemy7Pos[0]-4.5, 'center_y':enemy7Pos[1]-10})
                        Fl.add_widget(Color)
                    elif boost7 == True :
                        #gameScreen.blit(Color2, (enemy7Pos[0]-4.5, enemy7Pos[1]-10))
                        Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemy7Pos[0]-4.5, 'center_y':enemy7Pos[1]-10})
                        Fl.add_widget(Color2)
                    elif strikes7 == True :
                        #gameScreen.blit(Color3, (enemy7Pos[0]-4.5, enemy7Pos[1]-10))
                        Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemy7Pos[0]-4.5, 'center_y':enemy7Pos[1]-10})
                        Fl.add_widget(Color3)
                    elif shield7 == True :
                        #gameScreen.blit(Color5, (enemy7Pos[0]-4.5, enemy7Pos[1]-10))
                        Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemy7Pos[0]-4.5, 'center_y':enemy7Pos[1]-10})
                        Fl.add_widget(Color5)
                    else : 
                        #gameScreen.blit(Color4, (enemy7Pos[0]-4.5, enemy7Pos[1]-10))
                        #gameScreen.blit(enemyLabel7, (enemy7Pos[0], enemy7Pos[1]))
                        Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemy7Pos[0]-4.5, 'center_y':enemy7Pos[1]-10})
                        Fl.add_widget(Color4) 
                        Fl.add_widget(enemyLabel7)
                for enemy8Pos in enemyList8:
                    if coin8 == True :
                        #gameScreen.blit(Color, (enemy8Pos[0]-4.5, enemy8Pos[1]-10))
                        Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemy8Pos[0]-4.5, 'center_y':enemy8Pos[1]-10})
                        Fl.add_widget(Color)
                    elif boost8 == True :
                        #gameScreen.blit(Color2, (enemy8Pos[0]-4.5, enemy8Pos[1]-10))
                        Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemy8Pos[0]-4.5, 'center_y':enemy8Pos[1]-10})
                        Fl.add_widget(Color2)
                    elif strikes8 == True :
                        #gameScreen.blit(Color3, (enemy8Pos[0]-4.5, enemy8Pos[1]-10))
                        Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemy8Pos[0]-4.5, 'center_y':enemy8Pos[1]-10})
                        Fl.add_widget(Color3)
                    elif shield8 == True :
                        #gameScreen.blit(Color5, (enemy8Pos[0]-4.5, enemy8Pos[1]-10))
                        Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemy8Pos[0]-4.5, 'center_y':enemy8Pos[1]-10})
                        Fl.add_widget(Color5)
                    else :
                        #gameScreen.blit(Color4, (enemy8Pos[0]-4.5, enemy8Pos[1]-10))
                        #gameScreen.blit(enemyLabel8, (enemy8Pos[0], enemy8Pos[1]))
                        Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemy8Pos[0]-4.5, 'center_y':enemy8Pos[1]-10})
                        Fl.add_widget(Color4) 
                        Fl.add_widget(enemyLabel8)
                

        def update_enemy_positions(enemyList, enemyList2, enemyList3, enemyList4, enemyList5, enemyList6, enemyList7, enemyList8):

            #while gameStop == False :

                for idx, enemyPos in enumerate(enemyList):
                    if enemyPos[1] >= 0 and enemyPos[1] < gameHeight and (enemyPosb[1] <= 0 or enemyPosb[1] > gameHeight*.15):
                        enemyPos[1] += gameSpeed
                    else:
                        enemyList.pop(idx)
                    

                        
                for idx2, enemy2Pos in enumerate(enemyList2):
                    if enemy2Pos[1] >= 0 and enemy2Pos[1] < gameHeight and (enemy2Posb[1] <= 0 or enemy2Posb[1] > gameHeight*.15):
                        enemy2Pos[1] += gameSpeed
                    else:
                        enemyList2.pop(idx2)

                for idx3, enemy3Pos in enumerate(enemyList3):
                    if enemy3Pos[1] >= 0 and enemy3Pos[1] < gameHeight and (enemy3Posb[1] <= 0 or enemy3Posb[1] > gameHeight*.15) :
                        enemy3Pos[1] += gameSpeed
                    else:
                        enemyList3.pop(idx3)

                for idx4, enemy4Pos in enumerate(enemyList4):
                    if enemy4Pos[1] >= 0 and enemy4Pos[1] < gameHeight and (enemy4Posb[1] <= 0 or enemy4Posb[1] > gameHeight*.15):
                        enemy4Pos[1] += gameSpeed
                    else:
                        enemyList4.pop(idx4)

                for idx5, enemy5Pos in enumerate(enemyList5):
                    if enemy5Pos[1] >= 0 and enemy5Pos[1] < gameHeight and (enemy5Posb[1] <= 0 or enemy5Posb[1] > gameHeight*.15):
                        enemy5Pos[1] += gameSpeed
                    else:
                        enemyList5.pop(idx5)

                for idx6, enemy6Pos in enumerate(enemyList6):
                    if enemy6Pos[1] >= 0 and enemy6Pos[1] < gameHeight and (enemy6Posb[1] <= 0 or enemy6Posb[1] > gameHeight*.15):
                        enemy6Pos[1] += gameSpeed
                    else:
                        enemyList6.pop(idx6)

                for idx7, enemy7Pos in enumerate(enemyList7):
                    if enemy7Pos[1] >= 0 and enemy7Pos[1] < gameHeight and (enemy7Posb[1] <= 0 or enemy7Posb[1] > gameHeight*.15):
                        enemy7Pos[1] += gameSpeed
                    else:
                        enemyList7.pop(idx7)

                for idx8, enemy8Pos in enumerate(enemyList8):
                    if enemy8Pos[1] >= 0 and enemy8Pos[1] < gameHeight and (enemy8Posb[1] <= 0 or enemy8Posb[1] > gameHeight*.15):
                        enemy8Pos[1] += gameSpeed
                    else:
                        enemyList8.pop(idx8)



        global hitOn
        hitOn = False



        def drop_enemiesb(enemyListb, enemyList2b, enemyList3b, enemyList4b, enemyList5b, enemyList6b, enemyList7b, enemyList8b, enemyList, enemyList2, enemyList3, enemyList4, enemyList5, enemyList6, enemyList7, enemyList8, gameStop) :

            delay = random.random()
            global counter
            global counter2
            global coin1b
            global coin2b
            global coin3b
            global coin4b
            global coin5b
            global coin6b
            global coin7b
            global coin8b
            global boost1b
            global boost2b
            global boost3b
            global boost4b
            global boost5b
            global boost6b
            global boost7b
            global boost8b
            global strikes1b
            global strikes2b
            global strikes3b
            global strikes4b
            global strikes5b
            global strikes6b
            global strikes7b
            global strikes8b
            global shield1b
            global shield2b
            global shield3b
            global shield4b
            global shield5b
            global shield6b
            global shield7b
            global shield8b


            
            if counter == 5 and counter2 < 8 :

                    if delay > .29 and delay < .3 and len(enemyListb) < 1  and gameStop == False:
                        letterMod()
                        letter = random.choice(letterList)
                        global enemyColorb
                        enemyColorb = random.choice(colorList)
                        global enemyTextb
                        coin1b = False
                        boost1b = False
                        strikes1b = False
                        shield1b = False
                        if letter == "8" :
                            enemyTextb = ""
                            coin1b = True
                        elif letter == "&" :
                            enemyTextb = ""
                            boost1b = True
                        elif letter == "*" :
                            enemyTextb = ""
                            strikes1b = True
                        elif letter == "+" :
                            enemyTextb = ""
                            shield1b = True
                        else :    
                            enemyTextb = format(letter)
                        global dropDebugb
                        dropDebugb = False
                        global enemyLabelb
                        #enemyLabelb = myFont.render(enemyTextb, 1, WHITE)
                        enemyLabelb = Label(text = '[color=ffffff]' + enemyTextb, pos_hint={'center_x':enemyPosb[0], 'center_y':enemyPosb[1]}, markup = True)
                        x_posb = random.randint(delay1a, delay1b)
                        y_posb = 0
                        enemyListb.append([x_posb, y_posb])
                        counter2 += 1
                        
                        
                    if delay > .39 and delay < .4 and len(enemyList2b) <1  and gameStop == False:
                        letterMod()
                        letter2 = random.choice(letterList)
                        global enemyColor2b
                        enemyColor2b = random.choice(colorList)
                        global enemyText2b
                        coin2b = False
                        boost2b = False
                        strikes2b = False
                        shield2b = False
                        if letter2 == "8" :
                            enemyText2b = ""
                            coin2b = True
                        elif letter2 == "&" :
                            enemyText2b = ""
                            boost2b = True
                        elif letter2 == "*" :
                            enemyText2b = ""
                            strikes2b = True
                        elif letter2 == "+" :
                            enemyText2b = ""
                            shield2b = True
                        else :    
                            enemyText2b = format(letter2)
                        global dropDebug2b
                        dropDebug2b = False
                        global enemyLabel2b
                        #enemyLabel2b = myFont.render(enemyText2b, 1, WHITE)
                        enemyLabel2b = Label(text = '[color=ffffff]' + enemyText2b, pos_hint={'center_x':enemy2Posb[0], 'center_y':enemy2Posb[1]}, markup = True)
                        x_pos2b = random.randint(delay2a, delay2b)
                        y_pos2b = 0
                        enemyList2b.append([x_pos2b, y_pos2b])
                        counter2 += 1

                    if delay > .49 and delay < .5 and len(enemyList3b) <1 and gameStop == False  :
                        letterMod()
                        letter3 = random.choice(letterList)
                        global enemyText3b
                        coin3b = False
                        boost3b = False
                        strikes3b = False
                        shield3b = False
                        if letter3 == "8" :
                            enemyText3b = ""
                            coin3b = True
                        elif letter3 == "&" :
                            enemyText3b = ""
                            boost3b = True
                        elif letter3 == "*" :
                            enemyText3b = ""
                            strikes3b = True
                        elif letter3 == "+" :
                            enemyText3b = ""
                            shield3b = True
                        else :    
                            enemyText3b = format(letter3)
                        global dropDebug3b
                        dropDebug3b = False
                        global enemyColor3b
                        enemyColor3b = random.choice(colorList)
                        global enemyLabel3b
                        #enemyLabel3b = myFont.render(enemyText3b, 1, WHITE)
                        enemyLabel3b = Label(text = '[color=ffffff]' + enemyText3b, pos_hint={'center_x':enemy3Posb[0], 'center_y':enemy3Posb[1]}, markup = True)
                        x_pos3b = random.randint(delay3a, delay3b)
                        y_pos3b = 0
                        enemyList3b.append([x_pos3b, y_pos3b])
                        counter2 += 1
                    
                    if delay > .59 and delay < .6 and len(enemyList4b) <1 and gameStop == False:
                        letterMod()
                        letter4 = random.choice(letterList)
                        global enemyColor4b
                        enemyColor4b = random.choice(colorList)
                        global enemyText4b
                        coin4b = False
                        boost4b = False
                        strikes4b = False
                        shield4b = False
                        if letter4 == "8" :
                            enemyText4b = ""
                            coin4b = True
                        elif letter4 == "&" :
                            enemyText4b = ""
                            boost4b = True
                        elif letter4 == "*" :
                            enemyText4b = ""
                            strikes4b = True
                        elif letter4 == "+" :
                            enemyText4b = ""
                            shield4b = True
                        else :    
                            enemyText4b = format(letter4)
                        global dropDebug4b
                        dropDebug4b = False
                        global enemyLabel4b
                        #enemyLabel4b = myFont.render(enemyText4b, 1, WHITE)
                        enemyLabel4b = Label(text = '[color=ffffff]' + enemyText4b, pos_hint={'center_x':enemy4Posb[0], 'center_y':enemy4Posb[1]}, markup = True)
                        x_pos4b = random.randint(delay4a, delay4b)
                        y_pos4b = 0
                        enemyList4b.append([x_pos4b, y_pos4b])
                        counter2 += 1

                    if delay > .69 and delay < .7 and len(enemyList5b) <1 and gameStop == False:
                        letterMod()
                        letter5 = random.choice(letterList)
                        global enemyColor5b
                        enemyColor5b = random.choice(colorList)
                        global enemyText5b
                        coin5b = False
                        boost5b = False
                        strikes5b = False
                        shield5b = False
                        if letter5 == "8" :
                            enemyText5b = ""
                            coin5b = True
                        elif letter5 == "&" :
                            enemyText5b = ""
                            boost5b = True
                        elif letter5 == "*" :
                            enemyText5b = ""
                            strikes5b = True
                        elif letter5 == "+" :
                            enemyText5b = ""
                            shield5b = True
                        else :    
                            enemyText5b = format(letter5)
                        global dropDebug5b
                        dropDebug5b = False
                        global enemyLabel5b
                        #enemyLabel5b = myFont.render(enemyText5b, 1, WHITE)
                        enemyLabel5b = Label(text = '[color=ffffff]' + enemyText5b, pos_hint={'center_x':enemy5Posb[0], 'center_y':enemy5Posb[1]}, markup = True)
                        x_pos5b = random.randint(delay5a, delay5b)
                        y_pos5b = 0
                        enemyList5b.append([x_pos5b, y_pos5b])
                        counter2 += 1

                    if delay > .79 and delay < .8 and len(enemyList6b) <1 and gameStop == False :
                        letterMod()
                        letter6 = random.choice(letterList)
                        global enemyColor6b
                        enemyColor6b = random.choice(colorList)
                        global enemyText6b
                        coin6b = False
                        boost6b = False
                        strikes6b = False
                        shield6b = False
                        if letter6 == "8" :
                            enemyText6b = ""
                            coin6b = True
                        elif letter6 == "&" :
                            enemyText6b = ""
                            boost6b = True
                        elif letter6 == "*" :
                            enemyText6b = ""
                            strikes6b = True
                        elif letter6 == "+" :
                            enemyText6b = ""
                            shield6b = True
                        else :    
                            enemyText6b = format(letter6)
                        global dropDebug6b
                        dropDebug6b = False
                        global enemyLabel6b
                        #enemyLabel6b = myFont.render(enemyText6b, 1, WHITE)
                        enemyLabel6b = Label(text = '[color=ffffff]' + enemyText6b, pos_hint={'center_x':enemy6Posb[0], 'center_y':enemy6Posb[1]}, markup = True)
                        x_pos6b = random.randint(delay6a, delay6b)
                        y_pos6b = 0
                        enemyList6b.append([x_pos6b, y_pos6b])
                        counter2 += 1

                    if delay > .89 and delay < .9 and len(enemyList7b) <1 and gameStop == False:
                        letterMod()
                        letter7 = random.choice(letterList)
                        global enemyColor7b
                        enemyColor7b = random.choice(colorList)
                        global enemyText7b
                        coin7b = False
                        boost7b = False
                        strikes7b = False
                        shield7b = False
                        if letter7 == "8" :
                            enemyText7b = ""
                            coin7b = True
                        elif letter7 == "&" :
                            enemyText7b = ""
                            boost7b = True
                        elif letter7 == "*" :
                            enemyText7b = ""
                            strikes7b = True
                        elif letter7 == "+" :
                            enemyText7b = ""
                            shield7b = True
                        else :    
                            enemyText7b = format(letter7)
                        global dropDebug7b
                        dropDebug7b = False
                        global enemyLabel7b
                        #enemyLabel7b = myFont.render(enemyText7b, 1, WHITE)
                        enemyLabel7b = Label(text = '[color=ffffff]' + enemyText7b, pos_hint={'center_x':enemy7Posb[0], 'center_y':enemy7Posb[1]}, markup = True)    
                        x_pos7b = random.randint(delay7a, delay7b)
                        y_pos7b = 0
                        enemyList7b.append([x_pos7b, y_pos7b])
                        counter2 += 1

                    if delay > .99 and delay < 1 and len(enemyList8b) <1 and gameStop == False:
                        letterMod()
                        letter8 = random.choice(letterList)
                        global enemyColor8b
                        enemyColor8b = random.choice(colorList)
                        global enemyText8b
                        coin8b = False
                        boost8b = False
                        strikes8b = False
                        shield8b = False
                        if letter8 == "8" :
                            enemyText8b = ""
                            coin8b = True
                        elif letter8 == "&" :
                            enemyText8b = ""
                            boost8b = True
                        elif letter8 == "*" :
                            enemyText8b = ""
                            strikes8b = True
                        elif letter8 == "+" :
                            enemyText8b = ""
                            shield8b = True
                        else :    
                            enemyText8b = format(letter8)
                        global dropDebug8b
                        dropDebug8b = False
                        global enemyLabel8b
                        #enemyLabel8b = myFont.render(enemyText8b, 1, WHITE)
                        enemyLabel8b = Label(text = '[color=ffffff]' + enemyText8b, pos_hint={'center_x':enemy8Posb[0], 'center_y':enemy8Posb[1]}, markup = True)
                        x_pos8b = random.randint(delay8a, delay8b)
                        y_pos8b = 0
                        enemyList8b.append([x_pos8b, y_pos8b])
                        counter2 += 1


            if counter2 >= 8 :

                    if delay > .28 and delay < .3 and len(enemyListb) < 1 and (len(enemyList) == 0  or enemyPos[1] >  heightDelay)and gameStop == False :
                        letterMod()
                        letter = random.choice(letterList)
                        enemyColorb = random.choice(colorList)
                        coin1b = False
                        boost1b = False
                        strikes1b = False
                        shield1b = False
                        if letter == "8" :
                            enemyTextb = ""
                            coin1b = True
                        elif letter == "&" :
                            enemyTextb = ""
                            boost1b = True
                        elif letter == "*" :
                            enemyTextb = ""
                            strikes1b = True
                        elif letter == "+" :
                            enemyTextb = ""
                            shield1b = True
                        else :    
                            enemyTextb = format(letter)
                        dropDebugb = False
                        #enemyLabelb = myFont.render(enemyTextb, 1, WHITE)
                        enemyLabelb = Label(text = '[color=ffffff]' + enemyTextb, pos_hint={'center_x':enemyPosb[0], 'center_y':enemyPosb[1]}, markup = True)
                        x_posb = random.randint(delay1a, delay1b)
                        y_posb = 0
                        enemyListb.append([x_posb, y_posb])

                    if delay > .38 and delay < .4 and len(enemyList2b) <1 and (len(enemyList2) == 0   or enemy2Pos[1] >  heightDelay) and gameStop == False:
                        letterMod()
                        letter2 = random.choice(letterList)
                        enemyColor2b = random.choice(colorList)
                        coin2b = False
                        boost2b = False
                        strikes2b = False
                        shield2b = False
                        if letter2 == "8" :
                            enemyText2b = ""
                            coin2b = True
                        elif letter2 == "&" :
                            enemyText2b = ""
                            boost2b = True
                        elif letter2 == "*" :
                            enemyText2b = ""
                            strikes2b = True
                        elif letter2 == "+" :
                            enemyText2b = ""
                            shield2b = True
                        else :    
                            enemyText2b = format(letter2)
                        dropDebug2b = False
                        #enemyLabel2b = myFont.render(enemyText2b, 1, WHITE)
                        enemyLabel2b = Label(text = '[color=ffffff]' + enemyText2b, pos_hint={'center_x':enemy2Posb[0], 'center_y':enemy2Posb[1]}, markup = True)
                        x_pos2b = random.randint(delay2a, delay2b)
                        y_pos2b = 0
                        enemyList2b.append([x_pos2b, y_pos2b])

                    if delay > .48 and delay < .5 and len(enemyList3b) <1 and (len(enemyList3) == 0  or enemy3Pos[1] >  heightDelay) and gameStop == False:
                        letterMod()
                        letter3 = random.choice(letterList)
                        coin3b = False
                        boost3b = False
                        strikes3b = False
                        shield3b = False
                        if letter3 == "8" :
                            enemyText3b = ""
                            coin3b = True
                        elif letter3 == "&" :
                            enemyText3b = ""
                            boost3b = True
                        elif letter3 == "*" :
                            enemyText3b = ""
                            strikes3b = True
                        elif letter3 == "+" :
                            enemyText3b = ""
                            shield3b = True
                        else :    
                            enemyText3b = format(letter3)
                        dropDebug3b = False
                        enemyColor3b = random.choice(colorList)
                        #enemyLabel3b = myFont.render(enemyText3b, 1, WHITE)
                        enemyLabel3b = Label(text = '[color=ffffff]' + enemyText3b, pos_hint={'center_x':enemy3Posb[0], 'center_y':enemy3Posb[1]}, markup = True)
                        x_pos3b = random.randint(delay3a, delay3b)
                        y_pos3b = 0
                        enemyList3b.append([x_pos3b, y_pos3b])
                    
                    if delay > .58 and delay < .6 and len(enemyList4b) <1 and (len(enemyList4) == 0  or enemy4Pos[1] >  heightDelay) and gameStop == False:
                        letterMod()
                        letter4 = random.choice(letterList)
                        enemyColor4b = random.choice(colorList)
                        coin4b = False
                        boost4b = False
                        strikes4b = False
                        shield4b = False
                        if letter4 == "8" :
                            enemyText4b = ""
                            coin4b = True
                        elif letter4 == "&" :
                            enemyText4b = ""
                            boost4b = True
                        elif letter4 == "*" :
                            enemyText4b = ""
                            strikes4b = True
                        elif letter4 == "+" :
                            enemyText4b = ""
                            shield4b = True
                        else :    
                            enemyText4b = format(letter4)
                        dropDebug4b = False
                        #enemyLabel4b = myFont.render(enemyText4b, 1, WHITE)
                        enemyLabel4b = Label(text = '[color=ffffff]' + enemyText4b, pos_hint={'center_x':enemy4Posb[0], 'center_y':enemy4Posb[1]}, markup = True)
                        x_pos4b = random.randint(delay4a, delay4b)
                        y_pos4b = 0
                        enemyList4b.append([x_pos4b, y_pos4b])

                    if delay > .68 and delay < .7 and len(enemyList5b) <1 and (len(enemyList5) == 0 or enemy5Pos[1] >  heightDelay) and gameStop == False :
                        letterMod()
                        letter5 = random.choice(letterList)
                        enemyColor5b = random.choice(colorList)
                        coin5b = False
                        boost5b = False
                        strikes5b = False
                        shield5b = False
                        if letter5 == "8" :
                            enemyText5b = ""
                            coin5b = True
                        elif letter5 == "&" :
                            enemyText5b = ""
                            boost5b = True
                        elif letter5 == "*" :
                            enemyText5b = ""
                            strikes5b = True
                        elif letter5 == "+" :
                            enemyText5b = ""
                            shield5b = True
                        else :    
                            enemyText5b = format(letter5)
                        dropDebug5b = False
                        #enemyLabel5b = myFont.render(enemyText5b, 1, WHITE)
                        enemyLabel5b = Label(text = '[color=ffffff]' + enemyText5b, pos_hint={'center_x':enemy5Posb[0], 'center_y':enemy5Posb[1]}, markup = True)
                        x_pos5b = random.randint(delay5a, delay5b)
                        y_pos5b = 0
                        enemyList5b.append([x_pos5b, y_pos5b])

                    if delay > .78 and delay < .8 and len(enemyList6b) <1 and (len(enemyList6) == 0 or enemy6Pos[1] >  heightDelay)and gameStop == False :
                        letterMod()
                        letter6 = random.choice(letterList)
                        enemyColor6b = random.choice(colorList)
                        coin6b = False
                        boost6b = False
                        strikes6b = False
                        shield6b = False
                        if letter6 == "8" :
                            enemyText6b = ""
                            coin6b = True
                        elif letter6 == "&" :
                            enemyText6b = ""
                            boost6b = True
                        elif letter6 == "*" :
                            enemyText6b = ""
                            strikes6b = True
                        elif letter6 == "+" :
                            enemyText6b = ""
                            shield6b = True
                        else :    
                            enemyText6b = format(letter6)
                        dropDebug6b = False
                        #enemyLabel6b = myFont.render(enemyText6b, 1, WHITE)
                        enemyLabel6b = Label(text = '[color=ffffff]' + enemyText6b, pos_hint={'center_x':enemy6Posb[0], 'center_y':enemy6Posb[1]}, markup = True)    
                        x_pos6b = random.randint(delay6a, delay6b)
                        y_pos6b = 0
                        enemyList6b.append([x_pos6b, y_pos6b])

                    if delay > .88 and delay < .9 and len(enemyList7b) <1 and (len(enemyList7) == 0 or enemy7Pos[1] >  heightDelay) and gameStop == False:
                        letterMod()
                        letter7 = random.choice(letterList)
                        enemyColor7b = random.choice(colorList)
                        coin7b = False
                        boost7b = False
                        strikes7b = False
                        shield7b = False
                        if letter7 == "8" :
                            enemyText7b = ""
                            coin7b = True
                        elif letter7 == "&" :
                            enemyText7b = ""
                            boost7b = True
                        elif letter7 == "*" :
                            enemyText7b = ""
                            strikes7b = True
                        elif letter7 == "+" :
                            enemyText7b = ""
                            shield7b = True
                        else :    
                            enemyText7b = format(letter7)
                        dropDebug7b = False
                        #enemyLabel7b = myFont.render(enemyText7b, 1, WHITE)
                        enemyLabel7b = Label(text = '[color=ffffff]' + enemyText7b, pos_hint={'center_x':enemy7Posb[0], 'center_y':enemy7Posb[1]}, markup = True)
                        x_pos7b = random.randint(delay7a, delay7b)
                        y_pos7b = 0
                        enemyList7b.append([x_pos7b, y_pos7b])

                    if delay > .98 and delay < 1 and len(enemyList8b) <1 and (len(enemyList8) == 0 or enemy8Pos[1] >  heightDelay) and gameStop == False:
                        letterMod()
                        letter8 = random.choice(letterList)
                        enemyColor8b = random.choice(colorList)
                        coin8b = False
                        boost8b = False
                        strikes8b = False
                        shield8b = False
                        if letter8 == "8" :
                            enemyText8b = ""
                            coin8b = True
                        elif letter8 == "&" :
                            enemyText8b = ""
                            boost8b = True
                        elif letter8 == "*" :
                            enemyText8b = ""
                            strikes8b = True
                        elif letter8 == "+" :
                            enemyText8b = ""
                            shield8b = True
                        else :    
                            enemyText8b = format(letter8)
                        dropDebug8b = False
                        #enemyLabel8b = myFont.render(enemyText8b, 1, WHITE)
                        enemyLabel8b = Label(text = '[color=ffffff]' + enemyText8b, pos_hint={'center_x':enemy8Posb[0], 'center_y':enemy8Posb[1]}, markup = True)
                        x_pos8b = random.randint(delay8a, delay8b)
                        y_pos8b = 0
                        enemyList8b.append([x_pos8b, y_pos8b])





        def draw_enemiesb(enemyListb, enemyList2b, enemyList3b, enemyList4b, enemyList5b, enemyList6b, enemyList7b, enemyList8b):

            global coin1b
            global coin2b
            global coin3b
            global coin4b
            global coin5b
            global coin6b
            global coin7b
            global coin8b
            global boost1b
            global boost2b
            global boost3b
            global boost4b
            global boost5b
            global boost6b
            global boost7b
            global boost8b
            global strikes1b
            global strikes2b
            global strikes3b
            global strikes4b
            global strikes5b
            global strikes6b
            global strikes7b
            global strikes8b
            global shield1b
            global shield2b
            global shield3b
            global shield4b
            global shield5b
            global shield6b
            global shield7b
            global shield8b


            
#BOOKMARK 11/29                
            for enemyPosb in enemyListb :
                if coin1b == True :
                    #gameScreen.blit(Color, (enemyPosb[0]-4.5, enemyPosb[1]-10))
                    Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemyPosb[0]-4.5, 'center_y':enemyPosb[1]-10})
                    Fl.add_widget(Color)
                elif boost1b == True :
                    #gameScreen.blit(Color2, (enemyPosb[0]-4.5, enemyPosb[1]-10))
                    Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemyPosb[0]-4.5, 'center_y':enemyPosb[1]-10})
                    Fl.add_widget(Color2)
                elif strikes1b == True :
                    #gameScreen.blit(Color3, (enemyPosb[0]-4.5, enemyPosb[1]-10))
                    Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemyPosb[0]-4.5, 'center_y':enemyPosb[1]-10})
                    Fl.add_widget(Color3)
                elif shield1b == True :
                    #gameScreen.blit(Color5, (enemyPosb[0]-4.5, enemyPosb[1]-10))
                    Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemyPosb[0]-4.5, 'center_y':enemyPosb[1]-10})
                    Fl.add_widget(Color5)
                else :
                    #gameScreen.blit(Color4, (enemyPosb[0]-4.5, enemyPosb[1]-10))
                    #gameScreen.blit(enemyLabelb, (enemyPosb[0], enemyPosb[1]))
                    Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemyPosb[0]-4.5, 'center_y':enemyPosb[1]-10})
                    Fl.add_widget(Color4)
                    Fl.add_widget(enemyLabelb)
            for enemy2Posb in enemyList2b:
                if coin2b == True :
                    #gameScreen.blit(Color, (enemy2Posb[0]-4.5, enemy2Posb[1]-10))
                    Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemy2Posb[0]-4.5, 'center_y':enemy2Posb[1]-10})
                    Fl.add_widget(Color)
                elif boost2b == True :
                    #gameScreen.blit(Color2, (enemy2Posb[0]-4.5, enemy2Posb[1]-10))
                    Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemy2Posb[0]-4.5, 'center_y':enemy2Posb[1]-10})
                    Fl.add_widget(Color2)
                elif strikes2b == True :
                    #gameScreen.blit(Color3, (enemy2Posb[0]-4.5, enemy2Posb[1]-10))
                    Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemy2Posb[0]-4.5, 'center_y':enemy2Posb[1]-10})
                    Fl.add_widget(Color3)
                elif shield2b == True :
                    #gameScreen.blit(Color5, (enemy2Posb[0]-4.5, enemy2Posb[1]-10))
                    Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemy2Posb[0]-4.5, 'center_y':enemy2Posb[1]-10})
                    Fl.add_widget(Color5)
                else :
                    #gameScreen.blit(Color4, (enemy2Posb[0]-4.5, enemy2Posb[1]-10))
                    #gameScreen.blit(enemyLabel2b, (enemy2Posb[0], enemy2Posb[1]))
                    Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemy2Posb[0]-4.5, 'center_y':enemy2Posb[1]-10})
                    Fl.add_widget(Color4)
                    Fl.add_widget(enemyLabel2b)
            for enemy3Posb in enemyList3b:
                if coin3b == True :
                    #gameScreen.blit(Color, (enemy3Posb[0]-4.5, enemy3Posb[1]-10))
                    Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemy3Posb[0]-4.5, 'center_y':enemy3Posb[1]-10})
                    Fl.add_widget(Color)
                elif boost3b == True :
                    #gameScreen.blit(Color2, (enemy3Posb[0]-4.5, enemy3Posb[1]-10))
                    Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemy3Posb[0]-4.5, 'center_y':enemy3Posb[1]-10})
                    Fl.add_widget(Color2) 
                elif strikes3b == True :
                    #gameScreen.blit(Color3, (enemy3Posb[0]-4.5, enemy3Posb[1]-10))
                    Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemy3Posb[0]-4.5, 'center_y':enemy3Posb[1]-10})
                    Fl.add_widget(Color3)
                elif shield3b == True :
                    #gameScreen.blit(Color5, (enemy3Posb[0]-4.5, enemy3Posb[1]-10))
                    Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemy3Posb[0]-4.5, 'center_y':enemy3Posb[1]-10})
                    Fl.add_widget(Color5)
                else :
                    #gameScreen.blit(Color4, (enemy3Posb[0]-4.5, enemy3Posb[1]-10))
                    #gameScreen.blit(enemyLabel3b, (enemy3Posb[0], enemy3Posb[1]))
                    Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemy3Posb[0]-4.5, 'center_y':enemy3Posb[1]-10})
                    Fl.add_widget(Color4)
                    Fl.add_widget(enemyLabel3b)
            for enemy4Posb in enemyList4b:
                if coin4b == True :
                    #gameScreen.blit(Color, (enemy4Posb[0]-4.5, enemy4Posb[1]-10))
                    Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemy4Posb[0]-4.5, 'center_y':enemy4Posb[1]-10})
                    Fl.add_widget(Color)
                elif boost4b == True :
                    #gameScreen.blit(Color2, (enemy4Posb[0]-4.5, enemy4Posb[1]-10))
                    Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemy4Posb[0]-4.5, 'center_y':enemy4Posb[1]-10})
                    Fl.add_widget(Color2) 
                elif strikes4b == True :
                    #gameScreen.blit(Color3, (enemy4Posb[0]-4.5, enemy4Posb[1]-10))
                    Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemy4Posb[0]-4.5, 'center_y':enemy4Posb[1]-10})
                    Fl.add_widget(Color3)
                elif shield4b == True :
                    #gameScreen.blit(Color5, (enemy4Posb[0]-4.5, enemy4Posb[1]-10))
                    Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemy4Posb[0]-4.5, 'center_y':enemy4Posb[1]-10})
                    Fl.add_widget(Color5)
                else :
                    #gameScreen.blit(Color4, (enemy4Posb[0]-4.5, enemy4Posb[1]-10))
                    #gameScreen.blit(enemyLabel4b, (enemy4Posb[0], enemy4Posb[1]))
                    Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemy4Posb[0]-4.5, 'center_y':enemy4Posb[1]-10})
                    Fl.add_widget(Color4)
                    Fl.add_widget(enemyLabel4b)
            for enemy5Posb in enemyList5b:
                if coin5b == True :
                    #gameScreen.blit(Color, (enemy5Posb[0]-4.5, enemy5Posb[1]-10))
                    Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemy5Posb[0]-4.5, 'center_y':enemy5Posb[1]-10})
                    Fl.add_widget(Color)
                elif boost5b == True :
                    #gameScreen.blit(Color2, (enemy5Posb[0]-4.5, enemy5Posb[1]-10))
                    Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemy5Posb[0]-4.5, 'center_y':enemy5Posb[1]-10})
                    Fl.add_widget(Color2)
                elif strikes5b == True :
                    #gameScreen.blit(Color3, (enemy5Posb[0]-4.5, enemy5Posb[1]-10))
                    Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemy5Posb[0]-4.5, 'center_y':enemy5Posb[1]-10})
                    Fl.add_widget(Color3)    
                elif shield5b == True :
                    #gameScreen.blit(Color5, (enemy5Posb[0]-4.5, enemy5Posb[1]-10))
                    Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemy5Posb[0]-4.5, 'center_y':enemy5Posb[1]-10})
                    Fl.add_widget(Color5)
                else :
                    #gameScreen.blit(Color4, (enemy5Posb[0]-4.5, enemy5Posb[1]-10))
                    #gameScreen.blit(enemyLabel5b, (enemy5Posb[0], enemy5Posb[1]))
                    Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemy5Posb[0]-4.5, 'center_y':enemy5Posb[1]-10})
                    Fl.add_widget(Color4)
                    Fl.add_widget(enemyLabel5b)
            for enemy6Posb in enemyList6b:
                if coin6b == True :
                    #gameScreen.blit(Color, (enemy6Posb[0]-4.5, enemy6Posb[1]-10))
                    Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemy6Posb[0]-4.5, 'center_y':enemy6Posb[1]-10})
                    Fl.add_widget(Color)
                elif boost6b == True :
                    #gameScreen.blit(Color2, (enemy6Posb[0]-4.5, enemy6Posb[1]-10))
                    Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemy6Posb[0]-4.5, 'center_y':enemy6Posb[1]-10})
                    Fl.add_widget(Color2)
                elif strikes6b == True :
                    #gameScreen.blit(Color3, (enemy6Posb[0]-4.5, enemy6Posb[1]-10))
                    Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemy6Posb[0]-4.5, 'center_y':enemy6Posb[1]-10})
                    Fl.add_widget(Color3)
                elif shield6b == True :
                    #gameScreen.blit(Color5, (enemy6Posb[0]-4.5, enemy6Posb[1]-10))
                    Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemy6Posb[0]-4.5, 'center_y':enemy6Posb[1]-10})
                    Fl.add_widget(Color5)
                else :
                    #gameScreen.blit(Color4, (enemy6Posb[0]-4.5, enemy6Posb[1]-10))
                    #gameScreen.blit(enemyLabel6b, (enemy6Posb[0], enemy6Posb[1]))
                    Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemy6Posb[0]-4.5, 'center_y':enemy6Posb[1]-10})
                    Fl.add_widget(Color4)
                    Fl.add_widget(enemyLabel6b)
            for enemy7Posb in enemyList7b:
                if coin7b == True :
                    #gameScreen.blit(Color, (enemy7Posb[0]-4.5, enemy7Posb[1]-10))
                    Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemy7Posb[0]-4.5, 'center_y':enemy7Posb[1]-10})
                    Fl.add_widget(Color)
                elif boost7b == True :
                    #gameScreen.blit(Color2, (enemy7Posb[0]-4.5, enemy7Posb[1]-10))
                    Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemy7Posb[0]-4.5, 'center_y':enemy7Posb[1]-10})
                    Fl.add_widget(Color2)
                elif strikes7b == True :
                    #gameScreen.blit(Color3, (enemy7Posb[0]-4.5, enemy7Posb[1]-10))
                    Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemy7Posb[0]-4.5, 'center_y':enemy7Posb[1]-10})
                    Fl.add_widget(Color3)    
                elif shield7b == True :
                    #gameScreen.blit(Color5, (enemy7Posb[0]-4.5, enemy7Posb[1]-10))
                    Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemy7Posb[0]-4.5, 'center_y':enemy7Posb[1]-10})
                    Fl.add_widget(Color5)
                else : 
                    #gameScreen.blit(Color4, (enemy7Posb[0]-4.5, enemy7Posb[1]-10))
                    #gameScreen.blit(enemyLabel7b, (enemy7Posb[0], enemy7Posb[1]))
                    Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemy7Posb[0]-4.5, 'center_y':enemy7Posb[1]-10})
                    Fl.add_widget(Color4)
                    Fl.add_widget(enemyLabel7b)
            for enemy8Posb in enemyList8b:
                if coin8b == True :
                    #gameScreen.blit(Color, (enemy8Posb[0]-4.5, enemy8Posb[1]-10))
                    Color = Image(source = 'images/coin.gif', pos_hint={'center_x':enemy8Posb[0]-4.5, 'center_y':enemy8Posb[1]-10})
                    Fl.add_widget(Color)
                elif boost8b == True :
                    #gameScreen.blit(Color2, (enemy8Posb[0]-4.5, enemy8Posb[1]-10))
                    Color2 = Image(source = 'images/raindrop_red.png', pos_hint={'center_x':enemy8Posb[0]-4.5, 'center_y':enemy8Posb[1]-10})
                    Fl.add_widget(Color2)
                elif strikes8b == True :
                    #gameScreen.blit(Color3, (enemy8Posb[0]-4.5, enemy8Posb[1]-10))
                    Color3 = Image(source = 'images/raindrop_green.png', pos_hint={'center_x':enemy8Posb[0]-4.5, 'center_y':enemy8Posb[1]-10})
                    Fl.add_widget(Color3) 
                elif shield8b == True :
                    #gameScreen.blit(Color5, (enemy8Posb[0]-4.5, enemy8Posb[1]-10))
                    Color5 = Image(source = 'images/raindrop_purple.png', pos_hint={'center_x':enemy8Posb[0]-4.5, 'center_y':enemy8Posb[1]-10})
                    Fl.add_widget(Color5)
                else : 
                    #gameScreen.blit(Color4, (enemy8Posb[0]-4.5, enemy8Posb[1]-10))
                    #gameScreen.blit(enemyLabel8b, (enemy8Posb[0], enemy8Posb[1]))
                    Color4 = Image(source = 'images/raindrop_blue.png', pos_hint={'center_x':enemy8Posb[0]-4.5, 'center_y':enemy8Posb[1]-10})
                    Fl.add_widget(Color4)
                    Fl.add_widget(enemyLabel8b)

                        

        def update_enemy_positionsb(enemyListb, enemyList2b, enemyList3b, enemyList4b, enemyList5b, enemyList6b, enemyList7b, enemyList8b):



                for idx, enemyPosb in enumerate(enemyListb):
                    if enemyPosb[1] >= 0 and enemyPosb[1] < gameHeight and (enemyPos[1] <= 0 or enemyPos[1] > gameHeight*.15):
                        enemyPosb[1] += gameSpeed
                    else:
                        enemyListb.pop(idx)
                    

                        
                for idx2, enemy2Posb in enumerate(enemyList2b):
                    if enemy2Posb[1] >= 0 and enemy2Posb[1] < gameHeight and (enemy2Pos[1] <= 0 or enemy2Pos[1] > gameHeight*.15):
                        enemy2Posb[1] += gameSpeed
                    else:
                        enemyList2b.pop(idx2)

                for idx3, enemy3Posb in enumerate(enemyList3b):
                    if enemy3Posb[1] >= 0 and enemy3Posb[1] < gameHeight and (enemy3Pos[1] <= 0 or enemy3Pos[1] > gameHeight*.15):
                        enemy3Posb[1] += gameSpeed
                    else:
                        enemyList3b.pop(idx3)

                for idx4, enemy4Posb in enumerate(enemyList4b):
                    if enemy4Posb[1] >= 0 and enemy4Posb[1] < gameHeight and (enemy4Pos[1] <= 0 or enemy4Pos[1] > gameHeight*.15):
                        enemy4Posb[1] += gameSpeed
                    else:
                        enemyList4b.pop(idx4)

                for idx5, enemy5Posb in enumerate(enemyList5b):
                    if enemy5Posb[1] >= 0 and enemy5Posb[1] < gameHeight and (enemy5Pos[1] <= 0 or enemy5Pos[1] > gameHeight*.15):
                        enemy5Posb[1] += gameSpeed
                    else:
                        enemyList5b.pop(idx5)

                for idx6, enemy6Posb in enumerate(enemyList6b):
                    if enemy6Posb[1] >= 0 and enemy6Posb[1] < gameHeight and (enemy6Pos[1] <= 0 or enemy6Pos[1] > gameHeight*.15):
                        enemy6Posb[1] += gameSpeed
                    else:
                        enemyList6b.pop(idx6)

                for idx7, enemy7Posb in enumerate(enemyList7b):
                    if enemy7Posb[1] >= 0 and enemy7Posb[1] < gameHeight and (enemy7Pos[1] <= 0 or enemy7Pos[1] > gameHeight*.15):
                        enemy7Posb[1] += gameSpeed
                    else:
                        enemyList7b.pop(idx7)

                for idx8, enemy8Posb in enumerate(enemyList8b):
                    if enemy8Posb[1] >= 0 and enemy8Posb[1] < gameHeight and (enemy8Pos[1] <= 0 or enemy8Pos[1] > gameHeight*.15):
                        enemy8Posb[1] += gameSpeed
                    else:
                        enemyList8b.pop(idx8)





        def collision_check(enemyList, playerPos):
            for enemyPos in enemyList:
                if detect_collision(enemyPos, playerPos) and gameStop == False:
                    return True
            return False

        def detect_collision(playerPos, enemyPos):
            p_x = playerPos[0]
            p_y = playerPos[1]

            e_x = enemyPos[0]
            e_y = enemyPos[1]

            
            

            
            if (e_x >= p_x and e_x < (p_x + enemySizeW) and (e_y <= p_y and e_y > p_y-playerSize)  ) or ((p_x >= e_x and p_x < e_x+playerSize) and (e_y <= p_y and e_y > p_y-playerSizeL)) :
                global hitOn
                hitOn = True
                return True

            if   (e_y >= p_y and e_y < (p_y + enemySizeL-10) and p_x >= e_x and p_x < (e_x+playerSize)) :
                return True
            return False




#BOOKMARK 11/30

        while not gameOver :

            def __init__(self, **kwargs):
                super(MainApp, self).__init__(**kwargs)
                self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
                self._keyboard.bind(on_key_down=self._on_keyboard_down)

            def _keyboard_closed(self):
                self._keyboard.unbind(on_key_down=self._on_keyboard_down)
                self._keyboard = None


            def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
##                if keycode[1] == 'w':
##                    self.player1.center_y += 10
##                elif keycode[1] == 's':
##                    self.player1.center_y -= 10
##                elif keycode[1] == 'up':
##                    self.player2.center_y += 10
##                elif keycode[1] == 'down':
##                    self.player2.center_y -= 10
                x = playerPos[0]
                y = playerPos[1]
     
                if keycode[1] == 'left':
                    if speedOn == False:
                        x -= (playerSize*playerMove)
                    elif speedOn == True:
                        x -= (playerSize*playerMoveBoost)
                elif keycode[1] == 'right':
                    if speedOn == False:
                        x += (playerSize*playerMove)
                    elif speedOn == True:
                        x += (playerSize*playerMoveBoost)

                playerPos = [x,y]
                            
                
                if keycode[1] == 'backspace':
                    endGame = True

                if keycode[1] == 'enter':
                    letterWipe()

                if x < 0 :
                    playerPos[0] = 0
                    
                if x > (gameWidth - playerSize) :
                    playerPos[0] = gameWidth - playerSize

                if gameStop == True:
                    playerPos[0] = ((gameWidth/2) - (playerSize/2))
                return True
           
            #change for exit
##                                        
##                if keycode[1] == pygame.QUIT:
##                    pygame.quit()
##                    sys.exit()





                #cursor movement with pygame
##                if event.type == pygame.KEYDOWN:
##                    x = playerPos[0]
##                    y = playerPos[1]
##         
##                    if event.key == pygame.K_LEFT:
##                        if speedOn == False:
##                            x -= (playerSize*playerMove)
##                        elif speedOn == True:
##                            x -= (playerSize*playerMoveBoost)
##                    elif event.key == pygame.K_RIGHT:
##                        if speedOn == False:
##                            x += (playerSize*playerMove)
##                        elif speedOn == True:
##                            x += (playerSize*playerMoveBoost)
##
##                    playerPos = [x,y]
##                                
##                    
##                    if event.key == pygame.K_BACKSPACE:
##                        endGame = True
##
##                    if event.key == pygame.K_RETURN:
##                        letterWipe()
##
##                    if x < 0 :
##                        playerPos[0] = 0
##                        
##                    if x > (gameWidth - playerSize) :
##                        playerPos[0] = gameWidth - playerSize
##
##                    if gameStop == True:
##                        playerPos[0] = ((gameWidth/2) - (playerSize/2)) 
##                        


            gameScreen.fill(bgColor)

            def enemyColl(enemyList) :
                global enemyText
                enemyText = ""
                global enemyLabel
                enemyLabel = Label(text='', markup = True)

            def enemyColl2(enemyList2) :
                global enemyText2
                enemyText2 = ""
                global enemyLabel2
                enemyLabel2 = Label(text='', markup = True)

            def enemyColl3(enemyList3) :
                global enemyText3
                enemyText3 = ""
                global enemyLabel3
                enemyLabel3 = Label(text='', markup = True)

            def enemyColl4(enemyList4) :
                global enemyText4
                enemyText4 = ""
                global enemyLabel4
                enemyLabel4 = Label(text='', markup = True)

            def enemyColl5(enemyList5) :
                global enemyText5
                enemyText5 = ""
                global enemyLabel5
                enemyLabel5 = Label(text='', markup = True)

            def enemyColl6(enemyList6) :
                global enemyText6
                enemyText6 = ""
                global enemyLabel6
                enemyLabel6= Label(text='', markup = True)

            def enemyColl7(enemyList7) :
                global enemyText7
                enemyText7 = ""
                global enemyLabel7
                enemyLabel7 = Label(text='', markup = True)

            def enemyColl8(enemyList8) :
                global enemyText8
                enemyText8 = ""
                global enemyLabel8
                enemyLabel8 = Label(text='', markup = True)    

            def enemyCollB(enemyListb) :
                global enemyTextb
                enemyTextb = ""
                global enemyLabelb
                enemyLabelb = Label(text='', markup = True)

            def enemyColl2B(enemyList2b) :
                global enemyText2b
                enemyText2b = ""
                global enemyLabel2b
                enemyLabel2b = Label(text='', markup = True)

            def enemyColl3B(enemyList3b) :
                global enemyText3b
                enemyText3b = ""
                global enemyLabel3b
                enemyLabel3b = Label(text='', markup = True)

            def enemyColl4B(enemyList4b) :
                global enemyText4b
                enemyText4b = ""
                global enemyLabel4b
                enemyLabel4b = Label(text='', markup = True)

            def enemyColl5B(enemyList5b) :
                global enemyText5b
                enemyText5b = ""
                global enemyLabel5b
                enemyLabel5b = Label(text='', markup = True)

            def enemyColl6B(enemyList6b) :
                global enemyText6b
                enemyText6b = ""
                global enemyLabel6b
                enemyLabel6b = Label(text='', markup = True)

            def enemyColl7B(enemyList7b) :
                global enemyText7b
                enemyText7b = ""
                global enemyLabel7b
                enemyLabel7b = Label(text='', markup = True)

            def enemyColl8B(enemyList8b) :
                global enemyText8b
                enemyText8b = ""
                global enemyLabel8b
                enemyLabel8b = Label(text='', markup = True)

            


            def letterWipe() :
                global shieldOn
                global speedOn
                global speedTimer
                global wordList
                global wordScore
                global scoreList
                global lvl1word1CHK
                global lvl1word2CHK
                global lvl1word3CHK
                global lvl1word4CHK
                global lvl1word5CHK
                global lvl1word6CHK
                global lvl1word7CHK
                global lvl1word8CHK
                global lvl1word9CHK
                global lvl1word10CHK
                global lvl1word11CHK
                global lvl1word12CHK
                global lvl1word13CHK
                global lvl1word14CHK
                global lvl1word15CHK
                global lvl1word16CHK
                global lvl1word17CHK
                global lvl1word18CHK      
                global lvl1word19CHK
                global lvl1word20CHK
                global lvl1word21CHK
                global lvl1word22CHK
                global lvl1word23CHK
                global lvl1word24CHK
                global lvl1word25CHK
                global lvl1word26CHK
                global lvl1word27CHK
                global lvl1word28CHK
                global lvl1word29CHK
                global lvl1word30CHK
                global lvl1word31CHK
                global lvl1word32CHK
                global lvl1word33CHK
                global lvl1word34CHK
                global lvl1word35CHK
                global lvl1word36CHK
                global lvl1word37CHK
                global lvl1word38CHK
                global lvl1word39CHK
                global lvl1word40CHK
                global lvl1word41CHK
                global lvl1word42CHK
                global lvl1word43CHK
                global lvl1word44CHK
                global lvl1word45CHK
                global lvl1word46CHK
                global lvl1word47CHK
                global lvl1word48CHK
                global lvl1word49CHK
                global lvl1word50CHK
                global lvl1word51CHK
                global lvl1word52CHK
                global lvl1word53CHK
                global lvl1word54CHK
                global lvl1word55CHK
                global lvl1word56CHK
                global lvl1word57CHK
                global lvl1word58CHK
                global lvl1word59CHK
                global lvl1word60CHK
                global lvl1word61CHK
                global lvl1word62CHK
                global lvl1word63CHK
                global lvl1word64CHK
                global lvl1word65CHK
                global lvl1word66CHK
                global lvl1word67CHK
                global lvl1word68CHK
                global lvl1word69CHK
                global lvl1word70CHK
                global lvl1word71CHK
                global lvl1word72CHK
                global lvl1word73CHK
                global lvl1word74CHK
                global lvl1word75CHK
                global lvl1word76CHK
                global lvl1word77CHK
                global lvl1word78CHK
                global lvl1word79CHK
                global lvl1word80CHK
                global lvl1word81CHK
                global lvl1word82CHK
                global lvl1word83CHK
                global lvl1word84CHK
                global lvl1word85CHK
                global lvl1word86CHK
                global lvl1word87CHK
                global lvl1word88CHK
                global lvl1word89CHK
                global lvl1word90CHK
                global lvl1word91CHK
                global lvl1word92CHK
                global lvl1word93CHK
                global lvl1word94CHK
                global lvl1word95CHK
                global lvl1word96CHK
                global lvl1word97CHK
                global lvl1word98CHK
                global lvl1word99CHK
                global lvl1word100CHK
                global lvl1word101CHK
                global lvl1word102CHK
                global lvl1word103CHK
                global lvl1word104CHK
                global lvl1word105CHK
                global lvl1word106CHK
                global lvl1word107CHK
                global lvl1word108CHK
                global lvl1word109CHK
                global lvl1word110CHK
                global lvl1word111CHK
                global lvl1word112CHK
                global lvl1word113CHK
                global lvl1word114CHK
                global lvl1word115CHK
                global lvl1word116CHK
                global lvl1word117CHK
                global lvl1word118CHK
                global lvl1word119CHK
                global lvl1word120CHK
                global lvl1word121CHK
                global lvl1word122CHK
                global lvl1word123CHK
                global lvl1word124CHK
                global lvl1word125CHK
                global lvl1word126CHK
                global lvl1word127CHK
                global lvl1word128CHK
                global lvl1word129CHK
                global lvl1word130CHK
                global lvl1word131CHK
                global lvl1word132CHK
                global lvl1word133CHK
                global lvl1word134CHK
                global lvl1word135CHK
                global lvl1word136CHK
                global lvl1word137CHK
                global lvl1word138CHK
                global lvl1word139CHK
                global lvl1word140CHK
                global lvl1word141CHK
                global lvl1word142CHK
                global lvl1word143CHK
                global lvl1word144CHK
                global lvl1word145CHK
                global lvl1word146CHK
                global lvl1word147CHK
                global lvl1word148CHK
                global lvl1word149CHK
                global lvl1word150CHK
                global lvl1word151CHK
                global lvl1word152CHK
                global lvl1word153CHK
                global lvl1word154CHK
                global lvl1word155CHK
                global lvl1word156CHK
                global lvl1word157CHK
                global lvl1word158CHK
                global lvl1word159CHK
                global lvl1word160CHK
                global lvl1word161CHK
                global lvl1word162CHK
                global lvl1word163CHK
                global lvl1word164CHK
                global lvl1word165CHK
                global lvl1word166CHK
                global lvl1word167CHK
                global lvl1word168CHK
                global lvl1word169CHK
                global lvl1word170CHK
                global lvl1word171CHK
                global lvl1word172CHK
                global lvl1word173CHK
                global lvl1word174CHK
                global lvl1word175CHK
                global lvl1word176CHK
                global lvl1word177CHK
                global lvl1word178CHK
                global lvl1word179CHK
                global lvl1word180CHK
                global lvl1word181CHK
                global lvl1word182CHK
                global lvl1word183CHK
                global lvl1word184CHK
                global lvl1word185CHK
                global lvl1word186CHK
                global lvl1word187CHK
                global lvl1word188CHK
                global lvl1word189CHK
                global lvl1word190CHK
                global lvl1word191CHK
                global lvl1word192CHK
                global lvl1word193CHK
                global lvl1word194CHK
                global lvl1word195CHK
                global lvl1word196CHK
                global lvl1word197CHK
                global lvl1word198CHK
                global lvl1word199CHK
                global lvl1word200CHK
                global lvl1word201CHK
                global lvl1word202CHK
                global lvl1word203CHK
                global lvl1word204CHK
                global lvl1word205CHK
                global lvl1word206CHK
                global lvl1word207CHK
                global lvl1word208CHK
                global lvl1word209CHK
                global lvl1word210CHK
                global lvl1word211CHK
                global lvl1word212CHK
                global lvl1word213CHK
                global lvl1word214CHK
                global lvl1word215CHK
                global lvl1word216CHK
                global lvl1word217CHK
                global lvl1word218CHK
                global lvl1word219CHK
                global lvl1word220CHK
                global lvl1word221CHK
                global lvl1word222CHK
                global lvl1word223CHK
                global lvl1word224CHK
                global lvl1word225CHK
                global lvl1word226CHK
                global lvl1word227CHK
                global lvl1word228CHK
                global lvl1word229CHK
                global lvl1word230CHK
                global lvl1word231CHK
                global lvl1word232CHK
                global lvl1word233CHK
                global lvl1word234CHK
                global lvl1word235CHK
                global lvl1word236CHK
                global lvl1word237CHK
                global lvl1word238CHK
                global lvl1word239CHK
                global lvl1word240CHK
                global lvl1word241CHK
                global lvl1word242CHK
                global lvl1word243CHK
                global lvl1word244CHK
                global lvl1word245CHK
                global lvl1word246CHK
                global lvl1word247CHK
                global lvl1word248CHK
                global lvl1word249CHK
                global lvl1word250CHK
                global lvl1word251CHK
                global lvl1word252CHK
                global lvl1word253CHK
                global lvl1word254CHK
                global lvl1word255CHK
                global lvl1word256CHK
                global lvl1word257CHK
                global lvl1word258CHK
                global lvl1word259CHK
                global lvl1word260CHK
                global lvl1word261CHK
                global lvl1word262CHK
                global lvl1word263CHK
                global lvl1word264CHK
                global lvl1word265CHK
                global lvl1word266CHK
                global lvl1word267CHK
                global lvl1word268CHK
                global lvl1word269CHK
                global lvl1word270CHK
                global lvl1word271CHK
                global lvl1word272CHK
                global lvl1word273CHK
                global lvl1word274CHK
                global lvl1word275CHK
                global lvl1word276CHK
                global lvl1word277CHK
                global lvl1word278CHK
                global lvl1word279CHK
                global lvl1word280CHK
                global lvl1word281CHK
                global lvl1word282CHK
                global lvl1word283CHK
                global lvl1word284CHK
                global lvl1word285CHK
                global lvl1word286CHK
                global lvl1word287CHK
                global lvl1word288CHK
                global lvl1word289CHK
                global lvl1word290CHK
                global lvl1word291CHK
                global lvl1word292CHK
                global lvl1word293CHK
                global lvl1word294CHK
                global lvl1word295CHK
                global lvl1word296CHK
                global lvl1word297CHK
                global lvl1word298CHK
                global lvl1word299CHK
                global lvl1word300CHK
                global lvl1word301CHK
                global lvl1word302CHK
                global lvl1word303CHK
                global lvl1word304CHK
                global lvl1word305CHK
                global lvl1word306CHK
                global lvl1word307CHK
                global lvl1word308CHK
                global lvl1word309CHK
                global lvl1word310CHK
                global lvl1word311CHK
                global lvl1word312CHK
                global lvl1word313CHK
                global lvl1word314CHK
                global lvl1word315CHK
                global lvl1word316CHK
                global lvl1word317CHK
                global lvl1word318CHK
                global lvl1word319CHK
                global lvl1word320CHK
                global lvl1word321CHK
                global lvl1word322CHK
                global lvl1word323CHK
                global lvl1word324CHK
                global lvl1word325CHK
                global lvl1word326CHK
                global lvl1word327CHK
                global lvl1word328CHK
                global lvl1word329CHK
                global lvl1word330CHK
                global lvl1word331CHK
                global lvl1word332CHK
                global lvl1word333CHK
                global lvl1word334CHK
                global lvl1word335CHK
                global lvl1word336CHK
                global lvl1word337CHK
                global lvl1word338CHK
                global lvl1word339CHK
                global lvl1word340CHK
                global lvl1word341CHK
                global lvl1word342CHK
                global lvl1word343CHK
                global lvl1word344CHK
                global lvl1word345CHK
                global lvl1word346CHK
                global lvl1word347CHK
                global lvl1word348CHK
                global lvl1word349CHK
                global lvl1word350CHK
                global lvl1word351CHK
                global lvl1word352CHK
                global lvl1word353CHK
                global lvl1word354CHK
                global lvl1word355CHK
                global lvl1word356CHK
                global lvl1word357CHK
                global lvl1word358CHK
                global lvl1word359CHK
                global lvl1word360CHK
                global lvl1word361CHK
                global lvl1word362CHK
                global lvl1word363CHK
                global lvl1word364CHK
                global lvl1word365CHK
                global lvl1word366CHK
                global lvl1word367CHK
                global lvl1word368CHK
                global lvl1word369CHK
                global lvl1word370CHK
                global lvl1word371CHK
                global lvl1word372CHK
                global lvl1word373CHK
                global lvl1word374CHK
                global lvl1word375CHK
                global lvl1word376CHK
                global lvl1word377CHK
                global lvl1word378CHK
                global lvl1word379CHK
                global lvl1word380CHK
                global lvl1word381CHK
                global lvl1word382CHK
                global lvl1word383CHK
                global lvl1word384CHK
                global lvl1word385CHK
                global lvl1word386CHK
                global lvl1word387CHK
                global lvl1word388CHK
                global lvl1word389CHK
                global lvl1word390CHK
                global lvl1word391CHK
                global lvl1word392CHK
                global lvl1word393CHK
                global lvl1word394CHK
                global lvl1word395CHK
                global lvl1word396CHK
                global lvl1word397CHK
                global lvl1word398CHK
                global lvl1word399CHK
                global lvl1word400CHK
                global lvl1word401CHK
                global lvl1word402CHK
                global lvl1word403CHK
                global lvl1word404CHK
                global lvl1word405CHK
                global lvl1word406CHK
                global lvl1word407CHK
                global lvl1word408CHK
                global lvl1word409CHK
                global lvl1word410CHK
                global lvl1word411CHK
                global lvl1word412CHK
                global lvl1word413CHK
                global lvl1word414CHK
                global lvl1word415CHK
                global lvl1word416CHK
                global lvl1word417CHK
                global lvl1word418CHK
                global lvl1word419CHK
                global lvl1word420CHK
                global lvl1word421CHK
                global lvl1word422CHK
                global lvl1word423CHK
                global lvl1word424CHK
                global lvl1word425CHK
                global lvl1word426CHK
                global lvl1word427CHK
                global lvl1word428CHK
                global lvl1word429CHK
                global lvl1word430CHK
                global lvl1word431CHK
                global lvl1word432CHK
                global lvl1word433CHK
                global lvl1word434CHK
                global lvl1word435CHK
                global lvl1word436CHK
                global lvl1word437CHK
                global lvl1word438CHK
                global lvl1word439CHK
                global lvl1word440CHK
                global lvl1word441CHK
                global lvl1word442CHK
                global lvl1word443CHK
                global lvl1word444CHK
                global lvl1word445CHK
                global lvl1word446CHK
                global lvl1word447CHK
                global lvl1word448CHK
                global lvl1word449CHK
                global lvl1word450CHK
                global lvl1word451CHK
                global lvl1word452CHK
                global lvl1word453CHK
                global lvl1word454CHK
                global lvl1word455CHK
                global lvl1word456CHK
                global lvl1word457CHK
                global lvl1word458CHK
                global lvl1word459CHK
                global lvl1word460CHK
                global lvl1word461CHK
                global lvl1word462CHK
                global lvl1word463CHK
                global lvl1word464CHK
                global lvl1word465CHK
                global lvl1word466CHK
                global lvl1word467CHK
                global lvl1word468CHK
                global lvl1word469CHK
                global lvl1word470CHK
                global lvl1word471CHK
                global lvl1word472CHK
                global lvl1word473CHK
                global lvl1word474CHK
                global lvl1word475CHK
                global lvl1word476CHK
                global lvl1word477CHK
                global lvl1word478CHK
                global lvl1word479CHK
                global lvl1word480CHK
                global lvl1word481CHK
                global lvl1word482CHK
                global lvl1word483CHK
                global lvl1word484CHK
                global lvl1word485CHK
                global lvl1word486CHK
                global lvl1word487CHK
                global lvl1word488CHK
                global lvl1word489CHK
                global lvl1word490CHK
                global lvl1word491CHK
                global lvl1word492CHK
                global lvl1word493CHK
                global lvl1word494CHK
                global lvl1word495CHK
                global lvl1word496CHK
                global lvl1word497CHK
                global lvl1word498CHK
                global lvl1word499CHK
                global lvl1word500CHK
                global lvl1word501CHK
                global lvl1word502CHK
                global lvl1word503CHK
                global lvl1word504CHK
                global lvl1word505CHK
                global lvl1word506CHK
                global lvl1word507CHK
                global lvl1word508CHK
                global lvl1word509CHK
                global lvl1word510CHK
                global lvl1word511CHK
                global lvl1word512CHK
                global lvl1word513CHK
                global lvl1word514CHK
                global lvl1word515CHK
                global lvl1word516CHK
                global lvl1word517CHK
                global lvl1word518CHK
                global lvl1word519CHK
                global lvl1word520CHK
                global lvl1word521CHK
                global lvl1word522CHK
                global lvl1word523CHK
                global lvl1word524CHK
                global lvl1word525CHK
                global lvl1word526CHK
                global lvl1word527CHK
                global lvl1word528CHK
                global lvl1word529CHK
                global lvl1word530CHK
                global lvl1word531CHK
                global lvl1word532CHK
                global lvl1word533CHK
                global lvl1word534CHK
                global lvl1word535CHK
                global lvl1word536CHK
                global lvl1word537CHK
                global lvl1word538CHK
                global lvl1word539CHK
                global lvl1word540CHK
                global lvl1word541CHK
                global lvl1word542CHK
                global lvl1word543CHK
                global lvl1word544CHK
                global lvl1word545CHK
                global lvl1word546CHK
                global lvl1word547CHK
                global lvl1word548CHK
                global lvl1word549CHK
                global lvl1word550CHK
                global lvl1word551CHK
                global lvl1word552CHK
                global lvl1word553CHK
                global lvl1word554CHK
                global lvl1word555CHK
                global lvl1word556CHK
                global lvl1word557CHK
                global lvl1word558CHK
                global lvl1word559CHK
                global lvl1word560CHK
                global lvl1word561CHK
                global lvl1word562CHK
                global lvl1word563CHK
                global lvl1word564CHK
                global lvl1word565CHK
                global lvl1word566CHK
                global lvl1word567CHK
                global lvl1word568CHK
                global lvl1word569CHK
                global lvl1word570CHK
                global lvl1word571CHK
                global lvl1word572CHK
                global lvl1word573CHK
                global lvl1word574CHK
                global lvl1word575CHK
                global lvl1word576CHK
                global lvl1word577CHK
                global lvl1word578CHK
                global lvl1word579CHK
                global lvl1word580CHK
                global lvl1word581CHK
                global lvl1word582CHK
                global lvl1word583CHK
                global lvl1word584CHK
                global lvl1word585CHK
                global lvl1word586CHK
                global lvl1word587CHK
                global lvl1word588CHK
                global lvl1word589CHK
                global lvl1word590CHK
                global lvl1word591CHK
                global lvl1word592CHK
                global lvl1word593CHK
                global lvl1word594CHK
                global lvl1word595CHK
                global lvl1word596CHK
                global lvl1word597CHK
                global lvl1word598CHK
                global lvl1word599CHK
                global lvl1word600CHK
                global lvl1word601CHK
                global lvl1word602CHK
                global lvl1word603CHK
                global lvl1word604CHK
                global lvl1word605CHK
                global lvl1word606CHK
                global lvl1word607CHK
                global lvl1word608CHK
                global lvl1word609CHK
                global lvl1word610CHK
                global lvl1word611CHK
                global lvl1word612CHK
                global lvl1word613CHK
                global lvl1word614CHK
                global lvl1word615CHK
                global lvl1word616CHK
                global lvl1word617CHK
                global lvl1word618CHK
                global lvl1word619CHK
                global lvl1word620CHK
                global lvl1word621CHK
                global lvl1word622CHK
                global lvl1word623CHK
                global lvl1word624CHK
                global lvl1word625CHK
                global lvl1word626CHK
                global lvl1word627CHK
                global lvl1word628CHK
                global lvl1word629CHK
                global lvl1word630CHK
                global lvl1word631CHK
                global lvl1word632CHK
                global lvl1word633CHK
                global lvl1word634CHK
                global lvl1word635CHK
                global lvl1word636CHK
                global lvl1word637CHK
                global lvl1word638CHK
                global lvl1word639CHK
                global lvl1word640CHK
                global lvl1word641CHK
                global lvl1word642CHK
                global lvl1word643CHK
                global lvl1word644CHK
                global lvl1word645CHK
                global lvl1word646CHK
                global lvl1word647CHK
                global lvl1word648CHK
                global lvl1word649CHK
                global lvl1word650CHK
                global lvl1word651CHK
                global lvl1word652CHK
                global lvl1word653CHK
                global lvl1word654CHK
                global lvl1word655CHK
                global lvl1word656CHK
                global lvl1word657CHK
                global lvl1word658CHK
                global lvl1word659CHK
                global lvl1word660CHK
                global lvl1word661CHK
                global lvl1word662CHK
                global lvl1word663CHK
                global lvl1word664CHK
                global lvl1word665CHK
                global lvl1word666CHK
                global lvl1word667CHK
                global lvl1word668CHK
                global lvl1word669CHK
                global lvl1word670CHK
                global lvl1word671CHK
                global lvl1word672CHK
                global lvl1word673CHK
                global lvl1word674CHK
                global lvl1word675CHK
                global lvl1word676CHK
                global lvl1word677CHK
                global lvl1word678CHK
                global lvl1word679CHK
                global lvl1word680CHK
                global lvl1word681CHK
                global lvl1word682CHK
                global lvl1word683CHK
                global lvl1word684CHK
                global lvl1word685CHK
                global lvl1word686CHK
                global lvl1word687CHK
                global lvl1word688CHK
                global lvl1word689CHK
                global lvl1word690CHK
                global lvl1word691CHK
                global lvl1word692CHK
                global lvl1word693CHK
                global lvl1word694CHK
                global lvl1word695CHK
                global lvl1word696CHK
                global lvl1word697CHK
                global lvl1word698CHK
                global lvl1word699CHK
                global lvl1word700CHK
                global lvl1word701CHK
                global lvl1word702CHK
                global lvl1word703CHK
                global lvl1word704CHK
                global lvl1word705CHK
                global lvl1word706CHK
                global lvl1word707CHK
                global lvl1word708CHK
                global lvl1word709CHK
                global lvl1word710CHK
                global lvl1word711CHK
                global lvl1word712CHK
                global lvl1word713CHK
                global lvl1word714CHK
                global lvl1word715CHK
                global lvl1word716CHK
                global lvl1word717CHK
                global lvl1word718CHK
                global lvl1word719CHK
                global lvl1word720CHK
                global lvl1word721CHK
                global lvl1word722CHK
                global lvl1word723CHK
                global lvl1word724CHK
                global lvl1word725CHK
                global lvl1word726CHK
                global lvl1word727CHK
                global lvl1word728CHK
                global lvl1word729CHK
                global lvl1word730CHK
                global lvl1word731CHK
                global lvl1word732CHK
                global lvl1word733CHK
                global lvl1word734CHK
                global lvl1word735CHK
                global lvl1word736CHK
                global lvl1word737CHK
                global lvl1word738CHK
                global lvl1word739CHK
                global lvl1word740CHK
                global lvl1word741CHK
                global lvl1word742CHK
                global lvl1word743CHK
                global lvl1word744CHK
                global lvl1word745CHK
                global lvl1word746CHK
                global lvl1word747CHK
                global lvl1word748CHK
                global lvl1word749CHK
                global lvl1word750CHK
                global lvl1word751CHK
                global lvl1word752CHK
                global lvl1word753CHK
                global lvl1word754CHK
                global lvl1word755CHK
                global lvl1word756CHK
                global lvl1word757CHK
                global lvl1word758CHK
                global lvl1word759CHK
                global lvl1word760CHK
                global lvl1word761CHK
                global lvl1word762CHK
                global lvl1word763CHK
                global lvl1word764CHK
                global lvl1word765CHK
                global lvl1word766CHK
                global lvl1word767CHK
                global lvl1word768CHK
                global lvl1word769CHK
                global lvl1word770CHK
                global lvl1word771CHK
                global lvl1word772CHK
                global lvl1word773CHK
                global lvl1word774CHK
                global lvl1word775CHK
                global lvl1word776CHK
                global lvl1word777CHK
                global lvl1word778CHK
                global lvl1word779CHK
                global lvl1word780CHK
                global lvl1word781CHK
                global lvl1word782CHK
                global lvl1word783CHK
                global lvl1word784CHK
                global lvl1word785CHK
                global lvl1word786CHK
                global lvl1word787CHK
                global lvl1word788CHK
                global lvl1word789CHK
                global lvl1word790CHK
                global lvl1word791CHK
                global lvl1word792CHK
                global lvl1word793CHK
                global lvl1word794CHK
                global lvl1word795CHK
                global lvl1word796CHK
                global lvl1word797CHK
                global lvl1word798CHK
                global lvl1word799CHK
                global lvl1word800CHK
                global lvl1word801CHK
                global lvl1word800CHK
                global lvl1word801CHK
                global lvl1word802CHK
                global lvl1word803CHK
                global lvl1word804CHK
                global lvl1word805CHK
                global lvl1word806CHK
                global lvl1word807CHK
                global lvl1word808CHK
                global lvl1word809CHK
                global lvl1word810CHK
                global lvl1word811CHK
                global lvl1word812CHK
                global lvl1word813CHK
                global lvl1word814CHK
                global lvl1word815CHK
                global lvl1word816CHK
                global lvl1word817CHK
                global lvl1word818CHK
                global lvl1word819CHK
                global lvl1word820CHK
                global lvl1word821CHK
                global lvl1word822CHK
                global lvl1word823CHK
                global lvl1word824CHK
                global lvl1word825CHK
                global lvl1word826CHK
                global lvl1word827CHK
                global lvl1word828CHK
                global lvl1word829CHK
                global lvl1word830CHK
                global lvl1word831CHK
                global lvl1word832CHK
                global lvl1word833CHK
                global lvl1word834CHK
                global lvl1word835CHK
                global lvl1word836CHK
                global lvl1word837CHK
                global lvl1word838CHK
                global lvl1word839CHK
                global lvl1word840CHK
                global lvl1word841CHK
                global lvl1word842CHK
                global lvl1word843CHK
                global lvl1word844CHK
                global lvl1word845CHK
                global lvl1word846CHK
                global lvl1word847CHK
                global lvl1word848CHK
                global lvl1word849CHK
                global lvl1word850CHK
                global lvl1word851CHK
                global lvl1word852CHK
                global lvl1word853CHK
                global lvl1word854CHK
                global lvl1word855CHK
                global lvl1word856CHK
                global lvl1word857CHK
                global lvl1word858CHK
                global lvl1word859CHK
                global lvl1word860CHK
                global lvl1word861CHK
                global lvl1word862CHK
                global lvl1word863CHK
                global lvl1word864CHK
                global lvl1word865CHK
                global lvl1word866CHK
                global lvl1word867CHK
                global lvl1word868CHK
                global lvl1word869CHK
                global lvl1word870CHK
                global lvl1word871CHK
                global lvl1word872CHK
                global lvl1word873CHK
                global lvl1word874CHK
                global lvl1word875CHK
                global lvl1word876CHK
                global lvl1word877CHK
                global lvl1word878CHK
                global lvl1word879CHK
                global lvl1word880CHK
                global lvl1word881CHK
                global lvl1word882CHK
                global lvl1word883CHK
                global lvl1word884CHK
                global lvl1word885CHK
                global lvl1word886CHK
                global lvl1word887CHK
                global lvl1word888CHK
                global lvl1word889CHK
                global lvl1word890CHK
                global lvl1word891CHK
                global lvl1word892CHK
                global lvl1word893CHK
                global lvl1word894CHK
                global lvl1word895CHK
                global lvl1word896CHK
                global lvl1word897CHK
                global lvl1word898CHK
                global lvl1word899CHK
                global lvl1word900CHK
                global lvl1word901CHK
                global lvl1word902CHK
                global lvl1word903CHK
                global lvl1word904CHK
                global lvl1word905CHK
                global lvl1word906CHK
                global lvl1word907CHK
                global lvl1word908CHK
                global lvl1word909CHK
                global lvl1word910CHK
                global lvl1word911CHK
                global lvl1word912CHK
                global lvl1word913CHK
                global lvl1word914CHK
                global lvl1word915CHK
                global lvl1word916CHK
                global lvl1word917CHK
                global lvl1word918CHK
                global lvl1word919CHK
                global lvl1word920CHK
                global lvl1word921CHK
                global lvl1word922CHK
                global lvl1word923CHK
                global lvl1word924CHK
                global lvl1word925CHK
                global lvl1word926CHK
                global lvl1word927CHK
                global lvl1word928CHK
                global lvl1word929CHK
                global lvl1word930CHK
                global lvl1word931CHK
                global lvl1word932CHK
                global lvl1word933CHK
                global lvl1word934CHK
                global lvl1word935CHK
                global lvl1word936CHK
                global lvl1word937CHK
                global lvl1word938CHK
                global lvl1word939CHK
                global lvl1word940CHK
                global lvl1word941CHK
                global lvl1word942CHK
                global lvl1word943CHK
                global lvl1word944CHK
                global lvl1word945CHK
                global lvl1word946CHK
                global lvl1word947CHK
                global lvl1word948CHK
                global lvl1word949CHK
                global lvl1word950CHK
                global lvl1word951CHK
                global lvl1word952CHK
                global lvl1word953CHK
                global lvl1word954CHK
                global lvl1word955CHK
                global lvl1word956CHK
                global lvl1word957CHK
                global lvl1word958CHK
                global lvl1word959CHK
                global lvl1word960CHK
                global lvl1word961CHK
                global lvl1word962CHK
                global lvl1word963CHK
                global lvl1word964CHK
                global lvl1word965CHK
                global lvl1word966CHK
                global lvl1word967CHK
                global lvl1word968CHK
                global lvl1word969CHK
                global lvl1word970CHK
                global lvl1word971CHK
                global lvl1word972CHK
                global lvl1word973CHK
                global lvl1word974CHK
                global lvl1word975CHK
                global lvl1word976CHK
                global lvl1word977CHK
                global lvl1word978CHK
                global lvl1word979CHK
                global lvl1word980CHK
                global lvl1word981CHK
                global lvl1word982CHK
                global lvl1word983CHK
                global lvl1word984CHK
                global lvl1word985CHK
                global lvl1word986CHK
                global lvl1word987CHK
                global lvl1word988CHK
                global lvl1word989CHK
                global lvl1word990CHK
                global lvl1word991CHK
                global lvl1word992CHK
                global lvl1word993CHK
                global lvl1word994CHK
                global lvl1word995CHK
                global lvl1word996CHK
                global lvl1word997CHK
                global lvl1word998CHK
                global lvl1word999CHK
                global lvl1word1000CHK
                global lvl1word1001CHK
                global lvl1word1002CHK
                global lvl1word1003CHK
                global lvl1word1004CHK
                global lvl1word1005CHK
                global lvl1word1006CHK
                global lvl1word1007CHK
                global lvl1word1008CHK
                global lvl1word1009CHK
                global lvl1word1010CHK
                global lvl1word1011CHK
                global lvl1word1012CHK
                global lvl1word1013CHK
                global lvl1word1014CHK
                global lvl1word1015CHK
                global lvl1word1016CHK
                global lvl1word1017CHK
                global lvl1word1018CHK
                global lvl1word1019CHK
                global lvl1word1020CHK
                global lvl1word1021CHK
                global lvl1word1022CHK
                global lvl1word1023CHK
                global lvl1word1024CHK
                global lvl1word1025CHK
                global lvl1word1026CHK
                global lvl1word1027CHK
                global lvl1word1028CHK
                global lvl1word1029CHK
                global lvl1word1030CHK
                global lvl1word1031CHK
                global lvl1word1032CHK
                global lvl1word1033CHK
                global lvl1word1034CHK
                global lvl1word1035CHK
                global lvl1word1036CHK
                global lvl1word1037CHK
                global lvl1word1038CHK
                global lvl1word1039CHK
                global lvl1word1040CHK
                global lvl1word1041CHK
                global lvl1word1042CHK
                global lvl1word1043CHK
                global lvl1word1044CHK
                global lvl1word1045CHK
                global lvl1word1047CHK
                global lvl1word1048CHK
                global lvl1word1049CHK
                global lvl1word1050CHK
                global lvl1word1051CHK
                global lvl1word1052CHK
                global lvl1word1053CHK
                global lvl1word1054CHK
                global lvl1word1055CHK
                global lvl1word1056CHK
                global lvl1word1057CHK
                global lvl1word1058CHK
                global lvl1word1059CHK
                global lvl1word1060CHK
                global lvl1word1061CHK
                global lvl1word1062CHK
                global lvl1word1063CHK
                global lvl1word1064CHK
                global lvl1word1065CHK
                global lvl1word1067CHK
                global lvl1word1068CHK
                global lvl1word1069CHK
                global lvl1word1070CHK
                global lvl1word1072CHK
                global lvl1word1073CHK
                global lvl1word1074CHK
                global lvl1word1075CHK
                global lvl1word1076CHK
                global lvl1word1077CHK
                global lvl1word1078CHK
                global lvl1word1079CHK
                global lvl1word1080CHK
                global lvl1word1081CHK
                global lvl1word1082CHK
                global lvl1word1083CHK
                global lvl1word1084CHK
                global lvl1word1085CHK
                global lvl1word1086CHK
                global lvl1word1087CHK
                global lvl1word1088CHK
                global lvl1word1089CHK
                global lvl1word1090CHK
                global lvl1word1091CHK
                global lvl1word1092CHK
                global lvl1word1093CHK
                global lvl1word1094CHK
                global lvl1word1095CHK
                global lvl1word1096CHK
                global lvl1word1097CHK
                global lvl1word1098CHK
                global lvl1word1099CHK
                global lvl1word1100CHK
                global lvl1word1101CHK
                global lvl1word1103CHK
                global lvl1word1104CHK
                global lvl1word1105CHK
                global lvl1word1106CHK
                global lvl1word1108CHK
                global lvl1word1109CHK
                global lvl1word1110CHK
                global lvl1word1111CHK
                global lvl1word1112CHK
                global lvl1word1113CHK
                global lvl1word1116CHK
                global lvl1word1117CHK
                global lvl1word1118CHK
                global lvl1word1119CHK
                global lvl1word1120CHK
                global lvl1word1121CHK
                global lvl1word1122CHK
                global lvl1word1123CHK
                global lvl1word1124CHK
                global lvl1word1125CHK
                global lvl1word1126CHK
                global lvl1word1127CHK
                global lvl1word1128CHK
                global lvl1word1129CHK
                global lvl1word1130CHK
                global lvl1word1131CHK
                global lvl1word1132CHK
                global lvl1word1133CHK
                global lvl1word1134CHK
                global lvl1word1135CHK
                global lvl1word1136CHK
                global lvl1word1137CHK
                global lvl1word1138CHK
                global lvl1word1139CHK
                global lvl1word1140CHK
                global lvl1word1141CHK
                global lvl1word1142CHK
                global lvl1word1143CHK
                global lvl1word1144CHK
                global lvl1word1145CHK
                global lvl1word1146CHK
                global lvl1word1147CHK
                global lvl1word1148CHK
                global lvl1word1149CHK
                global lvl1word1150CHK
                global lvl1word1151CHK
                global lvl1word1153CHK
                global lvl1word1154CHK
                global lvl1word1155CHK
                global lvl1word1156CHK
                global lvl1word1157CHK
                global lvl1word1158CHK
                global lvl1word1159CHK
                global lvl1word1160CHK
                global lvl1word1161CHK
                global lvl1word1162CHK
                global lvl1word1163CHK
                global lvl1word1164CHK
                global lvl1word1165CHK
                global lvl1word1166CHK
                global lvl1word1167CHK
                global lvl1word1168CHK
                global lvl1word1169CHK
                global lvl1word1170CHK
                global lvl1word1171CHK
                global lvl1word1172CHK
                global lvl1word1173CHK
                global lvl1word1175CHK
                global lvl1word1176CHK
                global lvl1word1177CHK
                global lvl1word1178CHK
                global lvl1word1179CHK
                global lvl1word1180CHK
                global lvl1word1181CHK
                global lvl1word1182CHK
                global lvl1word1183CHK
                global lvl1word1184CHK
                global lvl1word1185CHK
                global lvl1word1186CHK
                global lvl1word1187CHK
                global lvl1word1188CHK
                global lvl1word1189CHK
                global lvl1word1190CHK
                global lvl1word1191CHK
                global lvl1word1192CHK
                global lvl1word1193CHK
                global lvl1word1194CHK
                global lvl1word1195CHK
                global lvl1word1196CHK
                global lvl1word1197CHK
                global lvl1word1198CHK
                global lvl1word1199CHK
                global lvl1word1200CHK
                global lvl1word1201CHK
                global lvl1word1202CHK
                global lvl1word1203CHK
                global lvl1word1204CHK
                global lvl1word1205CHK
                global lvl1word1206CHK
                global lvl1word1207CHK
                global lvl1word1208CHK
                global lvl1word1209CHK
                global lvl1word1210CHK
                global lvl1word1211CHK
                global lvl1word1212CHK
                global lvl1word1213CHK
                global lvl1word1214CHK
                global lvl1word1215CHK
                global lvl1word1216CHK
                global lvl1word1217CHK
                global lvl1word1218CHK
                global lvl1word1219CHK
                global lvl1word1220CHK
                global lvl1word1221CHK
                global lvl1word1222CHK
                global lvl1word1223CHK
                global lvl1word1224CHK
                global lvl1word1225CHK
                global lvl1word1226CHK
                global lvl1word1227CHK
                global lvl1word1228CHK
                global lvl1word1229CHK
                global lvl1word1230CHK
                global lvl1word1231CHK
                global lvl1word1232CHK
                global lvl1word1233CHK
                global lvl1word1234CHK
                global lvl1word1235CHK
                global lvl1word1236CHK
                global lvl1word1237CHK
                global lvl1word1238CHK
                global lvl1word1239CHK
                global lvl1word1240CHK
                global lvl1word1241CHK
                global lvl1word1242CHK
                global lvl1word1243CHK
                global lvl1word1244CHK
                global lvl1word1245CHK
                global lvl1word1246CHK
                global lvl1word1247CHK
                global lvl1word1248CHK
                global lvl1word1249CHK
                global lvl1word1250CHK
                global lvl1word1251CHK
                global lvl1word1253CHK
                global lvl1word1254CHK
                global lvl1word1255CHK
                global lvl1word1256CHK
                global lvl1word1257CHK
                global lvl1word1258CHK
                global lvl1word1259CHK
                global lvl1word1260CHK
                global lvl1word1261CHK
                global lvl1word1262CHK
                global lvl1word1263CHK
                global lvl1word1264CHK            
                global letterBlank




            
                
                if (wordList == lvl1word1 and lvl1word1CHK ==0 and letterBlank==False) or (wordList == lvl1word2 and lvl1word2CHK ==0 and letterBlank==False) or (wordList == lvl1word3 and lvl1word3CHK ==0 and letterBlank==False) or (wordList == lvl1word4 and lvl1word4CHK ==0 and letterBlank==False) or (wordList == lvl1word5 and lvl1word5CHK ==0 and letterBlank==False) or (wordList == lvl1word6 and lvl1word6CHK ==0 and letterBlank==False) or (wordList == lvl1word7 and lvl1word7CHK ==0 and letterBlank==False) or (wordList == lvl1word8 and lvl1word8CHK ==0 and letterBlank==False) or (wordList == lvl1word9 and lvl1word9CHK ==0 and letterBlank==False) or (wordList == lvl1word10 and lvl1word10CHK ==0 and letterBlank==False) or (wordList == lvl1word11 and lvl1word11CHK ==0 and letterBlank==False) or (wordList == lvl1word12 and lvl1word12CHK ==0 and letterBlank==False) or (wordList == lvl1word13 and lvl1word13CHK ==0 and letterBlank==False) or (wordList == lvl1word14 and lvl1word14CHK ==0 and letterBlank==False) or (wordList == lvl1word15 and lvl1word15CHK ==0 and letterBlank==False) or (wordList == lvl1word16 and lvl1word16CHK ==0 and letterBlank==False) or (wordList == lvl1word17 and lvl1word17CHK ==0 and letterBlank==False) or (wordList == lvl1word18 and lvl1word18CHK ==0 and letterBlank==False) or (wordList == lvl1word19 and lvl1word19CHK ==0 and letterBlank==False) or (wordList == lvl1word20 and lvl1word20CHK ==0 and letterBlank==False) or (wordList == lvl1word21 and lvl1word21CHK ==0 and letterBlank==False) or (wordList == lvl1word22 and lvl1word22CHK ==0 and letterBlank==False) or (wordList == lvl1word23 and lvl1word23CHK ==0 and letterBlank==False) or (wordList == lvl1word24 and lvl1word24CHK ==0 and letterBlank==False) or (wordList == lvl1word25 and lvl1word25CHK ==0 and letterBlank==False) or (wordList == lvl1word26 and lvl1word26CHK ==0 and letterBlank==False) or (wordList == lvl1word27 and lvl1word27CHK ==0 and letterBlank==False) or (wordList == lvl1word28 and lvl1word28CHK ==0 and letterBlank==False) or (wordList == lvl1word29 and lvl1word29CHK ==0 and letterBlank==False) or (wordList == lvl1word30 and lvl1word30CHK ==0 and letterBlank==False) or (wordList == lvl1word31 and lvl1word31CHK ==0 and letterBlank==False) or (wordList == lvl1word32 and lvl1word32CHK ==0 and letterBlank==False) or (wordList == lvl1word33 and lvl1word33CHK ==0 and letterBlank==False) or (wordList == lvl1word34 and lvl1word34CHK ==0 and letterBlank==False) or (wordList == lvl1word35 and lvl1word35CHK ==0 and letterBlank==False) or (wordList == lvl1word36 and lvl1word36CHK ==0 and letterBlank==False) or (wordList == lvl1word37 and lvl1word37CHK ==0 and letterBlank==False) or (wordList == lvl1word38 and lvl1word38CHK ==0 and letterBlank==False) or (wordList == lvl1word39 and lvl1word39CHK ==0 and letterBlank==False) or (wordList == lvl1word40 and lvl1word40CHK ==0 and letterBlank==False) or (wordList == lvl1word41 and lvl1word41CHK ==0 and letterBlank==False) or (wordList == lvl1word42 and lvl1word42CHK ==0 and letterBlank==False) or (wordList == lvl1word43 and lvl1word43CHK ==0 and letterBlank==False) or (wordList == lvl1word44 and lvl1word44CHK ==0 and letterBlank==False) or (wordList == lvl1word45 and lvl1word45CHK ==0 and letterBlank==False) or (wordList == lvl1word46 and lvl1word46CHK ==0 and letterBlank==False) or (wordList == lvl1word47 and lvl1word47CHK ==0 and letterBlank==False) or (wordList == lvl1word48 and lvl1word48CHK ==0 and letterBlank==False) or (wordList == lvl1word49 and lvl1word49CHK ==0 and letterBlank==False) or (wordList == lvl1word50 and lvl1word50CHK ==0 and letterBlank==False) or (wordList == lvl1word51 and lvl1word51CHK ==0 and letterBlank==False) or (wordList == lvl1word52 and lvl1word52CHK ==0 and letterBlank==False) or (wordList == lvl1word53 and lvl1word53CHK ==0 and letterBlank==False) or (wordList == lvl1word54 and lvl1word54CHK ==0 and letterBlank==False) or (wordList == lvl1word55 and lvl1word55CHK ==0 and letterBlank==False) or (wordList == lvl1word56 and lvl1word56CHK ==0 and letterBlank==False) or (wordList == lvl1word57 and lvl1word57CHK ==0 and letterBlank==False) or (wordList == lvl1word58 and lvl1word58CHK ==0 and letterBlank==False) or (wordList == lvl1word59 and lvl1word59CHK ==0 and letterBlank==False) or (wordList == lvl1word60 and lvl1word60CHK ==0 and letterBlank==False) or (wordList == lvl1word61 and lvl1word61CHK ==0 and letterBlank==False) or (wordList == lvl1word62 and lvl1word62CHK ==0 and letterBlank==False) or (wordList == lvl1word63 and lvl1word63CHK ==0 and letterBlank==False) or (wordList == lvl1word64 and lvl1word64CHK ==0 and letterBlank==False) or (wordList == lvl1word65 and lvl1word65CHK ==0 and letterBlank==False) or (wordList == lvl1word66 and lvl1word66CHK ==0 and letterBlank==False) or (wordList == lvl1word67 and lvl1word67CHK ==0 and letterBlank==False) or (wordList == lvl1word68 and lvl1word68CHK ==0 and letterBlank==False) or (wordList == lvl1word69 and lvl1word69CHK ==0 and letterBlank==False) or (wordList == lvl1word70 and lvl1word70CHK ==0 and letterBlank==False) or (wordList == lvl1word71 and lvl1word71CHK ==0 and letterBlank==False) or (wordList == lvl1word72 and lvl1word72CHK ==0 and letterBlank==False) or (wordList == lvl1word73 and lvl1word73CHK ==0 and letterBlank==False) or (wordList == lvl1word74 and lvl1word74CHK ==0 and letterBlank==False) or (wordList == lvl1word75 and lvl1word75CHK ==0 and letterBlank==False) or (wordList == lvl1word76 and lvl1word76CHK ==0 and letterBlank==False) or (wordList == lvl1word77 and lvl1word77CHK ==0 and letterBlank==False) or (wordList == lvl1word78 and lvl1word78CHK ==0 and letterBlank==False) or (wordList == lvl1word79 and lvl1word79CHK ==0 and letterBlank==False) or (wordList == lvl1word80 and lvl1word80CHK ==0 and letterBlank==False) or (wordList == lvl1word81 and lvl1word81CHK ==0 and letterBlank==False) or (wordList == lvl1word82 and lvl1word82CHK ==0 and letterBlank==False) or (wordList == lvl1word83 and lvl1word83CHK ==0 and letterBlank==False) or (wordList == lvl1word84 and lvl1word84CHK ==0 and letterBlank==False) or (wordList == lvl1word85 and lvl1word85CHK ==0 and letterBlank==False) or (wordList == lvl1word86 and lvl1word86CHK ==0 and letterBlank==False) or (wordList == lvl1word87 and lvl1word87CHK ==0 and letterBlank==False) or (wordList == lvl1word88 and lvl1word88CHK ==0 and letterBlank==False) or (wordList == lvl1word89 and lvl1word89CHK ==0 and letterBlank==False) or (wordList == lvl1word90 and lvl1word90CHK ==0 and letterBlank==False) or (wordList == lvl1word91 and lvl1word91CHK ==0 and letterBlank==False) or (wordList == lvl1word92 and lvl1word92CHK ==0 and letterBlank==False) or (wordList == lvl1word93 and lvl1word93CHK ==0 and letterBlank==False) or (wordList == lvl1word94 and lvl1word94CHK ==0 and letterBlank==False) or (wordList == lvl1word95 and lvl1word95CHK ==0 and letterBlank==False) or (wordList == lvl1word96 and lvl1word96CHK ==0 and letterBlank==False) or (wordList == lvl1word97 and lvl1word97CHK ==0 and letterBlank==False) or (wordList == lvl1word98 and lvl1word98CHK ==0 and letterBlank==False) or (wordList == lvl1word99 and lvl1word99CHK ==0 and letterBlank==False) or (wordList == lvl1word100 and lvl1word100CHK ==0 and letterBlank==False) or (wordList == lvl1word101 and lvl1word101CHK ==0 and letterBlank==False) or (wordList == lvl1word102 and lvl1word102CHK ==0 and letterBlank==False) or (wordList == lvl1word103 and lvl1word103CHK ==0 and letterBlank==False) or (wordList == lvl1word104 and lvl1word104CHK ==0 and letterBlank==False) or (wordList == lvl1word105 and lvl1word105CHK ==0 and letterBlank==False) or (wordList == lvl1word106 and lvl1word106CHK ==0 and letterBlank==False) or (wordList == lvl1word107 and lvl1word107CHK ==0 and letterBlank==False) or (wordList == lvl1word108 and lvl1word108CHK ==0 and letterBlank==False) or (wordList == lvl1word109 and lvl1word109CHK ==0 and letterBlank==False) or (wordList == lvl1word110 and lvl1word110CHK ==0 and letterBlank==False) or (wordList == lvl1word111 and lvl1word111CHK ==0 and letterBlank==False) or (wordList == lvl1word112 and lvl1word112CHK ==0 and letterBlank==False) or (wordList == lvl1word113 and lvl1word113CHK ==0 and letterBlank==False) or (wordList == lvl1word114 and lvl1word114CHK ==0 and letterBlank==False) or (wordList == lvl1word115 and lvl1word115CHK ==0 and letterBlank==False) or (wordList == lvl1word116 and lvl1word116CHK ==0 and letterBlank==False) or (wordList == lvl1word117 and lvl1word117CHK ==0 and letterBlank==False) or (wordList == lvl1word118 and lvl1word118CHK ==0 and letterBlank==False) or (wordList == lvl1word119 and lvl1word119CHK ==0 and letterBlank==False) or (wordList == lvl1word120 and lvl1word120CHK ==0 and letterBlank==False) or (wordList == lvl1word121 and lvl1word121CHK ==0 and letterBlank==False) or (wordList == lvl1word122 and lvl1word122CHK ==0 and letterBlank==False) or (wordList == lvl1word123 and lvl1word123CHK ==0 and letterBlank==False) or (wordList == lvl1word124 and lvl1word124CHK ==0 and letterBlank==False) or (wordList == lvl1word125 and lvl1word125CHK ==0 and letterBlank==False) or (wordList == lvl1word126 and lvl1word126CHK ==0 and letterBlank==False) or (wordList == lvl1word127 and lvl1word127CHK ==0 and letterBlank==False) or (wordList == lvl1word128 and lvl1word128CHK ==0 and letterBlank==False) or (wordList == lvl1word129 and lvl1word129CHK ==0 and letterBlank==False) or (wordList == lvl1word130 and lvl1word130CHK ==0 and letterBlank==False) or (wordList == lvl1word131 and lvl1word131CHK ==0 and letterBlank==False) or (wordList == lvl1word132 and lvl1word132CHK ==0 and letterBlank==False) or (wordList == lvl1word133 and lvl1word133CHK ==0 and letterBlank==False) or (wordList == lvl1word134 and lvl1word134CHK ==0 and letterBlank==False) or (wordList == lvl1word135 and lvl1word135CHK ==0 and letterBlank==False) or (wordList == lvl1word136 and lvl1word136CHK ==0 and letterBlank==False) or (wordList == lvl1word137 and lvl1word137CHK ==0 and letterBlank==False) or (wordList == lvl1word138 and lvl1word138CHK ==0 and letterBlank==False) or (wordList == lvl1word139 and lvl1word139CHK ==0 and letterBlank==False) or (wordList == lvl1word140 and lvl1word140CHK ==0 and letterBlank==False) or (wordList == lvl1word141 and lvl1word141CHK ==0 and letterBlank==False) or (wordList == lvl1word142 and lvl1word142CHK ==0 and letterBlank==False) or (wordList == lvl1word143 and lvl1word143CHK ==0 and letterBlank==False) or (wordList == lvl1word144 and lvl1word144CHK ==0 and letterBlank==False) or (wordList == lvl1word145 and lvl1word145CHK ==0 and letterBlank==False) or (wordList == lvl1word146 and lvl1word146CHK ==0 and letterBlank==False) or (wordList == lvl1word147 and lvl1word147CHK ==0 and letterBlank==False) or (wordList == lvl1word148 and lvl1word148CHK ==0 and letterBlank==False) or (wordList == lvl1word149 and lvl1word149CHK ==0 and letterBlank==False) or (wordList == lvl1word150 and lvl1word150CHK ==0 and letterBlank==False) or (wordList == lvl1word151 and lvl1word151CHK ==0 and letterBlank==False) or (wordList == lvl1word152 and lvl1word152CHK ==0 and letterBlank==False) or (wordList == lvl1word153 and lvl1word153CHK ==0 and letterBlank==False) or (wordList == lvl1word154 and lvl1word154CHK ==0 and letterBlank==False) or (wordList == lvl1word155 and lvl1word155CHK ==0 and letterBlank==False) or (wordList == lvl1word156 and lvl1word156CHK ==0 and letterBlank==False) or (wordList == lvl1word157 and lvl1word157CHK ==0 and letterBlank==False) or (wordList == lvl1word158 and lvl1word158CHK ==0 and letterBlank==False) or (wordList == lvl1word159 and lvl1word159CHK ==0 and letterBlank==False) or (wordList == lvl1word160 and lvl1word160CHK ==0 and letterBlank==False) or (wordList == lvl1word161 and lvl1word161CHK ==0 and letterBlank==False) or (wordList == lvl1word162 and lvl1word162CHK ==0 and letterBlank==False) or (wordList == lvl1word163 and lvl1word163CHK ==0 and letterBlank==False) or (wordList == lvl1word164 and lvl1word164CHK ==0 and letterBlank==False) or (wordList == lvl1word165 and lvl1word165CHK ==0 and letterBlank==False) or (wordList == lvl1word166 and lvl1word166CHK ==0 and letterBlank==False) or (wordList == lvl1word167 and lvl1word167CHK ==0 and letterBlank==False) or (wordList == lvl1word168 and lvl1word168CHK ==0 and letterBlank==False) or (wordList == lvl1word169 and lvl1word169CHK ==0 and letterBlank==False) or (wordList == lvl1word170 and lvl1word170CHK ==0 and letterBlank==False) or (wordList == lvl1word171 and lvl1word171CHK ==0 and letterBlank==False) or (wordList == lvl1word172 and lvl1word172CHK ==0 and letterBlank==False) or (wordList == lvl1word173 and lvl1word173CHK ==0 and letterBlank==False) or (wordList == lvl1word174 and lvl1word174CHK ==0 and letterBlank==False) or (wordList == lvl1word175 and lvl1word175CHK ==0 and letterBlank==False) or (wordList == lvl1word176 and lvl1word176CHK ==0 and letterBlank==False) or (wordList == lvl1word177 and lvl1word177CHK ==0 and letterBlank==False) or (wordList == lvl1word178 and lvl1word178CHK ==0 and letterBlank==False) or (wordList == lvl1word179 and lvl1word179CHK ==0 and letterBlank==False) or (wordList == lvl1word180 and lvl1word180CHK ==0 and letterBlank==False) or (wordList == lvl1word181 and lvl1word181CHK ==0 and letterBlank==False) or (wordList == lvl1word182 and lvl1word182CHK ==0 and letterBlank==False) or (wordList == lvl1word183 and lvl1word183CHK ==0 and letterBlank==False) or (wordList == lvl1word184 and lvl1word184CHK ==0 and letterBlank==False) or (wordList == lvl1word185 and lvl1word185CHK ==0 and letterBlank==False) or (wordList == lvl1word186 and lvl1word186CHK ==0 and letterBlank==False) or (wordList == lvl1word187 and lvl1word187CHK ==0 and letterBlank==False) or (wordList == lvl1word188 and lvl1word188CHK ==0 and letterBlank==False) or (wordList == lvl1word189 and lvl1word189CHK ==0 and letterBlank==False) or (wordList == lvl1word190 and lvl1word190CHK ==0 and letterBlank==False) or (wordList == lvl1word191 and lvl1word191CHK ==0 and letterBlank==False) or (wordList == lvl1word192 and lvl1word192CHK ==0 and letterBlank==False) or (wordList == lvl1word193 and lvl1word193CHK ==0 and letterBlank==False) or (wordList == lvl1word194 and lvl1word194CHK ==0 and letterBlank==False) or (wordList == lvl1word195 and lvl1word195CHK ==0 and letterBlank==False) or (wordList == lvl1word196 and lvl1word196CHK ==0 and letterBlank==False) or (wordList == lvl1word197 and lvl1word197CHK ==0 and letterBlank==False) or (wordList == lvl1word198 and lvl1word198CHK ==0 and letterBlank==False) or (wordList == lvl1word199 and lvl1word199CHK ==0 and letterBlank==False) or (wordList == lvl1word200 and lvl1word200CHK ==0 and letterBlank==False) or (wordList == lvl1word201 and lvl1word201CHK ==0 and letterBlank==False) or (wordList == lvl1word202 and lvl1word202CHK ==0 and letterBlank==False) or (wordList == lvl1word203 and lvl1word203CHK ==0 and letterBlank==False) or (wordList == lvl1word204 and lvl1word204CHK ==0 and letterBlank==False) or (wordList == lvl1word205 and lvl1word205CHK ==0 and letterBlank==False) or (wordList == lvl1word206 and lvl1word206CHK ==0 and letterBlank==False) or (wordList == lvl1word207 and lvl1word207CHK ==0 and letterBlank==False) or (wordList == lvl1word208 and lvl1word208CHK ==0 and letterBlank==False) or (wordList == lvl1word209 and lvl1word209CHK ==0 and letterBlank==False) or (wordList == lvl1word210 and lvl1word210CHK ==0 and letterBlank==False) or (wordList == lvl1word211 and lvl1word211CHK ==0 and letterBlank==False) or (wordList == lvl1word212 and lvl1word212CHK ==0 and letterBlank==False) or (wordList == lvl1word213 and lvl1word213CHK ==0 and letterBlank==False) or (wordList == lvl1word214 and lvl1word214CHK ==0 and letterBlank==False) or (wordList == lvl1word215 and lvl1word215CHK ==0 and letterBlank==False) or (wordList == lvl1word216 and lvl1word216CHK ==0 and letterBlank==False) or (wordList == lvl1word217 and lvl1word217CHK ==0 and letterBlank==False) or (wordList == lvl1word218 and lvl1word218CHK ==0 and letterBlank==False) or (wordList == lvl1word219 and lvl1word219CHK ==0 and letterBlank==False) or (wordList == lvl1word220 and lvl1word220CHK ==0 and letterBlank==False) or (wordList == lvl1word221 and lvl1word221CHK ==0 and letterBlank==False) or (wordList == lvl1word222 and lvl1word222CHK ==0 and letterBlank==False) or (wordList == lvl1word223 and lvl1word223CHK ==0 and letterBlank==False) or (wordList == lvl1word224 and lvl1word224CHK ==0 and letterBlank==False) or (wordList == lvl1word225 and lvl1word225CHK ==0 and letterBlank==False) or (wordList == lvl1word226 and lvl1word226CHK ==0 and letterBlank==False) or (wordList == lvl1word227 and lvl1word227CHK ==0 and letterBlank==False) or (wordList == lvl1word228 and lvl1word228CHK ==0 and letterBlank==False) or (wordList == lvl1word229 and lvl1word229CHK ==0 and letterBlank==False) or (wordList == lvl1word230 and lvl1word230CHK ==0 and letterBlank==False) or (wordList == lvl1word231 and lvl1word231CHK ==0 and letterBlank==False) or (wordList == lvl1word232 and lvl1word232CHK ==0 and letterBlank==False) or (wordList == lvl1word233 and lvl1word233CHK ==0 and letterBlank==False) or (wordList == lvl1word234 and lvl1word234CHK ==0 and letterBlank==False) or (wordList == lvl1word235 and lvl1word235CHK ==0 and letterBlank==False) or (wordList == lvl1word236 and lvl1word236CHK ==0 and letterBlank==False) or (wordList == lvl1word237 and lvl1word237CHK ==0 and letterBlank==False) or (wordList == lvl1word238 and lvl1word238CHK ==0 and letterBlank==False) or (wordList == lvl1word239 and lvl1word239CHK ==0 and letterBlank==False) or (wordList == lvl1word240 and lvl1word240CHK ==0 and letterBlank==False) or (wordList == lvl1word241 and lvl1word241CHK ==0 and letterBlank==False) or (wordList == lvl1word242 and lvl1word242CHK ==0 and letterBlank==False) or (wordList == lvl1word243 and lvl1word243CHK ==0 and letterBlank==False) or (wordList == lvl1word244 and lvl1word244CHK ==0 and letterBlank==False) or (wordList == lvl1word245 and lvl1word245CHK ==0 and letterBlank==False) or (wordList == lvl1word246 and lvl1word246CHK ==0 and letterBlank==False) or (wordList == lvl1word247 and lvl1word247CHK ==0 and letterBlank==False) or (wordList == lvl1word248 and lvl1word248CHK ==0 and letterBlank==False) or (wordList == lvl1word249 and lvl1word249CHK ==0 and letterBlank==False) or (wordList == lvl1word250 and lvl1word250CHK ==0 and letterBlank==False) or (wordList == lvl1word251 and lvl1word251CHK ==0 and letterBlank==False) or (wordList == lvl1word252 and lvl1word252CHK ==0 and letterBlank==False) or (wordList == lvl1word253 and lvl1word253CHK ==0 and letterBlank==False) or (wordList == lvl1word254 and lvl1word254CHK ==0 and letterBlank==False) or (wordList == lvl1word255 and lvl1word255CHK ==0 and letterBlank==False) or (wordList == lvl1word256 and lvl1word256CHK ==0 and letterBlank==False) or (wordList == lvl1word257 and lvl1word257CHK ==0 and letterBlank==False) or (wordList == lvl1word258 and lvl1word258CHK ==0 and letterBlank==False) or (wordList == lvl1word259 and lvl1word259CHK ==0 and letterBlank==False)  or (wordList == lvl1word260 and lvl1word260CHK ==0 and letterBlank==False)  or (wordList == lvl1word261 and lvl1word261CHK ==0 and letterBlank==False)  or (wordList == lvl1word262 and lvl1word262CHK ==0 and letterBlank==False)  or (wordList == lvl1word263 and lvl1word263CHK ==0 and letterBlank==False)  or (wordList == lvl1word264 and lvl1word264CHK ==0 and letterBlank==False)  or (wordList == lvl1word265 and lvl1word265CHK ==0 and letterBlank==False)  or (wordList == lvl1word266 and lvl1word266CHK ==0 and letterBlank==False)  or (wordList == lvl1word267 and lvl1word267CHK ==0 and letterBlank==False)   or (wordList == lvl1word268 and lvl1word268CHK ==0 and letterBlank==False)   or (wordList == lvl1word269 and lvl1word269CHK ==0 and letterBlank==False)   or (wordList == lvl1word270 and lvl1word270CHK ==0 and letterBlank==False)   or (wordList == lvl1word271 and lvl1word271CHK ==0 and letterBlank==False)  or (wordList == lvl1word272 and lvl1word272CHK ==0 and letterBlank==False)  or (wordList == lvl1word273 and lvl1word273CHK ==0 and letterBlank==False)  or (wordList == lvl1word274 and lvl1word274CHK ==0 and letterBlank==False)  or (wordList == lvl1word275 and lvl1word275CHK ==0 and letterBlank==False)  or (wordList == lvl1word276 and lvl1word276CHK ==0 and letterBlank==False)   or (wordList == lvl1word277 and lvl1word277CHK ==0 and letterBlank==False)  or (wordList == lvl1word278 and lvl1word278CHK ==0 and letterBlank==False)  or (wordList == lvl1word279 and lvl1word279CHK ==0 and letterBlank==False)  or (wordList == lvl1word280 and lvl1word280CHK ==0 and letterBlank==False)  or (wordList == lvl1word281 and lvl1word281CHK ==0 and letterBlank==False)  or (wordList == lvl1word282 and lvl1word282CHK ==0 and letterBlank==False)  or (wordList == lvl1word283 and lvl1word283CHK ==0 and letterBlank==False)  or (wordList == lvl1word284 and lvl1word284CHK ==0 and letterBlank==False)  or (wordList == lvl1word285 and lvl1word285CHK ==0 and letterBlank==False)  or (wordList == lvl1word286 and lvl1word286CHK ==0 and letterBlank==False)  or (wordList == lvl1word287 and lvl1word287CHK ==0 and letterBlank==False)  or (wordList == lvl1word288 and lvl1word288CHK ==0 and letterBlank==False)  or (wordList == lvl1word289 and lvl1word289CHK ==0 and letterBlank==False)  or (wordList == lvl1word290 and lvl1word290CHK ==0 and letterBlank==False)  or (wordList == lvl1word291 and lvl1word291CHK ==0 and letterBlank==False)  or (wordList == lvl1word292 and lvl1word292CHK ==0 and letterBlank==False)  or (wordList == lvl1word293 and lvl1word293CHK ==0 and letterBlank==False)  or (wordList == lvl1word294 and lvl1word294CHK ==0 and letterBlank==False)  or (wordList == lvl1word295 and lvl1word295CHK ==0 and letterBlank==False)  or (wordList == lvl1word296 and lvl1word296CHK ==0 and letterBlank==False)  or (wordList == lvl1word297 and lvl1word297CHK ==0 and letterBlank==False)  or (wordList == lvl1word298 and lvl1word298CHK ==0 and letterBlank==False)  or (wordList == lvl1word299 and lvl1word299CHK ==0 and letterBlank==False)  or (wordList == lvl1word300 and lvl1word300CHK ==0 and letterBlank==False)  or (wordList == lvl1word301 and lvl1word301CHK ==0 and letterBlank==False)  or (wordList == lvl1word302 and lvl1word302CHK ==0 and letterBlank==False)  or (wordList == lvl1word303 and lvl1word303CHK ==0 and letterBlank==False)  or (wordList == lvl1word304 and lvl1word304CHK ==0 and letterBlank==False)  or (wordList == lvl1word305 and lvl1word305CHK ==0 and letterBlank==False)  or (wordList == lvl1word306 and lvl1word306CHK ==0 and letterBlank==False)  or (wordList == lvl1word307 and lvl1word307CHK ==0 and letterBlank==False)  or (wordList == lvl1word308 and lvl1word308CHK ==0 and letterBlank==False)  or (wordList == lvl1word309 and lvl1word309CHK ==0 and letterBlank==False)  or (wordList == lvl1word310 and lvl1word310CHK ==0 and letterBlank==False)  or (wordList == lvl1word311 and lvl1word311CHK ==0 and letterBlank==False)  or (wordList == lvl1word312 and lvl1word312CHK ==0 and letterBlank==False)  or (wordList == lvl1word313 and lvl1word313CHK ==0 and letterBlank==False)  or (wordList == lvl1word314 and lvl1word314CHK ==0 and letterBlank==False)  or (wordList == lvl1word315 and lvl1word315CHK ==0 and letterBlank==False)  or (wordList == lvl1word316 and lvl1word316CHK ==0 and letterBlank==False)  or (wordList == lvl1word317 and lvl1word317CHK ==0 and letterBlank==False)  or (wordList == lvl1word318 and lvl1word318CHK ==0 and letterBlank==False)  or (wordList == lvl1word319 and lvl1word319CHK ==0 and letterBlank==False)  or (wordList == lvl1word320 and lvl1word320CHK ==0 and letterBlank==False)  or (wordList == lvl1word321 and lvl1word321CHK ==0 and letterBlank==False)  or (wordList == lvl1word322 and lvl1word322CHK ==0 and letterBlank==False)  or (wordList == lvl1word323 and lvl1word323CHK ==0 and letterBlank==False)  or (wordList == lvl1word324 and lvl1word324CHK ==0 and letterBlank==False)  or (wordList == lvl1word325 and lvl1word325CHK ==0 and letterBlank==False)  or (wordList == lvl1word326 and lvl1word326CHK ==0 and letterBlank==False)  or (wordList == lvl1word327 and lvl1word327CHK ==0 and letterBlank==False)  or (wordList == lvl1word328 and lvl1word328CHK ==0 and letterBlank==False)  or (wordList == lvl1word329 and lvl1word329CHK ==0 and letterBlank==False)  or (wordList == lvl1word330 and lvl1word330CHK ==0 and letterBlank==False)  or (wordList == lvl1word331 and lvl1word331CHK ==0 and letterBlank==False)  or (wordList == lvl1word332 and lvl1word332CHK ==0 and letterBlank==False)  or (wordList == lvl1word333 and lvl1word333CHK ==0 and letterBlank==False)  or (wordList == lvl1word334 and lvl1word334CHK ==0 and letterBlank==False)  or (wordList == lvl1word335 and lvl1word335CHK ==0 and letterBlank==False)  or (wordList == lvl1word336 and lvl1word336CHK ==0 and letterBlank==False)  or (wordList == lvl1word337 and lvl1word337CHK ==0 and letterBlank==False)  or (wordList == lvl1word338 and lvl1word338CHK ==0 and letterBlank==False)  or (wordList == lvl1word339 and lvl1word339CHK ==0 and letterBlank==False)  or (wordList == lvl1word340 and lvl1word340CHK ==0 and letterBlank==False)  or (wordList == lvl1word341 and lvl1word341CHK ==0 and letterBlank==False)  or (wordList == lvl1word342 and lvl1word342CHK ==0 and letterBlank==False)  or (wordList == lvl1word343 and lvl1word343CHK ==0 and letterBlank==False)  or (wordList == lvl1word344 and lvl1word344CHK ==0 and letterBlank==False)  or (wordList == lvl1word345 and lvl1word345CHK ==0 and letterBlank==False)  or (wordList == lvl1word346 and lvl1word346CHK ==0 and letterBlank==False)  or (wordList == lvl1word347 and lvl1word347CHK ==0 and letterBlank==False)  or (wordList == lvl1word348 and lvl1word348CHK ==0 and letterBlank==False)  or (wordList == lvl1word349 and lvl1word349CHK ==0 and letterBlank==False)  or (wordList == lvl1word350 and lvl1word350CHK ==0 and letterBlank==False)  or (wordList == lvl1word351 and lvl1word351CHK ==0 and letterBlank==False)  or (wordList == lvl1word352 and lvl1word352CHK ==0 and letterBlank==False)  or (wordList == lvl1word353 and lvl1word353CHK ==0 and letterBlank==False)  or (wordList == lvl1word354 and lvl1word354CHK ==0 and letterBlank==False)  or (wordList == lvl1word355 and lvl1word355CHK ==0 and letterBlank==False)  or (wordList == lvl1word356 and lvl1word356CHK ==0 and letterBlank==False)  or (wordList == lvl1word357 and lvl1word357CHK ==0 and letterBlank==False)  or (wordList == lvl1word358 and lvl1word358CHK ==0 and letterBlank==False)  or (wordList == lvl1word359 and lvl1word359CHK ==0 and letterBlank==False)  or (wordList == lvl1word360 and lvl1word360CHK ==0 and letterBlank==False)  or (wordList == lvl1word361 and lvl1word361CHK ==0 and letterBlank==False)  or (wordList == lvl1word362 and lvl1word362CHK ==0 and letterBlank==False)  or (wordList == lvl1word363 and lvl1word363CHK ==0 and letterBlank==False)  or (wordList == lvl1word364 and lvl1word364CHK ==0 and letterBlank==False)  or (wordList == lvl1word365 and lvl1word365CHK ==0 and letterBlank==False)  or (wordList == lvl1word366 and lvl1word366CHK ==0 and letterBlank==False)  or (wordList == lvl1word367 and lvl1word367CHK ==0 and letterBlank==False)  or (wordList == lvl1word368 and lvl1word368CHK ==0 and letterBlank==False)  or (wordList == lvl1word369 and lvl1word369CHK ==0 and letterBlank==False)  or (wordList == lvl1word370 and lvl1word370CHK ==0 and letterBlank==False)   or (wordList == lvl1word371 and lvl1word371CHK ==0 and letterBlank==False)  or (wordList == lvl1word372 and lvl1word372CHK ==0 and letterBlank==False)  or (wordList == lvl1word373 and lvl1word373CHK ==0 and letterBlank==False)  or (wordList == lvl1word374 and lvl1word374CHK ==0 and letterBlank==False)  or (wordList == lvl1word375 and lvl1word375CHK ==0 and letterBlank==False)  or (wordList == lvl1word376 and lvl1word376CHK ==0 and letterBlank==False)  or (wordList == lvl1word377 and lvl1word377CHK ==0 and letterBlank==False)  or (wordList == lvl1word378 and lvl1word378CHK ==0 and letterBlank==False)  or (wordList == lvl1word379 and lvl1word379CHK ==0 and letterBlank==False)  or (wordList == lvl1word380 and lvl1word380CHK ==0 and letterBlank==False)   or (wordList == lvl1word381 and lvl1word381CHK ==0 and letterBlank==False)  or (wordList == lvl1word382 and lvl1word382CHK ==0 and letterBlank==False)  or (wordList == lvl1word383 and lvl1word383CHK ==0 and letterBlank==False)  or (wordList == lvl1word384 and lvl1word384CHK ==0 and letterBlank==False)  or (wordList == lvl1word385 and lvl1word385CHK ==0 and letterBlank==False)  or (wordList == lvl1word386 and lvl1word386CHK ==0 and letterBlank==False)  or (wordList == lvl1word387 and lvl1word387CHK ==0 and letterBlank==False)  or (wordList == lvl1word388 and lvl1word388CHK ==0 and letterBlank==False)  or (wordList == lvl1word389 and lvl1word389CHK ==0 and letterBlank==False)  or (wordList == lvl1word390 and lvl1word390CHK ==0 and letterBlank==False)  or (wordList == lvl1word391 and lvl1word391CHK ==0 and letterBlank==False)  or (wordList == lvl1word392 and lvl1word392CHK ==0 and letterBlank==False)  or (wordList == lvl1word393 and lvl1word393CHK ==0 and letterBlank==False)  or (wordList == lvl1word394 and lvl1word394CHK ==0 and letterBlank==False)  or (wordList == lvl1word395 and lvl1word395CHK ==0 and letterBlank==False)  or (wordList == lvl1word396 and lvl1word396CHK ==0 and letterBlank==False)  or (wordList == lvl1word397 and lvl1word397CHK ==0 and letterBlank==False)  or (wordList == lvl1word398 and lvl1word398CHK ==0 and letterBlank==False)  or (wordList == lvl1word399 and lvl1word399CHK ==0 and letterBlank==False)    or (wordList == lvl1word400 and lvl1word400CHK ==0 and letterBlank==False)  or (wordList == lvl1word401 and lvl1word401CHK ==0 and letterBlank==False)  or (wordList == lvl1word402 and lvl1word402CHK ==0 and letterBlank==False)  or (wordList == lvl1word403 and lvl1word403CHK ==0 and letterBlank==False)  or (wordList == lvl1word404 and lvl1word404CHK ==0 and letterBlank==False)  or (wordList == lvl1word405 and lvl1word405CHK ==0 and letterBlank==False)  or (wordList == lvl1word406 and lvl1word406CHK ==0 and letterBlank==False)  or (wordList == lvl1word407 and lvl1word407CHK ==0 and letterBlank==False)  or (wordList == lvl1word408 and lvl1word408CHK ==0 and letterBlank==False)  or (wordList == lvl1word409 and lvl1word409CHK ==0 and letterBlank==False)  or (wordList == lvl1word410 and lvl1word410CHK ==0 and letterBlank==False)  or (wordList == lvl1word411 and lvl1word411CHK ==0 and letterBlank==False)  or (wordList == lvl1word412 and lvl1word412CHK ==0 and letterBlank==False)  or (wordList == lvl1word413 and lvl1word413CHK ==0 and letterBlank==False)  or (wordList == lvl1word414 and lvl1word414CHK ==0 and letterBlank==False)  or (wordList == lvl1word415 and lvl1word415CHK ==0 and letterBlank==False)  or (wordList == lvl1word416 and lvl1word416CHK ==0 and letterBlank==False)  or (wordList == lvl1word417 and lvl1word417CHK ==0 and letterBlank==False)  or (wordList == lvl1word418 and lvl1word418CHK ==0 and letterBlank==False)  or (wordList == lvl1word419 and lvl1word419CHK ==0 and letterBlank==False)  or (wordList == lvl1word420 and lvl1word420CHK ==0 and letterBlank==False)  or (wordList == lvl1word421 and lvl1word421CHK ==0 and letterBlank==False)  or (wordList == lvl1word422 and lvl1word422CHK ==0 and letterBlank==False)  or (wordList == lvl1word423 and lvl1word423CHK ==0 and letterBlank==False)  or (wordList == lvl1word424 and lvl1word424CHK ==0 and letterBlank==False)  or (wordList == lvl1word425 and lvl1word425CHK ==0 and letterBlank==False)  or (wordList == lvl1word426 and lvl1word426CHK ==0 and letterBlank==False)  or (wordList == lvl1word427 and lvl1word427CHK ==0 and letterBlank==False)  or (wordList == lvl1word428 and lvl1word428CHK ==0 and letterBlank==False)  or (wordList == lvl1word429 and lvl1word429CHK ==0 and letterBlank==False)  or (wordList == lvl1word430 and lvl1word430CHK ==0 and letterBlank==False)  or (wordList == lvl1word431 and lvl1word431CHK ==0 and letterBlank==False)  or (wordList == lvl1word432 and lvl1word432CHK ==0 and letterBlank==False)  or (wordList == lvl1word433 and lvl1word433CHK ==0 and letterBlank==False)  or (wordList == lvl1word434 and lvl1word434CHK ==0 and letterBlank==False)  or (wordList == lvl1word435 and lvl1word435CHK ==0 and letterBlank==False)  or (wordList == lvl1word436 and lvl1word436CHK ==0 and letterBlank==False)  or (wordList == lvl1word437 and lvl1word437CHK ==0 and letterBlank==False)  or (wordList == lvl1word438 and lvl1word438CHK ==0 and letterBlank==False)  or (wordList == lvl1word439 and lvl1word439CHK ==0 and letterBlank==False)  or (wordList == lvl1word440 and lvl1word440CHK ==0 and letterBlank==False)  or (wordList == lvl1word441 and lvl1word441CHK ==0 and letterBlank==False)  or (wordList == lvl1word442 and lvl1word442CHK ==0 and letterBlank==False)  or (wordList == lvl1word443 and lvl1word443CHK ==0 and letterBlank==False)  or (wordList == lvl1word444 and lvl1word444CHK ==0 and letterBlank==False)  or (wordList == lvl1word445 and lvl1word445CHK ==0 and letterBlank==False)  or (wordList == lvl1word446 and lvl1word446CHK ==0 and letterBlank==False)  or (wordList == lvl1word447 and lvl1word447CHK ==0 and letterBlank==False)  or (wordList == lvl1word448 and lvl1word448CHK ==0 and letterBlank==False)  or (wordList == lvl1word449 and lvl1word449CHK ==0 and letterBlank==False)  or (wordList == lvl1word450 and lvl1word450CHK ==0 and letterBlank==False)  or (wordList == lvl1word451 and lvl1word451CHK ==0 and letterBlank==False)  or (wordList == lvl1word452 and lvl1word452CHK ==0 and letterBlank==False)  or (wordList == lvl1word453 and lvl1word453CHK ==0 and letterBlank==False)  or (wordList == lvl1word454 and lvl1word454CHK ==0 and letterBlank==False)  or (wordList == lvl1word455 and lvl1word455CHK ==0 and letterBlank==False)  or (wordList == lvl1word456 and lvl1word456CHK ==0 and letterBlank==False)  or (wordList == lvl1word457 and lvl1word457CHK ==0 and letterBlank==False)  or (wordList == lvl1word458 and lvl1word458CHK ==0 and letterBlank==False)  or (wordList == lvl1word459 and lvl1word459CHK ==0 and letterBlank==False)  or (wordList == lvl1word460 and lvl1word460CHK ==0 and letterBlank==False)  or (wordList == lvl1word461 and lvl1word461CHK ==0 and letterBlank==False)  or (wordList == lvl1word462 and lvl1word462CHK ==0 and letterBlank==False)  or (wordList == lvl1word463 and lvl1word463CHK ==0 and letterBlank==False)  or (wordList == lvl1word464 and lvl1word464CHK ==0 and letterBlank==False)  or (wordList == lvl1word465 and lvl1word465CHK ==0 and letterBlank==False)  or (wordList == lvl1word466 and lvl1word466CHK ==0 and letterBlank==False)  or (wordList == lvl1word467 and lvl1word467CHK ==0 and letterBlank==False)  or (wordList == lvl1word468 and lvl1word468CHK ==0 and letterBlank==False)  or (wordList == lvl1word469 and lvl1word469CHK ==0 and letterBlank==False)  or (wordList == lvl1word470 and lvl1word470CHK ==0 and letterBlank==False)   or (wordList == lvl1word471 and lvl1word471CHK ==0 and letterBlank==False)  or (wordList == lvl1word472 and lvl1word472CHK ==0 and letterBlank==False)  or (wordList == lvl1word473 and lvl1word473CHK ==0 and letterBlank==False)  or (wordList == lvl1word474 and lvl1word474CHK ==0 and letterBlank==False)  or (wordList == lvl1word475 and lvl1word475CHK ==0 and letterBlank==False)  or (wordList == lvl1word476 and lvl1word476CHK ==0 and letterBlank==False)  or (wordList == lvl1word477 and lvl1word477CHK ==0 and letterBlank==False)  or (wordList == lvl1word478 and lvl1word478CHK ==0 and letterBlank==False)  or (wordList == lvl1word479 and lvl1word479CHK ==0 and letterBlank==False)  or (wordList == lvl1word480 and lvl1word480CHK ==0 and letterBlank==False)   or (wordList == lvl1word481 and lvl1word481CHK ==0 and letterBlank==False)  or (wordList == lvl1word482 and lvl1word482CHK ==0 and letterBlank==False)  or (wordList == lvl1word483 and lvl1word483CHK ==0 and letterBlank==False)  or (wordList == lvl1word484 and lvl1word484CHK ==0 and letterBlank==False)  or (wordList == lvl1word485 and lvl1word485CHK ==0 and letterBlank==False)  or (wordList == lvl1word486 and lvl1word486CHK ==0 and letterBlank==False)  or (wordList == lvl1word487 and lvl1word487CHK ==0 and letterBlank==False)  or (wordList == lvl1word488 and lvl1word488CHK ==0 and letterBlank==False)  or (wordList == lvl1word489 and lvl1word489CHK ==0 and letterBlank==False)  or (wordList == lvl1word490 and lvl1word490CHK ==0 and letterBlank==False)  or (wordList == lvl1word491 and lvl1word491CHK ==0 and letterBlank==False)  or (wordList == lvl1word492 and lvl1word492CHK ==0 and letterBlank==False)  or (wordList == lvl1word493 and lvl1word493CHK ==0 and letterBlank==False)  or (wordList == lvl1word494 and lvl1word494CHK ==0 and letterBlank==False)  or (wordList == lvl1word495 and lvl1word495CHK ==0 and letterBlank==False)  or (wordList == lvl1word496 and lvl1word496CHK ==0 and letterBlank==False)  or (wordList == lvl1word497 and lvl1word497CHK ==0 and letterBlank==False)  or (wordList == lvl1word498 and lvl1word498CHK ==0 and letterBlank==False)  or (wordList == lvl1word499 and lvl1word499CHK ==0 and letterBlank==False)  or (wordList == lvl1word500 and lvl1word500CHK ==0 and letterBlank==False)  or (wordList == lvl1word501 and lvl1word501CHK ==0 and letterBlank==False)  or (wordList == lvl1word502 and lvl1word502CHK ==0 and letterBlank==False)  or (wordList == lvl1word503 and lvl1word503CHK ==0 and letterBlank==False)  or (wordList == lvl1word504 and lvl1word504CHK ==0 and letterBlank==False)  or (wordList == lvl1word505 and lvl1word505CHK ==0 and letterBlank==False)  or (wordList == lvl1word506 and lvl1word506CHK ==0 and letterBlank==False)  or (wordList == lvl1word507 and lvl1word507CHK ==0 and letterBlank==False)  or (wordList == lvl1word508 and lvl1word508CHK ==0 and letterBlank==False)  or (wordList == lvl1word509 and lvl1word509CHK ==0 and letterBlank==False)  or (wordList == lvl1word510 and lvl1word510CHK ==0 and letterBlank==False)  or (wordList == lvl1word511 and lvl1word511CHK ==0 and letterBlank==False)  or (wordList == lvl1word512 and lvl1word512CHK ==0 and letterBlank==False)  or (wordList == lvl1word513 and lvl1word513CHK ==0 and letterBlank==False)  or (wordList == lvl1word514 and lvl1word514CHK ==0 and letterBlank==False)  or (wordList == lvl1word515 and lvl1word515CHK ==0 and letterBlank==False)  or (wordList == lvl1word516 and lvl1word516CHK ==0 and letterBlank==False)  or (wordList == lvl1word517 and lvl1word517CHK ==0 and letterBlank==False)  or (wordList == lvl1word518 and lvl1word518CHK ==0 and letterBlank==False)  or (wordList == lvl1word519 and lvl1word519CHK ==0 and letterBlank==False)  or (wordList == lvl1word520 and lvl1word520CHK ==0 and letterBlank==False)  or (wordList == lvl1word521 and lvl1word521CHK ==0 and letterBlank==False)  or (wordList == lvl1word522 and lvl1word522CHK ==0 and letterBlank==False) or (wordList == lvl1word523 and lvl1word523CHK ==0 and letterBlank==False)  or (wordList == lvl1word524 and lvl1word524CHK ==0 and letterBlank==False)  or (wordList == lvl1word525 and lvl1word525CHK ==0 and letterBlank==False)  or (wordList == lvl1word526 and lvl1word526CHK ==0 and letterBlank==False)  or (wordList == lvl1word527 and lvl1word527CHK ==0 and letterBlank==False)  or (wordList == lvl1word528 and lvl1word528CHK ==0 and letterBlank==False)  or (wordList == lvl1word529 and lvl1word529CHK ==0 and letterBlank==False)  or (wordList == lvl1word530 and lvl1word530CHK ==0 and letterBlank==False)  or (wordList == lvl1word531 and lvl1word531CHK ==0 and letterBlank==False)  or (wordList == lvl1word532 and lvl1word532CHK ==0 and letterBlank==False)  or (wordList == lvl1word533 and lvl1word533CHK ==0 and letterBlank==False)  or (wordList == lvl1word534 and lvl1word534CHK ==0 and letterBlank==False)  or (wordList == lvl1word535 and lvl1word535CHK ==0 and letterBlank==False)  or (wordList == lvl1word536 and lvl1word536CHK ==0 and letterBlank==False)  or (wordList == lvl1word537 and lvl1word537CHK ==0 and letterBlank==False)  or (wordList == lvl1word538 and lvl1word538CHK ==0 and letterBlank==False)  or (wordList == lvl1word539 and lvl1word539CHK ==0 and letterBlank==False)  or (wordList == lvl1word540 and lvl1word540CHK ==0 and letterBlank==False)  or (wordList == lvl1word541 and lvl1word541CHK ==0 and letterBlank==False)  or (wordList == lvl1word542 and lvl1word542CHK ==0 and letterBlank==False)  or (wordList == lvl1word543 and lvl1word543CHK ==0 and letterBlank==False)  or (wordList == lvl1word544 and lvl1word544CHK ==0 and letterBlank==False)  or (wordList == lvl1word545 and lvl1word545CHK ==0 and letterBlank==False)  or (wordList == lvl1word546 and lvl1word546CHK ==0 and letterBlank==False)  or (wordList == lvl1word547 and lvl1word547CHK ==0 and letterBlank==False)  or (wordList == lvl1word548 and lvl1word548CHK ==0 and letterBlank==False)  or (wordList == lvl1word549 and lvl1word549CHK ==0 and letterBlank==False)  or (wordList == lvl1word550 and lvl1word550CHK ==0 and letterBlank==False)  or (wordList == lvl1word551 and lvl1word551CHK ==0 and letterBlank==False)  or (wordList == lvl1word552 and lvl1word552CHK ==0 and letterBlank==False)  or (wordList == lvl1word553 and lvl1word553CHK ==0 and letterBlank==False)  or (wordList == lvl1word554 and lvl1word554CHK ==0 and letterBlank==False)  or (wordList == lvl1word555 and lvl1word555CHK ==0 and letterBlank==False)  or (wordList == lvl1word556 and lvl1word556CHK ==0 and letterBlank==False)  or (wordList == lvl1word557 and lvl1word557CHK ==0 and letterBlank==False)  or (wordList == lvl1word558 and lvl1word558CHK ==0 and letterBlank==False)  or (wordList == lvl1word559 and lvl1word559CHK ==0 and letterBlank==False)  or (wordList == lvl1word560 and lvl1word560CHK ==0 and letterBlank==False)  or (wordList == lvl1word561 and lvl1word561CHK ==0 and letterBlank==False)  or (wordList == lvl1word562 and lvl1word562CHK ==0 and letterBlank==False)  or (wordList == lvl1word563 and lvl1word563CHK ==0 and letterBlank==False)  or (wordList == lvl1word564 and lvl1word564CHK ==0 and letterBlank==False)  or (wordList == lvl1word565 and lvl1word565CHK ==0 and letterBlank==False)  or (wordList == lvl1word566 and lvl1word566CHK ==0 and letterBlank==False)  or (wordList == lvl1word567 and lvl1word567CHK ==0 and letterBlank==False)  or (wordList == lvl1word568 and lvl1word568CHK ==0 and letterBlank==False)  or (wordList == lvl1word569 and lvl1word569CHK ==0 and letterBlank==False)  or (wordList == lvl1word570 and lvl1word570CHK ==0 and letterBlank==False)   or (wordList == lvl1word571 and lvl1word571CHK ==0 and letterBlank==False)  or (wordList == lvl1word572 and lvl1word572CHK ==0 and letterBlank==False)  or (wordList == lvl1word573 and lvl1word573CHK ==0 and letterBlank==False)  or (wordList == lvl1word574 and lvl1word574CHK ==0 and letterBlank==False)  or (wordList == lvl1word575 and lvl1word575CHK ==0 and letterBlank==False)  or (wordList == lvl1word576 and lvl1word576CHK ==0 and letterBlank==False)  or (wordList == lvl1word577 and lvl1word577CHK ==0 and letterBlank==False)  or (wordList == lvl1word578 and lvl1word578CHK ==0 and letterBlank==False)  or (wordList == lvl1word579 and lvl1word579CHK ==0 and letterBlank==False)  or (wordList == lvl1word580 and lvl1word580CHK ==0 and letterBlank==False)   or (wordList == lvl1word581 and lvl1word581CHK ==0 and letterBlank==False)  or (wordList == lvl1word582 and lvl1word582CHK ==0 and letterBlank==False)  or (wordList == lvl1word583 and lvl1word583CHK ==0 and letterBlank==False)  or (wordList == lvl1word584 and lvl1word584CHK ==0 and letterBlank==False)  or (wordList == lvl1word585 and lvl1word585CHK ==0 and letterBlank==False)  or (wordList == lvl1word586 and lvl1word586CHK ==0 and letterBlank==False)  or (wordList == lvl1word587 and lvl1word587CHK ==0 and letterBlank==False)  or (wordList == lvl1word588 and lvl1word588CHK ==0 and letterBlank==False)  or (wordList == lvl1word589 and lvl1word589CHK ==0 and letterBlank==False)  or (wordList == lvl1word590 and lvl1word590CHK ==0 and letterBlank==False)  or (wordList == lvl1word591 and lvl1word591CHK ==0 and letterBlank==False)  or (wordList == lvl1word592 and lvl1word592CHK ==0 and letterBlank==False)  or (wordList == lvl1word593 and lvl1word593CHK ==0 and letterBlank==False)  or (wordList == lvl1word594 and lvl1word594CHK ==0 and letterBlank==False)  or (wordList == lvl1word595 and lvl1word595CHK ==0 and letterBlank==False)  or (wordList == lvl1word596 and lvl1word596CHK ==0 and letterBlank==False)  or (wordList == lvl1word597 and lvl1word597CHK ==0 and letterBlank==False)  or (wordList == lvl1word598 and lvl1word598CHK ==0 and letterBlank==False)  or (wordList == lvl1word599 and lvl1word599CHK ==0 and letterBlank==False) or (wordList == lvl1word600 and lvl1word600CHK ==0 and letterBlank==False) or (wordList == lvl1word601 and lvl1word601CHK ==0 and letterBlank==False) or (wordList == lvl1word602 and lvl1word602CHK ==0 and letterBlank==False) or (wordList == lvl1word603 and lvl1word603CHK ==0 and letterBlank==False) or (wordList == lvl1word604 and lvl1word604CHK ==0 and letterBlank==False) or (wordList == lvl1word605 and lvl1word605CHK ==0 and letterBlank==False) or (wordList == lvl1word606 and lvl1word606CHK ==0 and letterBlank==False) or (wordList == lvl1word607 and lvl1word607CHK ==0 and letterBlank==False) or (wordList == lvl1word608 and lvl1word608CHK ==0 and letterBlank==False) or (wordList == lvl1word609 and lvl1word609CHK ==0 and letterBlank==False) or (wordList == lvl1word610 and lvl1word610CHK ==0 and letterBlank==False) or (wordList == lvl1word611 and lvl1word611CHK ==0 and letterBlank==False) or (wordList == lvl1word612 and lvl1word612CHK ==0 and letterBlank==False) or (wordList == lvl1word613 and lvl1word613CHK ==0 and letterBlank==False) or (wordList == lvl1word614 and lvl1word614CHK ==0 and letterBlank==False) or (wordList == lvl1word615 and lvl1word615CHK ==0 and letterBlank==False) or (wordList == lvl1word616 and lvl1word616CHK ==0 and letterBlank==False) or (wordList == lvl1word617 and lvl1word617CHK ==0 and letterBlank==False) or (wordList == lvl1word618 and lvl1word618CHK ==0 and letterBlank==False) or (wordList == lvl1word619 and lvl1word619CHK ==0 and letterBlank==False) or (wordList == lvl1word620 and lvl1word620CHK ==0 and letterBlank==False) or (wordList == lvl1word621 and lvl1word621CHK ==0 and letterBlank==False) or (wordList == lvl1word622 and lvl1word622CHK ==0 and letterBlank==False) or (wordList == lvl1word623 and lvl1word623CHK ==0 and letterBlank==False) or (wordList == lvl1word624 and lvl1word624CHK ==0 and letterBlank==False) or (wordList == lvl1word625 and lvl1word625CHK ==0 and letterBlank==False) or (wordList == lvl1word626 and lvl1word626CHK ==0 and letterBlank==False) or (wordList == lvl1word627 and lvl1word627CHK ==0 and letterBlank==False) or (wordList == lvl1word628 and lvl1word628CHK ==0 and letterBlank==False) or (wordList == lvl1word629 and lvl1word629CHK ==0 and letterBlank==False) or (wordList == lvl1word630 and lvl1word630CHK ==0 and letterBlank==False) or (wordList == lvl1word631 and lvl1word631CHK ==0 and letterBlank==False) or (wordList == lvl1word632 and lvl1word632CHK ==0 and letterBlank==False) or (wordList == lvl1word633 and lvl1word633CHK ==0 and letterBlank==False) or (wordList == lvl1word634 and lvl1word634CHK ==0 and letterBlank==False) or (wordList == lvl1word635 and lvl1word635CHK ==0 and letterBlank==False) or (wordList == lvl1word636 and lvl1word636CHK ==0 and letterBlank==False) or (wordList == lvl1word637 and lvl1word637CHK ==0 and letterBlank==False) or (wordList == lvl1word638 and lvl1word638CHK ==0 and letterBlank==False) or (wordList == lvl1word639 and lvl1word639CHK ==0 and letterBlank==False) or (wordList == lvl1word640 and lvl1word640CHK ==0 and letterBlank==False) or (wordList == lvl1word641 and lvl1word641CHK ==0 and letterBlank==False) or (wordList == lvl1word642 and lvl1word642CHK ==0 and letterBlank==False) or (wordList == lvl1word643 and lvl1word643CHK ==0 and letterBlank==False) or (wordList == lvl1word644 and lvl1word644CHK ==0 and letterBlank==False) or (wordList == lvl1word645 and lvl1word645CHK ==0 and letterBlank==False) or (wordList == lvl1word646 and lvl1word646CHK ==0 and letterBlank==False) or (wordList == lvl1word647 and lvl1word647CHK ==0 and letterBlank==False) or (wordList == lvl1word648 and lvl1word648CHK ==0 and letterBlank==False) or (wordList == lvl1word649 and lvl1word649CHK ==0 and letterBlank==False) or (wordList == lvl1word650 and lvl1word650CHK ==0 and letterBlank==False) or (wordList == lvl1word651 and lvl1word651CHK ==0 and letterBlank==False) or (wordList == lvl1word652 and lvl1word652CHK ==0 and letterBlank==False) or (wordList == lvl1word653 and lvl1word653CHK ==0 and letterBlank==False) or (wordList == lvl1word654 and lvl1word654CHK ==0 and letterBlank==False) or (wordList == lvl1word655 and lvl1word655CHK ==0 and letterBlank==False) or (wordList == lvl1word656 and lvl1word656CHK ==0 and letterBlank==False) or (wordList == lvl1word657 and lvl1word657CHK ==0 and letterBlank==False) or (wordList == lvl1word658 and lvl1word658CHK ==0 and letterBlank==False) or (wordList == lvl1word659 and lvl1word659CHK ==0 and letterBlank==False) or (wordList == lvl1word660 and lvl1word660CHK ==0 and letterBlank==False) or (wordList == lvl1word661 and lvl1word661CHK ==0 and letterBlank==False) or (wordList == lvl1word662 and lvl1word662CHK ==0 and letterBlank==False) or (wordList == lvl1word663 and lvl1word663CHK ==0 and letterBlank==False) or (wordList == lvl1word664 and lvl1word664CHK ==0 and letterBlank==False) or (wordList == lvl1word665 and lvl1word665CHK ==0 and letterBlank==False) or (wordList == lvl1word666 and lvl1word666CHK ==0 and letterBlank==False) or (wordList == lvl1word667 and lvl1word667CHK ==0 and letterBlank==False) or (wordList == lvl1word668 and lvl1word668CHK ==0 and letterBlank==False) or (wordList == lvl1word669 and lvl1word669CHK ==0 and letterBlank==False) or (wordList == lvl1word670 and lvl1word670CHK ==0 and letterBlank==False) or (wordList == lvl1word671 and lvl1word671CHK ==0 and letterBlank==False) or (wordList == lvl1word672 and lvl1word672CHK ==0 and letterBlank==False) or (wordList == lvl1word673 and lvl1word673CHK ==0 and letterBlank==False) or (wordList == lvl1word674 and lvl1word674CHK ==0 and letterBlank==False) or (wordList == lvl1word675 and lvl1word675CHK ==0 and letterBlank==False) or (wordList == lvl1word676 and lvl1word676CHK ==0 and letterBlank==False) or (wordList == lvl1word677 and lvl1word677CHK ==0 and letterBlank==False) or (wordList == lvl1word678 and lvl1word678CHK ==0 and letterBlank==False) or (wordList == lvl1word679 and lvl1word679CHK ==0 and letterBlank==False) or (wordList == lvl1word680 and lvl1word680CHK ==0 and letterBlank==False) or (wordList == lvl1word681 and lvl1word681CHK ==0 and letterBlank==False) or (wordList == lvl1word682 and lvl1word682CHK ==0 and letterBlank==False) or (wordList == lvl1word683 and lvl1word683CHK ==0 and letterBlank==False) or (wordList == lvl1word684 and lvl1word684CHK ==0 and letterBlank==False) or (wordList == lvl1word685 and lvl1word685CHK ==0 and letterBlank==False) or (wordList == lvl1word686 and lvl1word686CHK ==0 and letterBlank==False) or (wordList == lvl1word687 and lvl1word687CHK ==0 and letterBlank==False) or (wordList == lvl1word688 and lvl1word688CHK ==0 and letterBlank==False) or (wordList == lvl1word689 and lvl1word689CHK ==0 and letterBlank==False) or (wordList == lvl1word690 and lvl1word690CHK ==0 and letterBlank==False) or (wordList == lvl1word691 and lvl1word691CHK ==0 and letterBlank==False) or (wordList == lvl1word692 and lvl1word692CHK ==0 and letterBlank==False) or (wordList == lvl1word693 and lvl1word693CHK ==0 and letterBlank==False) or (wordList == lvl1word694 and lvl1word694CHK ==0 and letterBlank==False) or (wordList == lvl1word695 and lvl1word695CHK ==0 and letterBlank==False) or (wordList == lvl1word696 and lvl1word696CHK ==0 and letterBlank==False) or (wordList == lvl1word697 and lvl1word697CHK ==0 and letterBlank==False) or (wordList == lvl1word698 and lvl1word698CHK ==0 and letterBlank==False) or (wordList == lvl1word699 and lvl1word699CHK ==0 and letterBlank==False)  or (wordList == lvl1word700 and lvl1word700CHK ==0 and letterBlank==False) or (wordList == lvl1word701 and lvl1word701CHK ==0 and letterBlank==False) or (wordList == lvl1word702 and lvl1word702CHK ==0 and letterBlank==False) or (wordList == lvl1word703 and lvl1word703CHK ==0 and letterBlank==False) or (wordList == lvl1word704 and lvl1word704CHK ==0 and letterBlank==False) or (wordList == lvl1word705 and lvl1word705CHK ==0 and letterBlank==False) or (wordList == lvl1word706 and lvl1word706CHK ==0 and letterBlank==False) or (wordList == lvl1word707 and lvl1word707CHK ==0 and letterBlank==False) or (wordList == lvl1word708 and lvl1word708CHK ==0 and letterBlank==False) or (wordList == lvl1word709 and lvl1word709CHK ==0 and letterBlank==False) or (wordList == lvl1word710 and lvl1word710CHK ==0 and letterBlank==False) or (wordList == lvl1word711 and lvl1word711CHK ==0 and letterBlank==False) or (wordList == lvl1word712 and lvl1word712CHK ==0 and letterBlank==False) or (wordList == lvl1word713 and lvl1word713CHK ==0 and letterBlank==False) or (wordList == lvl1word714 and lvl1word714CHK ==0 and letterBlank==False) or (wordList == lvl1word715 and lvl1word715CHK ==0 and letterBlank==False) or (wordList == lvl1word716 and lvl1word716CHK ==0 and letterBlank==False) or (wordList == lvl1word717 and lvl1word717CHK ==0 and letterBlank==False) or (wordList == lvl1word718 and lvl1word718CHK ==0 and letterBlank==False) or (wordList == lvl1word719 and lvl1word719CHK ==0 and letterBlank==False) or (wordList == lvl1word720 and lvl1word720CHK ==0 and letterBlank==False) or (wordList == lvl1word721 and lvl1word721CHK ==0 and letterBlank==False) or (wordList == lvl1word722 and lvl1word722CHK ==0 and letterBlank==False) or (wordList == lvl1word723 and lvl1word723CHK ==0 and letterBlank==False) or (wordList == lvl1word724 and lvl1word724CHK ==0 and letterBlank==False) or (wordList == lvl1word725 and lvl1word725CHK ==0 and letterBlank==False) or (wordList == lvl1word726 and lvl1word726CHK ==0 and letterBlank==False) or (wordList == lvl1word727 and lvl1word727CHK ==0 and letterBlank==False) or (wordList == lvl1word728 and lvl1word728CHK ==0 and letterBlank==False) or (wordList == lvl1word729 and lvl1word729CHK ==0 and letterBlank==False) or (wordList == lvl1word730 and lvl1word730CHK ==0 and letterBlank==False) or (wordList == lvl1word731 and lvl1word731CHK ==0 and letterBlank==False) or (wordList == lvl1word732 and lvl1word732CHK ==0 and letterBlank==False) or (wordList == lvl1word733 and lvl1word733CHK ==0 and letterBlank==False) or (wordList == lvl1word734 and lvl1word734CHK ==0 and letterBlank==False) or (wordList == lvl1word735 and lvl1word735CHK ==0 and letterBlank==False) or (wordList == lvl1word736 and lvl1word736CHK ==0 and letterBlank==False) or (wordList == lvl1word737 and lvl1word737CHK ==0 and letterBlank==False) or (wordList == lvl1word738 and lvl1word738CHK ==0 and letterBlank==False) or (wordList == lvl1word739 and lvl1word739CHK ==0 and letterBlank==False) or (wordList == lvl1word740 and lvl1word740CHK ==0 and letterBlank==False) or (wordList == lvl1word741 and lvl1word741CHK ==0 and letterBlank==False) or (wordList == lvl1word742 and lvl1word742CHK ==0 and letterBlank==False) or (wordList == lvl1word743 and lvl1word743CHK ==0 and letterBlank==False) or (wordList == lvl1word744 and lvl1word744CHK ==0 and letterBlank==False) or (wordList == lvl1word745 and lvl1word745CHK ==0 and letterBlank==False) or (wordList == lvl1word746 and lvl1word746CHK ==0 and letterBlank==False) or (wordList == lvl1word747 and lvl1word747CHK ==0 and letterBlank==False) or (wordList == lvl1word748 and lvl1word748CHK ==0 and letterBlank==False) or (wordList == lvl1word749 and lvl1word749CHK ==0 and letterBlank==False) or (wordList == lvl1word750 and lvl1word750CHK ==0 and letterBlank==False) or (wordList == lvl1word751 and lvl1word751CHK ==0 and letterBlank==False) or (wordList == lvl1word752 and lvl1word752CHK ==0 and letterBlank==False) or (wordList == lvl1word753 and lvl1word753CHK ==0 and letterBlank==False) or (wordList == lvl1word754 and lvl1word754CHK ==0 and letterBlank==False) or (wordList == lvl1word755 and lvl1word755CHK ==0 and letterBlank==False) or (wordList == lvl1word756 and lvl1word756CHK ==0 and letterBlank==False) or (wordList == lvl1word757 and lvl1word757CHK ==0 and letterBlank==False) or (wordList == lvl1word758 and lvl1word758CHK ==0 and letterBlank==False) or (wordList == lvl1word759 and lvl1word759CHK ==0 and letterBlank==False) or (wordList == lvl1word760 and lvl1word760CHK ==0 and letterBlank==False) or (wordList == lvl1word761 and lvl1word761CHK ==0 and letterBlank==False) or (wordList == lvl1word762 and lvl1word762CHK ==0 and letterBlank==False) or (wordList == lvl1word763 and lvl1word763CHK ==0 and letterBlank==False) or (wordList == lvl1word764 and lvl1word764CHK ==0 and letterBlank==False) or (wordList == lvl1word765 and lvl1word765CHK ==0 and letterBlank==False) or (wordList == lvl1word766 and lvl1word766CHK ==0 and letterBlank==False) or (wordList == lvl1word767 and lvl1word767CHK ==0 and letterBlank==False) or (wordList == lvl1word768 and lvl1word768CHK ==0 and letterBlank==False) or (wordList == lvl1word769 and lvl1word769CHK ==0 and letterBlank==False) or (wordList == lvl1word770 and lvl1word770CHK ==0 and letterBlank==False) or (wordList == lvl1word771 and lvl1word771CHK ==0 and letterBlank==False) or (wordList == lvl1word772 and lvl1word772CHK ==0 and letterBlank==False) or (wordList == lvl1word773 and lvl1word773CHK ==0 and letterBlank==False) or (wordList == lvl1word774 and lvl1word774CHK ==0 and letterBlank==False) or (wordList == lvl1word775 and lvl1word775CHK ==0 and letterBlank==False) or (wordList == lvl1word776 and lvl1word776CHK ==0 and letterBlank==False) or (wordList == lvl1word777 and lvl1word777CHK ==0 and letterBlank==False) or (wordList == lvl1word778 and lvl1word778CHK ==0 and letterBlank==False) or (wordList == lvl1word779 and lvl1word779CHK ==0 and letterBlank==False) or (wordList == lvl1word780 and lvl1word780CHK ==0 and letterBlank==False) or (wordList == lvl1word781 and lvl1word781CHK ==0 and letterBlank==False) or (wordList == lvl1word782 and lvl1word782CHK ==0 and letterBlank==False) or (wordList == lvl1word783 and lvl1word783CHK ==0 and letterBlank==False) or (wordList == lvl1word784 and lvl1word784CHK ==0 and letterBlank==False) or (wordList == lvl1word785 and lvl1word785CHK ==0 and letterBlank==False) or (wordList == lvl1word786 and lvl1word786CHK ==0 and letterBlank==False) or (wordList == lvl1word787 and lvl1word787CHK ==0 and letterBlank==False) or (wordList == lvl1word788 and lvl1word788CHK ==0 and letterBlank==False) or (wordList == lvl1word789 and lvl1word789CHK ==0 and letterBlank==False) or (wordList == lvl1word790 and lvl1word790CHK ==0 and letterBlank==False) or (wordList == lvl1word791 and lvl1word791CHK ==0 and letterBlank==False) or (wordList == lvl1word792 and lvl1word792CHK ==0 and letterBlank==False) or (wordList == lvl1word793 and lvl1word793CHK ==0 and letterBlank==False) or (wordList == lvl1word794 and lvl1word794CHK ==0 and letterBlank==False) or (wordList == lvl1word795 and lvl1word795CHK ==0 and letterBlank==False) or (wordList == lvl1word796 and lvl1word796CHK ==0 and letterBlank==False) or (wordList == lvl1word797 and lvl1word797CHK ==0 and letterBlank==False) or (wordList == lvl1word798 and lvl1word798CHK ==0 and letterBlank==False) or (wordList == lvl1word799 and lvl1word799CHK ==0 and letterBlank==False) or (wordList == lvl1word800 and lvl1word800CHK) or (wordList == lvl1word801 and lvl1word801CHK ==0 and letterBlank==False) or (wordList == lvl1word802 and lvl1word802CHK ==0 and letterBlank==False) or (wordList == lvl1word803 and lvl1word803CHK ==0 and letterBlank==False) or (wordList == lvl1word804 and lvl1word804CHK ==0 and letterBlank==False) or (wordList == lvl1word805 and lvl1word805CHK ==0 and letterBlank==False) or (wordList == lvl1word806 and lvl1word806CHK ==0 and letterBlank==False) or (wordList == lvl1word807 and lvl1word807CHK ==0 and letterBlank==False) or (wordList == lvl1word808 and lvl1word808CHK ==0 and letterBlank==False) or (wordList == lvl1word809 and lvl1word809CHK ==0 and letterBlank==False) or (wordList == lvl1word810 and lvl1word810CHK ==0 and letterBlank==False) or (wordList == lvl1word811 and lvl1word811CHK ==0 and letterBlank==False) or (wordList == lvl1word812 and lvl1word812CHK ==0 and letterBlank==False) or (wordList == lvl1word813 and lvl1word813CHK ==0 and letterBlank==False) or (wordList == lvl1word814 and lvl1word814CHK ==0 and letterBlank==False) or (wordList == lvl1word815 and lvl1word815CHK ==0 and letterBlank==False) or (wordList == lvl1word816 and lvl1word816CHK ==0 and letterBlank==False) or (wordList == lvl1word817 and lvl1word817CHK ==0 and letterBlank==False) or (wordList == lvl1word818 and lvl1word818CHK ==0 and letterBlank==False) or (wordList == lvl1word819 and lvl1word819CHK ==0 and letterBlank==False) or (wordList == lvl1word820 and lvl1word820CHK ==0 and letterBlank==False) or (wordList == lvl1word821 and lvl1word821CHK ==0 and letterBlank==False) or (wordList == lvl1word822 and lvl1word822CHK ==0 and letterBlank==False) or (wordList == lvl1word823 and lvl1word823CHK ==0 and letterBlank==False) or (wordList == lvl1word824 and lvl1word824CHK ==0 and letterBlank==False) or (wordList == lvl1word825 and lvl1word825CHK ==0 and letterBlank==False) or (wordList == lvl1word826 and lvl1word826CHK ==0 and letterBlank==False) or (wordList == lvl1word827 and lvl1word827CHK ==0 and letterBlank==False) or (wordList == lvl1word828 and lvl1word828CHK ==0 and letterBlank==False) or (wordList == lvl1word829 and lvl1word829CHK ==0 and letterBlank==False) or (wordList == lvl1word830 and lvl1word830CHK ==0 and letterBlank==False) or (wordList == lvl1word831 and lvl1word831CHK ==0 and letterBlank==False) or (wordList == lvl1word832 and lvl1word832CHK ==0 and letterBlank==False) or (wordList == lvl1word833 and lvl1word833CHK ==0 and letterBlank==False) or (wordList == lvl1word834 and lvl1word834CHK ==0 and letterBlank==False) or (wordList == lvl1word835 and lvl1word835CHK ==0 and letterBlank==False) or (wordList == lvl1word836 and lvl1word836CHK ==0 and letterBlank==False) or (wordList == lvl1word837 and lvl1word837CHK ==0 and letterBlank==False) or (wordList == lvl1word838 and lvl1word838CHK ==0 and letterBlank==False) or (wordList == lvl1word839 and lvl1word839CHK ==0 and letterBlank==False) or (wordList == lvl1word840 and lvl1word840CHK ==0 and letterBlank==False) or (wordList == lvl1word841 and lvl1word841CHK ==0 and letterBlank==False) or (wordList == lvl1word842 and lvl1word842CHK ==0 and letterBlank==False) or (wordList == lvl1word843 and lvl1word843CHK ==0 and letterBlank==False) or (wordList == lvl1word844 and lvl1word844CHK ==0 and letterBlank==False) or (wordList == lvl1word845 and lvl1word845CHK ==0 and letterBlank==False) or (wordList == lvl1word846 and lvl1word846CHK ==0 and letterBlank==False) or (wordList == lvl1word847 and lvl1word847CHK ==0 and letterBlank==False) or (wordList == lvl1word848 and lvl1word848CHK ==0 and letterBlank==False) or (wordList == lvl1word849 and lvl1word849CHK ==0 and letterBlank==False) or (wordList == lvl1word850 and lvl1word850CHK ==0 and letterBlank==False) or (wordList == lvl1word851 and lvl1word851CHK ==0 and letterBlank==False) or (wordList == lvl1word852 and lvl1word852CHK ==0 and letterBlank==False) or (wordList == lvl1word853 and lvl1word853CHK ==0 and letterBlank==False) or (wordList == lvl1word854 and lvl1word854CHK ==0 and letterBlank==False) or (wordList == lvl1word855 and lvl1word855CHK ==0 and letterBlank==False) or (wordList == lvl1word856 and lvl1word856CHK ==0 and letterBlank==False) or (wordList == lvl1word857 and lvl1word857CHK ==0 and letterBlank==False) or (wordList == lvl1word858 and lvl1word858CHK ==0 and letterBlank==False) or (wordList == lvl1word859 and lvl1word859CHK ==0 and letterBlank==False) or (wordList == lvl1word860 and lvl1word860CHK ==0 and letterBlank==False) or (wordList == lvl1word861 and lvl1word861CHK ==0 and letterBlank==False) or (wordList == lvl1word862 and lvl1word862CHK ==0 and letterBlank==False) or (wordList == lvl1word863 and lvl1word863CHK ==0 and letterBlank==False) or (wordList == lvl1word864 and lvl1word864CHK ==0 and letterBlank==False) or (wordList == lvl1word865 and lvl1word865CHK ==0 and letterBlank==False) or (wordList == lvl1word866 and lvl1word866CHK ==0 and letterBlank==False) or (wordList == lvl1word867 and lvl1word867CHK ==0 and letterBlank==False) or (wordList == lvl1word868 and lvl1word868CHK ==0 and letterBlank==False) or (wordList == lvl1word869 and lvl1word869CHK ==0 and letterBlank==False) or (wordList == lvl1word870 and lvl1word870CHK ==0 and letterBlank==False) or (wordList == lvl1word871 and lvl1word871CHK ==0 and letterBlank==False) or (wordList == lvl1word872 and lvl1word872CHK ==0 and letterBlank==False) or (wordList == lvl1word873 and lvl1word873CHK ==0 and letterBlank==False) or (wordList == lvl1word874 and lvl1word874CHK ==0 and letterBlank==False) or (wordList == lvl1word875 and lvl1word875CHK ==0 and letterBlank==False) or (wordList == lvl1word876 and lvl1word876CHK ==0 and letterBlank==False) or (wordList == lvl1word877 and lvl1word877CHK ==0 and letterBlank==False) or (wordList == lvl1word878 and lvl1word878CHK ==0 and letterBlank==False) or (wordList == lvl1word879 and lvl1word879CHK ==0 and letterBlank==False) or (wordList == lvl1word880 and lvl1word880CHK ==0 and letterBlank==False) or (wordList == lvl1word881 and lvl1word881CHK ==0 and letterBlank==False) or (wordList == lvl1word882 and lvl1word882CHK ==0 and letterBlank==False) or (wordList == lvl1word883 and lvl1word883CHK ==0 and letterBlank==False) or (wordList == lvl1word884 and lvl1word884CHK ==0 and letterBlank==False) or (wordList == lvl1word885 and lvl1word885CHK ==0 and letterBlank==False) or (wordList == lvl1word886 and lvl1word886CHK ==0 and letterBlank==False) or (wordList == lvl1word887 and lvl1word887CHK ==0 and letterBlank==False) or (wordList == lvl1word888 and lvl1word888CHK ==0 and letterBlank==False) or (wordList == lvl1word889 and lvl1word889CHK ==0 and letterBlank==False) or (wordList == lvl1word890 and lvl1word890CHK ==0 and letterBlank==False) or (wordList == lvl1word891 and lvl1word891CHK ==0 and letterBlank==False) or (wordList == lvl1word892 and lvl1word892CHK ==0 and letterBlank==False) or (wordList == lvl1word893 and lvl1word893CHK ==0 and letterBlank==False) or (wordList == lvl1word894 and lvl1word894CHK ==0 and letterBlank==False) or (wordList == lvl1word895 and lvl1word895CHK ==0 and letterBlank==False) or (wordList == lvl1word896 and lvl1word896CHK ==0 and letterBlank==False) or (wordList == lvl1word897 and lvl1word897CHK ==0 and letterBlank==False) or (wordList == lvl1word898 and lvl1word898CHK ==0 and letterBlank==False) or (wordList == lvl1word899 and lvl1word899CHK ==0 and letterBlank==False) or (wordList == lvl1word900 and lvl1word900CHK ==0 and letterBlank==False) or (wordList == lvl1word901 and lvl1word901CHK ==0 and letterBlank==False) or (wordList == lvl1word902 and lvl1word902CHK ==0 and letterBlank==False) or (wordList == lvl1word903 and lvl1word903CHK ==0 and letterBlank==False) or (wordList == lvl1word904 and lvl1word904CHK ==0 and letterBlank==False) or (wordList == lvl1word905 and lvl1word905CHK ==0 and letterBlank==False) or (wordList == lvl1word906 and lvl1word906CHK ==0 and letterBlank==False) or (wordList == lvl1word907 and lvl1word907CHK ==0 and letterBlank==False) or (wordList == lvl1word908 and lvl1word908CHK ==0 and letterBlank==False) or (wordList == lvl1word909 and lvl1word909CHK ==0 and letterBlank==False) or (wordList == lvl1word910 and lvl1word910CHK ==0 and letterBlank==False) or (wordList == lvl1word911 and lvl1word911CHK ==0 and letterBlank==False) or (wordList == lvl1word912 and lvl1word912CHK ==0 and letterBlank==False) or (wordList == lvl1word913 and lvl1word913CHK ==0 and letterBlank==False) or (wordList == lvl1word914 and lvl1word914CHK ==0 and letterBlank==False) or (wordList == lvl1word915 and lvl1word915CHK ==0 and letterBlank==False) or (wordList == lvl1word916 and lvl1word916CHK ==0 and letterBlank==False) or (wordList == lvl1word917 and lvl1word917CHK ==0 and letterBlank==False) or (wordList == lvl1word918 and lvl1word918CHK ==0 and letterBlank==False) or (wordList == lvl1word919 and lvl1word919CHK ==0 and letterBlank==False) or (wordList == lvl1word920 and lvl1word920CHK ==0 and letterBlank==False) or (wordList == lvl1word921 and lvl1word921CHK ==0 and letterBlank==False) or (wordList == lvl1word922 and lvl1word922CHK ==0 and letterBlank==False) or (wordList == lvl1word923 and lvl1word923CHK ==0 and letterBlank==False) or (wordList == lvl1word924 and lvl1word924CHK ==0 and letterBlank==False) or (wordList == lvl1word925 and lvl1word925CHK ==0 and letterBlank==False) or (wordList == lvl1word926 and lvl1word926CHK ==0 and letterBlank==False) or (wordList == lvl1word927 and lvl1word927CHK ==0 and letterBlank==False) or (wordList == lvl1word928 and lvl1word928CHK ==0 and letterBlank==False) or (wordList == lvl1word929 and lvl1word929CHK ==0 and letterBlank==False) or (wordList == lvl1word930 and lvl1word930CHK ==0 and letterBlank==False) or (wordList == lvl1word931 and lvl1word931CHK ==0 and letterBlank==False) or (wordList == lvl1word932 and lvl1word932CHK ==0 and letterBlank==False) or (wordList == lvl1word933 and lvl1word933CHK ==0 and letterBlank==False) or (wordList == lvl1word934 and lvl1word934CHK ==0 and letterBlank==False) or (wordList == lvl1word935 and lvl1word935CHK ==0 and letterBlank==False) or (wordList == lvl1word936 and lvl1word936CHK ==0 and letterBlank==False) or (wordList == lvl1word937 and lvl1word937CHK ==0 and letterBlank==False) or (wordList == lvl1word938 and lvl1word938CHK ==0 and letterBlank==False) or (wordList == lvl1word939 and lvl1word939CHK ==0 and letterBlank==False) or (wordList == lvl1word940 and lvl1word940CHK ==0 and letterBlank==False) or (wordList == lvl1word941 and lvl1word941CHK ==0 and letterBlank==False) or (wordList == lvl1word942 and lvl1word942CHK ==0 and letterBlank==False) or (wordList == lvl1word943 and lvl1word943CHK ==0 and letterBlank==False) or (wordList == lvl1word944 and lvl1word944CHK ==0 and letterBlank==False) or (wordList == lvl1word945 and lvl1word945CHK ==0 and letterBlank==False) or (wordList == lvl1word946 and lvl1word946CHK ==0 and letterBlank==False) or (wordList == lvl1word947 and lvl1word947CHK ==0 and letterBlank==False) or (wordList == lvl1word948 and lvl1word948CHK ==0 and letterBlank==False) or (wordList == lvl1word949 and lvl1word949CHK ==0 and letterBlank==False) or (wordList == lvl1word950 and lvl1word950CHK ==0 and letterBlank==False) or (wordList == lvl1word951 and lvl1word951CHK ==0 and letterBlank==False) or (wordList == lvl1word952 and lvl1word952CHK ==0 and letterBlank==False) or (wordList == lvl1word953 and lvl1word953CHK ==0 and letterBlank==False) or (wordList == lvl1word954 and lvl1word954CHK ==0 and letterBlank==False) or (wordList == lvl1word955 and lvl1word955CHK ==0 and letterBlank==False) or (wordList == lvl1word956 and lvl1word956CHK ==0 and letterBlank==False) or (wordList == lvl1word957 and lvl1word957CHK ==0 and letterBlank==False) or (wordList == lvl1word958 and lvl1word958CHK ==0 and letterBlank==False) or (wordList == lvl1word959 and lvl1word959CHK ==0 and letterBlank==False) or (wordList == lvl1word960 and lvl1word960CHK ==0 and letterBlank==False) or (wordList == lvl1word961 and lvl1word961CHK ==0 and letterBlank==False) or (wordList == lvl1word962 and lvl1word962CHK ==0 and letterBlank==False) or (wordList == lvl1word963 and lvl1word963CHK ==0 and letterBlank==False) or (wordList == lvl1word964 and lvl1word964CHK ==0 and letterBlank==False) or (wordList == lvl1word965 and lvl1word965CHK ==0 and letterBlank==False) or (wordList == lvl1word966 and lvl1word966CHK ==0 and letterBlank==False) or (wordList == lvl1word967 and lvl1word967CHK ==0 and letterBlank==False) or (wordList == lvl1word968 and lvl1word968CHK ==0 and letterBlank==False) or (wordList == lvl1word969 and lvl1word969CHK ==0 and letterBlank==False) or (wordList == lvl1word970 and lvl1word970CHK ==0 and letterBlank==False) or (wordList == lvl1word971 and lvl1word971CHK ==0 and letterBlank==False) or (wordList == lvl1word972 and lvl1word972CHK ==0 and letterBlank==False) or (wordList == lvl1word973 and lvl1word973CHK ==0 and letterBlank==False) or (wordList == lvl1word974 and lvl1word974CHK ==0 and letterBlank==False) or (wordList == lvl1word975 and lvl1word975CHK ==0 and letterBlank==False) or (wordList == lvl1word976 and lvl1word976CHK ==0 and letterBlank==False) or (wordList == lvl1word977 and lvl1word977CHK ==0 and letterBlank==False) or (wordList == lvl1word978 and lvl1word978CHK ==0 and letterBlank==False) or (wordList == lvl1word979 and lvl1word979CHK ==0 and letterBlank==False) or (wordList == lvl1word980 and lvl1word980CHK ==0 and letterBlank==False) or (wordList == lvl1word981 and lvl1word981CHK ==0 and letterBlank==False) or (wordList == lvl1word982 and lvl1word982CHK ==0 and letterBlank==False) or (wordList == lvl1word983 and lvl1word983CHK ==0 and letterBlank==False) or (wordList == lvl1word984 and lvl1word984CHK ==0 and letterBlank==False) or (wordList == lvl1word985 and lvl1word985CHK ==0 and letterBlank==False) or (wordList == lvl1word986 and lvl1word986CHK ==0 and letterBlank==False) or (wordList == lvl1word987 and lvl1word987CHK ==0 and letterBlank==False) or (wordList == lvl1word988 and lvl1word988CHK ==0 and letterBlank==False) or (wordList == lvl1word989 and lvl1word989CHK ==0 and letterBlank==False) or (wordList == lvl1word990 and lvl1word990CHK ==0 and letterBlank==False) or (wordList == lvl1word991 and lvl1word991CHK ==0 and letterBlank==False) or (wordList == lvl1word992 and lvl1word992CHK ==0 and letterBlank==False) or (wordList == lvl1word993 and lvl1word993CHK ==0 and letterBlank==False) or (wordList == lvl1word994 and lvl1word994CHK ==0 and letterBlank==False) or (wordList == lvl1word995 and lvl1word995CHK ==0 and letterBlank==False) or (wordList == lvl1word996 and lvl1word996CHK ==0 and letterBlank==False) or (wordList == lvl1word997 and lvl1word997CHK ==0 and letterBlank==False) or (wordList == lvl1word998 and lvl1word998CHK ==0 and letterBlank==False) or (wordList == lvl1word999 and lvl1word999CHK ==0 and letterBlank==False) or (wordList == lvl1word1000 and lvl1word1000CHK ==0 and letterBlank==False) or (wordList == lvl1word1001 and lvl1word1001CHK ==0 and letterBlank==False) or (wordList == lvl1word1002 and lvl1word1002CHK ==0 and letterBlank==False) or (wordList == lvl1word1003 and lvl1word1003CHK ==0 and letterBlank==False) or (wordList == lvl1word1004 and lvl1word1004CHK ==0 and letterBlank==False) or (wordList == lvl1word1005 and lvl1word1005CHK ==0 and letterBlank==False) or (wordList == lvl1word1006 and lvl1word1006CHK ==0 and letterBlank==False) or (wordList == lvl1word1007 and lvl1word1007CHK ==0 and letterBlank==False) or (wordList == lvl1word1008 and lvl1word1008CHK ==0 and letterBlank==False) or (wordList == lvl1word1009 and lvl1word1009CHK ==0 and letterBlank==False) or (wordList == lvl1word1010 and lvl1word1010CHK ==0 and letterBlank==False) or (wordList == lvl1word1011 and lvl1word1011CHK ==0 and letterBlank==False) or (wordList == lvl1word1012 and lvl1word1012CHK ==0 and letterBlank==False) or (wordList == lvl1word1013 and lvl1word1013CHK ==0 and letterBlank==False) or (wordList == lvl1word1014 and lvl1word1014CHK ==0 and letterBlank==False) or (wordList == lvl1word1015 and lvl1word1015CHK ==0 and letterBlank==False) or (wordList == lvl1word1016 and lvl1word1016CHK ==0 and letterBlank==False) or (wordList == lvl1word1017 and lvl1word1017CHK ==0 and letterBlank==False) or (wordList == lvl1word1018 and lvl1word1018CHK ==0 and letterBlank==False) or (wordList == lvl1word1019 and lvl1word1019CHK ==0 and letterBlank==False) or (wordList == lvl1word1020 and lvl1word1020CHK ==0 and letterBlank==False) or (wordList == lvl1word1021 and lvl1word1021CHK ==0 and letterBlank==False) or (wordList == lvl1word1022 and lvl1word1022CHK ==0 and letterBlank==False) or (wordList == lvl1word1023 and lvl1word1023CHK ==0 and letterBlank==False) or (wordList == lvl1word1024 and lvl1word1024CHK ==0 and letterBlank==False) or (wordList == lvl1word1025 and lvl1word1025CHK ==0 and letterBlank==False) or (wordList == lvl1word1026 and lvl1word1026CHK ==0 and letterBlank==False) or (wordList == lvl1word1027 and lvl1word1027CHK ==0 and letterBlank==False) or (wordList == lvl1word1028 and lvl1word1028CHK ==0 and letterBlank==False) or (wordList == lvl1word1029 and lvl1word1029CHK ==0 and letterBlank==False) or (wordList == lvl1word1030 and lvl1word1030CHK ==0 and letterBlank==False) or (wordList == lvl1word1031 and lvl1word1031CHK ==0 and letterBlank==False) or (wordList == lvl1word1032 and lvl1word1032CHK ==0 and letterBlank==False) or (wordList == lvl1word1033 and lvl1word1033CHK ==0 and letterBlank==False) or (wordList == lvl1word1034 and lvl1word1034CHK ==0 and letterBlank==False) or (wordList == lvl1word1035 and lvl1word1035CHK ==0 and letterBlank==False) or (wordList == lvl1word1036 and lvl1word1036CHK ==0 and letterBlank==False) or (wordList == lvl1word1037 and lvl1word1037CHK ==0 and letterBlank==False) or (wordList == lvl1word1038 and lvl1word1038CHK ==0 and letterBlank==False) or (wordList == lvl1word1039 and lvl1word1039CHK ==0 and letterBlank==False) or (wordList == lvl1word1040 and lvl1word1040CHK ==0 and letterBlank==False) or (wordList == lvl1word1041 and lvl1word1041CHK ==0 and letterBlank==False) or (wordList == lvl1word1042 and lvl1word1042CHK ==0 and letterBlank==False) or (wordList == lvl1word1043 and lvl1word1043CHK ==0 and letterBlank==False) or (wordList == lvl1word1044 and lvl1word1044CHK ==0 and letterBlank==False) or (wordList == lvl1word1045 and lvl1word1045CHK ==0 and letterBlank==False) or (wordList == lvl1word1047 and lvl1word1047CHK ==0 and letterBlank==False) or (wordList == lvl1word1048 and lvl1word1048CHK ==0 and letterBlank==False) or (wordList == lvl1word1049 and lvl1word1049CHK ==0 and letterBlank==False) or (wordList == lvl1word1050 and lvl1word1050CHK ==0 and letterBlank==False) or (wordList == lvl1word1051 and lvl1word1051CHK ==0 and letterBlank==False) or (wordList == lvl1word1052 and lvl1word1052CHK ==0 and letterBlank==False) or (wordList == lvl1word1053 and lvl1word1053CHK ==0 and letterBlank==False) or (wordList == lvl1word1054 and lvl1word1054CHK ==0 and letterBlank==False) or (wordList == lvl1word1055 and lvl1word1055CHK ==0 and letterBlank==False) or (wordList == lvl1word1056 and lvl1word1056CHK ==0 and letterBlank==False) or (wordList == lvl1word1057 and lvl1word1057CHK ==0 and letterBlank==False) or (wordList == lvl1word1058 and lvl1word1058CHK ==0 and letterBlank==False) or (wordList == lvl1word1059 and lvl1word1059CHK ==0 and letterBlank==False) or (wordList == lvl1word1060 and lvl1word1060CHK ==0 and letterBlank==False) or (wordList == lvl1word1061 and lvl1word1061CHK ==0 and letterBlank==False) or (wordList == lvl1word1062 and lvl1word1062CHK ==0 and letterBlank==False) or (wordList == lvl1word1063 and lvl1word1063CHK ==0 and letterBlank==False) or (wordList == lvl1word1064 and lvl1word1064CHK ==0 and letterBlank==False) or (wordList == lvl1word1065 and lvl1word1065CHK ==0 and letterBlank==False)  or (wordList == lvl1word1067 and lvl1word1067CHK ==0 and letterBlank==False) or (wordList == lvl1word1068 and lvl1word1068CHK ==0 and letterBlank==False) or (wordList == lvl1word1069 and lvl1word1069CHK ==0 and letterBlank==False) or (wordList == lvl1word1070 and lvl1word1070CHK ==0 and letterBlank==False) or (wordList == lvl1word1072 and lvl1word1072CHK ==0 and letterBlank==False) or (wordList == lvl1word1073 and lvl1word1073CHK ==0 and letterBlank==False) or (wordList == lvl1word1074 and lvl1word1074CHK ==0 and letterBlank==False) or (wordList == lvl1word1075 and lvl1word1075CHK ==0 and letterBlank==False) or (wordList == lvl1word1076 and lvl1word1076CHK ==0 and letterBlank==False) or (wordList == lvl1word1077 and lvl1word1077CHK ==0 and letterBlank==False) or (wordList == lvl1word1078 and lvl1word1078CHK ==0 and letterBlank==False) or (wordList == lvl1word1079 and lvl1word1079CHK ==0 and letterBlank==False) or (wordList == lvl1word1080 and lvl1word1080CHK ==0 and letterBlank==False) or (wordList == lvl1word1081 and lvl1word1081CHK ==0 and letterBlank==False) or (wordList == lvl1word1082 and lvl1word1082CHK ==0 and letterBlank==False) or (wordList == lvl1word1083 and lvl1word1083CHK ==0 and letterBlank==False) or (wordList == lvl1word1084 and lvl1word1084CHK ==0 and letterBlank==False) or (wordList == lvl1word1085 and lvl1word1085CHK ==0 and letterBlank==False) or (wordList == lvl1word1086 and lvl1word1086CHK ==0 and letterBlank==False) or (wordList == lvl1word1087 and lvl1word1087CHK ==0 and letterBlank==False) or (wordList == lvl1word1088 and lvl1word1088CHK ==0 and letterBlank==False) or (wordList == lvl1word1089 and lvl1word1089CHK ==0 and letterBlank==False) or (wordList == lvl1word1090 and lvl1word1090CHK ==0 and letterBlank==False) or (wordList == lvl1word1091 and lvl1word1091CHK ==0 and letterBlank==False) or (wordList == lvl1word1092 and lvl1word1092CHK ==0 and letterBlank==False) or (wordList == lvl1word1093 and lvl1word1093CHK ==0 and letterBlank==False) or (wordList == lvl1word1094 and lvl1word1094CHK ==0 and letterBlank==False) or (wordList == lvl1word1095 and lvl1word1095CHK ==0 and letterBlank==False) or (wordList == lvl1word1096 and lvl1word1096CHK ==0 and letterBlank==False) or (wordList == lvl1word1097 and lvl1word1097CHK ==0 and letterBlank==False) or (wordList == lvl1word1098 and lvl1word1098CHK ==0 and letterBlank==False) or (wordList == lvl1word1099 and lvl1word1099CHK ==0 and letterBlank==False) or (wordList == lvl1word1100 and lvl1word1100CHK ==0 and letterBlank==False) or (wordList == lvl1word1101 and lvl1word1101CHK ==0 and letterBlank==False)  or (wordList == lvl1word1103 and lvl1word1103CHK ==0 and letterBlank==False) or (wordList == lvl1word1104 and lvl1word1104CHK ==0 and letterBlank==False) or (wordList == lvl1word1105 and lvl1word1105CHK ==0 and letterBlank==False) or (wordList == lvl1word1106 and lvl1word1106CHK ==0 and letterBlank==False)  or (wordList == lvl1word1108 and lvl1word1108CHK ==0 and letterBlank==False) or (wordList == lvl1word1109 and lvl1word1109CHK ==0 and letterBlank==False) or (wordList == lvl1word1110 and lvl1word1110CHK ==0 and letterBlank==False) or (wordList == lvl1word1111 and lvl1word1111CHK ==0 and letterBlank==False) or (wordList == lvl1word1112 and lvl1word1112CHK ==0 and letterBlank==False) or (wordList == lvl1word1113 and lvl1word1113CHK ==0 and letterBlank==False)  or (wordList == lvl1word1116 and lvl1word1116CHK ==0 and letterBlank==False) or (wordList == lvl1word1117 and lvl1word1117CHK ==0 and letterBlank==False) or (wordList == lvl1word1118 and lvl1word1118CHK ==0 and letterBlank==False) or (wordList == lvl1word1119 and lvl1word1119CHK ==0 and letterBlank==False) or (wordList == lvl1word1120 and lvl1word1120CHK ==0 and letterBlank==False) or (wordList == lvl1word1121 and lvl1word1121CHK ==0 and letterBlank==False) or (wordList == lvl1word1122 and lvl1word1122CHK ==0 and letterBlank==False) or (wordList == lvl1word1123 and lvl1word1123CHK ==0 and letterBlank==False) or (wordList == lvl1word1124 and lvl1word1124CHK ==0 and letterBlank==False) or (wordList == lvl1word1125 and lvl1word1125CHK ==0 and letterBlank==False) or (wordList == lvl1word1126 and lvl1word1126CHK ==0 and letterBlank==False) or (wordList == lvl1word1127 and lvl1word1127CHK ==0 and letterBlank==False) or (wordList == lvl1word1128 and lvl1word1128CHK ==0 and letterBlank==False) or (wordList == lvl1word1129 and lvl1word1129CHK ==0 and letterBlank==False) or (wordList == lvl1word1130 and lvl1word1130CHK ==0 and letterBlank==False) or (wordList == lvl1word1131 and lvl1word1131CHK ==0 and letterBlank==False) or (wordList == lvl1word1132 and lvl1word1132CHK ==0 and letterBlank==False) or (wordList == lvl1word1133 and lvl1word1133CHK ==0 and letterBlank==False) or (wordList == lvl1word1134 and lvl1word1134CHK ==0 and letterBlank==False) or (wordList == lvl1word1135 and lvl1word1135CHK ==0 and letterBlank==False) or (wordList == lvl1word1136 and lvl1word1136CHK ==0 and letterBlank==False) or (wordList == lvl1word1137 and lvl1word1137CHK ==0 and letterBlank==False) or (wordList == lvl1word1138 and lvl1word1138CHK ==0 and letterBlank==False) or (wordList == lvl1word1139 and lvl1word1139CHK ==0 and letterBlank==False) or (wordList == lvl1word1140 and lvl1word1140CHK ==0 and letterBlank==False) or (wordList == lvl1word1141 and lvl1word1141CHK ==0 and letterBlank==False) or (wordList == lvl1word1142 and lvl1word1142CHK ==0 and letterBlank==False) or (wordList == lvl1word1143 and lvl1word1143CHK ==0 and letterBlank==False) or (wordList == lvl1word1144 and lvl1word1144CHK ==0 and letterBlank==False) or (wordList == lvl1word1145 and lvl1word1145CHK ==0 and letterBlank==False) or (wordList == lvl1word1146 and lvl1word1146CHK ==0 and letterBlank==False) or (wordList == lvl1word1147 and lvl1word1147CHK ==0 and letterBlank==False) or (wordList == lvl1word1148 and lvl1word1148CHK ==0 and letterBlank==False) or (wordList == lvl1word1149 and lvl1word1149CHK ==0 and letterBlank==False) or (wordList == lvl1word1150 and lvl1word1150CHK ==0 and letterBlank==False) or (wordList == lvl1word1151 and lvl1word1151CHK ==0 and letterBlank==False) or (wordList == lvl1word1153 and lvl1word1153CHK ==0 and letterBlank==False) or (wordList == lvl1word1154 and lvl1word1154CHK ==0 and letterBlank==False) or (wordList == lvl1word1155 and lvl1word1155CHK ==0 and letterBlank==False) or (wordList == lvl1word1156 and lvl1word1156CHK ==0 and letterBlank==False) or (wordList == lvl1word1157 and lvl1word1157CHK ==0 and letterBlank==False) or (wordList == lvl1word1158 and lvl1word1158CHK ==0 and letterBlank==False) or (wordList == lvl1word1159 and lvl1word1159CHK ==0 and letterBlank==False) or (wordList == lvl1word1160 and lvl1word1160CHK ==0 and letterBlank==False) or (wordList == lvl1word1161 and lvl1word1161CHK ==0 and letterBlank==False) or (wordList == lvl1word1162 and lvl1word1162CHK ==0 and letterBlank==False) or (wordList == lvl1word1163 and lvl1word1163CHK ==0 and letterBlank==False) or (wordList == lvl1word1164 and lvl1word1164CHK ==0 and letterBlank==False) or (wordList == lvl1word1165 and lvl1word1165CHK ==0 and letterBlank==False) or (wordList == lvl1word1166 and lvl1word1166CHK ==0 and letterBlank==False) or (wordList == lvl1word1167 and lvl1word1167CHK ==0 and letterBlank==False) or (wordList == lvl1word1168 and lvl1word1168CHK ==0 and letterBlank==False) or (wordList == lvl1word1169 and lvl1word1169CHK ==0 and letterBlank==False) or (wordList == lvl1word1170 and lvl1word1170CHK ==0 and letterBlank==False) or (wordList == lvl1word1171 and lvl1word1171CHK ==0 and letterBlank==False) or (wordList == lvl1word1173 and lvl1word1173CHK ==0 and letterBlank==False) or (wordList == lvl1word1175 and lvl1word1175CHK ==0 and letterBlank==False) or (wordList == lvl1word1176 and lvl1word1176CHK ==0 and letterBlank==False) or (wordList == lvl1word1177 and lvl1word1177CHK ==0 and letterBlank==False) or (wordList == lvl1word1178 and lvl1word1178CHK ==0 and letterBlank==False) or (wordList == lvl1word1179 and lvl1word1179CHK ==0 and letterBlank==False) or (wordList == lvl1word1180 and lvl1word1180CHK ==0 and letterBlank==False) or (wordList == lvl1word1181 and lvl1word1181CHK ==0 and letterBlank==False) or (wordList == lvl1word1182 and lvl1word1182CHK ==0 and letterBlank==False) or (wordList == lvl1word1183 and lvl1word1183CHK ==0 and letterBlank==False) or (wordList == lvl1word1184 and lvl1word1184CHK ==0 and letterBlank==False) or (wordList == lvl1word1185 and lvl1word1185CHK ==0 and letterBlank==False) or (wordList == lvl1word1186 and lvl1word1186CHK ==0 and letterBlank==False) or (wordList == lvl1word1187 and lvl1word1187CHK ==0 and letterBlank==False) or (wordList == lvl1word1188 and lvl1word1188CHK ==0 and letterBlank==False) or (wordList == lvl1word1189 and lvl1word1189CHK ==0 and letterBlank==False) or (wordList == lvl1word1190 and lvl1word1190CHK ==0 and letterBlank==False) or (wordList == lvl1word1191 and lvl1word1191CHK ==0 and letterBlank==False) or (wordList == lvl1word1192 and lvl1word1192CHK ==0 and letterBlank==False) or (wordList == lvl1word1193 and lvl1word1193CHK ==0 and letterBlank==False) or (wordList == lvl1word1194 and lvl1word1194CHK ==0 and letterBlank==False) or (wordList == lvl1word1195 and lvl1word1195CHK ==0 and letterBlank==False) or (wordList == lvl1word1196 and lvl1word1196CHK ==0 and letterBlank==False) or (wordList == lvl1word1197 and lvl1word1197CHK ==0 and letterBlank==False) or (wordList == lvl1word1198 and lvl1word1198CHK ==0 and letterBlank==False) or (wordList == lvl1word1199 and lvl1word1199CHK ==0 and letterBlank==False) or (wordList == lvl1word1200 and lvl1word1200CHK ==0 and letterBlank==False) or (wordList == lvl1word1201 and lvl1word1201CHK ==0 and letterBlank==False) or (wordList == lvl1word1202 and lvl1word1202CHK ==0 and letterBlank==False) or (wordList == lvl1word1203 and lvl1word1203CHK ==0 and letterBlank==False) or (wordList == lvl1word1204 and lvl1word1204CHK ==0 and letterBlank==False) or (wordList == lvl1word1205 and lvl1word1205CHK ==0 and letterBlank==False) or (wordList == lvl1word1206 and lvl1word1206CHK ==0 and letterBlank==False) or (wordList == lvl1word1207 and lvl1word1207CHK ==0 and letterBlank==False) or (wordList == lvl1word1208 and lvl1word1208CHK ==0 and letterBlank==False) or (wordList == lvl1word1209 and lvl1word1209CHK ==0 and letterBlank==False) or (wordList == lvl1word1210 and lvl1word1210CHK ==0 and letterBlank==False) or (wordList == lvl1word1211 and lvl1word1211CHK ==0 and letterBlank==False) or (wordList == lvl1word1212 and lvl1word1212CHK ==0 and letterBlank==False) or (wordList == lvl1word1213 and lvl1word1213CHK ==0 and letterBlank==False) or (wordList == lvl1word1214 and lvl1word1214CHK ==0 and letterBlank==False) or (wordList == lvl1word1215 and lvl1word1215CHK ==0 and letterBlank==False) or (wordList == lvl1word1216 and lvl1word1216CHK ==0 and letterBlank==False) or (wordList == lvl1word1217 and lvl1word1217CHK ==0 and letterBlank==False) or (wordList == lvl1word1218 and lvl1word1218CHK ==0 and letterBlank==False) or (wordList == lvl1word1219 and lvl1word1219CHK ==0 and letterBlank==False) or (wordList == lvl1word1220 and lvl1word1220CHK ==0 and letterBlank==False) or (wordList == lvl1word1221 and lvl1word1221CHK ==0 and letterBlank==False) or (wordList == lvl1word1222 and lvl1word1222CHK ==0 and letterBlank==False) or (wordList == lvl1word1223 and lvl1word1223CHK ==0 and letterBlank==False) or (wordList == lvl1word1224 and lvl1word1224CHK ==0 and letterBlank==False) or (wordList == lvl1word1225 and lvl1word1225CHK ==0 and letterBlank==False) or (wordList == lvl1word1226 and lvl1word1226CHK ==0 and letterBlank==False) or (wordList == lvl1word1227 and lvl1word1227CHK ==0 and letterBlank==False) or (wordList == lvl1word1228 and lvl1word1228CHK ==0 and letterBlank==False) or (wordList == lvl1word1229 and lvl1word1229CHK ==0 and letterBlank==False) or (wordList == lvl1word1230 and lvl1word1230CHK ==0 and letterBlank==False) or (wordList == lvl1word1231 and lvl1word1231CHK ==0 and letterBlank==False) or (wordList == lvl1word1232 and lvl1word1232CHK ==0 and letterBlank==False) or (wordList == lvl1word1233 and lvl1word1233CHK ==0 and letterBlank==False) or (wordList == lvl1word1234 and lvl1word1234CHK ==0 and letterBlank==False) or (wordList == lvl1word1235 and lvl1word1235CHK ==0 and letterBlank==False) or (wordList == lvl1word1236 and lvl1word1236CHK ==0 and letterBlank==False) or (wordList == lvl1word1237 and lvl1word1237CHK ==0 and letterBlank==False) or (wordList == lvl1word1238 and lvl1word1238CHK ==0 and letterBlank==False) or (wordList == lvl1word1239 and lvl1word1239CHK ==0 and letterBlank==False) or (wordList == lvl1word1240 and lvl1word1240CHK ==0 and letterBlank==False) or (wordList == lvl1word1241 and lvl1word1241CHK ==0 and letterBlank==False) or (wordList == lvl1word1242 and lvl1word1242CHK ==0 and letterBlank==False) or (wordList == lvl1word1243 and lvl1word1243CHK ==0 and letterBlank==False) or (wordList == lvl1word1244 and lvl1word1244CHK ==0 and letterBlank==False) or (wordList == lvl1word1245 and lvl1word1245CHK ==0 and letterBlank==False) or  (wordList == lvl1word1246 and lvl1word1246CHK ==0 and letterBlank==False) or (wordList == lvl1word1247 and lvl1word1247CHK ==0 and letterBlank==False) or (wordList == lvl1word1248 and lvl1word1248CHK ==0 and letterBlank==False) or (wordList == lvl1word1249 and lvl1word1249CHK ==0 and letterBlank==False) or (wordList == lvl1word1250 and lvl1word1250CHK ==0 and letterBlank==False) or (wordList == lvl1word1251 and lvl1word1251CHK ==0 and letterBlank==False) or (wordList == lvl1word1253 and lvl1word1253CHK ==0 and letterBlank==False) or (wordList == lvl1word1254 and lvl1word1254CHK ==0 and letterBlank==False) or (wordList == lvl1word1255 and lvl1word1255CHK ==0 and letterBlank==False) or (wordList == lvl1word1256 and lvl1word1256CHK ==0 and letterBlank==False) or (wordList == lvl1word1257 and lvl1word1257CHK ==0 and letterBlank==False) or (wordList == lvl1word1258 and lvl1word1258CHK ==0 and letterBlank==False) or (wordList == lvl1word1259 and lvl1word1259CHK ==0 and letterBlank==False) or (wordList == lvl1word1260 and lvl1word1260CHK ==0 and letterBlank==False) or (wordList == lvl1word1261 and lvl1word1261CHK ==0 and letterBlank==False) or (wordList == lvl1word1262 and lvl1word1262CHK ==0 and letterBlank==False) or (wordList == lvl1word1263 and lvl1word1263CHK ==0 and letterBlank==False) or (wordList == lvl1word1264 and lvl1word1264CHK ==0 and letterBlank==False)   :
                    scoreAddSet()
                    global foundCount
                    global scoreCount
                    global scoreMinus
                    global scoreAdd1
                    global scoreAdd
                    global scoreAdd2
                    global scoreMult
                    global scoreNum
                    global scoreNum2
                    global scoreLabel
                    global scoreUp
                    global scoreUpb
                    global scoreUpc
                    

                        

                    if len(wordList) == 2:
                        correctSound.play()
                        wordScore.append(wordList[0] + wordList[1])
                        print(wordScore[foundCount])
                        scoreCount += round(scoreNum2*scoreMult)
                        scoreCount += round(10*scoreMult)
                        scoreAdd = "+ " + format(round(scoreNum2*scoreMult)+round(10*scoreMult))
                        scoreList.append(round(scoreNum2*scoreMult)+round(10*scoreMult))
                        scoreAdd1 = "Two letter word!"
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd
                            global scoreAdd1
                            global scoreAdd2
                            global scoreUp
                            global scoreUpb
                            global scoreUpc
                            scoreAdd = ""
                            scoreAdd1 = ""
                            scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                        print("+" + format(round(10*scoreMult)) + " pts length score")
                        print("+" + format(round(scoreNum2*scoreMult)) + " letter score")
                        scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    if len(wordList) == 3:
                        correctSound.play()
                        wordScore.append(wordList[0] + wordList[1] + wordList[2])
                        print(wordScore[foundCount])
                        scoreCount += round(scoreNum2*scoreMult)
                        scoreCount += round(20*scoreMult)
                        scoreAdd = "+ " + format(round(scoreNum2*scoreMult)+round(20*scoreMult))
                        scoreList.append(round(scoreNum2*scoreMult)+round(20*scoreMult))
                        scoreAdd1 = "Three letter word!"
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE) 
                        def scoreDisp():
                            global scoreAdd
                            global scoreAdd1
                            global scoreUp
                            global scoreUpb
                            scoreAdd = ""
                            scoreAdd1 = ""
                            scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                        print("+" + format(round(20*scoreMult)) + " length score")
                        print("+" + format(round(scoreNum2*scoreMult)) + " letter score")
                        scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    if len(wordList) == 4:
                        correctSound.play()
                        wordScore.append(wordList[0] + wordList[1] + wordList[2] + wordList[3])
                        print(wordScore[foundCount])
                        scoreCount += round(scoreNum2*scoreMult)
                        scoreCount += round(35*scoreMult)
                        scoreAdd = "+ " + format(round(scoreNum2*scoreMult)+round(35*scoreMult))
                        scoreList.append(round(scoreNum2*scoreMult)+round(35*scoreMult))
                        scoreAdd1 = "Four letter word!"
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE) 
                        def scoreDisp():
                            global scoreAdd
                            global scoreAdd1
                            global scoreUp
                            global scoreUpb
                            scoreAdd = ""
                            scoreAdd1 = ""
                            scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                        print("+" + format(round(35*scoreMult)) + " length score")
                        print("+" + format(round(scoreNum2*scoreMult)) + " letter score")
                        scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    if len(wordList) == 5:
                        correctSound.play()
                        wordScore.append(wordList[0] + wordList[1] + wordList[2] + wordList[3] + wordList[4])
                        print(wordScore[foundCount])  
                        scoreCount += round(scoreNum2*scoreMult)
                        scoreCount += round(50*scoreMult)
                        scoreAdd = "+ " + format(round(scoreNum2*scoreMult)+round(50*scoreMult))
                        scoreList.append(round(scoreNum2*scoreMult)+round(50*scoreMult))
                        scoreAdd1 = "Five letter word!"
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd
                            global scoreAdd1
                            global scoreUp
                            global scoreUpb
                            scoreAdd = ""
                            scoreAdd1 = ""
                            scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                        print("+" + format(round(50*scoreMult)) + " length score")
                        print("+" + format(round(scoreNum2*scoreMult)) + " letter score")
                        scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    if len(wordList) == 6:
                        correctSound.play()
                        wordScore.append(wordList[0] + wordList[1] + wordList[2] + wordList[3] + wordList[4] + wordList[5])
                        print(wordScore[foundCount])  
                        scoreCount += round(scoreNum2*scoreMult)
                        scoreCount += round(70*scoreMult)
                        scoreAdd = "+ " + format(round(scoreNum2*scoreMult)+round(70*scoreMult))
                        scoreList.append(round(scoreNum2*scoreMult)+round(70*scoreMult))
                        scoreAdd1 = "Six letter word!"
                        scoreAdd2 = "VERY NICE!"
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scoreUpc = myFont4.render(scoreAdd2, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd
                            global scoreAdd1
                            global scoreAdd2
                            global scoreUp
                            global scoreUpb
                            global scoreUpc
                            scoreAdd = ""
                            scoreAdd1 = ""
                            scoreAdd2 = ""
                            scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                            scoreUpc = myFont4.render(scoreAdd2, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                        print("+" + format(round(70*scoreMult)) + " length score")
                        print("+" + format(round(scoreNum2*scoreMult)) + " letter score")
                        scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    if len(wordList) == 7:
                        correctSound.play()
                        wordScore.append(wordList[0] + wordList[1] + wordList[2] + wordList[3] + wordList[4] + wordList[5] + wordList[6])
                        print(wordScore[foundCount]) 
                        scoreCount += round(scoreNum2*scoreMult)
                        scoreCount += round(100*scoreMult)
                        scoreAdd = "+ " + format(round(scoreNum2*scoreMult)+round(100*scoreMult))
                        scoreList.append(round(scoreNum2*scoreMult)+round(100*scoreMult))
                        scoreAdd1 = "Seven letter word!"
                        scoreAdd2 = "GREAT!"
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scoreUpc = myFont4.render(scoreAdd2, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd
                            global scoreAdd1
                            global scoreAdd2
                            global scoreUp
                            global scoreUpb
                            global scoreUpc
                            scoreAdd = ""
                            scoreAdd1 = ""
                            scoreAdd2 = ""
                            scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                            scoreUpc = myFont4.render(scoreAdd2, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                        print("+" + format(round(100*scoreMult)) + " length score")
                        print("+" + format(round(scoreNum2*scoreMult)) + " letter score")
                        scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    if len(wordList) == 8:
                        correctSound.play()
                        wordScore.append(wordList[0] + wordList[1] + wordList[2] + wordList[3] + wordList[4] + wordList[5] + wordList[6] + wordList[7])
                        print(wordScore[foundCount]) 
                        scoreCount += round(scoreNum2*scoreMult)
                        scoreCount += round(150*scoreMult)
                        scoreAdd = "+ " + format(round(scoreNum2*scoreMult)+round(150*scoreMult))
                        scoreList.append(round(scoreNum2*scoreMult)+round(150*scoreMult))
                        scoreAdd1 = "Eight letter word!"
                        scoreAdd2 = "AWESOME!"
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scoreUpc = myFont4.render(scoreAdd2, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd
                            global scoreAdd1
                            global scoreAdd2
                            global scoreUp
                            global scoreUpb
                            global scoreUpc
                            scoreAdd = ""
                            scoreAdd1 = ""
                            scoreAdd2 = ""
                            scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                            scoreUpc = myFont4.render(scoreAdd2, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                        print("+" + format(round(150*scoreMult)) + " length score")
                        print("+" + format(round(scoreNum2*scoreMult)) + " letter score")
                        scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    if len(wordList) == 9:
                        correctSound.play()
                        wordScore.append(wordList[0] + wordList[1] + wordList[2] + wordList[3] + wordList[4] + wordList[5] + wordList[6] + wordList[7] + wordList[8])
                        print(wordScore[foundCount])
                        scoreCount += round(scoreNum2*scoreMult)
                        scoreCount += round(250*scoreMult)
                        scoreAdd = "+ " + format(round(scoreNum2*scoreMult)+round(250*scoreMult))
                        scoreList.append(round(scoreNum2*scoreMult)+round(250*scoreMult))
                        scoreAdd1 = "Nine letter word!"
                        scoreAdd2 = "INCREDIBLE!"
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scoreUpc = myFont4.render(scoreAdd2, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd
                            global scoreAdd1
                            global scoreAdd2
                            global scoreUp
                            global scoreUpb
                            global scoreUpc
                            scoreAdd = ""
                            scoreAdd1 = ""
                            scoreAdd2 = ""
                            scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                            scoreUpc = myFont4.render(scoreAdd2, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                        print("+" + format(round(250*scoreMult)) + " length score")
                        print("+" + format(round(scoreNum2*scoreMult)) + " letter score")
                        scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    if len(wordList) == 10:
                        correctSound.play()
                        wordScore.append(wordList[0] + wordList[1] + wordList[2] + wordList[3] + wordList[4] + wordList[5] + wordList[6] + wordList[7] + wordList[8] + wordList[9])
                        print(wordScore[foundCount])
                        scoreCount += round(scoreNum2*scoreMult)
                        scoreCount += round(400*scoreMult)
                        scoreAdd = "+ " + format(round(scoreNum2*scoreMult)+round(400*scoreMult))
                        scoreList.append(round(scoreNum2*scoreMult)+round(400*scoreMult))
                        scoreAdd1 = "Ten letter word!"
                        scoreAdd2 = "SUPERB!"
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scoreUpc = myFont4.render(scoreAdd2, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd
                            global scoreAdd1
                            global scoreAdd2
                            global scoreUp
                            global scoreUpb
                            global scoreUpc
                            scoreAdd = ""
                            scoreAdd1 = ""
                            scoreAdd2 = ""
                            scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                            scoreUpc = myFont4.render(scoreAdd2, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                        print("+" + format(round(400*scoreMult)) + " length score")
                        print("+" + format(round(scoreNum2*scoreMult)) + " letter score")
                        scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    if len(wordList) == 11:
                        correctSound.play()
                        wordScore.append(wordList[0] + wordList[1] + wordList[2] + wordList[3] + wordList[4] + wordList[5] + wordList[6] + wordList[7] + wordList[8] + wordList[9] + wordList[10])
                        print(wordScore[foundCount])
                        scoreCount += round(scoreNum2*scoreMult)
                        scoreCount += round(600*scoreMult)
                        scoreAdd = "+ " + format(round(scoreNum2*scoreMult)+round(600*scoreMult))
                        scoreList.append(round(scoreNum2*scoreMult)+round(600*scoreMult))
                        scoreAdd1 = "Eleven letter word!"
                        scoreAdd2 = "AMAZING!"
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scoreUpc = myFont4.render(scoreAdd2, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd
                            global scoreAdd1
                            global scoreAdd2
                            global scoreUp
                            global scoreUpb
                            global scoreUpc
                            scoreAdd = ""
                            scoreAdd1 = ""
                            scoreAdd2 = ""
                            scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                            scoreUpc = myFont4.render(scoreAdd2, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                        print("+" + format(round(600*scoreMult)) + " length score")
                        print("+" + format(round(scoreNum2*scoreMult)) + " letter score")
                        scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    if len(wordList) == 12:
                        correctSound.play()
                        wordScore.append(wordList[0] + wordList[1] + wordList[2] + wordList[3] + wordList[4] + wordList[5] + wordList[6] + wordList[7] + wordList[8] + wordList[9] + wordList[10] + wordList[11])
                        print(wordScore[foundCount])
                        scoreCount += round(scoreNum2*scoreMult)
                        scoreCount += round(1000*scoreMult)
                        scoreAdd = "+ " + format(round(scoreNum2*scoreMult)+round(1000*scoreMult))
                        scoreList.append(round(scoreNum2*scoreMult)+round(1000*scoreMult))
                        scoreAdd1 = "Twelve letter word!"
                        scoreAdd2 = "THE BEST!"
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scoreUpc = myFont4.render(scoreAdd2, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd
                            global scoreAdd1
                            global scoreAdd2
                            global scoreUp
                            global scoreUpb
                            global scoreUpc
                            scoreAdd = ""
                            scoreAdd1 = ""
                            scoreAdd2 = ""
                            scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                            scoreUpc = myFont4.render(scoreAdd2, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                        print("+" + format(round(1000*scoreMult)) + " length score")
                        print("+" + format(round(scoreNum2*scoreMult)) + " letter score")
                        scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    if len(wordList) == 13:
                        wrongSound.play()
                        letterWipe()

                    if wordList == lvl1word1 and lvl1word1CHK == 0:
                        lvl1word1CHK = 1
                        foundCount += 1
                        global foundLabel
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word2 and lvl1word2CHK == 0:
                        lvl1word2CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word3 and lvl1word3CHK == 0:
                        lvl1word3CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word4 and lvl1word4CHK == 0:
                        lvl1word4CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word5 and lvl1word5CHK == 0:
                        lvl1word5CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word6 and lvl1word6CHK == 0:
                        lvl1word6CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word7 and lvl1word7CHK == 0:
                        lvl1word7CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word8 and lvl1word8CHK == 0:
                        lvl1word8CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word9 and lvl1word9CHK == 0:
                        lvl1word9CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word10 and lvl1word10CHK == 0:
                        lvl1word10CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word11 and lvl1word11CHK == 0:
                        lvl1word11CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word12 and lvl1word12CHK == 0:
                        lvl1word12CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word13 and lvl1word13CHK == 0:
                        lvl1word13CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word14 and lvl1word14CHK == 0:
                        lvl1word14CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word15 and lvl1word15CHK == 0:
                        lvl1word15CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word16 and lvl1word16CHK == 0:
                        lvl1word16CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word17 and lvl1word17CHK == 0:
                        lvl1word17CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word18 and lvl1word18CHK == 0:
                        lvl1word18CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word19 and lvl1word19CHK == 0:
                        lvl1word19CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word20 and lvl1word20CHK == 0:
                        lvl1word20CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word21 and lvl1word21CHK == 0:
                        lvl1word21CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word22 and lvl1word22CHK == 0:
                        lvl1word22CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word23 and lvl1word23CHK == 0:
                        lvl1word23CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word24 and lvl1word24CHK == 0:
                        lvl1word24CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word25 and lvl1word25CHK == 0:
                        lvl1word25CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word26 and lvl1word26CHK == 0:
                        lvl1word26CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word27 and lvl1word27CHK == 0:
                        lvl1word27CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word28 and lvl1word28CHK == 0:
                        lvl1word28CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word29 and lvl1word29CHK == 0:
                        lvl1word29CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word30 and lvl1word30CHK == 0:
                        lvl1word30CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word31 and lvl1word31CHK == 0:
                        lvl1word31CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word32 and lvl1word32CHK == 0:
                        lvl1word32CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word33 and lvl1word33CHK == 0:
                        lvl1word33CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word34 and lvl1word34CHK == 0:
                        lvl1word34CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word35 and lvl1word35CHK == 0:
                        lvl1word35CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word36 and lvl1word36CHK == 0:
                        lvl1word36CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word37 and lvl1word37CHK == 0:
                        lvl1word37CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word38 and lvl1word38CHK == 0:
                        lvl1word38CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word39 and lvl1word39CHK == 0:
                        lvl1word39CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word40 and lvl1word40CHK == 0:
                        lvl1word40CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word41 and lvl1word41CHK == 0:
                        lvl1word41CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word42 and lvl1word42CHK == 0:
                        lvl1word42CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word43 and lvl1word43CHK == 0:
                        lvl1word43CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word44 and lvl1word44CHK == 0:
                        lvl1word44CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word45 and lvl1word45CHK == 0:
                        lvl1word45CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word46 and lvl1word46CHK == 0:
                        lvl1word46CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word47 and lvl1word47CHK == 0:
                        lvl1word47CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word48 and lvl1word48CHK == 0:
                        lvl1word48CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word49 and lvl1word49CHK == 0:
                        lvl1word49CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word50 and lvl1word50CHK == 0:
                        lvl1word50CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word51 and lvl1word51CHK == 0:
                        lvl1word51CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word52 and lvl1word52CHK == 0:
                        lvl1word52CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word53 and lvl1word53CHK == 0:
                        lvl1word53CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word54 and lvl1word54CHK == 0:
                        lvl1word54CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word55 and lvl1word55CHK == 0:
                        lvl1word55CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word56 and lvl1word56CHK == 0:
                        lvl1word56CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word57 and lvl1word57CHK == 0:
                        lvl1word57CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word58 and lvl1word58CHK == 0:
                        lvl1word58CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word59 and lvl1word59CHK == 0:
                        lvl1word59CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word60 and lvl1word60CHK == 0:
                        lvl1word60CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word61 and lvl1word61CHK == 0:
                        lvl1word61CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word62 and lvl1word62CHK == 0:
                        lvl1word62CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word63 and lvl1word63CHK == 0:
                        lvl1word63CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word64 and lvl1word64CHK == 0:
                        lvl1word64CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word65 and lvl1word65CHK == 0:
                        lvl1word65CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word66 and lvl1word66CHK == 0:
                        lvl1word66CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word67 and lvl1word67CHK == 0:
                        lvl1word67CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word68 and lvl1word68CHK == 0:
                        lvl1word68CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word69 and lvl1word69CHK == 0:
                        lvl1word69CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word70 and lvl1word70CHK == 0:
                        lvl1word70CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word71 and lvl1word71CHK == 0:
                        lvl1word71CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word72 and lvl1word72CHK == 0:
                        lvl1word72CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word73 and lvl1word73CHK == 0:
                        lvl1word73CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word74 and lvl1word74CHK == 0:
                        lvl1word74CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word75 and lvl1word75CHK == 0:
                        lvl1word75CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word76 and lvl1word76CHK == 0:
                        lvl1word76CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word77 and lvl1word77CHK == 0:
                        lvl1word77CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word78 and lvl1word78CHK == 0:
                        lvl1word78CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word79 and lvl1word79CHK == 0:
                        lvl1word79CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word80 and lvl1word80CHK == 0:
                        lvl1word80CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word81 and lvl1word81CHK == 0:
                        lvl1word81CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word82 and lvl1word82CHK == 0:
                        lvl1word82CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word83 and lvl1word83CHK == 0:
                        lvl1word83CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word84 and lvl1word84CHK == 0:
                        lvl1word84CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word85 and lvl1word85CHK == 0:
                        lvl1word85CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word86 and lvl1word86CHK == 0:
                        lvl1word86CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word87 and lvl1word87CHK == 0:
                        lvl1word87CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word88 and lvl1word88CHK == 0:
                        lvl1word88CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word89 and lvl1word89CHK == 0:
                        lvl1word89CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word90 and lvl1word90CHK == 0:
                        lvl1word90CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word91 and lvl1word91CHK == 0:
                        lvl1word91CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word92 and lvl1word92CHK == 0:
                        lvl1word92CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word93 and lvl1word93CHK == 0:
                        lvl1word93CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word94 and lvl1word94CHK == 0:
                        lvl1word94CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word95 and lvl1word95CHK == 0:
                        lvl1word95CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word96 and lvl1word96CHK == 0:
                        lvl1word96CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word97 and lvl1word97CHK == 0:
                        lvl1word97CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word98 and lvl1word98CHK == 0:
                        lvl1word98CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word99 and lvl1word99CHK == 0:
                        lvl1word99CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word100 and lvl1word100CHK == 0:
                        lvl1word100CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word101 and lvl1word101CHK == 0:
                        lvl1word101CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word102 and lvl1word102CHK == 0:
                        lvl1word102CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word103 and lvl1word103CHK == 0:
                        lvl1word103CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word104 and lvl1word104CHK == 0:
                        lvl1word104CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word105 and lvl1word105CHK == 0:
                        lvl1word105CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word106 and lvl1word106CHK == 0:
                        lvl1word106CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word107 and lvl1word107CHK == 0:
                        lvl1word107CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word108 and lvl1word108CHK == 0:
                        lvl1word108CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word109 and lvl1word109CHK == 0:
                        lvl1word109CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word110 and lvl1word110CHK == 0:
                        lvl1word110CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word111 and lvl1word111CHK == 0:
                        lvl1word111CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word112 and lvl1word112CHK == 0:
                        lvl1word112CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word113 and lvl1word113CHK == 0:
                        lvl1word113CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word114 and lvl1word114CHK == 0:
                        lvl1word114CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word115 and lvl1word115CHK == 0:
                        lvl1word115CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word116 and lvl1word116CHK == 0:
                        lvl1word116CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word117 and lvl1word117CHK == 0:
                        lvl1word117CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word118 and lvl1word118CHK == 0:
                        lvl1word118CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word119 and lvl1word119CHK == 0:
                        lvl1word119CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word120 and lvl1word120CHK == 0:
                        lvl1word120CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word121 and lvl1word121CHK == 0:
                        lvl1word121CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word122 and lvl1word122CHK == 0:
                        lvl1word122CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word123 and lvl1word123CHK == 0:
                        lvl1word123CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word124 and lvl1word124CHK == 0:
                        lvl1word124CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word125 and lvl1word125CHK == 0:
                        lvl1word125CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word126 and lvl1word126CHK == 0:
                        lvl1word126CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word127 and lvl1word127CHK == 0:
                        lvl1word127CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word128 and lvl1word128CHK == 0:
                        lvl1word128CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word129 and lvl1word129CHK == 0:
                        lvl1word129CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word130 and lvl1word130CHK == 0:
                        lvl1word130CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word131 and lvl1word131CHK == 0:
                        lvl1word131CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word132 and lvl1word132CHK == 0:
                        lvl1word132CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word133 and lvl1word133CHK == 0:
                        lvl1word133CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word134 and lvl1word134CHK == 0:
                        lvl1word134CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word135 and lvl1word135CHK == 0:
                        lvl1word135CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word136 and lvl1word136CHK == 0:
                        lvl1word136CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word137 and lvl1word137CHK == 0:
                        lvl1word137CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word138 and lvl1word138CHK == 0:
                        lvl1word138CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word139 and lvl1word139CHK == 0:
                        lvl1word139CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word140 and lvl1word140CHK == 0:
                        lvl1word140CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word141 and lvl1word141CHK == 0:
                        lvl1word141CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word142 and lvl1word142CHK == 0:
                        lvl1word142CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word143 and lvl1word143CHK == 0:
                        lvl1word143CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word144 and lvl1word144CHK == 0:
                        lvl1word144CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word145 and lvl1word145CHK == 0:
                        lvl1word145CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word146 and lvl1word146CHK == 0:
                        lvl1word146CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word147 and lvl1word147CHK == 0:
                        lvl1word147CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word148 and lvl1word148CHK == 0:
                        lvl1word148CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word149 and lvl1word149CHK == 0:
                        lvl1word149CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word150 and lvl1word150CHK == 0:
                        lvl1word150CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word151 and lvl1word151CHK == 0:
                        lvl1word151CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word152 and lvl1word152CHK == 0:
                        lvl1word152CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word153 and lvl1word153CHK == 0:
                        lvl1word153CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word154 and lvl1word154CHK == 0:
                        lvl1word154CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word155 and lvl1word155CHK == 0:
                        lvl1word155CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word156 and lvl1word156CHK == 0:
                        lvl1word156CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word157 and lvl1word157CHK == 0:
                        lvl1word157CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word158 and lvl1word158CHK == 0:
                        lvl1word158CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word159 and lvl1word159CHK == 0:
                        lvl1word159CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word160 and lvl1word160CHK == 0:
                        lvl1word160CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word161 and lvl1word161CHK == 0:
                        lvl1word161CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word162 and lvl1word162CHK == 0:
                        lvl1word162CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word163 and lvl1word163CHK == 0:
                        lvl1word163CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word164 and lvl1word164CHK == 0:
                        lvl1word164CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word165 and lvl1word165CHK == 0:
                        lvl1word165CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word166 and lvl1word166CHK == 0:
                        lvl1word166CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word167 and lvl1word167CHK == 0:
                        lvl1word167CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word168 and lvl1word168CHK == 0:
                        lvl1word168CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word169 and lvl1word169CHK == 0:
                        lvl1word169CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word170 and lvl1word170CHK == 0:
                        lvl1word170CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word171 and lvl1word171CHK == 0:
                        lvl1word171CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word172 and lvl1word172CHK == 0:
                        lvl1word172CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word173 and lvl1word173CHK == 0:
                        lvl1word173CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word174 and lvl1word174CHK == 0:
                        lvl1word174CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word175 and lvl1word175CHK == 0:
                        lvl1word175CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word176 and lvl1word176CHK == 0:
                        lvl1word176CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word177 and lvl1word177CHK == 0:
                        lvl1word177CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word178 and lvl1word178CHK == 0:
                        lvl1word178CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word179 and lvl1word179CHK == 0:
                        lvl1word179CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word180 and lvl1word180CHK == 0:
                        lvl1word180CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word181 and lvl1word181CHK == 0:
                        lvl1word181CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word182 and lvl1word182CHK == 0:
                        lvl1word182CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word183 and lvl1word183CHK == 0:
                        lvl1word183CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word184 and lvl1word184CHK == 0:
                        lvl1word184CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word185 and lvl1word185CHK == 0:
                        lvl1word185CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word186 and lvl1word186CHK == 0:
                        lvl1word186CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word187 and lvl1word187CHK == 0:
                        lvl1word187CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word188 and lvl1word188CHK == 0:
                        lvl1word188CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word189 and lvl1word189CHK == 0:
                        lvl1word189CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word190 and lvl1word190CHK == 0:
                        lvl1word190CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word191 and lvl1word191CHK == 0:
                        lvl1word191CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word192 and lvl1word192CHK == 0:
                        lvl1word192CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word193 and lvl1word193CHK == 0:
                        lvl1word193CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word194 and lvl1word194CHK == 0:
                        lvl1word194CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word195 and lvl1word195CHK == 0:
                        lvl1word195CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word196 and lvl1word196CHK == 0:
                        lvl1word196CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word197 and lvl1word197CHK == 0:
                        lvl1word197CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word198 and lvl1word198CHK == 0:
                        lvl1word198CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word199 and lvl1word199CHK == 0:
                        lvl1word199CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word200 and lvl1word200CHK == 0:
                        lvl1word200CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word201 and lvl1word201CHK == 0:
                        lvl1word201CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word202 and lvl1word202CHK == 0:
                        lvl1word202CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word203 and lvl1word203CHK == 0:
                        lvl1word203CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word204 and lvl1word204CHK == 0:
                        lvl1word204CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word205 and lvl1word205CHK == 0:
                        lvl1word205CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word206 and lvl1word206CHK == 0:
                        lvl1word206CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word207 and lvl1word207CHK == 0:
                        lvl1word207CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word208 and lvl1word208CHK == 0:
                        lvl1word208CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word209 and lvl1word209CHK == 0:
                        lvl1word209CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word210 and lvl1word210CHK == 0:
                        lvl1word210CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word211 and lvl1word211CHK == 0:
                        lvl1word211CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word212 and lvl1word212CHK == 0:
                        lvl1word212CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word213 and lvl1word213CHK == 0:
                        lvl1word213CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word214 and lvl1word214CHK == 0:
                        lvl1word214CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word215 and lvl1word215CHK == 0:
                        lvl1word215CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word216 and lvl1word216CHK == 0:
                        lvl1word216CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word217 and lvl1word217CHK == 0:
                        lvl1word217CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word218 and lvl1word218CHK == 0:
                        lvl1word218CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word219 and lvl1word219CHK == 0:
                        lvl1word219CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word220 and lvl1word220CHK == 0:
                        lvl1word220CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word221 and lvl1word221CHK == 0:
                        lvl1word221CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word222 and lvl1word222CHK == 0:
                        lvl1word222CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word223 and lvl1word223CHK == 0:
                        lvl1word223CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word224 and lvl1word224CHK == 0:
                        lvl1word224CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word225 and lvl1word225CHK == 0:
                        lvl1word225CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word226 and lvl1word226CHK == 0:
                        lvl1word226CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word227 and lvl1word227CHK == 0:
                        lvl1word227CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word228 and lvl1word228CHK == 0:
                        lvl1word228CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word229 and lvl1word229CHK == 0:
                        lvl1word229CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word230 and lvl1word230CHK == 0:
                        lvl1word230CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word231 and lvl1word231CHK == 0:
                        lvl1word231CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word232 and lvl1word232CHK == 0:
                        lvl1word232CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word233 and lvl1word233CHK == 0:
                        lvl1word233CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word234 and lvl1word234CHK == 0:
                        lvl1word234CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word235 and lvl1word235CHK == 0:
                        lvl1word235CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word236 and lvl1word236CHK == 0:
                        lvl1word236CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word237 and lvl1word237CHK == 0:
                        lvl1word237CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word238 and lvl1word238CHK == 0:
                        lvl1word238CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word239 and lvl1word239CHK == 0:
                        lvl1word239CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word240 and lvl1word240CHK == 0:
                        lvl1word240CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word241 and lvl1word241CHK == 0:
                        lvl1word241CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word242 and lvl1word242CHK == 0:
                        lvl1word242CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word243 and lvl1word243CHK == 0:
                        lvl1word243CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word244 and lvl1word244CHK == 0:
                        lvl1word244CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word245 and lvl1word245CHK == 0:
                        lvl1word245CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word246 and lvl1word246CHK == 0:
                        lvl1word246CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word247 and lvl1word247CHK == 0:
                        lvl1word247CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word248 and lvl1word248CHK == 0:
                        lvl1word248CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word249 and lvl1word249CHK == 0:
                        lvl1word249CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word250 and lvl1word250CHK == 0:
                        lvl1word250CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word251 and lvl1word251CHK == 0:
                        lvl1word251CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word252 and lvl1word252CHK == 0:
                        lvl1word252CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word253 and lvl1word253CHK == 0:
                        lvl1word253CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word254 and lvl1word254CHK == 0:
                        lvl1word254CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word255 and lvl1word255CHK == 0:
                        lvl1word255CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word256 and lvl1word256CHK == 0:
                        lvl1word256CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word257 and lvl1word257CHK == 0:
                        lvl1word257CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word258 and lvl1word258CHK == 0:
                        lvl1word258CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word259 and lvl1word259CHK == 0:
                        lvl1word259CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word260 and lvl1word260CHK == 0:
                        lvl1word260CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word261 and lvl1word261CHK == 0:
                        lvl1word261CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word262 and lvl1word262CHK == 0:
                        lvl1word262CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word263 and lvl1word263CHK == 0:
                        lvl1word263CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word264 and lvl1word264CHK == 0:
                        lvl1word264CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word265 and lvl1word265CHK == 0:
                        lvl1word265CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word266 and lvl1word266CHK == 0:
                        lvl1word266CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word267 and lvl1word267CHK == 0:
                        lvl1word267CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word268 and lvl1word268CHK == 0:
                        lvl1word268CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word269 and lvl1word269CHK == 0:
                        lvl1word269CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word270 and lvl1word270CHK == 0:
                        lvl1word270CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word271 and lvl1word271CHK == 0:
                        lvl1word271CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word272 and lvl1word272CHK == 0:
                        lvl1word272CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word273 and lvl1word273CHK == 0:
                        lvl1word273CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word274 and lvl1word274CHK == 0:
                        lvl1word274CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word275 and lvl1word275CHK == 0:
                        lvl1word275CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word276 and lvl1word276CHK == 0:
                        lvl1word276CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word277 and lvl1word277CHK == 0:
                        lvl1word277CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word278 and lvl1word278CHK == 0:
                        lvl1word278CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word279 and lvl1word279CHK == 0:
                        lvl1word279CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word280 and lvl1word280CHK == 0:
                        lvl1word280CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word281 and lvl1word281CHK == 0:
                        lvl1word281CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word282 and lvl1word282CHK == 0:
                        lvl1word282CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word283 and lvl1word283CHK == 0:
                        lvl1word283CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word284 and lvl1word284CHK == 0:
                        lvl1word284CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word285 and lvl1word285CHK == 0:
                        lvl1word285CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word286 and lvl1word286CHK == 0:
                        lvl1word286CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word287 and lvl1word287CHK == 0:
                        lvl1word287CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word288 and lvl1word288CHK == 0:
                        lvl1word288CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word289 and lvl1word289CHK == 0:
                        lvl1word289CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word290 and lvl1word290CHK == 0:
                        lvl1word290CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word291 and lvl1word291CHK == 0:
                        lvl1word291CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word292 and lvl1word292CHK == 0:
                        lvl1word292CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word293 and lvl1word293CHK == 0:
                        lvl1word293CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word294 and lvl1word294CHK == 0:
                        lvl1word294CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word295 and lvl1word295CHK == 0:
                        lvl1word295CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word296 and lvl1word296CHK == 0:
                        lvl1word296CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word297 and lvl1word297CHK == 0:
                        lvl1word297CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word298 and lvl1word298CHK == 0:
                        lvl1word298CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word299 and lvl1word299CHK == 0:
                        lvl1word299CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word300 and lvl1word300CHK == 0:
                        lvl1word300CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word301 and lvl1word301CHK == 0:
                        lvl1word301CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word302 and lvl1word302CHK == 0:
                        lvl1word302CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word303 and lvl1word303CHK == 0:
                        lvl1word303CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word304 and lvl1word304CHK == 0:
                        lvl1word304CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word305 and lvl1word305CHK == 0:
                        lvl1word305CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word306 and lvl1word306CHK == 0:
                        lvl1word306CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word307 and lvl1word307CHK == 0:
                        lvl1word307CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word308 and lvl1word308CHK == 0:
                        lvl1word308CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word309 and lvl1word309CHK == 0:
                        lvl1word309CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word310 and lvl1word300CHK == 0:
                        lvl1word310CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word311 and lvl1word311CHK == 0:
                        lvl1word311CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word312 and lvl1word312CHK == 0:
                        lvl1word312CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word313 and lvl1word313CHK == 0:
                        lvl1word313CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word314 and lvl1word314CHK == 0:
                        lvl1word314CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word315 and lvl1word315CHK == 0:
                        lvl1word315CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word316 and lvl1word316CHK == 0:
                        lvl1word316CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word317 and lvl1word317CHK == 0:
                        lvl1word317CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word318 and lvl1word318CHK == 0:
                        lvl1word318CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word319 and lvl1word319CHK == 0:
                        lvl1word319CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word320 and lvl1word320CHK == 0:
                        lvl1word320CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word321 and lvl1word321CHK == 0:
                        lvl1word321CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word322 and lvl1word322CHK == 0:
                        lvl1word322CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word323 and lvl1word323CHK == 0:
                        lvl1word323CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word324 and lvl1word324CHK == 0:
                        lvl1word324CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word325 and lvl1word325CHK == 0:
                        lvl1word325CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word326 and lvl1word326CHK == 0:
                        lvl1word326CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word327 and lvl1word327CHK == 0:
                        lvl1word327CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word328 and lvl1word328CHK == 0:
                        lvl1word328CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word329 and lvl1word329CHK == 0:
                        lvl1word329CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word330 and lvl1word330CHK == 0:
                        lvl1word330CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word331 and lvl1word331CHK == 0:
                        lvl1word331CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word332 and lvl1word332CHK == 0:
                        lvl1word332CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word333 and lvl1word333CHK == 0:
                        lvl1word333CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word334 and lvl1word334CHK == 0:
                        lvl1word334CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word335 and lvl1word335CHK == 0:
                        lvl1word335CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word336 and lvl1word336CHK == 0:
                        lvl1word336CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word337 and lvl1word337CHK == 0:
                        lvl1word337CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word338 and lvl1word338CHK == 0:
                        lvl1word338CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word339 and lvl1word339CHK == 0:
                        lvl1word339CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word340 and lvl1word340CHK == 0:
                        lvl1word340CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word341 and lvl1word341CHK == 0:
                        lvl1word341CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word342 and lvl1word342CHK == 0:
                        lvl1word342CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word343 and lvl1word343CHK == 0:
                        lvl1word343CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word344 and lvl1word344CHK == 0:
                        lvl1word344CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word345 and lvl1word345CHK == 0:
                        lvl1word345CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word346 and lvl1word346CHK == 0:
                        lvl1word346CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word347 and lvl1word347CHK == 0:
                        lvl1word347CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word348 and lvl1word348CHK == 0:
                        lvl1word348CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word349 and lvl1word349CHK == 0:
                        lvl1word349CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word350 and lvl1word350CHK == 0:
                        lvl1word350CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word351 and lvl1word351CHK == 0:
                        lvl1word351CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word352 and lvl1word352CHK == 0:
                        lvl1word352CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word353 and lvl1word353CHK == 0:
                        lvl1word353CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word354 and lvl1word354CHK == 0:
                        lvl1word354CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word355 and lvl1word355CHK == 0:
                        lvl1word355CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word356 and lvl1word356CHK == 0:
                        lvl1word356CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word357 and lvl1word357CHK == 0:
                        lvl1word357CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word358 and lvl1word358CHK == 0:
                        lvl1word358CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word359 and lvl1word359CHK == 0:
                        lvl1word359CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word360 and lvl1word360CHK == 0:
                        lvl1word360CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word361 and lvl1word361CHK == 0:
                        lvl1word361CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word362 and lvl1word362CHK == 0:
                        lvl1word362CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word363 and lvl1word363CHK == 0:
                        lvl1word363CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word364 and lvl1word364CHK == 0:
                        lvl1word364CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word365 and lvl1word365CHK == 0:
                        lvl1word365CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word366 and lvl1word366CHK == 0:
                        lvl1word366CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word367 and lvl1word367CHK == 0:
                        lvl1word367CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word368 and lvl1word368CHK == 0:
                        lvl1word368CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word369 and lvl1word369CHK == 0:
                        lvl1word369CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word370 and lvl1word370CHK == 0:
                        lvl1word370CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word371 and lvl1word371CHK == 0:
                        lvl1word371CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word372 and lvl1word372CHK == 0:
                        lvl1word372CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word373 and lvl1word373CHK == 0:
                        lvl1word373CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word374 and lvl1word374CHK == 0:
                        lvl1word374CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word375 and lvl1word375CHK == 0:
                        lvl1word375CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word376 and lvl1word376CHK == 0:
                        lvl1word376CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word377 and lvl1word377CHK == 0:
                        lvl1word377CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word378 and lvl1word378CHK == 0:
                        lvl1word378CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word379 and lvl1word379CHK == 0:
                        lvl1word379CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word380 and lvl1word380CHK == 0:
                        lvl1word380CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word381 and lvl1word381CHK == 0:
                        lvl1word381CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word382 and lvl1word382CHK == 0:
                        lvl1word382CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word383 and lvl1word383CHK == 0:
                        lvl1word383CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word384 and lvl1word384CHK == 0:
                        lvl1word384CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word385 and lvl1word385CHK == 0:
                        lvl1word385CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word386 and lvl1word386CHK == 0:
                        lvl1word386CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word387 and lvl1word387CHK == 0:
                        lvl1word387CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word388 and lvl1word388CHK == 0:
                        lvl1word388CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word389 and lvl1word389CHK == 0:
                        lvl1word389CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word390 and lvl1word390CHK == 0:
                        lvl1word390CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word391 and lvl1word391CHK == 0:
                        lvl1word391CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word392 and lvl1word392CHK == 0:
                        lvl1word392CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word393 and lvl1word393CHK == 0:
                        lvl1word393CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word394 and lvl1word394CHK == 0:
                        lvl1word394CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word395 and lvl1word395CHK == 0:
                        lvl1word395CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word396 and lvl1word396CHK == 0:
                        lvl1word396CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word397 and lvl1word397CHK == 0:
                        lvl1word397CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word398 and lvl1word398CHK == 0:
                        lvl1word398CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word399 and lvl1word399CHK == 0:
                        lvl1word399CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word400 and lvl1word400CHK == 0:
                        lvl1word400CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word401 and lvl1word401CHK == 0:
                        lvl1word401CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word402 and lvl1word402CHK == 0:
                        lvl1word402CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word403 and lvl1word403CHK == 0:
                        lvl1word403CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word404 and lvl1word404CHK == 0:
                        lvl1word404CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word405 and lvl1word405CHK == 0:
                        lvl1word405CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word406 and lvl1word406CHK == 0:
                        lvl1word406CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word407 and lvl1word407CHK == 0:
                        lvl1word407CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word408 and lvl1word408CHK == 0:
                        lvl1word408CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word409 and lvl1word409CHK == 0:
                        lvl1word409CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word410 and lvl1word400CHK == 0:
                        lvl1word410CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word411 and lvl1word411CHK == 0:
                        lvl1word411CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word412 and lvl1word412CHK == 0:
                        lvl1word412CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word413 and lvl1word413CHK == 0:
                        lvl1word413CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word414 and lvl1word414CHK == 0:
                        lvl1word414CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word415 and lvl1word415CHK == 0:
                        lvl1word415CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word416 and lvl1word416CHK == 0:
                        lvl1word416CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word417 and lvl1word417CHK == 0:
                        lvl1word417CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word418 and lvl1word418CHK == 0:
                        lvl1word418CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word419 and lvl1word419CHK == 0:
                        lvl1word419CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word420 and lvl1word420CHK == 0:
                        lvl1word420CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word421 and lvl1word421CHK == 0:
                        lvl1word421CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word422 and lvl1word422CHK == 0:
                        lvl1word422CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word423 and lvl1word423CHK == 0:
                        lvl1word423CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word424 and lvl1word424CHK == 0:
                        lvl1word424CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word425 and lvl1word425CHK == 0:
                        lvl1word425CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word426 and lvl1word426CHK == 0:
                        lvl1word426CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word427 and lvl1word427CHK == 0:
                        lvl1word427CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word428 and lvl1word428CHK == 0:
                        lvl1word428CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word429 and lvl1word429CHK == 0:
                        lvl1word429CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word430 and lvl1word430CHK == 0:
                        lvl1word430CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word431 and lvl1word431CHK == 0:
                        lvl1word431CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word432 and lvl1word432CHK == 0:
                        lvl1word432CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word433 and lvl1word433CHK == 0:
                        lvl1word433CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word434 and lvl1word434CHK == 0:
                        lvl1word434CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word435 and lvl1word435CHK == 0:
                        lvl1word435CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word436 and lvl1word436CHK == 0:
                        lvl1word436CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word437 and lvl1word437CHK == 0:
                        lvl1word437CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word438 and lvl1word438CHK == 0:
                        lvl1word438CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word439 and lvl1word439CHK == 0:
                        lvl1word439CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word440 and lvl1word440CHK == 0:
                        lvl1word440CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word441 and lvl1word441CHK == 0:
                        lvl1word441CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word442 and lvl1word442CHK == 0:
                        lvl1word442CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word443 and lvl1word443CHK == 0:
                        lvl1word443CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word444 and lvl1word444CHK == 0:
                        lvl1word444CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word445 and lvl1word445CHK == 0:
                        lvl1word445CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word446 and lvl1word446CHK == 0:
                        lvl1word446CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word447 and lvl1word447CHK == 0:
                        lvl1word447CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word448 and lvl1word448CHK == 0:
                        lvl1word448CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word449 and lvl1word449CHK == 0:
                        lvl1word449CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word450 and lvl1word450CHK == 0:
                        lvl1word450CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word451 and lvl1word451CHK == 0:
                        lvl1word451CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word452 and lvl1word452CHK == 0:
                        lvl1word452CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word453 and lvl1word453CHK == 0:
                        lvl1word453CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word454 and lvl1word454CHK == 0:
                        lvl1word454CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word455 and lvl1word455CHK == 0:
                        lvl1word455CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word456 and lvl1word456CHK == 0:
                        lvl1word456CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word457 and lvl1word457CHK == 0:
                        lvl1word457CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word458 and lvl1word458CHK == 0:
                        lvl1word458CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word459 and lvl1word459CHK == 0:
                        lvl1word459CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word460 and lvl1word460CHK == 0:
                        lvl1word460CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word461 and lvl1word461CHK == 0:
                        lvl1word461CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word462 and lvl1word462CHK == 0:
                        lvl1word462CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word463 and lvl1word463CHK == 0:
                        lvl1word463CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word464 and lvl1word464CHK == 0:
                        lvl1word464CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word465 and lvl1word465CHK == 0:
                        lvl1word465CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word466 and lvl1word466CHK == 0:
                        lvl1word466CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word467 and lvl1word467CHK == 0:
                        lvl1word467CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word468 and lvl1word468CHK == 0:
                        lvl1word468CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word469 and lvl1word469CHK == 0:
                        lvl1word469CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word470 and lvl1word470CHK == 0:
                        lvl1word470CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word471 and lvl1word471CHK == 0:
                        lvl1word471CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word472 and lvl1word472CHK == 0:
                        lvl1word472CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word473 and lvl1word473CHK == 0:
                        lvl1word473CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word474 and lvl1word474CHK == 0:
                        lvl1word474CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word475 and lvl1word475CHK == 0:
                        lvl1word475CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word476 and lvl1word476CHK == 0:
                        lvl1word476CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word477 and lvl1word477CHK == 0:
                        lvl1word477CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word478 and lvl1word478CHK == 0:
                        lvl1word478CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word479 and lvl1word479CHK == 0:
                        lvl1word479CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word480 and lvl1word480CHK == 0:
                        lvl1word480CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word481 and lvl1word481CHK == 0:
                        lvl1word481CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word482 and lvl1word482CHK == 0:
                        lvl1word482CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word483 and lvl1word483CHK == 0:
                        lvl1word483CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word484 and lvl1word484CHK == 0:
                        lvl1word484CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word485 and lvl1word485CHK == 0:
                        lvl1word485CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word486 and lvl1word486CHK == 0:
                        lvl1word486CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word487 and lvl1word487CHK == 0:
                        lvl1word487CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word488 and lvl1word488CHK == 0:
                        lvl1word488CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word489 and lvl1word489CHK == 0:
                        lvl1word489CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word490 and lvl1word490CHK == 0:
                        lvl1word490CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word491 and lvl1word491CHK == 0:
                        lvl1word491CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word492 and lvl1word492CHK == 0:
                        lvl1word492CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word493 and lvl1word493CHK == 0:
                        lvl1word493CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word494 and lvl1word494CHK == 0:
                        lvl1word494CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word495 and lvl1word495CHK == 0:
                        lvl1word495CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word496 and lvl1word496CHK == 0:
                        lvl1word496CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word497 and lvl1word497CHK == 0:
                        lvl1word497CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word498 and lvl1word498CHK == 0:
                        lvl1word498CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word499 and lvl1word499CHK == 0:
                        lvl1word499CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word500 and lvl1word500CHK == 0:
                        lvl1word500CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word501 and lvl1word501CHK == 0:
                        lvl1word501CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word502 and lvl1word502CHK == 0:
                        lvl1word502CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word503 and lvl1word503CHK == 0:
                        lvl1word503CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word504 and lvl1word504CHK == 0:
                        lvl1word504CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word505 and lvl1word505CHK == 0:
                        lvl1word505CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word506 and lvl1word506CHK == 0:
                        lvl1word506CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word507 and lvl1word507CHK == 0:
                        lvl1word507CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word508 and lvl1word508CHK == 0:
                        lvl1word508CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word509 and lvl1word509CHK == 0:
                        lvl1word509CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word510 and lvl1word500CHK == 0:
                        lvl1word510CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word511 and lvl1word511CHK == 0:
                        lvl1word511CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word512 and lvl1word512CHK == 0:
                        lvl1word512CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word513 and lvl1word513CHK == 0:
                        lvl1word513CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word514 and lvl1word514CHK == 0:
                        lvl1word514CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word515 and lvl1word515CHK == 0:
                        lvl1word515CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word516 and lvl1word516CHK == 0:
                        lvl1word516CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word517 and lvl1word517CHK == 0:
                        lvl1word517CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word518 and lvl1word518CHK == 0:
                        lvl1word518CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word519 and lvl1word519CHK == 0:
                        lvl1word519CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word520 and lvl1word520CHK == 0:
                        lvl1word520CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word521 and lvl1word521CHK == 0:
                        lvl1word521CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word522 and lvl1word522CHK == 0:
                        lvl1word522CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)                
                    if wordList == lvl1word523 and lvl1word523CHK == 0:
                        lvl1word523CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word524 and lvl1word524CHK == 0:
                        lvl1word524CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word525 and lvl1word525CHK == 0:
                        lvl1word525CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word526 and lvl1word526CHK == 0:
                        lvl1word526CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word527 and lvl1word527CHK == 0:
                        lvl1word527CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word528 and lvl1word528CHK == 0:
                        lvl1word528CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word529 and lvl1word529CHK == 0:
                        lvl1word529CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word530 and lvl1word530CHK == 0:
                        lvl1word530CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word531 and lvl1word531CHK == 0:
                        lvl1word531CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word532 and lvl1word532CHK == 0:
                        lvl1word532CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word533 and lvl1word533CHK == 0:
                        lvl1word533CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word534 and lvl1word534CHK == 0:
                        lvl1word534CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word535 and lvl1word535CHK == 0:
                        lvl1word535CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word536 and lvl1word536CHK == 0:
                        lvl1word536CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word537 and lvl1word537CHK == 0:
                        lvl1word537CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word538 and lvl1word538CHK == 0:
                        lvl1word538CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word539 and lvl1word539CHK == 0:
                        lvl1word539CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word540 and lvl1word540CHK == 0:
                        lvl1word540CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word541 and lvl1word541CHK == 0:
                        lvl1word541CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word542 and lvl1word542CHK == 0:
                        lvl1word542CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word543 and lvl1word543CHK == 0:
                        lvl1word543CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word544 and lvl1word544CHK == 0:
                        lvl1word544CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word545 and lvl1word545CHK == 0:
                        lvl1word545CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word546 and lvl1word546CHK == 0:
                        lvl1word546CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word547 and lvl1word547CHK == 0:
                        lvl1word547CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word548 and lvl1word548CHK == 0:
                        lvl1word548CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word549 and lvl1word549CHK == 0:
                        lvl1word549CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word550 and lvl1word550CHK == 0:
                        lvl1word550CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word551 and lvl1word551CHK == 0:
                        lvl1word551CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word552 and lvl1word552CHK == 0:
                        lvl1word552CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word553 and lvl1word553CHK == 0:
                        lvl1word553CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word554 and lvl1word554CHK == 0:
                        lvl1word554CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word555 and lvl1word555CHK == 0:
                        lvl1word555CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word556 and lvl1word556CHK == 0:
                        lvl1word556CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word557 and lvl1word557CHK == 0:
                        lvl1word557CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word558 and lvl1word558CHK == 0:
                        lvl1word558CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word559 and lvl1word559CHK == 0:
                        lvl1word559CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word560 and lvl1word560CHK == 0:
                        lvl1word560CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word561 and lvl1word561CHK == 0:
                        lvl1word561CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word562 and lvl1word562CHK == 0:
                        lvl1word562CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word563 and lvl1word563CHK == 0:
                        lvl1word563CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word564 and lvl1word564CHK == 0:
                        lvl1word564CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word565 and lvl1word565CHK == 0:
                        lvl1word565CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word566 and lvl1word566CHK == 0:
                        lvl1word566CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word567 and lvl1word567CHK == 0:
                        lvl1word567CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word568 and lvl1word568CHK == 0:
                        lvl1word568CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word569 and lvl1word569CHK == 0:
                        lvl1word569CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word570 and lvl1word570CHK == 0:
                        lvl1word570CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word571 and lvl1word571CHK == 0:
                        lvl1word571CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word572 and lvl1word572CHK == 0:
                        lvl1word572CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word573 and lvl1word573CHK == 0:
                        lvl1word573CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word574 and lvl1word574CHK == 0:
                        lvl1word574CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word575 and lvl1word575CHK == 0:
                        lvl1word575CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word576 and lvl1word576CHK == 0:
                        lvl1word576CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word577 and lvl1word577CHK == 0:
                        lvl1word577CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word578 and lvl1word578CHK == 0:
                        lvl1word578CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word579 and lvl1word579CHK == 0:
                        lvl1word579CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word580 and lvl1word580CHK == 0:
                        lvl1word580CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word581 and lvl1word581CHK == 0:
                        lvl1word581CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word582 and lvl1word582CHK == 0:
                        lvl1word582CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word583 and lvl1word583CHK == 0:
                        lvl1word583CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word584 and lvl1word584CHK == 0:
                        lvl1word584CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word585 and lvl1word585CHK == 0:
                        lvl1word585CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word586 and lvl1word586CHK == 0:
                        lvl1word586CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word587 and lvl1word587CHK == 0:
                        lvl1word587CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word588 and lvl1word588CHK == 0:
                        lvl1word588CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word589 and lvl1word589CHK == 0:
                        lvl1word589CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word590 and lvl1word590CHK == 0:
                        lvl1word590CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word591 and lvl1word591CHK == 0:
                        lvl1word591CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word592 and lvl1word592CHK == 0:
                        lvl1word592CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word593 and lvl1word593CHK == 0:
                        lvl1word593CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word594 and lvl1word594CHK == 0:
                        lvl1word594CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word595 and lvl1word595CHK == 0:
                        lvl1word595CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word596 and lvl1word596CHK == 0:
                        lvl1word596CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word597 and lvl1word597CHK == 0:
                        lvl1word597CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word598 and lvl1word598CHK == 0:
                        lvl1word598CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word599 and lvl1word599CHK == 0:
                        lvl1word599CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word600 and lvl1word600CHK == 0:
                        lvl1word600CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word601 and lvl1word601CHK == 0:
                        lvl1word601CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word602 and lvl1word602CHK == 0:
                        lvl1word602CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word603 and lvl1word603CHK == 0:
                        lvl1word603CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word604 and lvl1word604CHK == 0:
                        lvl1word604CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word605 and lvl1word605CHK == 0:
                        lvl1word605CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word606 and lvl1word606CHK == 0:
                        lvl1word606CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word607 and lvl1word607CHK == 0:
                        lvl1word607CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word608 and lvl1word608CHK == 0:
                        lvl1word608CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word609 and lvl1word609CHK == 0:
                        lvl1word609CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word610 and lvl1word600CHK == 0:
                        lvl1word610CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word611 and lvl1word611CHK == 0:
                        lvl1word611CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word612 and lvl1word612CHK == 0:
                        lvl1word612CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word613 and lvl1word613CHK == 0:
                        lvl1word613CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word614 and lvl1word614CHK == 0:
                        lvl1word614CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word615 and lvl1word615CHK == 0:
                        lvl1word615CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word616 and lvl1word616CHK == 0:
                        lvl1word616CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word617 and lvl1word617CHK == 0:
                        lvl1word617CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word618 and lvl1word618CHK == 0:
                        lvl1word618CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word619 and lvl1word619CHK == 0:
                        lvl1word619CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word620 and lvl1word620CHK == 0:
                        lvl1word620CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word621 and lvl1word621CHK == 0:
                        lvl1word621CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word622 and lvl1word622CHK == 0:
                        lvl1word622CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)                
                    if wordList == lvl1word623 and lvl1word623CHK == 0:
                        lvl1word623CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word624 and lvl1word624CHK == 0:
                        lvl1word624CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word625 and lvl1word625CHK == 0:
                        lvl1word625CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word626 and lvl1word626CHK == 0:
                        lvl1word626CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word627 and lvl1word627CHK == 0:
                        lvl1word627CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word628 and lvl1word628CHK == 0:
                        lvl1word628CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word629 and lvl1word629CHK == 0:
                        lvl1word629CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word630 and lvl1word630CHK == 0:
                        lvl1word630CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word631 and lvl1word631CHK == 0:
                        lvl1word631CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word632 and lvl1word632CHK == 0:
                        lvl1word632CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word633 and lvl1word633CHK == 0:
                        lvl1word633CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word634 and lvl1word634CHK == 0:
                        lvl1word634CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word635 and lvl1word635CHK == 0:
                        lvl1word635CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word636 and lvl1word636CHK == 0:
                        lvl1word636CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word637 and lvl1word637CHK == 0:
                        lvl1word637CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word638 and lvl1word638CHK == 0:
                        lvl1word638CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word639 and lvl1word639CHK == 0:
                        lvl1word639CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word640 and lvl1word640CHK == 0:
                        lvl1word640CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word641 and lvl1word641CHK == 0:
                        lvl1word641CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word642 and lvl1word642CHK == 0:
                        lvl1word642CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word643 and lvl1word643CHK == 0:
                        lvl1word643CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word644 and lvl1word644CHK == 0:
                        lvl1word644CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word645 and lvl1word645CHK == 0:
                        lvl1word645CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word646 and lvl1word646CHK == 0:
                        lvl1word646CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word647 and lvl1word647CHK == 0:
                        lvl1word647CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word648 and lvl1word648CHK == 0:
                        lvl1word648CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word649 and lvl1word649CHK == 0:
                        lvl1word649CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word650 and lvl1word650CHK == 0:
                        lvl1word650CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word651 and lvl1word651CHK == 0:
                        lvl1word651CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word652 and lvl1word652CHK == 0:
                        lvl1word652CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word653 and lvl1word653CHK == 0:
                        lvl1word653CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word654 and lvl1word654CHK == 0:
                        lvl1word654CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word655 and lvl1word655CHK == 0:
                        lvl1word655CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word656 and lvl1word656CHK == 0:
                        lvl1word656CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word657 and lvl1word657CHK == 0:
                        lvl1word657CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word658 and lvl1word658CHK == 0:
                        lvl1word658CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word659 and lvl1word659CHK == 0:
                        lvl1word659CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word660 and lvl1word660CHK == 0:
                        lvl1word660CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word661 and lvl1word661CHK == 0:
                        lvl1word661CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word662 and lvl1word662CHK == 0:
                        lvl1word662CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word663 and lvl1word663CHK == 0:
                        lvl1word663CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word664 and lvl1word664CHK == 0:
                        lvl1word664CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word665 and lvl1word665CHK == 0:
                        lvl1word665CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word666 and lvl1word666CHK == 0:
                        lvl1word666CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word667 and lvl1word667CHK == 0:
                        lvl1word667CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word668 and lvl1word668CHK == 0:
                        lvl1word668CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word669 and lvl1word669CHK == 0:
                        lvl1word669CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word670 and lvl1word670CHK == 0:
                        lvl1word670CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word671 and lvl1word671CHK == 0:
                        lvl1word671CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word672 and lvl1word672CHK == 0:
                        lvl1word672CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word673 and lvl1word673CHK == 0:
                        lvl1word673CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word674 and lvl1word674CHK == 0:
                        lvl1word674CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word675 and lvl1word675CHK == 0:
                        lvl1word675CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word676 and lvl1word676CHK == 0:
                        lvl1word676CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word677 and lvl1word677CHK == 0:
                        lvl1word677CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word678 and lvl1word678CHK == 0:
                        lvl1word678CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word679 and lvl1word679CHK == 0:
                        lvl1word679CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word680 and lvl1word680CHK == 0:
                        lvl1word680CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word681 and lvl1word681CHK == 0:
                        lvl1word681CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word682 and lvl1word682CHK == 0:
                        lvl1word682CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word683 and lvl1word683CHK == 0:
                        lvl1word683CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word684 and lvl1word684CHK == 0:
                        lvl1word684CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word685 and lvl1word685CHK == 0:
                        lvl1word685CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word686 and lvl1word686CHK == 0:
                        lvl1word686CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word687 and lvl1word687CHK == 0:
                        lvl1word687CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word688 and lvl1word688CHK == 0:
                        lvl1word688CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word689 and lvl1word689CHK == 0:
                        lvl1word689CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word690 and lvl1word690CHK == 0:
                        lvl1word690CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word691 and lvl1word691CHK == 0:
                        lvl1word691CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word692 and lvl1word692CHK == 0:
                        lvl1word692CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word693 and lvl1word693CHK == 0:
                        lvl1word693CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word694 and lvl1word694CHK == 0:
                        lvl1word694CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word695 and lvl1word695CHK == 0:
                        lvl1word695CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word696 and lvl1word696CHK == 0:
                        lvl1word696CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word697 and lvl1word697CHK == 0:
                        lvl1word697CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word698 and lvl1word698CHK == 0:
                        lvl1word698CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word699 and lvl1word699CHK == 0:
                        lvl1word699CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word700 and lvl1word700CHK == 0:
                        lvl1word700CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word701 and lvl1word701CHK == 0:
                        lvl1word701CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word702 and lvl1word702CHK == 0:
                        lvl1word702CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word703 and lvl1word703CHK == 0:
                        lvl1word703CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word704 and lvl1word704CHK == 0:
                        lvl1word704CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word705 and lvl1word705CHK == 0:
                        lvl1word705CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word706 and lvl1word706CHK == 0:
                        lvl1word706CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word707 and lvl1word707CHK == 0:
                        lvl1word707CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word708 and lvl1word708CHK == 0:
                        lvl1word708CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word709 and lvl1word709CHK == 0:
                        lvl1word709CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word710 and lvl1word700CHK == 0:
                        lvl1word710CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word711 and lvl1word711CHK == 0:
                        lvl1word711CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word712 and lvl1word712CHK == 0:
                        lvl1word712CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word713 and lvl1word713CHK == 0:
                        lvl1word713CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word714 and lvl1word714CHK == 0:
                        lvl1word714CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word715 and lvl1word715CHK == 0:
                        lvl1word715CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word716 and lvl1word716CHK == 0:
                        lvl1word716CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word717 and lvl1word717CHK == 0:
                        lvl1word717CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word718 and lvl1word718CHK == 0:
                        lvl1word718CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word719 and lvl1word719CHK == 0:
                        lvl1word719CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word720 and lvl1word720CHK == 0:
                        lvl1word720CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word721 and lvl1word721CHK == 0:
                        lvl1word721CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word722 and lvl1word722CHK == 0:
                        lvl1word722CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)                
                    if wordList == lvl1word723 and lvl1word723CHK == 0:
                        lvl1word723CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word724 and lvl1word724CHK == 0:
                        lvl1word724CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word725 and lvl1word725CHK == 0:
                        lvl1word725CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word726 and lvl1word726CHK == 0:
                        lvl1word726CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word727 and lvl1word727CHK == 0:
                        lvl1word727CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word728 and lvl1word728CHK == 0:
                        lvl1word728CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word729 and lvl1word729CHK == 0:
                        lvl1word729CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word730 and lvl1word730CHK == 0:
                        lvl1word730CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word731 and lvl1word731CHK == 0:
                        lvl1word731CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word732 and lvl1word732CHK == 0:
                        lvl1word732CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word733 and lvl1word733CHK == 0:
                        lvl1word733CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word734 and lvl1word734CHK == 0:
                        lvl1word734CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word735 and lvl1word735CHK == 0:
                        lvl1word735CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word736 and lvl1word736CHK == 0:
                        lvl1word736CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word737 and lvl1word737CHK == 0:
                        lvl1word737CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word738 and lvl1word738CHK == 0:
                        lvl1word738CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word739 and lvl1word739CHK == 0:
                        lvl1word739CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word740 and lvl1word740CHK == 0:
                        lvl1word740CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word741 and lvl1word741CHK == 0:
                        lvl1word741CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word742 and lvl1word742CHK == 0:
                        lvl1word742CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word743 and lvl1word743CHK == 0:
                        lvl1word743CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word744 and lvl1word744CHK == 0:
                        lvl1word744CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word745 and lvl1word745CHK == 0:
                        lvl1word745CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word746 and lvl1word746CHK == 0:
                        lvl1word746CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word747 and lvl1word747CHK == 0:
                        lvl1word747CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word748 and lvl1word748CHK == 0:
                        lvl1word748CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word749 and lvl1word749CHK == 0:
                        lvl1word749CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word750 and lvl1word750CHK == 0:
                        lvl1word750CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word751 and lvl1word751CHK == 0:
                        lvl1word751CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word752 and lvl1word752CHK == 0:
                        lvl1word752CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word753 and lvl1word753CHK == 0:
                        lvl1word753CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word754 and lvl1word754CHK == 0:
                        lvl1word754CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word755 and lvl1word755CHK == 0:
                        lvl1word755CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word756 and lvl1word756CHK == 0:
                        lvl1word756CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word757 and lvl1word757CHK == 0:
                        lvl1word757CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word758 and lvl1word758CHK == 0:
                        lvl1word758CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word759 and lvl1word759CHK == 0:
                        lvl1word759CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word760 and lvl1word760CHK == 0:
                        lvl1word760CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word761 and lvl1word761CHK == 0:
                        lvl1word761CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word762 and lvl1word762CHK == 0:
                        lvl1word762CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word763 and lvl1word763CHK == 0:
                        lvl1word763CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word764 and lvl1word764CHK == 0:
                        lvl1word764CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word765 and lvl1word765CHK == 0:
                        lvl1word765CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word766 and lvl1word766CHK == 0:
                        lvl1word766CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word767 and lvl1word767CHK == 0:
                        lvl1word767CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word768 and lvl1word768CHK == 0:
                        lvl1word768CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word769 and lvl1word769CHK == 0:
                        lvl1word769CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word770 and lvl1word770CHK == 0:
                        lvl1word770CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word771 and lvl1word771CHK == 0:
                        lvl1word771CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word772 and lvl1word772CHK == 0:
                        lvl1word772CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word773 and lvl1word773CHK == 0:
                        lvl1word773CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word774 and lvl1word774CHK == 0:
                        lvl1word774CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word775 and lvl1word775CHK == 0:
                        lvl1word775CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word776 and lvl1word776CHK == 0:
                        lvl1word776CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word777 and lvl1word777CHK == 0:
                        lvl1word777CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word778 and lvl1word778CHK == 0:
                        lvl1word778CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word779 and lvl1word779CHK == 0:
                        lvl1word779CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word780 and lvl1word780CHK == 0:
                        lvl1word780CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word781 and lvl1word781CHK == 0:
                        lvl1word781CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word782 and lvl1word782CHK == 0:
                        lvl1word782CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word783 and lvl1word783CHK == 0:
                        lvl1word783CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word784 and lvl1word784CHK == 0:
                        lvl1word784CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word785 and lvl1word785CHK == 0:
                        lvl1word785CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word786 and lvl1word786CHK == 0:
                        lvl1word786CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word787 and lvl1word787CHK == 0:
                        lvl1word787CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word788 and lvl1word788CHK == 0:
                        lvl1word788CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word789 and lvl1word789CHK == 0:
                        lvl1word789CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word790 and lvl1word790CHK == 0:
                        lvl1word790CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word791 and lvl1word791CHK == 0:
                        lvl1word791CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word792 and lvl1word792CHK == 0:
                        lvl1word792CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word793 and lvl1word793CHK == 0:
                        lvl1word793CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word794 and lvl1word794CHK == 0:
                        lvl1word794CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word795 and lvl1word795CHK == 0:
                        lvl1word795CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word796 and lvl1word796CHK == 0:
                        lvl1word796CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word797 and lvl1word797CHK == 0:
                        lvl1word797CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word798 and lvl1word798CHK == 0:
                        lvl1word798CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word799 and lvl1word799CHK == 0:
                        lvl1word799CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word800 and lvl1word800CHK == 0:
                        lvl1word800CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word801 and lvl1word801CHK == 0:
                        lvl1word801CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word802 and lvl1word802CHK == 0:
                        lvl1word802CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word803 and lvl1word803CHK == 0:
                        lvl1word803CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word804 and lvl1word804CHK == 0:
                        lvl1word804CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word805 and lvl1word805CHK == 0:
                        lvl1word805CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word806 and lvl1word806CHK == 0:
                        lvl1word806CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word807 and lvl1word807CHK == 0:
                        lvl1word807CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word808 and lvl1word808CHK == 0:
                        lvl1word808CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word809 and lvl1word809CHK == 0:
                        lvl1word809CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word810 and lvl1word800CHK == 0:
                        lvl1word810CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word811 and lvl1word811CHK == 0:
                        lvl1word811CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word812 and lvl1word812CHK == 0:
                        lvl1word812CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word813 and lvl1word813CHK == 0:
                        lvl1word813CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word814 and lvl1word814CHK == 0:
                        lvl1word814CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word815 and lvl1word815CHK == 0:
                        lvl1word815CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word816 and lvl1word816CHK == 0:
                        lvl1word816CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word817 and lvl1word817CHK == 0:
                        lvl1word817CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word818 and lvl1word818CHK == 0:
                        lvl1word818CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word819 and lvl1word819CHK == 0:
                        lvl1word819CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word820 and lvl1word820CHK == 0:
                        lvl1word820CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word821 and lvl1word821CHK == 0:
                        lvl1word821CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word822 and lvl1word822CHK == 0:
                        lvl1word822CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)                
                    if wordList == lvl1word823 and lvl1word823CHK == 0:
                        lvl1word823CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word824 and lvl1word824CHK == 0:
                        lvl1word824CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word825 and lvl1word825CHK == 0:
                        lvl1word825CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word826 and lvl1word826CHK == 0:
                        lvl1word826CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word827 and lvl1word827CHK == 0:
                        lvl1word827CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word828 and lvl1word828CHK == 0:
                        lvl1word828CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word829 and lvl1word829CHK == 0:
                        lvl1word829CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word830 and lvl1word830CHK == 0:
                        lvl1word830CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word831 and lvl1word831CHK == 0:
                        lvl1word831CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word832 and lvl1word832CHK == 0:
                        lvl1word832CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word833 and lvl1word833CHK == 0:
                        lvl1word833CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word834 and lvl1word834CHK == 0:
                        lvl1word834CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word835 and lvl1word835CHK == 0:
                        lvl1word835CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word836 and lvl1word836CHK == 0:
                        lvl1word836CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word837 and lvl1word837CHK == 0:
                        lvl1word837CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word838 and lvl1word838CHK == 0:
                        lvl1word838CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word839 and lvl1word839CHK == 0:
                        lvl1word839CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word840 and lvl1word840CHK == 0:
                        lvl1word840CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word841 and lvl1word841CHK == 0:
                        lvl1word841CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word842 and lvl1word842CHK == 0:
                        lvl1word842CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word843 and lvl1word843CHK == 0:
                        lvl1word843CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word844 and lvl1word844CHK == 0:
                        lvl1word844CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word845 and lvl1word845CHK == 0:
                        lvl1word845CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word846 and lvl1word846CHK == 0:
                        lvl1word846CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word847 and lvl1word847CHK == 0:
                        lvl1word847CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word848 and lvl1word848CHK == 0:
                        lvl1word848CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word849 and lvl1word849CHK == 0:
                        lvl1word849CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word850 and lvl1word850CHK == 0:
                        lvl1word850CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word851 and lvl1word851CHK == 0:
                        lvl1word851CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word852 and lvl1word852CHK == 0:
                        lvl1word852CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word853 and lvl1word853CHK == 0:
                        lvl1word853CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word854 and lvl1word854CHK == 0:
                        lvl1word854CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word855 and lvl1word855CHK == 0:
                        lvl1word855CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word856 and lvl1word856CHK == 0:
                        lvl1word856CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word857 and lvl1word857CHK == 0:
                        lvl1word857CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word858 and lvl1word858CHK == 0:
                        lvl1word858CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word859 and lvl1word859CHK == 0:
                        lvl1word859CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word860 and lvl1word860CHK == 0:
                        lvl1word860CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word861 and lvl1word861CHK == 0:
                        lvl1word861CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word862 and lvl1word862CHK == 0:
                        lvl1word862CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word863 and lvl1word863CHK == 0:
                        lvl1word863CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word864 and lvl1word864CHK == 0:
                        lvl1word864CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word865 and lvl1word865CHK == 0:
                        lvl1word865CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word866 and lvl1word866CHK == 0:
                        lvl1word866CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word867 and lvl1word867CHK == 0:
                        lvl1word867CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word868 and lvl1word868CHK == 0:
                        lvl1word868CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word869 and lvl1word869CHK == 0:
                        lvl1word869CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word870 and lvl1word870CHK == 0:
                        lvl1word870CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word871 and lvl1word871CHK == 0:
                        lvl1word871CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word872 and lvl1word872CHK == 0:
                        lvl1word872CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word873 and lvl1word873CHK == 0:
                        lvl1word873CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word874 and lvl1word874CHK == 0:
                        lvl1word874CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word875 and lvl1word875CHK == 0:
                        lvl1word875CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word876 and lvl1word876CHK == 0:
                        lvl1word876CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word877 and lvl1word877CHK == 0:
                        lvl1word877CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word878 and lvl1word878CHK == 0:
                        lvl1word878CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word879 and lvl1word879CHK == 0:
                        lvl1word879CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word880 and lvl1word880CHK == 0:
                        lvl1word880CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word881 and lvl1word881CHK == 0:
                        lvl1word881CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word882 and lvl1word882CHK == 0:
                        lvl1word882CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word883 and lvl1word883CHK == 0:
                        lvl1word883CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word884 and lvl1word884CHK == 0:
                        lvl1word884CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word885 and lvl1word885CHK == 0:
                        lvl1word885CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word886 and lvl1word886CHK == 0:
                        lvl1word886CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word887 and lvl1word887CHK == 0:
                        lvl1word887CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word888 and lvl1word888CHK == 0:
                        lvl1word888CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word889 and lvl1word889CHK == 0:
                        lvl1word889CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word890 and lvl1word890CHK == 0:
                        lvl1word890CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word891 and lvl1word891CHK == 0:
                        lvl1word891CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word892 and lvl1word892CHK == 0:
                        lvl1word892CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word893 and lvl1word893CHK == 0:
                        lvl1word893CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word894 and lvl1word894CHK == 0:
                        lvl1word894CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word895 and lvl1word895CHK == 0:
                        lvl1word895CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word896 and lvl1word896CHK == 0:
                        lvl1word896CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word897 and lvl1word897CHK == 0:
                        lvl1word897CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word898 and lvl1word898CHK == 0:
                        lvl1word898CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word899 and lvl1word899CHK == 0:
                        lvl1word899CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word900 and lvl1word900CHK == 0:
                        lvl1word900CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word901 and lvl1word901CHK == 0:
                        lvl1word901CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word902 and lvl1word902CHK == 0:
                        lvl1word902CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word903 and lvl1word903CHK == 0:
                        lvl1word903CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word904 and lvl1word904CHK == 0:
                        lvl1word904CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word905 and lvl1word905CHK == 0:
                        lvl1word905CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word906 and lvl1word906CHK == 0:
                        lvl1word906CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word907 and lvl1word907CHK == 0:
                        lvl1word907CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word908 and lvl1word908CHK == 0:
                        lvl1word908CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word909 and lvl1word909CHK == 0:
                        lvl1word909CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word910 and lvl1word900CHK == 0:
                        lvl1word910CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word911 and lvl1word911CHK == 0:
                        lvl1word911CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word912 and lvl1word912CHK == 0:
                        lvl1word912CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word913 and lvl1word913CHK == 0:
                        lvl1word913CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word914 and lvl1word914CHK == 0:
                        lvl1word914CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word915 and lvl1word915CHK == 0:
                        lvl1word915CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word916 and lvl1word916CHK == 0:
                        lvl1word916CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word917 and lvl1word917CHK == 0:
                        lvl1word917CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word918 and lvl1word918CHK == 0:
                        lvl1word918CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word919 and lvl1word919CHK == 0:
                        lvl1word919CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word920 and lvl1word920CHK == 0:
                        lvl1word920CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word921 and lvl1word921CHK == 0:
                        lvl1word921CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word922 and lvl1word922CHK == 0:
                        lvl1word922CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)                
                    if wordList == lvl1word923 and lvl1word923CHK == 0:
                        lvl1word923CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word924 and lvl1word924CHK == 0:
                        lvl1word924CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word925 and lvl1word925CHK == 0:
                        lvl1word925CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word926 and lvl1word926CHK == 0:
                        lvl1word926CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word927 and lvl1word927CHK == 0:
                        lvl1word927CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word928 and lvl1word928CHK == 0:
                        lvl1word928CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word929 and lvl1word929CHK == 0:
                        lvl1word929CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word930 and lvl1word930CHK == 0:
                        lvl1word930CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word931 and lvl1word931CHK == 0:
                        lvl1word931CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word932 and lvl1word932CHK == 0:
                        lvl1word932CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word933 and lvl1word933CHK == 0:
                        lvl1word933CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word934 and lvl1word934CHK == 0:
                        lvl1word934CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word935 and lvl1word935CHK == 0:
                        lvl1word935CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word936 and lvl1word936CHK == 0:
                        lvl1word936CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word937 and lvl1word937CHK == 0:
                        lvl1word937CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word938 and lvl1word938CHK == 0:
                        lvl1word938CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word939 and lvl1word939CHK == 0:
                        lvl1word939CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word940 and lvl1word940CHK == 0:
                        lvl1word940CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word941 and lvl1word941CHK == 0:
                        lvl1word941CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word942 and lvl1word942CHK == 0:
                        lvl1word942CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word943 and lvl1word943CHK == 0:
                        lvl1word943CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word944 and lvl1word944CHK == 0:
                        lvl1word944CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word945 and lvl1word945CHK == 0:
                        lvl1word945CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word946 and lvl1word946CHK == 0:
                        lvl1word946CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word947 and lvl1word947CHK == 0:
                        lvl1word947CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word948 and lvl1word948CHK == 0:
                        lvl1word948CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word949 and lvl1word949CHK == 0:
                        lvl1word949CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word950 and lvl1word950CHK == 0:
                        lvl1word950CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word951 and lvl1word951CHK == 0:
                        lvl1word951CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word952 and lvl1word952CHK == 0:
                        lvl1word952CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word953 and lvl1word953CHK == 0:
                        lvl1word953CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word954 and lvl1word954CHK == 0:
                        lvl1word954CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word955 and lvl1word955CHK == 0:
                        lvl1word955CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word956 and lvl1word956CHK == 0:
                        lvl1word956CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word957 and lvl1word957CHK == 0:
                        lvl1word957CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word958 and lvl1word958CHK == 0:
                        lvl1word958CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word959 and lvl1word959CHK == 0:
                        lvl1word959CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word960 and lvl1word960CHK == 0:
                        lvl1word960CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word961 and lvl1word961CHK == 0:
                        lvl1word961CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word962 and lvl1word962CHK == 0:
                        lvl1word962CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word963 and lvl1word963CHK == 0:
                        lvl1word963CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word964 and lvl1word964CHK == 0:
                        lvl1word964CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word965 and lvl1word965CHK == 0:
                        lvl1word965CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word966 and lvl1word966CHK == 0:
                        lvl1word966CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word967 and lvl1word967CHK == 0:
                        lvl1word967CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word968 and lvl1word968CHK == 0:
                        lvl1word968CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word969 and lvl1word969CHK == 0:
                        lvl1word969CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word970 and lvl1word970CHK == 0:
                        lvl1word970CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word971 and lvl1word971CHK == 0:
                        lvl1word971CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word972 and lvl1word972CHK == 0:
                        lvl1word972CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word973 and lvl1word973CHK == 0:
                        lvl1word973CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word974 and lvl1word974CHK == 0:
                        lvl1word974CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word975 and lvl1word975CHK == 0:
                        lvl1word975CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word976 and lvl1word976CHK == 0:
                        lvl1word976CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word977 and lvl1word977CHK == 0:
                        lvl1word977CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word978 and lvl1word978CHK == 0:
                        lvl1word978CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word979 and lvl1word979CHK == 0:
                        lvl1word979CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word980 and lvl1word980CHK == 0:
                        lvl1word980CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word981 and lvl1word981CHK == 0:
                        lvl1word981CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word982 and lvl1word982CHK == 0:
                        lvl1word982CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word983 and lvl1word983CHK == 0:
                        lvl1word983CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word984 and lvl1word984CHK == 0:
                        lvl1word984CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word985 and lvl1word985CHK == 0:
                        lvl1word985CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word986 and lvl1word986CHK == 0:
                        lvl1word986CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word987 and lvl1word987CHK == 0:
                        lvl1word987CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word988 and lvl1word988CHK == 0:
                        lvl1word988CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word989 and lvl1word989CHK == 0:
                        lvl1word989CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word990 and lvl1word990CHK == 0:
                        lvl1word990CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word991 and lvl1word991CHK == 0:
                        lvl1word991CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word992 and lvl1word992CHK == 0:
                        lvl1word992CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word993 and lvl1word993CHK == 0:
                        lvl1word993CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word994 and lvl1word994CHK == 0:
                        lvl1word994CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word995 and lvl1word995CHK == 0:
                        lvl1word995CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word996 and lvl1word996CHK == 0:
                        lvl1word996CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word997 and lvl1word997CHK == 0:
                        lvl1word997CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word998 and lvl1word998CHK == 0:
                        lvl1word998CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word999 and lvl1word999CHK == 0:
                        lvl1word999CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1000 and lvl1word1000CHK == 0:
                        lvl1word1000CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1001 and lvl1word1001CHK == 0:
                        lvl1word1001CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1002 and lvl1word1002CHK == 0:
                        lvl1word1002CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1003 and lvl1word1003CHK == 0:
                        lvl1word1003CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1004 and lvl1word1004CHK == 0:
                        lvl1word1004CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1005 and lvl1word1005CHK == 0:
                        lvl1word1005CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1006 and lvl1word1006CHK == 0:
                        lvl1word1006CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1007 and lvl1word1007CHK == 0:
                        lvl1word1007CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1008 and lvl1word1008CHK == 0:
                        lvl1word1008CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1009 and lvl1word1009CHK == 0:
                        lvl1word1009CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1010 and lvl1word1000CHK == 0:
                        lvl1word1010CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1011 and lvl1word1011CHK == 0:
                        lvl1word1011CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1012 and lvl1word1012CHK == 0:
                        lvl1word1012CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1013 and lvl1word1013CHK == 0:
                        lvl1word1013CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1014 and lvl1word1014CHK == 0:
                        lvl1word1014CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1015 and lvl1word1015CHK == 0:
                        lvl1word1015CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1016 and lvl1word1016CHK == 0:
                        lvl1word1016CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1017 and lvl1word1017CHK == 0:
                        lvl1word1017CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1018 and lvl1word1018CHK == 0:
                        lvl1word1018CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1019 and lvl1word1019CHK == 0:
                        lvl1word1019CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1020 and lvl1word1020CHK == 0:
                        lvl1word1020CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1021 and lvl1word1021CHK == 0:
                        lvl1word1021CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1022 and lvl1word1022CHK == 0:
                        lvl1word1022CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)                
                    if wordList == lvl1word1023 and lvl1word1023CHK == 0:
                        lvl1word1023CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1024 and lvl1word1024CHK == 0:
                        lvl1word1024CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1025 and lvl1word1025CHK == 0:
                        lvl1word1025CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1026 and lvl1word1026CHK == 0:
                        lvl1word1026CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1027 and lvl1word1027CHK == 0:
                        lvl1word1027CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1028 and lvl1word1028CHK == 0:
                        lvl1word1028CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1029 and lvl1word1029CHK == 0:
                        lvl1word1029CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1030 and lvl1word1030CHK == 0:
                        lvl1word1030CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1031 and lvl1word1031CHK == 0:
                        lvl1word1031CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1032 and lvl1word1032CHK == 0:
                        lvl1word1032CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1033 and lvl1word1033CHK == 0:
                        lvl1word1033CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1034 and lvl1word1034CHK == 0:
                        lvl1word1034CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1035 and lvl1word1035CHK == 0:
                        lvl1word1035CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1036 and lvl1word1036CHK == 0:
                        lvl1word1036CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1037 and lvl1word1037CHK == 0:
                        lvl1word1037CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1038 and lvl1word1038CHK == 0:
                        lvl1word1038CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1039 and lvl1word1039CHK == 0:
                        lvl1word1039CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1040 and lvl1word1040CHK == 0:
                        lvl1word1040CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1041 and lvl1word1041CHK == 0:
                        lvl1word1041CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1042 and lvl1word1042CHK == 0:
                        lvl1word1042CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1043 and lvl1word1043CHK == 0:
                        lvl1word1043CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1044 and lvl1word1044CHK == 0:
                        lvl1word1044CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1045 and lvl1word1045CHK == 0:
                        lvl1word1045CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1047 and lvl1word1047CHK == 0:
                        lvl1word1047CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1048 and lvl1word1048CHK == 0:
                        lvl1word1048CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1049 and lvl1word1049CHK == 0:
                        lvl1word1049CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1050 and lvl1word1050CHK == 0:
                        lvl1word1050CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1051 and lvl1word1051CHK == 0:
                        lvl1word1051CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1052 and lvl1word1052CHK == 0:
                        lvl1word1052CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1053 and lvl1word1053CHK == 0:
                        lvl1word1053CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1054 and lvl1word1054CHK == 0:
                        lvl1word1054CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1055 and lvl1word1055CHK == 0:
                        lvl1word1055CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1056 and lvl1word1056CHK == 0:
                        lvl1word1056CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1057 and lvl1word1057CHK == 0:
                        lvl1word1057CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1058 and lvl1word1058CHK == 0:
                        lvl1word1058CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1059 and lvl1word1059CHK == 0:
                        lvl1word1059CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1060 and lvl1word1060CHK == 0:
                        lvl1word1060CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1061 and lvl1word1061CHK == 0:
                        lvl1word1061CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1062 and lvl1word1062CHK == 0:
                        lvl1word1062CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1063 and lvl1word1063CHK == 0:
                        lvl1word1063CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1064 and lvl1word1064CHK == 0:
                        lvl1word1064CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1065 and lvl1word1065CHK == 0:
                        lvl1word1065CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1067 and lvl1word1067CHK == 0:
                        lvl1word1067CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1068 and lvl1word1068CHK == 0:
                        lvl1word1068CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1069 and lvl1word1069CHK == 0:
                        lvl1word1069CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1070 and lvl1word1070CHK == 0:
                        lvl1word1070CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1072 and lvl1word1072CHK == 0:
                        lvl1word1072CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1073 and lvl1word1073CHK == 0:
                        lvl1word1073CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1074 and lvl1word1074CHK == 0:
                        lvl1word1074CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1075 and lvl1word1075CHK == 0:
                        lvl1word1075CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1076 and lvl1word1076CHK == 0:
                        lvl1word1076CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1077 and lvl1word1077CHK == 0:
                        lvl1word1077CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1078 and lvl1word1078CHK == 0:
                        lvl1word1078CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1079 and lvl1word1079CHK == 0:
                        lvl1word1079CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1080 and lvl1word1080CHK == 0:
                        lvl1word1080CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1081 and lvl1word1081CHK == 0:
                        lvl1word1081CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1082 and lvl1word1082CHK == 0:
                        lvl1word1082CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1083 and lvl1word1083CHK == 0:
                        lvl1word1083CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1084 and lvl1word1084CHK == 0:
                        lvl1word1084CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1085 and lvl1word1085CHK == 0:
                        lvl1word1085CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1086 and lvl1word1086CHK == 0:
                        lvl1word1086CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1087 and lvl1word1087CHK == 0:
                        lvl1word1087CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1088 and lvl1word1088CHK == 0:
                        lvl1word1088CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1089 and lvl1word1089CHK == 0:
                        lvl1word1089CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1090 and lvl1word1090CHK == 0:
                        lvl1word1090CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1091 and lvl1word1091CHK == 0:
                        lvl1word1091CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1092 and lvl1word1092CHK == 0:
                        lvl1word1092CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1093 and lvl1word1093CHK == 0:
                        lvl1word1093CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1094 and lvl1word1094CHK == 0:
                        lvl1word1094CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1095 and lvl1word1095CHK == 0:
                        lvl1word1095CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1096 and lvl1word1096CHK == 0:
                        lvl1word1096CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1097 and lvl1word1097CHK == 0:
                        lvl1word1097CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1098 and lvl1word1098CHK == 0:
                        lvl1word1098CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1099 and lvl1word1099CHK == 0:
                        lvl1word1099CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1100 and lvl1word1100CHK == 0:
                        lvl1word1100CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1101 and lvl1word1101CHK == 0:
                        lvl1word1101CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1103 and lvl1word1103CHK == 0:
                        lvl1word1103CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1104 and lvl1word1104CHK == 0:
                        lvl1word1104CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1105 and lvl1word1105CHK == 0:
                        lvl1word1105CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1106 and lvl1word1106CHK == 0:
                        lvl1word1106CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1108 and lvl1word1108CHK == 0:
                        lvl1word1108CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1109 and lvl1word1109CHK == 0:
                        lvl1word1109CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1110 and lvl1word1100CHK == 0:
                        lvl1word1110CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1111 and lvl1word1111CHK == 0:
                        lvl1word1111CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1112 and lvl1word1112CHK == 0:
                        lvl1word1112CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1113 and lvl1word1113CHK == 0:
                        lvl1word1113CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1116 and lvl1word1116CHK == 0:
                        lvl1word1116CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1117 and lvl1word1117CHK == 0:
                        lvl1word1117CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1118 and lvl1word1118CHK == 0:
                        lvl1word1118CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1119 and lvl1word1119CHK == 0:
                        lvl1word1119CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1120 and lvl1word1120CHK == 0:
                        lvl1word1120CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1121 and lvl1word1121CHK == 0:
                        lvl1word1121CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1122 and lvl1word1122CHK == 0:
                        lvl1word1122CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)                
                    if wordList == lvl1word1123 and lvl1word1123CHK == 0:
                        lvl1word1123CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1124 and lvl1word1124CHK == 0:
                        lvl1word1124CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1125 and lvl1word1125CHK == 0:
                        lvl1word1125CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1126 and lvl1word1126CHK == 0:
                        lvl1word1126CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1127 and lvl1word1127CHK == 0:
                        lvl1word1127CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1128 and lvl1word1128CHK == 0:
                        lvl1word1128CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1129 and lvl1word1129CHK == 0:
                        lvl1word1129CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1130 and lvl1word1130CHK == 0:
                        lvl1word1130CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1131 and lvl1word1131CHK == 0:
                        lvl1word1131CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1132 and lvl1word1132CHK == 0:
                        lvl1word1132CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1133 and lvl1word1133CHK == 0:
                        lvl1word1133CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1134 and lvl1word1134CHK == 0:
                        lvl1word1134CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1135 and lvl1word1135CHK == 0:
                        lvl1word1135CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1136 and lvl1word1136CHK == 0:
                        lvl1word1136CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1137 and lvl1word1137CHK == 0:
                        lvl1word1137CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1138 and lvl1word1138CHK == 0:
                        lvl1word1138CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1139 and lvl1word1139CHK == 0:
                        lvl1word1139CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1140 and lvl1word1140CHK == 0:
                        lvl1word1140CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1141 and lvl1word1141CHK == 0:
                        lvl1word1141CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1142 and lvl1word1142CHK == 0:
                        lvl1word1142CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1143 and lvl1word1143CHK == 0:
                        lvl1word1143CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1144 and lvl1word1144CHK == 0:
                        lvl1word1144CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1145 and lvl1word1145CHK == 0:
                        lvl1word1145CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1146 and lvl1word1146CHK == 0:
                        lvl1word1146CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1147 and lvl1word1147CHK == 0:
                        lvl1word1147CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1148 and lvl1word1148CHK == 0:
                        lvl1word1148CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1149 and lvl1word1149CHK == 0:
                        lvl1word1149CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1150 and lvl1word1150CHK == 0:
                        lvl1word1150CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1151 and lvl1word1151CHK == 0:
                        lvl1word1151CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1153 and lvl1word1153CHK == 0:
                        lvl1word1153CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1154 and lvl1word1154CHK == 0:
                        lvl1word1154CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1155 and lvl1word1155CHK == 0:
                        lvl1word1155CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1156 and lvl1word1156CHK == 0:
                        lvl1word1156CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1157 and lvl1word1157CHK == 0:
                        lvl1word1157CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1158 and lvl1word1158CHK == 0:
                        lvl1word1158CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1159 and lvl1word1159CHK == 0:
                        lvl1word1159CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1160 and lvl1word1160CHK == 0:
                        lvl1word1160CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1161 and lvl1word1161CHK == 0:
                        lvl1word1161CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1162 and lvl1word1162CHK == 0:
                        lvl1word1162CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1163 and lvl1word1163CHK == 0:
                        lvl1word1163CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1164 and lvl1word1164CHK == 0:
                        lvl1word1164CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1165 and lvl1word1165CHK == 0:
                        lvl1word1165CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1166 and lvl1word1166CHK == 0:
                        lvl1word1166CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1167 and lvl1word1167CHK == 0:
                        lvl1word1167CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1168 and lvl1word1168CHK == 0:
                        lvl1word1168CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1169 and lvl1word1169CHK == 0:
                        lvl1word1169CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1170 and lvl1word1170CHK == 0:
                        lvl1word1170CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1171 and lvl1word1171CHK == 0:
                        lvl1word1171CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1172 and lvl1word1172CHK == 0:
                        lvl1word1172CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1173 and lvl1word1173CHK == 0:
                        lvl1word1173CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1175 and lvl1word1175CHK == 0:
                        lvl1word1175CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1176 and lvl1word1176CHK == 0:
                        lvl1word1176CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1177 and lvl1word1177CHK == 0:
                        lvl1word1177CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1178 and lvl1word1178CHK == 0:
                        lvl1word1178CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1179 and lvl1word1179CHK == 0:
                        lvl1word1179CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1180 and lvl1word1180CHK == 0:
                        lvl1word1180CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1181 and lvl1word1181CHK == 0:
                        lvl1word1181CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1182 and lvl1word1182CHK == 0:
                        lvl1word1182CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1183 and lvl1word1183CHK == 0:
                        lvl1word1183CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1184 and lvl1word1184CHK == 0:
                        lvl1word1184CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1185 and lvl1word1185CHK == 0:
                        lvl1word1185CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1186 and lvl1word1186CHK == 0:
                        lvl1word1186CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1187 and lvl1word1187CHK == 0:
                        lvl1word1187CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1188 and lvl1word1188CHK == 0:
                        lvl1word1188CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1189 and lvl1word1189CHK == 0:
                        lvl1word1189CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1190 and lvl1word1190CHK == 0:
                        lvl1word1190CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1191 and lvl1word1191CHK == 0:
                        lvl1word1191CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1192 and lvl1word1192CHK == 0:
                        lvl1word1192CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1193 and lvl1word1193CHK == 0:
                        lvl1word1193CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1194 and lvl1word1194CHK == 0:
                        lvl1word1194CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1195 and lvl1word1195CHK == 0:
                        lvl1word1195CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1196 and lvl1word1196CHK == 0:
                        lvl1word1196CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1197 and lvl1word1197CHK == 0:
                        lvl1word1197CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1198 and lvl1word1198CHK == 0:
                        lvl1word1198CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1199 and lvl1word1199CHK == 0:
                        lvl1word1199CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1200 and lvl1word1200CHK == 0:
                        lvl1word1200CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1201 and lvl1word1201CHK == 0:
                        lvl1word1201CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1202 and lvl1word1202CHK == 0:
                        lvl1word1202CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1203 and lvl1word1203CHK == 0:
                        lvl1word1203CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1204 and lvl1word1204CHK == 0:
                        lvl1word1204CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1205 and lvl1word1205CHK == 0:
                        lvl1word1205CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1206 and lvl1word1206CHK == 0:
                        lvl1word1206CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1207 and lvl1word1207CHK == 0:
                        lvl1word1207CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1208 and lvl1word1208CHK == 0:
                        lvl1word1208CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1209 and lvl1word1209CHK == 0:
                        lvl1word1209CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1210 and lvl1word1200CHK == 0:
                        lvl1word1210CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1211 and lvl1word1211CHK == 0:
                        lvl1word1211CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1212 and lvl1word1212CHK == 0:
                        lvl1word1212CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1213 and lvl1word1213CHK == 0:
                        lvl1word1213CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1214 and lvl1word1214CHK == 0:
                        lvl1word1214CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1215 and lvl1word1215CHK == 0:
                        lvl1word1215CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1216 and lvl1word1216CHK == 0:
                        lvl1word1216CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1217 and lvl1word1217CHK == 0:
                        lvl1word1217CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1218 and lvl1word1218CHK == 0:
                        lvl1word1218CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1219 and lvl1word1219CHK == 0:
                        lvl1word1219CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1220 and lvl1word1220CHK == 0:
                        lvl1word1220CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1221 and lvl1word1221CHK == 0:
                        lvl1word1221CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1222 and lvl1word1222CHK == 0:
                        lvl1word1222CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)                
                    if wordList == lvl1word1223 and lvl1word1223CHK == 0:
                        lvl1word1223CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1224 and lvl1word1224CHK == 0:
                        lvl1word1224CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1225 and lvl1word1225CHK == 0:
                        lvl1word1225CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1226 and lvl1word1226CHK == 0:
                        lvl1word1226CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1227 and lvl1word1227CHK == 0:
                        lvl1word1227CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1228 and lvl1word1228CHK == 0:
                        lvl1word1228CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1229 and lvl1word1229CHK == 0:
                        lvl1word1229CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1230 and lvl1word1230CHK == 0:
                        lvl1word1230CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1231 and lvl1word1231CHK == 0:
                        lvl1word1231CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1232 and lvl1word1232CHK == 0:
                        lvl1word1232CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1233 and lvl1word1233CHK == 0:
                        lvl1word1233CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1234 and lvl1word1234CHK == 0:
                        lvl1word1234CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1235 and lvl1word1235CHK == 0:
                        lvl1word1235CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1236 and lvl1word1236CHK == 0:
                        lvl1word1236CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1237 and lvl1word1237CHK == 0:
                        lvl1word1237CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1238 and lvl1word1238CHK == 0:
                        lvl1word1238CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1239 and lvl1word1239CHK == 0:
                        lvl1word1239CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1240 and lvl1word1240CHK == 0:
                        lvl1word1240CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1241 and lvl1word1241CHK == 0:
                        lvl1word1241CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1242 and lvl1word1242CHK == 0:
                        lvl1word1242CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1243 and lvl1word1243CHK == 0:
                        lvl1word1243CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1244 and lvl1word1244CHK == 0:
                        lvl1word1244CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1245 and lvl1word1245CHK == 0:
                        lvl1word1245CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1246 and lvl1word1246CHK == 0:
                        lvl1word1246CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1247 and lvl1word1247CHK == 0:
                        lvl1word1247CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1248 and lvl1word1248CHK == 0:
                        lvl1word1248CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1249 and lvl1word1249CHK == 0:
                        lvl1word1249CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1250 and lvl1word1250CHK == 0:
                        lvl1word1250CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1251 and lvl1word1251CHK == 0:
                        lvl1word1251CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1253 and lvl1word1253CHK == 0:
                        lvl1word1253CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1254 and lvl1word1254CHK == 0:
                        lvl1word1254CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1255 and lvl1word1255CHK == 0:
                        lvl1word1255CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1256 and lvl1word1256CHK == 0:
                        lvl1word1256CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1257 and lvl1word1257CHK == 0:
                        lvl1word1257CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1258 and lvl1word1258CHK == 0:
                        lvl1word1258CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1259 and lvl1word1259CHK == 0:
                        lvl1word1259CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1260 and lvl1word1260CHK == 0:
                        lvl1word1260CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1261 and lvl1word1261CHK == 0:
                        lvl1word1261CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1262 and lvl1word1262CHK == 0:
                        lvl1word1262CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1263 and lvl1word1263CHK == 0:
                        lvl1word1263CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    if wordList == lvl1word1264 and lvl1word1264CHK == 0:
                        lvl1word1264CHK = 1
                        foundCount += 1
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                    


                
                        
                    scoreNum = 0
                    scoreNum2 = 0
                    print(scoreNum2)

                    global wordCounter
                    wordCounter = 0
                    wordList = []
                    global newLabel
                    newLabel = Label(text='', markup = True)
                    global newLabel2
                    newLabel2 = Label(text='', markup = True)
                    global newLabel3
                    newLabel3 = Label(text='', markup = True)
                    global newLabel4
                    newLabel4 = Label(text='', markup = True)
                    global newLabel5
                    newLabel5 = Label(text='', markup = True)
                    global newLabel6
                    newLabel6 = Label(text='', markup = True)
                    global newLabel7
                    newLabel7 = Label(text='', markup = True)
                    global newLabel8
                    newLabel8 = Label(text='', markup = True)
                    global newLabel9
                    newLabel9 = Label(text='', markup = True)
                    global newLabel10
                    newLabel10 = Label(text='', markup = True)
                    global newLabel11
                    newLabel11 = Label(text='', markup = True)
                    global newLabel12
                    newLabel12 = Label(text='', markup = True)

                elif (shieldOn > 0 and letterBlank == True)  :
                    blockSound.play()
                    shieldOn -= 1
                    global shieldScore 
                    shieldScore += 1
                    scoreAdd1 = "Blocked!"
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    global shieldLabel
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                    def scoreDisp():
                        global scoreAdd1
                        global scoreUpb
                        scoreAdd= ""
                        scoreAdd1 = ""
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                    letterBlank = False

                elif (shieldOn > 0 and hitOn == True and letterBlank == False):
                    blockSound.play()
                    shieldOn -= 1 
                    shieldScore += 1
                    scoreAdd1 = "Blocked!"
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                    def scoreDisp():
                        global scoreAdd1
                        global scoreUpb
                        scoreAdd= ""
                        scoreAdd1 = ""
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                    
                else:
                    if gameStop == False :
                        wrongSound.play()
                        scoreNum = 0
                        scoreNum2 = 0
                        scoreCount -= 30
                        scoreMinus -= 30
                        wrongRand = random.randint(1,5)
                        print("-30 pts")
                        print(scoreNum)
                        scoreAdd = "- " + format(30)
                        if wrongRand == 1:
                            scoreAdd1 ="Try Again!"
                        if wrongRand == 2:
                            scoreAdd1 ="Oops!"
                        if wrongRand == 3:
                            scoreAdd1 ="Incorrect!"
                        if wrongRand == 4:
                            scoreAdd1 ="Sorry!"
                        if wrongRand == 5:
                            scoreAdd1 ="Wrong!"
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd
                            global scoreAdd1
                            global scoreUp
                            global scoreUpb
                            scoreAdd= ""
                            scoreAdd1 = ""
                            scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                        global strikesLabel
                        global strikesCount
                        global strikesScore
                        strikesCount -=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                        strikesScore += 1
                        wordCounter = 0
                        wordList = []
                        letterBlank = False
                        newLabel = Label(text='', markup = True)

                        newLabel2 = Label(text='', markup = True)

                        newLabel3 = Label(text='', markup = True)

                        newLabel4 = Label(text='', markup = True)

                        newLabel5 = Label(text='', markup = True)
                     
                        newLabel6 = Label(text='', markup = True)
                      
                        newLabel7 = Label(text='', markup = True)
                     
                        newLabel8 = Label(text='', markup = True)
                  
                        newLabel9 = Label(text='', markup = True)
                  
                        newLabel10 = Label(text='', markup = True)
                        
                        newLabel11 = Label(text='', markup = True)
                   
                        newLabel12 = Label(text='', markup = True)
                



            def speedDisp():
                global speedOn
                global speedLabel
                global speedTimer
                speedOn = False
                speedLabel = myFont3.render((speedText), 1, WHITE)
                speedTimer = 0

            if speedOn == True and boost1 == True  :
                for enemyPos in enemyList :
                    pygame.draw.rect(gameScreen, BLACK, (enemyPos[0], enemyPos[1], 0, 0))
                enemyList = []
            if speedOn == True and boost2 == True : 
                for enemy2Pos in enemyList2 :
                    pygame.draw.rect(gameScreen, BLACK, (enemy2Pos[0], enemy2Pos[1], 0, 0))
                enemyList2 = []
            if speedOn == True and boost3 == True : 
                for enemy3Pos in enemyList3 :
                    pygame.draw.rect(gameScreen, BLACK, (enemy3Pos[0], enemy3Pos[1], 0, 0))
                enemyList3 = []
            if speedOn == True and boost4 == True : 
                for enemy4Pos in enemyList4 :
                    pygame.draw.rect(gameScreen, BLACK, (enemy4Pos[0], enemy4Pos[1], 0, 0))
                enemyList4 = []
            if speedOn == True and boost5 == True : 
                for enemy5Pos in enemyList5 :
                    pygame.draw.rect(gameScreen, BLACK, (enemy5Pos[0], enemy5Pos[1], 0, 0))
                enemyList5 = []
            if speedOn == True and boost6 == True : 
                for enemy6Pos in enemyList6 :
                    pygame.draw.rect(gameScreen, BLACK, (enemy6Pos[0], enemy6Pos[1], 0, 0))
                enemyList6 = []
            if speedOn == True and boost7 == True : 
                for enemy7Pos in enemyList7 :
                    pygame.draw.rect(gameScreen, BLACK, (enemy7Pos[0], enemy7Pos[1], 0, 0))
                enemyList7 = []
            if speedOn == True and boost8 == True : 
                for enemy8Pos in enemyList8 :
                    pygame.draw.rect(gameScreen, BLACK, (enemy8Pos[0], enemy8Pos[1], 0, 0))
                enemyList8 = []
            if speedOn == True and boost1b == True : 
                for enemyPosb in enemyListb :
                    pygame.draw.rect(gameScreen, BLACK, (enemyPosb[0], enemyPosb[1], 0, 0))
                enemyListb = []
            if speedOn == True and boost2b == True : 
                for enemy2Posb in enemyList2b :
                    pygame.draw.rect(gameScreen, BLACK, (enemy2Posb[0], enemy2Posb[1], 0, 0))
                enemyList2b = []
            if speedOn == True and boost3b == True : 
                for enemy3Posb in enemyList3b :
                    pygame.draw.rect(gameScreen, BLACK, (enemy3Posb[0], enemy3Posb[1], 0, 0))
                enemyList3b = []
            if speedOn == True and boost4b == True : 
                for enemy4Posb in enemyList4b :
                    pygame.draw.rect(gameScreen, BLACK, (enemy4Posb[0], enemy4Posb[1], 0, 0))
                enemyList4b = []
            if speedOn == True and boost5b == True : 
                for enemy5Posb in enemyList5b :
                    pygame.draw.rect(gameScreen, BLACK, (enemy5Posb[0], enemy5Posb[1], 0, 0))
                enemyList5b = []
            if speedOn == True and boost6b == True : 
                for enemy6Posb in enemyList6b :
                    pygame.draw.rect(gameScreen, BLACK, (enemy6Posb[0], enemy6Posb[1], 0, 0))
                enemyList6b = []
            if speedOn == True and boost7b == True : 
                for enemy7Posb in enemyList7b :
                    pygame.draw.rect(gameScreen, BLACK, (enemy7Posb[0], enemy7Posb[1], 0, 0))
                enemyList7b = []
            if speedOn == True and boost8b == True : 
                for enemy8Posb in enemyList8b :
                    pygame.draw.rect(gameScreen, BLACK, (enemy8Posb[0], enemy8Posb[1], 0, 0))
                enemyList8b = []
            
            
            if foundCount < 5 :
                lettersLabel = myFont3.render(lettersText, 1, WHITE) 
            if foundCount >= 5:
                lettersLabel = myFont3.render(lettersText2, 1, WHITE)
            if foundCount >= 10:
                lettersLabel = myFont3.render(lettersText3, 1, WHITE)
            if foundCount >= 15:
                lettersLabel = myFont3.render(lettersText4, 1, WHITE)
            if foundCount >= 20:
                lettersLabel = myFont3.render(lettersText5, 1, WHITE)
            if foundCount >= 25:
                lettersLabel = myFont3.render(lettersText6, 1, WHITE)
            if foundCount >= 30:
                lettersLabel = myFont3.render(lettersText7, 1, WHITE)
            if foundCount >= 35:
                lettersLabel = myFont3.render(lettersText8, 1, WHITE)
            if foundCount >= 40:
                lettersLabel = myFont3.render(lettersText9, 1, WHITE)
            if foundCount >= 45:
                lettersLabel = myFont3.render(lettersText10, 1, WHITE)

            if foundCount >= 5 and lettersShow2 == False :
                lettersAdd = "A, C, D, E, T"  
                lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                def lettersDisp():
                    global lettersAdd
                    global lettersUp
                    global lettersShow2
                    lettersAdd = ""
                    lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                    lettersShow2 = True
                lettersPop = threading.Timer(1.5, lettersDisp)
                lettersPop.start()
                

            if foundCount >= 10 and lettersShow3 == False :
                lettersAdd = "C, D, E, O, T"  
                lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                def lettersDisp():
                    global lettersAdd
                    global lettersUp
                    global lettersShow3
                    lettersAdd = ""
                    lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                    lettersShow3 = True
                lettersPop = threading.Timer(1.5, lettersDisp)
                lettersPop.start()

            if foundCount >= 15 and lettersShow4 == False:
                lettersAdd = "D, E, M, O, T"  
                lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                def lettersDisp():
                    global lettersAdd
                    global lettersUp
                    global lettersShow4
                    lettersAdd = ""
                    lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                    lettersShow4 = True
                lettersPop = threading.Timer(1.5, lettersDisp)
                lettersPop.start()

            if foundCount >= 20 and lettersShow5 == False:
                lettersAdd = "D, E, F, M, O, Y"  
                lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                def lettersDisp():
                    global lettersAdd
                    global lettersUp
                    global lettersShow5
                    lettersAdd = ""
                    lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                    lettersShow5 = True
                lettersPop = threading.Timer(1.5, lettersDisp)
                lettersPop.start()

            if foundCount >= 25 and lettersShow6 == False:
                lettersAdd = "B, F, I, M, O, Y"  
                lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                def lettersDisp():
                    global lettersAdd
                    global lettersUp
                    global lettersShow6
                    lettersAdd = ""
                    lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                    lettersShow6 = True
                lettersPop = threading.Timer(1.5, lettersDisp)
                lettersPop.start()

            if foundCount >= 30 and lettersShow7 == False:
                lettersAdd = "A, B, F, I, M, Y"  
                lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                def lettersDisp():
                    global lettersAdd
                    global lettersUp
                    global lettersShow7
                    lettersAdd = ""
                    lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                    lettersShow7 = True
                lettersPop = threading.Timer(1.5, lettersDisp)
                lettersPop.start()

            if foundCount >= 35 and lettersShow8 == False :
                lettersAdd = "A, B, E, F, L, Y"  
                lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                def lettersDisp():
                    global lettersAdd
                    global lettersUp
                    global lettersShow8
                    lettersAdd = ""
                    lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                    lettersShow8 = True
                lettersPop = threading.Timer(1.5, lettersDisp)
                lettersPop.start()

            if foundCount >= 40 and lettersShow9 == False:
                lettersAdd = "A, E, G, P, I, U, S"  
                lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                def lettersDisp():
                    global lettersAdd
                    global lettersUp
                    global lettersShow9
                    lettersAdd = ""
                    lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                    lettersShow9 = True
                lettersPop = threading.Timer(1.5, lettersDisp)
                lettersPop.start()

            if foundCount >= 45 and lettersShow10 == False:
                lettersAdd = "E, G, I, O, R, S, U, V"  
                lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                def lettersDisp():
                    global lettersAdd
                    global lettersUp
                    global lettersShow10
                    lettersAdd = ""
                    lettersUp = myFont4.render(lettersAdd, 1, WHITE)
                    lettersShow10 = True
                lettersPop = threading.Timer(1.5, lettersDisp)
                lettersPop.start()

           



                


            
            drop_enemies(enemyList, enemyList2, enemyList3, enemyList4, enemyList5, enemyList6, enemyList7, enemyList8, enemyListb, gameStop)
             
            draw_enemies(enemyList, enemyList2, enemyList3, enemyList4, enemyList5, enemyList6, enemyList7, enemyList8)

            update_enemy_positions(enemyList, enemyList2, enemyList3, enemyList4, enemyList5, enemyList6, enemyList7, enemyList8)

            drop_enemiesb(enemyListb, enemyList2b, enemyList3b, enemyList4b, enemyList5b, enemyList6b, enemyList7b, enemyList8b, enemyList, enemyList2, enemyList3, enemyList4, enemyList5, enemyList6, enemyList7, enemyList8, gameStop) 
                    
            draw_enemiesb(enemyListb, enemyList2b, enemyList3b, enemyList4b, enemyList5b, enemyList6b, enemyList7b, enemyList8b)

            update_enemy_positionsb(enemyListb, enemyList2b, enemyList3b, enemyList4b, enemyList5b, enemyList6b, enemyList7b, enemyList8b)

            gameScreen.blit(playerIMG, (playerPos[0], playerPos[1]))
                
            

            if collision_check(enemyList, playerPos) and dropDebug == False :
                playerNum = enemyText
                if playerNum == "" and shield1 == True :
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNum == "" and coin1 == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                elif playerNum == "" and strikes1 == True :
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNum == "" and boost1 == True and hitOn == False :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNum == "" and hitOn == True :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText, 1, WORD_COLOR)               
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText, 1, WORD_COLOR)               
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText, 1, WORD_COLOR)                          
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText, 1, WORD_COLOR)                          
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText, 1, WORD_COLOR)               
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText, 1, WORD_COLOR)               
                    if wordCounter == 6 :
                        newLabel7 = myFont.render(enemyText, 1, WORD_COLOR)
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText, 1, WORD_COLOR)               
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText, 1, WORD_COLOR)               
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText, 1, WORD_COLOR)              
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText, 1, WORD_COLOR)               
                    if wordCounter == 11 :
                        newLabel12 = myFont.render(enemyText, 1, WHITE)
                    hitOn = False
                    
                elif shieldOn > 0 and hitOn == True :
                    playerNum = ""
                    shield1 = False
                    coin1 = False
                    strikes1 = False
                    boost1 = False
                    hitOn = False
                    
                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText, 1, WORD_COLOR)               
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText, 1, WORD_COLOR)               
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText, 1, WORD_COLOR)                          
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText, 1, WORD_COLOR)                          
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText, 1, WORD_COLOR)               
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText, 1, WORD_COLOR)               
                    if wordCounter == 6 :
                        newLabel7 = myFont.render(enemyText, 1, WORD_COLOR)
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText, 1, WORD_COLOR)               
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText, 1, WORD_COLOR)               
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText, 1, WORD_COLOR)              
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText, 1, WORD_COLOR)             
                    if wordCounter == 11 :
                        newLabel12 = myFont.render(enemyText, 1, WORD_COLOR)
               
                    
                enemyColl(enemyList)
                for enemyPos in enemyList :
                    pygame.draw.rect(gameScreen, BLACK, (enemyPos[0], enemyPos[1], 0, 0))
                enemyList = []
                print("1A - " + playerNum)
                if playerNum == "" and coin1 == False and boost1 == False and strikes1 == False and shield1 == False :
                    letterBlank = True
                    letterWipe()
                elif playerNum == "" and coin1 == True  and hitOn == False :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNum == "" and coin1== False and strikes1 == False and boost1 == True and speedOn == False and shield1 == False and hitOn == False :
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  #debug for score popups
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNum == "" and boost1 == True and speedOn == True and hitOn == False :
                        speedOn = True

                else :
                    if playerNum == "" and coin1== False and boost1 == False and strikes1 == False and shield1 == True and hitOn == False :
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNum == "" and coin1== False and strikes1 == True and boost1 == False and shield1 == False and hitOn == False:
                        dripSound.play()
                        strikesCount +=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum == "" and hitOn == True and (coin1==True or strikes1==True or boost1==True or shield1==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False
                    else:
                        scoreAdd()
                        dripSound.play()
                        wordList.append(playerNum)
                        wordCounter += 1
                print(wordList)

            if collision_check(enemyList2, playerPos) and dropDebug2 == False:       
                playerNum2 = enemyText2
                if playerNum2 == "" and shield2 == True :
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNum2 == "" and coin2 == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                elif playerNum2 == "" and strikes2 == True :
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNum2 == "" and boost2 == True and hitOn == False :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNum2 == "" and hitOn == True  :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    hitOn = False
                elif shieldOn > 0 and hitOn == True :
                    playerNum2 = ""
                    shield2 = False
                    coin2 = False
                    strikes2 = False
                    boost2 = False
                    hitOn = False
                    
                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText2, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText2, 1, WORD_COLOR) 
               
                    
                enemyColl2(enemyList2)
                for enemy2Pos in enemyList2 :
                    pygame.draw.rect(gameScreen, BLACK, (enemy2Pos[0], enemy2Pos[1], 0, 0))
                enemyList2 = []
                print("2A - " + playerNum2)
                if playerNum2 == "" and coin2 == False and boost2 == False and strikes2 == False and shield2 == False :
                    letterBlank = True
                    letterWipe()
                elif playerNum2 == "" and coin2 == True  and hitOn == False :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNum2 == "" and coin2 == False and strikes2 == False and boost2 == True and speedOn == False and shield2 == False and hitOn == False:
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  #debug for score popups
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNum2 == "" and boost2 == True and speedOn == True and hitOn == False:
                        speedOn = True
                else :
                    if playerNum2 == "" and coin2 == False and boost2 == False and strikes2 == False and shield2 == True and hitOn == False:
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNum2 == "" and coin2 == False and strikes2 == True and boost2 == False  and shield2 == False and hitOn == False:
                        dripSound.play()
                        strikesCount +=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum2 == "" and hitOn == True and (coin2==True or strikes2==True or boost2==True or shield2==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False
                    else:
                        scoreAdd2()
                        dripSound.play()
                        wordList.append(playerNum2)
                        wordCounter += 1
                print(wordList)

            if collision_check(enemyList3, playerPos) and dropDebug3 == False:
                playerNum3 = enemyText3
                if playerNum3 == "" and shield3 == True : 
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNum3 == "" and coin3 == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)    
                elif playerNum3 == "" and strikes3 == True :
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNum3 == "" and boost3 == True and hitOn == False :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNum3 == "" and hitOn == True  :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    hitOn = False
                elif shieldOn > 0 and hitOn == True :
                    playerNum3 = ""
                    shield3 = False
                    coin3 = False
                    strikes3 = False
                    boost3 = False
                    hitOn = False
                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText3, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText3, 1, WORD_COLOR)  
                   
                    
                enemyColl3(enemyList3)
                for enemy3Pos in enemyList3 :
                    pygame.draw.rect(gameScreen, BLACK, (enemy3Pos[0], enemy3Pos[1], 0, 0))
                enemyList3 = []
                print("3A - " + playerNum3)
                if playerNum3 == "" and coin3 == False and boost3 == False and strikes3 == False and shield3 == False:
                    letterBlank = True
                    letterWipe()
                elif playerNum3 == "" and coin3 == True and hitOn == False  :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNum3 == "" and coin3 == False and strikes3 == False and boost3 == True and speedOn == False and shield3 == False and hitOn == False:
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  #debug for score popups
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNum3 == "" and boost3 == True and speedOn == True and hitOn == False:
                        speedOn = True
                else :
                    if playerNum3 == "" and coin3 == False and boost3 == False and strikes3 == False and shield3 == True and hitOn == False :
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNum3 == "" and coin3== False and strikes3 == True and boost3 == False and shield3 == False and hitOn == False:
                        dripSound.play()
                        strikesCount +=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum2 == "" and hitOn == True and (coin2==True or strikes2==True or boost2==True or shield2==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False
                    else:
                        scoreAdd3()
                        dripSound.play()
                        wordList.append(playerNum3)
                        wordCounter += 1
                print(wordList)

            if collision_check(enemyList4, playerPos) and dropDebug4 == False:
                playerNum4 = enemyText4
                if playerNum4 == "" and shield4 == True :
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNum4 == "" and coin4 == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                elif playerNum4 == "" and strikes4 == True :
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNum4 == "" and boost4 == True and hitOn == False :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNum4 == "" and hitOn == True :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    hitOn = False
                elif shieldOn > 0 and hitOn == True :
                    playerNum4 = ""
                    shield4 = False
                    coin4 = False
                    strikes4 = False
                    boost4 = False
                    hitOn = False


                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText4, 1, WORD_COLOR) 
                    
                    
                enemyColl4(enemyList4)
                for enemy4Pos in enemyList4 :
                    pygame.draw.rect(gameScreen, BLACK, (enemy4Pos[0], enemy4Pos[1], 0, 0))
                enemyList4 = []
                print("4A - " + playerNum4)
                if playerNum4 == "" and coin4 == False and boost4 == False and strikes4 == False and shield4 == False :
                    letterBlank = True
                    letterWipe()
                elif playerNum4 == "" and coin4 == True and hitOn == False :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNum4 == "" and coin4 == False and strikes4 == False and boost4 == True and speedOn == False and shield4 == False and hitOn == False:
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  #debug for score popups
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNum4 == "" and boost4 == True and speedOn == True and hitOn == False:
                        speedOn = True
                else :
                    if playerNum4 == "" and coin4 == False and boost4 == False and strikes4 == False and shield4 == True and hitOn == False :
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNum4 == "" and coin4 == False and strikes4 == True and boost4 == False and shield4 == False and hitOn == False :
                        dripSound.play()
                        strikesCount +=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum4 == "" and hitOn == True and (coin4==True or strikes4==True or boost4==True or shield4==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False
                    else:
                        scoreAdd4()
                        dripSound.play()
                        wordList.append(playerNum4)
                        wordCounter += 1
                print(wordList)

            if collision_check(enemyList5, playerPos) and dropDebug5 == False:
                playerNum5 = enemyText5
                if playerNum5 == "" and shield5 == True :
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNum5 == "" and coin5 == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                elif playerNum5 == "" and strikes5 == True :
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNum5 == "" and boost5 == True and hitOn == False :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNum5 == "" and hitOn == True :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    hitOn = False
                elif shieldOn > 0 and hitOn == True :
                    playerNum5 = ""
                    shield5 = False
                    coin5 = False
                    strikes5 = False
                    boost5 = False
                    hitOn = False


                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText5, 1, WORD_COLOR) 
                
                    
                enemyColl5(enemyList5)
                for enemy5Pos in enemyList5 :
                    pygame.draw.rect(gameScreen, BLACK, (enemy5Pos[0], enemy5Pos[1], 0, 0))
                enemyList5 = []
                print("5A - " + playerNum5)
                if playerNum5 == "" and coin5 == False and boost5 == False and strikes5 == False and shield5 == False:
                    letterBlank = True
                    letterWipe()
                elif playerNum5 == "" and coin5 == True and hitOn == False  :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNum5 == "" and coin5 == False and strikes5 == False and boost5 == True and speedOn == False and shield5 == False and hitOn == False :
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  #debug for score popups
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNum5 == "" and boost5 == True and speedOn == True and hitOn == False :
                        speedOn = True
                else :
                    if playerNum5 == "" and coin5 == False and boost5 == False and strikes5 == False and shield5 == True and hitOn == False :
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNum5 == "" and coin5 == False and boost5 == False and strikes5 == True and shield5 == False and hitOn == False :
                        dripSound.play()
                        strikesCount +=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum5 == "" and hitOn == True and (coin5==True or strikes5==True or boost5==True or shield5==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False
                    else:
                        scoreAdd5()
                        dripSound.play()
                        wordList.append(playerNum5)
                        wordCounter += 1
                print(wordList)

            if collision_check(enemyList6, playerPos) and dropDebug6 == False:
                playerNum6 = enemyText6
                if playerNum6 == "" and shield1 == True :
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNum6 == "" and coin6 == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                elif playerNum6 == "" and strikes6 == True :
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNum6 == "" and boost6 == True and hitOn == False :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNum6 == "" and hitOn == True :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    hitOn = False
                elif shieldOn > 0 and hitOn == True :
                    playerNum6 = ""
                    shield6 = False
                    coin6 = False
                    strikes6 = False
                    boost6 = False
                    hitOn = False


                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText6, 1, WORD_COLOR) 
                    
                    
                enemyColl6(enemyList6)
                for enemy6Pos in enemyList6 :
                    pygame.draw.rect(gameScreen, BLACK, (enemy6Pos[0], enemy6Pos[1], 0, 0))
                enemyList6 = []
                print("6A - " + playerNum6)
                if playerNum6 == "" and coin6 == False and boost6 == False and strikes6 == False and shield6 == False :
                   letterBlank = True
                   letterWipe()
                elif playerNum6 == "" and coin6 == True and hitOn == False  :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNum6 == "" and coin6 == False and strikes6 == False and boost6 == True and speedOn == False and shield6 == False and hitOn == False :
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  #debug for score popups
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNum6 == "" and boost6 == True and speedOn == True and hitOn == False :
                        speedOn = True
                else :
                    if playerNum6 == "" and coin6 == False and boost6 == False and strikes6 == False and shield6 == True and hitOn == False :
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNum6 == "" and coin6 == False and strikes6 == True and boost6 == False and shield6 == False and hitOn == False :
                        dripSound.play()
                        strikesCount +=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum6 == "" and hitOn == True and (coin6==True or strikes6==True or boost6==True or shield6==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False
                    
                    else:
                        scoreAdd6()
                        dripSound.play()
                        wordList.append(playerNum6)
                        wordCounter += 1
                print(wordList)

            if collision_check(enemyList7, playerPos) and dropDebug7 == False:
                playerNum7 = enemyText7
                if playerNum7 == "" and shield7 == True :
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNum7 == "" and coin7 == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                elif playerNum7 == "" and strikes7 == True :
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNum7 == "" and boost7 == True and hitOn == False :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNum7 == "" and hitOn == True :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    hitOn = False
                elif shieldOn > 0 and hitOn == True :
                    playerNum7 = ""
                    shield7 = False
                    coin7 = False
                    strikes7 = False
                    boost7 = False
                    hitOn = False
                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText7, 1, WORD_COLOR) 
                    
                    
                enemyColl7(enemyList7)
                for enemy7Pos in enemyList7 :
                    pygame.draw.rect(gameScreen, BLACK, (enemy7Pos[0], enemy7Pos[1], 0, 0))
                enemyList7 = []
                print("7A - " + playerNum7)
                if playerNum7 == "" and coin7 == False and boost7 == False and strikes7 == False and shield7 == False :
                    letterBlank = True
                    letterWipe()
                elif playerNum7 == "" and coin7 == True and hitOn == False :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNum7 == "" and coin7 == False and strikes7 == False and boost7 == True and speedOn == False and shield7 == False and hitOn == False :
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  #debug for score popups
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNum7 == "" and boost7 == True and speedOn == True and hitOn == False :
                        speedOn = True
                else :
                    if playerNum7 == "" and coin7 == False and boost7 == False and strikes7 == False and shield7 == True and hitOn == False :
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNum7 == "" and coin7 == False and strikes7 == True and boost7 == False and shield7 == False and hitOn == False :
                        dripSound.play()
                        strikesCount +=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum7 == "" and hitOn == True and (coin7==True or strikes7==True or boost7==True or shield7==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False
                    
                    else:
                        scoreAdd7()
                        dripSound.play()
                        wordList.append(playerNum7)
                        wordCounter += 1
                print(wordList)

            if collision_check(enemyList8, playerPos) and dropDebug8 == False:
                playerNum8 = enemyText8
                if playerNum8 == "" and shield8 == True :
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNum8 == "" and coin8 == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                elif playerNum8 == "" and strikes8 == True :
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNum8 == "" and boost8 == True and hitOn == False :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNum8 == "" and hitOn == True :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    hitOn = False
                elif shieldOn > 0 and hitOn == True :
                    playerNum8 = ""
                    shield8 = False
                    coin8 = False
                    strikes8 = False
                    boost8 = False
                    hitOn = False
                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText8, 1, WORD_COLOR) 
                enemyColl8(enemyList8)
                for enemy8Pos in enemyList8 :
                    pygame.draw.rect(gameScreen, BLACK, (enemy8Pos[0], enemy8Pos[1], 0, 0))
                enemyList8 = []
                print("8A - " + playerNum8)
                if playerNum8 == "" and coin8 == False and boost8 == False and strikes8 == False and shield8 == False:
                    letterBlank = True
                    letterWipe()
                elif playerNum8 == "" and coin8 == True and hitOn == False  :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNum8 == "" and coin8 == False and strikes8 == False and boost8 == True and speedOn == False and shield8 == False and hitOn == False :
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  #debug for score popups
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNum8 == "" and boost8 == True and speedOn == True and hitOn == False :
                        speedOn = True
                else :
                    if playerNum8 == "" and coin8 == False and boost8 == False and strikes8 == False and shield8 == True and hitOn == False :
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNum8 == "" and coin8 == False and strikes8 == True and boost8 == False and shield8 == False and hitOn == False :
                        dripSound.play()
                        strikesCount +=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum8 == "" and hitOn == True and (coin8==True or strikes8==True or boost8==True or shield8==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False

                    else:
                        scoreAdd8()
                        dripSound.play()
                        wordList.append(playerNum8)
                        wordCounter += 1
                print(wordList)





            if collision_check(enemyListb, playerPos) and dropDebugb == False:
                playerNumb = enemyTextb
                if playerNumb == "" and shield1b == True :
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNumb == "" and coin1b == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                elif playerNumb == "" and strikes1b == True :
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNumb == "" and boost1b == True and hitOn == False :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNumb == "" and hitOn == True :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    hitOn = False
                elif shieldOn > 0 and hitOn == True :
                    playerNumb = ""
                    shield1b = False
                    coin1b = False
                    strikes1b = False
                    boost1b = False
                    hitOn == False
                    
                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyTextb, 1, WORD_COLOR) 
                
                enemyCollB(enemyListb)
                for enemyPosb in enemyListb :
                    pygame.draw.rect(gameScreen, BLACK, (enemyPosb[0], enemyPosb[1], 0, 0))
                enemyListb = []
                print("1B - " + playerNumb)
                if playerNumb == "" and coin1b == False and boost1b == False and strikes1b == False and shield1b == False:
                    letterBlank = True
                    letterWipe()
                elif playerNumb == "" and coin1b == True  and hitOn == False :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNumb == "" and coin1b == False and strikes1b == False and boost1b == True and speedOn == False and shield1b == False and hitOn == False:
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  #debug for score popups
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNumb == "" and boost1b == True and speedOn == True and hitOn == False:
                        speedOn = True
                else:
                    if playerNumb == "" and coin1b == False and boost1b == False and strikes1b == False and shield1b == True and hitOn == False :
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNumb == "" and coin1b == False and strikes1b == True and boost1b == False and shield1b == False and hitOn == False :
                        dripSound.play()
                        strikesCount +=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum == "" and hitOn == True and (coin1==True or strikes1==True or boost1==True or shield1==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False
                    else: 
                        scoreAddb()
                        dripSound.play()
                        wordList.append(playerNumb)
                        wordCounter += 1
                print(wordList)


            if collision_check(enemyList2b, playerPos) and dropDebug2b == False:
                playerNum2b = enemyText2b
                if playerNum2b == "" and shield2b == True :
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNum2b == "" and coin2b == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                elif playerNum2b == "" and strikes2b == True :
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNum2b == "" and boost2b == True and hitOn == False :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNum2b == "" and hitOn == True :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    hitOn = False
                elif shieldOn > 0 and hitOn == True :
                    playerNum2b = ""
                    shield2b = False
                    coin2b = False
                    strikes2b = False
                    boost2b = False
                    hitOn = False
                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText2b, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText2b, 1, WORD_COLOR)   
                enemyColl2B(enemyList2b)
                for enemy2Posb in enemyList2b :
                    pygame.draw.rect(gameScreen, BLACK, (enemy2Posb[0], enemy2Posb[1], 0, 0))
                enemyList2b = []
                print("2B - " + playerNum2b)
                if playerNum2b == "" and coin2b == False and boost2b == False and strikes2b == False and shield2b == False :
                    letterBlank = True
                    letterWipe()
                elif playerNum2b == "" and coin2b == True and hitOn == False :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNum2b == "" and coin2b == False and strikes2b == False and boost2b == True  and speedOn == False and shield2b == False and hitOn == False :
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  #debug for score popups
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNum2b == "" and boost2b == True and speedOn == True and hitOn == False :
                        speedOn = True
                else:
                    if playerNum2b == "" and coin2b == False and boost2b == False and strikes2b == False and shield2b == True and hitOn == False:
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNum2b == "" and coin2b == False and strikes2b == True and boost2b == False and shield2b == False and hitOn == False :
                        dripSound.play()
                        strikesCount +=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum2b == "" and hitOn == True and (coin2b==True or strikes2b==True or boost2b==True or shield2b==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False
                    else:
                        scoreAdd2b()
                        dripSound.play()
                        wordList.append(playerNum2b)
                        wordCounter += 1
                print(wordList)
                
            if collision_check(enemyList3b, playerPos) and dropDebug3b == False: 
                playerNum3b = enemyText3b
                if playerNum3b == "" and shield3b == True :
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNum3b == "" and coin3b == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                elif playerNum3b == "" and strikes3b == True :
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNum3b == "" and boost3b == True and hitOn == False :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNum3b == "" and hitOn == True :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    hitOn = False
                elif shieldOn > 0 and hitOn == True :
                    playerNum3b = ""
                    shield3b = False
                    coin3b = False
                    strikes3b = False
                    boost3b = False
                    hitOn = False
                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText3b, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText3b, 1, WORD_COLOR)  
                enemyColl3B(enemyList3b)
                for enemy3Posb in enemyList3b :
                    pygame.draw.rect(gameScreen, BLACK, (enemy3Posb[0], enemy3Posb[1], 0, 0))
                enemyList3b = []
                print("3B - " + playerNum3b)
                if playerNum3b == "" and coin3b == False and boost3b == False and strikes3b == False and shield3b == False:
                    letterBlank = True
                    letterWipe()
                elif playerNum3b == "" and coin3b == True and hitOn == False :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNum3b == "" and coin3b == False and strikes3b == False and boost3b == True and speedOn == False and shield3b == False and hitOn == False :
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  #debug for score popups
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNum3b == "" and boost3b == True and speedOn == True and hitOn == False :
                        speedOn = True
                else:
                    if playerNum3b == "" and coin3b == False and boost3b == False and strikes3b == False and shield3b == True and hitOn == False :
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNum3b == "" and coin3b == False and strikes3b == True and boost3b == False and shield3b == False and hitOn == False:
                        dripSound.play()
                        strikesCount +=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum3b == "" and hitOn == True and (coin3b==True or strikes3b==True or boost3b==True or shield3b==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False
                    else:
                        scoreAdd3b()
                        dripSound.play()
                        wordList.append(playerNum3b)
                        wordCounter += 1
                print(wordList)
                
            if collision_check(enemyList4b, playerPos) and dropDebug4b == False:
                playerNum4b = enemyText4b
                if playerNum4b == "" and shield4b == True :
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNum4b == "" and coin4b == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                elif playerNum4b == "" and strikes4b == True:
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNum4b == "" and boost4b == True and hitOn == False :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNum4b == "" and hitOn == True :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    hitOn = False
                elif shieldOn > 0 and hitOn == True :
                    playerNum4b = ""
                    shield4b = False
                    coin4b = False
                    strikes4b = False
                    boost4b = False
                    hitOn = False
                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText4b, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText4b, 1, WORD_COLOR)  
                enemyColl4B(enemyList4b)
                for enemy4Posb in enemyList4b :
                    pygame.draw.rect(gameScreen, BLACK, (enemy4Posb[0], enemy4Posb[1], 0, 0))
                enemyList4b = []
                print("4B - " + playerNum4b)
                if playerNum4b == "" and coin4b == False and boost4b == False and strikes4b == False and shield4b == False:
                    letterBlank = True
                    letterWipe()
                elif playerNum4b == "" and coin4b == True and hitOn == False :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNum4b == "" and coin4b == False and strikes4b == False and boost4b == True and speedOn == False and shield4b == False and hitOn == False :
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  #debug for score popups
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNum4b == "" and boost4b == True and speedOn == True and hitOn == False :
                        speedOn = True
                else:
                    if playerNum4b == "" and coin4b == False and boost4b == False and strikes4b == False and shield4b == True and hitOn == False :
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNum4b == "" and coin4b == False and strikes4b == True and boost4b == False and shield4b == False and hitOn == False :
                        dripSound.play()
                        strikesCount +=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum4b == "" and hitOn == True and (coin4b==True or strikes4b==True or boost4b==True or shield4b==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False
                    
                    else:
                        scoreAdd4b()
                        dripSound.play()
                        wordList.append(playerNum4b)
                        wordCounter += 1
                print(wordList)

            if collision_check(enemyList5b, playerPos) and dropDebug5b == False:
                playerNum5b = enemyText5b
                if playerNum5b == "" and shield5b == True :
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNum5b == "" and coin5b == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                elif playerNum5b == "" and strikes5b == True :
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNum5b == "" and boost5b == True and hitOn == False :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNum5b == "" and hitOn == True :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    hitOn = False
                elif shieldOn > 0 and hitOn == True :
                    playerNum5b = ""
                    shield5b = False
                    coin5b = False
                    strikes5b = False
                    boost5b = False
                    hitOn = False
                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText5b, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText5b, 1, WORD_COLOR)  
                enemyColl5B(enemyList5b)
                for enemy5Posb in enemyList5b :
                    pygame.draw.rect(gameScreen, BLACK, (enemy5Posb[0], enemy5Posb[1], 0, 0))
                enemyList5b = []
                print("5B - " + playerNum5b)
                if playerNum5b == "" and coin5b == False and boost5b == False and strikes5b == False and shield5b == False:
                    letterBlank = True
                    letterWipe()
                elif playerNum5b == "" and coin5b == True and hitOn == False  :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNum5b == "" and coin5b == False and strikes5b == False and boost5b == True and speedOn == False and shield5b == False and hitOn == False :
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  #debug for score popups
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNum5b == "" and boost5b == True and speedOn == True and hitOn == False :
                        speedOn = True
                else:
                    if playerNum5b == "" and coin5b == False and boost5b == False and strikes5b == False and shield5b == True and hitOn == False :
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNum5b == "" and coin5b == False and strikes5b == True and boost5b == False and shield5b == False and hitOn == False :
                        dripSound.play()
                        strikesCount +=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum5b == "" and hitOn == True and (coin5b==True or strikes5b==True or boost5b==True or shield5b==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False
                    
                    else:
                        scoreAdd5b()
                        dripSound.play()
                        wordList.append(playerNum5b)
                        wordCounter += 1
                print(wordList)

            if collision_check(enemyList6b, playerPos) and dropDebug6b == False:
                playerNum6b = enemyText6b
                if playerNum6b == "" and shield6b == True :
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNum6b == "" and coin6b == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                elif playerNum6b == "" and strikes6b == True :
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNum6b == "" and boost6b == True and hitOn == False :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNum6b == "" and hitOn == True :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    hitOn = False
                elif shieldOn > 0 and hitOn == True :
                    playerNum6b = ""
                    shield6b = False
                    coin6b = False
                    strikes6b = False
                    boost6b = False
                    hitOn = False
                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText6b, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText6b, 1, WORD_COLOR)  
                enemyColl6B(enemyList6b)
                for enemy6Posb in enemyList6b :
                    pygame.draw.rect(gameScreen, BLACK, (enemy6Posb[0], enemy6Posb[1], 0, 0))
                enemyList6b = []
                print("6B - " + playerNum6b)
                if playerNum6b == "" and coin6b == False and boost6b == False and strikes6b == False and shield6b == False:
                    letterBlank = True
                    letterWipe()
                elif playerNum6b == "" and coin6b == True and hitOn == False :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNum6b == "" and coin6b == False and strikes6b == False and boost6b == True and speedOn == False and shield6b == False and hitOn == False :
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  #debug for score popups
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNum6b == "" and boost6b == True and speedOn == True and hitOn == False :
                        speedOn = True
                else:
                    if playerNum6b == "" and coin6b == False and boost6b == False and strikes6b == False and shield6b == True and hitOn == False :
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNum6b == "" and coin6b == False and strikes6b == True and boost6b == False and shield6b == False and hitOn == False :
                        dripSound.play()
                        strikesCount +=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum6b == "" and hitOn == True and (coin6b==True or strikes6b==True or boost6b==True or shield6b==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False
                    
                    else:
                        scoreAdd6b()
                        dripSound.play()
                        wordList.append(playerNum6b)
                        wordCounter += 1
                print(wordList)

            if collision_check(enemyList7b, playerPos) and dropDebug7b == False:
                playerNum7b = enemyText7b
                if playerNum7b == "" and shield7b == True :
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNum7b == "" and coin7b == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                elif playerNum7b == "" and strikes7b == True :
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNum7b == "" and boost7b == True and hitOn == False :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNum7b == "" and hitOn == True :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    hitOn = False
                elif shieldOn > 0 and hitOn == True :
                    playerNum7b = ""
                    shield7b = False
                    coin7b = False
                    strikes7b = False
                    boost7b = False
                    hitOn = False
                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText7b, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText7b, 1, WORD_COLOR)  
                enemyColl7B(enemyList7b)
                for enemy7Posb in enemyList7b :
                    pygame.draw.rect(gameScreen, BLACK, (enemy7Posb[0], enemy7Posb[1], 0, 0))
                enemyList7b = []
                print("7B - " + playerNum7b)
                if playerNum7b == "" and coin7b == False and boost7b == False and strikes7b == False and shield7b == False:
                    letterBlank = True
                    letterWipe()
                elif playerNum7b == "" and coin7b == True and hitOn == False :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNum7b == "" and coin7b == False and strikes7b == False and boost7b == True and speedOn == False and shield7b == False and hitOn == False :
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  #debug for score popups
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNum7b == "" and boost7b == True and speedOn == True and hitOn == False :
                        speedOn = True
                else:
                    if playerNum7b == "" and coin7b == False and boost7b == False and strikes7b == False and shield7b == True and hitOn == False :
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNum7b == "" and coin7b == False and strikes7b == True and boost7b == False and shield7b == False and hitOn == False :
                        dripSound.play()
                        strikesCount +=1
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum7b == "" and hitOn == True and (coin7b==True or strikes7b==True or boost7b==True or shield7b==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False
            
                    else:
                        scoreAdd7b()
                        dripSound.play()
                        wordList.append(playerNum7b)
                        wordCounter += 1
                print(wordList)

            if collision_check(enemyList8b, playerPos) and dropDebug8b == False:
                playerNum8b = enemyText8b
                if playerNum8b == "" and shield8b == True :
                    shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                elif playerNum8b == "" and coin8b == True  :
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                elif playerNum8b == "" and strikes8b == True :
                    strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                elif playerNum8b == "" and boost8b == True and hitOn == False  :
                    speedLabel = myFont3.render((speedText), 1, (255,0,50))
                elif playerNum8b == "" and hitOn == True :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    hitOn = False
                elif shieldOn > 0 and hitOn == True :
                    playerNum8b = ""
                    shield8b = False
                    coin8b = False
                    strikes8b = False
                    boost8b = False
                    hitOn = False
                    
                else :
                    if wordCounter == 0 :
                        newLabel = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 1 :
                        newLabel2 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 2 :
                        newLabel3 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 3 :
                        newLabel4 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 4 :
                        newLabel5 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 5 :
                        newLabel6 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 6 :
                        newLabel7 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 7 :
                        newLabel8 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 8 :
                        newLabel9 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 9 :
                        newLabel10 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 10 :
                        newLabel11 = myFontb.render(enemyText8b, 1, WORD_COLOR) 
                    if wordCounter == 11 :
                        newLabel12 = myFontb.render(enemyText8b, 1, WORD_COLOR)  
                enemyColl8B(enemyList8b)
                for enemy8Posb in enemyList8b :
                    pygame.draw.rect(gameScreen, BLACK, (enemy8Posb[0], enemy8Posb[1], 0, 0))
                enemyList8b = []
                print("8B - " + playerNum8b)
                if playerNum8b == "" and boost8b == False and coin8b == False and strikes8b == False and shield8b == False:
                    letterBlank = True
                    letterWipe()
                elif playerNum8b == "" and coin8b == True and hitOn == False :
                    coinSound.play()
                    addCoin += 1
                    coinLabel = myFont3.render(coinText + format(addCoin), 1, WHITE)
                    scoreCount += 5
                    scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                    scoreAdd = "+ 5"
                    scoreAdd1 = "Found a Coin!"
                    scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                    scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    def scoreDisp():
                        global scoreAdd
                        global scoreAdd1
                        global scoreUp
                        global scoreUpb
                        scoreAdd = ""
                        scoreAdd1 = ""
                        scoreUp = myFontb.render(scoreAdd, 1, WHITE)
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                    scorePop = threading.Timer(1.5, scoreDisp)
                    scorePop.start()
                elif playerNum8b == "" and coin8b == False and strikes8b == False and boost8b == True and speedOn == False and shield8b == False and hitOn == False :
                        speedSound.play()
                        boostsUsed += 1
                        speedLabel = myFont3.render((speedText), 1, (255,0,50))
                        boostAdd = "SPEED BOOST!"  
                        boostUp = myFont4.render(boostAdd, 1, WHITE)
                        def boostDisp():
                            global boostAdd
                            global boostUp
                            boostAdd = ""
                            boostUp = myFont4.render(boostAdd, 1, WHITE)
                        boostPop = threading.Timer(1.5, boostDisp)
                        boostPop.start()
                        speedTimer += 20 
                        speedPop = threading.Timer(speedTimer, speedDisp)
                        speedPop.start()
                        speedOn = True
                elif playerNum8b == "" and boost8b == True and speedOn == True and hitOn == False :
                        speedOn = True
                else:
                    if playerNum8b == "" and coin8b == False and boost8b == False and strikes8b == False and shield8b == True and hitOn == False :
                        dripSound.play()
                        shieldOn +=1
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        scoreAdd1 = "Shield +!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif playerNum8b == "" and coin8b == False and strikes8b == True and boost8b == False and shield8b == False and hitOn == False : 
                        strikesCount +=1
                        dripSound.play()
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        scoreAdd1 = "Extra Strike!"
                        scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        def scoreDisp():
                            global scoreAdd1
                            global scoreUpb
                            scoreAdd1 = ""
                            scoreUpb = myFont3.render(scoreAdd1, 1, WHITE)
                        scorePop = threading.Timer(1.5, scoreDisp)
                        scorePop.start()
                    elif hitOn == True: 
                        letterWipe()
                        hitOn = False
                    elif playerNum8b == "" and hitOn == True and (coin8b==True or strikes8b==True or boost8b==True or shield8b==True):
                        letterBlank = True
                        letterWipe()
                        hitOn = False
                    
                    else:
                        scoreAdd8b()
                        dripSound.play()
                        wordList.append(playerNum8b)
                        wordCounter += 1
                print(wordList)

            if wordCounter >= 11:
                letterWipe()

            if foundCount >=50:
                endGame = True

                

            if (strikesCount <= 0 or endGame == True )and endStop == False:
                

                gameStop = True
                gameScreen.blit(BLANK_BG, (0, 0))
                

                strikesLabel = myFont3.render(blankText, 1, WHITE)

                foundLabel = myFont3.render(blankText, 1, WHITE)
                scoreLabel = myFont3.render(blankText, 1, WHITE)
                shieldLabel = myFont3.render(blankText, 1, WHITE)
                lettersLabel = myFont3.render(blankText, 1, WHITE)
                speedLabel = myFont3.render(blankText, 1, WHITE)
                scoreUp = myFontb.render(blankText, 1, WHITE)
                scoreUpb = myFont.render(blankText, 1, WHITE)
                scoreUpc = myFont.render(blankText, 1, WHITE)
                wordLabel = myFont.render(blankText, 1, WHITE)
                lettersTextLabel = myFont.render(blankText, 1, WHITE)
                coinLabel = myFont.render(blankText, 1, WHITE)

                
                boostFoundText = "Boosts Used: "
                boostFoundLabel = myFont3.render(boostFoundText + format(boostsUsed), 1, (100,100,100))
                gameScreen.blit(boostFoundLabel, (275, 70))
                shieldScoreText = "Shields Used: "
                shieldScoreLabel = myFont3.render(shieldScoreText + format(shieldScore), 1, (100,100,100))
                gameScreen.blit(shieldScoreLabel, (275, 85))
                strikesScoreText = "Strikes Used: "
                strikesScoreLabel = myFont3.render(strikesScoreText + format(strikesScore), 1, (100,100,100))
                gameScreen.blit(strikesScoreLabel, (550, 85))
                coinsFoundText = "Gold Earned: "
                coinsFoundLabel = myFont3.render(coinsFoundText + format(addCoin), 1, (100,100,100))
                gameScreen.blit(coinsFoundLabel, (550, 70))        
                wordsFoundText = "Words Found: "
                wordsFoundLabel = myFont3.render(wordsFoundText, 1, (100,100,100))
                gameScreen.blit(wordsFoundLabel, (150, 115))
                scorePlusText = "Points Scored: " + format(scoreCount-scoreMinus)
                scorePlusLabel = myFont3.render(scorePlusText, 1, (100,100,100))
                gameScreen.blit(scorePlusLabel, (150, 540))
                scoreMinusText = format(scoreMinus) + " Points Lost"
                scoreMinusLabel = myFont3.render(scoreMinusText, 1, (100,100,100))
                gameScreen.blit(scoreMinusLabel, (150, 555))
                totalScoreText = "Total Score: " + format(scoreCount)
                totalScoreLabel = myFont3.render(totalScoreText, 1, (100,100,100))
                gameScreen.blit(totalScoreLabel, (150, 570))
                exitText = "Press [ESCAPE] to exit"
                exitLabel = myFont3.render(exitText, 1, (100,100,100))
                gameScreen.blit(exitLabel, (550, 570))
                if foundCount == 0 :
                    wordScoreText0 = " You didn't find any words... "
                    wordScoreLabel0 = myFont3.render(wordScoreText0, 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel0, (150, 190))
                if foundCount >= 1:
                    wordScoreText0 = " #1.  "
                    wordSpacer = "   -   "
                    ptsText = " pts"
                    wordScoreLabel0 = myFont3.render((wordScoreText0 + wordScore[0] + wordSpacer + format(scoreList[0]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel0, (150, 130))
                if foundCount >= 2:
                    wordScoreText1 = " #2.  "
                    wordScoreLabel1 = myFont3.render((wordScoreText1 + wordScore[1] + wordSpacer + format(scoreList[1]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel1, (425, 130))
                if foundCount >= 3:
                    wordScoreText2 = " #3.  "
                    wordScoreLabel2 = myFont3.render((wordScoreText2 + wordScore[2] + wordSpacer + format(scoreList[2]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel2, (150, 145))
                if foundCount >= 4:
                    wordScoreText3 = " #4.  "
                    wordScoreLabel3 = myFont3.render((wordScoreText3 + wordScore[3] + wordSpacer + format(scoreList[3]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel3, (425, 145))
                if foundCount >= 5:
                    wordScoreText4 = " #5.  "
                    wordScoreLabel4 = myFont3.render((wordScoreText4 + wordScore[4] + wordSpacer + format(scoreList[4]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel4, (150, 160))
                if foundCount >= 6:
                    wordScoreText5 = " #6.  "
                    wordScoreLabel5 = myFont3.render((wordScoreText5 + wordScore[5] + wordSpacer + format(scoreList[5]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel5, (425, 160))
                if foundCount >= 7:
                    wordScoreText6 = " #7.  "
                    wordScoreLabel6 = myFont3.render((wordScoreText6 + wordScore[6] + wordSpacer + format(scoreList[6]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel6, (150, 175))    
                if foundCount >= 8:
                    wordScoreText7 = " #8.  "
                    wordScoreLabel7 = myFont3.render((wordScoreText7 + wordScore[7] + wordSpacer + format(scoreList[7]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel7, (425, 175))
                if foundCount >= 9:
                    wordScoreText8 = " #9.  "
                    wordScoreLabel8 = myFont3.render((wordScoreText8 + wordScore[8] + wordSpacer + format(scoreList[8]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel8, (150, 190))
                if foundCount >= 10:
                    wordScoreText9 = "#10.  "
                    wordScoreLabel9 = myFont3.render((wordScoreText9 + wordScore[9] + wordSpacer + format(scoreList[9]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel9, (425, 190))
                if foundCount >= 11:
                    wordScoreText10 = "#11.  "
                    wordScoreLabel10 = myFont3.render((wordScoreText10 + wordScore[10] + wordSpacer + format(scoreList[10]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel10, (150, 205))
                if foundCount >= 12:
                    wordScoreText11 = "#12.  "
                    wordScoreLabel11 = myFont3.render((wordScoreText11 + wordScore[11] + wordSpacer + format(scoreList[11]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel11, (425, 205))
                if foundCount >= 13:
                    wordScoreText12 = "#13.  "
                    wordScoreLabel12 = myFont3.render((wordScoreText12 + wordScore[12] + wordSpacer + format(scoreList[12]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel12, (150, 220))
                if foundCount >= 14:
                    wordScoreText13 = "#14.  "
                    wordScoreLabel13 = myFont3.render((wordScoreText13 + wordScore[13] + wordSpacer + format(scoreList[13]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel13, (425, 220))
                if foundCount >= 15:
                    wordScoreText14 = "#15.  "
                    wordScoreLabel14 = myFont3.render((wordScoreText14 + wordScore[14] + wordSpacer + format(scoreList[14]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel14, (150, 235))
                if foundCount >= 16:
                    wordScoreText15 = "#16.  "
                    wordScoreLabel15 = myFont3.render((wordScoreText15 + wordScore[15] + wordSpacer + format(scoreList[15]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel15, (425, 235))
                if foundCount >= 17:
                    wordScoreText16 = "#17.  "
                    wordScoreLabel16 = myFont3.render((wordScoreText16 + wordScore[16] + wordSpacer + format(scoreList[16]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel16, (150, 250))
                if foundCount >= 18:
                    wordScoreText17 = "#18.  "
                    wordScoreLabel17 = myFont3.render((wordScoreText17 + wordScore[17] + wordSpacer + format(scoreList[17]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel17, (425, 250))
                if foundCount >= 19:
                    wordScoreText18 = "#19.  "
                    wordScoreLabel18 = myFont3.render((wordScoreText18 + wordScore[18] + wordSpacer + format(scoreList[18]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel18, (150, 265))
                if foundCount >= 20:
                    wordScoreText19 = "#20.  "
                    wordScoreLabel19 = myFont3.render((wordScoreText19 + wordScore[19] + wordSpacer + format(scoreList[19]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel19, (425, 265))
                if foundCount >= 21:
                    wordScoreText20 = "#21.  "
                    wordScoreLabel20 = myFont3.render((wordScoreText20 + wordScore[20] + wordSpacer + format(scoreList[20]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel20, (150, 280))
                if foundCount >= 22:
                    wordScoreText21 = "#22.  "
                    wordScoreLabel21 = myFont3.render((wordScoreText21 + wordScore[21] + wordSpacer + format(scoreList[21]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel21, (425, 280))
                if foundCount >= 23:
                    wordScoreText22 = "#23.  "
                    wordScoreLabel22 = myFont3.render((wordScoreText22 + wordScore[22] + wordSpacer + format(scoreList[22]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel22, (150, 295))
                if foundCount >= 24:
                    wordScoreText23 = "#24.  "
                    wordScoreLabel23 = myFont3.render((wordScoreText23 + wordScore[23] + wordSpacer + format(scoreList[23]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel23, (425, 295))
                if foundCount >= 25:
                    wordScoreText24 = "#25.  "
                    wordScoreLabel24 = myFont3.render((wordScoreText24 + wordScore[24] + wordSpacer + format(scoreList[24]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel24, (150, 310))
                if foundCount >= 26:
                    wordScoreText25 = "#26.  "
                    wordScoreLabel25 = myFont3.render((wordScoreText25 + wordScore[25] + wordSpacer + format(scoreList[25]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel25, (425, 310))
                if foundCount >= 27:
                    wordScoreText26 = "#27.  "
                    wordScoreLabel26 = myFont3.render((wordScoreText26 + wordScore[26] + wordSpacer + format(scoreList[26]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel26, (150, 325))
                if foundCount >= 28:
                    wordScoreText27 = "#28.  "
                    wordScoreLabel27 = myFont3.render((wordScoreText27 + wordScore[27] + wordSpacer + format(scoreList[27]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel27, (425, 325))
                if foundCount >= 29:
                    wordScoreText28 = "#29.  "
                    wordScoreLabel28 = myFont3.render((wordScoreText28 + wordScore[28] + wordSpacer + format(scoreList[28]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel28, (150, 340))
                if foundCount >= 30:
                    wordScoreText29 = "#30.  "
                    wordScoreLabel29 = myFont3.render((wordScoreText29 + wordScore[29] + wordSpacer + format(scoreList[29]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel29, (425, 340))
                if foundCount >= 31:
                    wordScoreText30 = "#31.  "
                    wordScoreLabel30 = myFont3.render((wordScoreText30 + wordScore[30] + wordSpacer + format(scoreList[30]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel30, (150, 355))
                if foundCount >= 32:
                    wordScoreText31 = "#32.  "
                    wordScoreLabel31 = myFont3.render((wordScoreText31 + wordScore[31] + wordSpacer + format(scoreList[31]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel31, (425, 355))
                if foundCount >= 33:
                    wordScoreText32 = "#33.  "
                    wordScoreLabel32 = myFont3.render((wordScoreText32 + wordScore[32] + wordSpacer + format(scoreList[32]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel32, (150, 360))
                if foundCount >= 34:
                    wordScoreText33 = "#34.  "
                    wordScoreLabel33 = myFont3.render((wordScoreText33 + wordScore[33] + wordSpacer + format(scoreList[33]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel33, (425, 360))
                if foundCount >= 35:
                    wordScoreText34 = "#35.  "
                    wordScoreLabel34 = myFont3.render((wordScoreText34 + wordScore[34] + wordSpacer + format(scoreList[34]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel34, (150, 375))
                if foundCount >= 36:
                    wordScoreText35 = "#36.  "
                    wordScoreLabel35 = myFont3.render((wordScoreText35 + wordScore[35] + wordSpacer + format(scoreList[35]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel35, (425, 375))
                if foundCount >= 37:
                    wordScoreText36 = "#37.  "
                    wordScoreLabel36 = myFont3.render((wordScoreText36 + wordScore[36] + wordSpacer + format(scoreList[36]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel36, (150, 390))
                if foundCount >= 38:
                    wordScoreText37 = "#38.  "
                    wordScoreLabel37 = myFont3.render((wordScoreText37 + wordScore[37] + wordSpacer + format(scoreList[37]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel37, (425, 390))
                if foundCount >= 39:
                    wordScoreText38 = "#39.  "
                    wordScoreLabel38 = myFont3.render((wordScoreText38 + wordScore[38] + wordSpacer + format(scoreList[38]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel38, (150, 405))
                if foundCount >= 40:
                    wordScoreText39 = "#40.  "
                    wordScoreLabel39 = myFont3.render((wordScoreText39 + wordScore[39] + wordSpacer + format(scoreList[39]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel39, (425, 405))
                if foundCount >= 41:
                    wordScoreText40 = "#41.  "
                    wordScoreLabel40 = myFont3.render((wordScoreText40 + wordScore[40] + wordSpacer + format(scoreList[40]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel40, (150, 420))
                if foundCount >= 42:
                    wordScoreText41 = "#42.  "
                    wordScoreLabel41 = myFont3.render((wordScoreText41 + wordScore[41] + wordSpacer + format(scoreList[41]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel41, (425, 420))
                if foundCount >= 43:
                    wordScoreText42 = "#43.  "
                    wordScoreLabel42 = myFont3.render((wordScoreText42 + wordScore[42] + wordSpacer + format(scoreList[42]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel42, (150, 435))
                if foundCount >= 44:
                    wordScoreText43 = "#44.  "
                    wordScoreLabel43 = myFont3.render((wordScoreText43 + wordScore[43] + wordSpacer + format(scoreList[43]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel43, (425, 435))
                if foundCount >= 45:
                    wordScoreText44 = "#45.  "
                    wordScoreLabel44 = myFont3.render((wordScoreText44 + wordScore[44] + wordSpacer + format(scoreList[44]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel44, (150, 450))
                if foundCount >= 46:
                    wordScoreText45 = "#46.  "
                    wordScoreLabel45 = myFont3.render((wordScoreText45 + wordScore[45] + wordSpacer + format(scoreList[45]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel45, (425, 450))
                if foundCount >= 47:
                    wordScoreText46 = "#47.  "
                    wordScoreLabel46 = myFont3.render((wordScoreText46 + wordScore[46] + wordSpacer + format(scoreList[46]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel46, (150, 465))
                if foundCount >= 48:
                    wordScoreText47 = "#48.  "
                    wordScoreLabel47 = myFont3.render((wordScoreText47 + wordScore[47] + wordSpacer + format(scoreList[47]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel47, (425, 465))
                if foundCount >= 49:
                    wordScoreText48 = "#49.  "
                    wordScoreLabel48 = myFont3.render((wordScoreText48 + wordScore[48] + wordSpacer + format(scoreList[48]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel48, (150, 480))
                if foundCount >= 50:
                    wordScoreText49 = "#50.  "
                    wordScoreLabel49 = myFont3.render((wordScoreText49 + wordScore[49] + wordSpacer + format(scoreList[49]) + ptsText), 1, (100,100,100))
                    gameScreen.blit(wordScoreLabel49, (425, 480))

                    
                    
                pygame.display.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()   

                        
                    


            if foundCount == 0 and startStop == False and tutStop == False:
                gameStop = True        
                strikesLabel = myFont3.render(blankText, 1, WHITE)
                foundLabel = myFont3.render(blankText, 1, WHITE)
                scoreLabel = myFont3.render(blankText, 1, WHITE)
                shieldLabel = myFont3.render(blankText, 1, WHITE)
                speedLabel = myFont3.render(blankText, 1, WHITE)
                lettersLabel = myFont3.render(blankText, 1, WHITE)
                scoreUp = myFontb.render(blankText, 1, WHITE)
                scoreUpb = myFont.render(blankText, 1, WHITE)
                scoreUpc = myFont.render(blankText, 1, WHITE)
                wordLabel = myFont.render(blankText, 1, WHITE)
                lettersTextLabel = myFont.render(blankText, 1, WHITE)
                coinLabel = myFont.render(blankText, 1, WHITE)
                gameScreen.blit(TITLE_SCREEN, (0, 0))
                pygame.display.update()



                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        tutStop  = True


                    if event.key == pygame.K_SPACE:
                        pygame.draw.rect(gameScreen, (100,100,100), (0, 0, gameWidth, gameHeight*.1))  
                        strikesLabel = myFont3.render(strikesText + format(strikesCount), 1, WHITE)
                        foundLabel = myFont3.render(foundText + format(foundCount), 1, WHITE)
                        scoreLabel = myFont3.render(scoreText + format(scoreCount), 1, WHITE)
                        shieldLabel = myFont3.render(shieldText + format(shieldOn), 1, WHITE)
                        speedLabel = myFont3.render(speedText, 1, WHITE)
                        wordLabel = myFont3.render(wordLabelText, 1, BLACK)
                        lettersTextLabel = myFont3.render(lettersTextLabelText, 1, WHITE)
                        coinLabel = myFont3.render(coinText, 1, WHITE)
                        pygame.display.update()
                        startStop = True
                        tutStop = True


            if foundCount == 0 and startStop == False and tutStop == True:
                gameStop = True        
                strikesLabel = myFont3.render(blankText, 1, WHITE)
                foundLabel = myFont3.render(blankText, 1, WHITE)
                scoreLabel = myFont3.render(blankText, 1, WHITE)
                shieldLabel = myFont3.render(blankText, 1, WHITE)
                speedLabel = myFont3.render(blankText, 1, WHITE)
                lettersLabel = myFont3.render(blankText, 1, WHITE)
                scoreUp = myFontb.render(blankText, 1, WHITE)
                scoreUpb = myFont.render(blankText, 1, WHITE)
                scoreUpc = myFont.render(blankText, 1, WHITE)
                wordLabel = myFont.render(blankText, 1, WHITE)
                lettersTextLabel = myFont.render(blankText, 1, WHITE)
                coinLabel = myFont.render(blankText, 1, WHITE)
                gameScreen.blit(TUT_SCREEN, (0, 0))
                pygame.display.update()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        gameScreen.blit(TITLE_SCREEN, (0, 0))
                        pygame.display.update()
                        tutStop  = False

                  
                



            if foundCount == 0 and startStop == True and strikesCount != 0 :
                gameStop = False

                
            def scoreAdd():
                global playerNum
                global scoreNum
                if playerNum == "A" or playerNum == "E" or playerNum == "O" or playerNum == "T" :
                    scoreNum += 1
                elif playerNum == "D" or playerNum == "H" or playerNum == "I" or playerNum == "L" or playerNum == "N" or playerNum == "R" or playerNum == "S" :
                    scoreNum += 3
                elif playerNum == "C" or playerNum == "F" or playerNum == "G" or playerNum == "M" or playerNum == "U" or playerNum == "W" :
                    scoreNum += 6
                elif playerNum == "B" or playerNum == "J" or playerNum == "K" or playerNum == "P" or playerNum == "V" or playerNum == "Y" :
                    scoreNum += 8
                elif playerNum == "Q" or playerNum == "X" or playerNumb == "Z" :
                    scoreNum += 12
                print(scoreNum)

            def scoreAddb():
                global playerNumb
                global scoreNum
                if playerNumb == "A" or playerNumb == "E" or playerNumb == "O" or playerNumb == "T" :
                    scoreNum += 1
                elif playerNumb == "D" or playerNumb == "H" or playerNumb == "I" or playerNumb == "L" or playerNumb == "N" or playerNumb == "R" or playerNumb == "S" :
                    scoreNum += 3
                elif playerNumb == "C" or playerNumb == "F" or playerNumb == "G" or playerNumb == "M" or playerNumb == "U" or playerNumb == "W" :
                    scoreNum += 6
                elif playerNumb == "B" or playerNumb == "J" or playerNumb == "K" or playerNumb == "P" or playerNumb == "V" or playerNumb == "Y" :
                    scoreNum += 8
                elif playerNumb == "Q" or playerNumb == "X" or playerNumb == "Z" :
                    scoreNum += 12
                print(scoreNum)

            def scoreAdd2():
                global playerNum2
                global scoreNum        
                if playerNum2 == "A" or playerNum2 == "E" or playerNum2 == "O" or playerNum2 == "T" :
                    scoreNum += 1
                elif playerNum2 == "D" or playerNum2 == "H" or playerNum2 == "I" or playerNum2 == "L" or playerNum2 == "N" or playerNum2 == "R" or playerNum2 == "S" :
                    scoreNum += 3
                elif playerNum2 == "C" or playerNum2 == "F" or playerNum2 == "G" or playerNum2 == "M" or playerNum2 == "U" or playerNum2 == "W" :
                    scoreNum += 6
                elif playerNum2 == "B" or playerNum2 == "J" or playerNum2 == "K" or playerNum2 == "P" or playerNum2 == "V" or playerNum2 == "Y" :
                    scoreNum += 8
                elif playerNum2 == "Q" or playerNum2 == "X" or playerNum2 == "Z" :
                    scoreNum += 12
                print(scoreNum)

            def scoreAdd2b():
                global playerNum2b
                global scoreNum            
                if playerNum2b == "A" or playerNum2b == "E" or playerNum2b == "O" or playerNum2b == "T" :
                    scoreNum += 1
                elif playerNum2b == "D" or playerNum2b == "H" or playerNum2b == "I" or playerNum2b == "L" or playerNum2b == "N" or playerNum2b == "R" or playerNum2b == "S" :
                    scoreNum += 3
                elif playerNum2b == "C" or playerNum2b == "F" or playerNum2b == "G" or playerNum2b == "M" or playerNum2b == "U" or playerNum2b == "W" :
                    scoreNum += 6
                elif playerNum2b == "B" or playerNum2b == "J" or playerNum2b == "K" or playerNum2b == "P" or playerNum2b == "V" or playerNum2b == "Y" :
                    scoreNum += 8
                elif playerNum2b == "Q" or playerNum2b == "X" or playerNum2b == "Z" :
                    scoreNum += 12
                print(scoreNum)

            def scoreAdd3():
                global playerNum3
                global scoreNum            
                if playerNum3 == "A" or playerNum3 == "E" or playerNum3 == "O" or playerNum3 == "T" :
                    scoreNum += 1
                elif playerNum3 == "D" or playerNum3 == "H" or playerNum3 == "I" or playerNum3 == "L" or playerNum3 == "N" or playerNum3 == "R" or playerNum3 == "S" :
                    scoreNum += 3
                elif playerNum3 == "C" or playerNum3 == "F" or playerNum3 == "G" or playerNum3 == "M" or playerNum3 == "U" or playerNum3 == "W" :
                    scoreNum += 6
                elif playerNum3 == "B" or playerNum3 == "J" or playerNum3 == "K" or playerNum3 == "P" or playerNum3 == "V" or playerNum3 == "Y" :
                    scoreNum += 8
                elif playerNum3 == "Q" or playerNum3 == "X" or playerNum3 == "Z" :
                    scoreNum += 12
                print(scoreNum)
                    
            def scoreAdd3b():
                global playerNum3b
                global scoreNum
                if playerNum3b == "A" or playerNum3b == "E" or playerNum3b == "O" or playerNum3b == "T" :
                    scoreNum += 1
                elif playerNum3b == "D" or playerNum3b == "H" or playerNum3b == "I" or playerNum3b == "L" or playerNum3b == "N" or playerNum3b == "R" or playerNum3b == "S" :
                    scoreNum += 3
                elif playerNum3b == "C" or playerNum3b == "F" or playerNum3b == "G" or playerNum3b == "M" or playerNum3b == "U" or playerNum3b == "W" :
                    scoreNum += 6
                elif playerNum3b == "B" or playerNum3b == "J" or playerNum3b == "K" or playerNum3b == "P" or playerNum3b == "V" or playerNum3b == "Y" :
                    scoreNum += 8
                elif playerNum3b == "Q" or playerNum3b == "X" or playerNum3b == "Z" :
                    scoreNum += 12
                print(scoreNum)

            def scoreAdd4():
                global playerNum4
                global scoreNum
                if playerNum4 == "A" or playerNum4 == "E" or playerNum4 == "O" or playerNum4 == "T" :
                    scoreNum += 1
                elif playerNum4 == "D" or playerNum4 == "H" or playerNum4 == "I" or playerNum4 == "L" or playerNum4 == "N" or playerNum4 == "R" or playerNum4 == "S" :
                    scoreNum += 3
                elif playerNum4 == "C" or playerNum4 == "F" or playerNum4 == "G" or playerNum4 == "M" or playerNum4 == "U" or playerNum4 == "W" :
                    scoreNum += 6
                elif playerNum4 == "B" or playerNum4 == "J" or playerNum4 == "K" or playerNum4 == "P" or playerNum4 == "V" or playerNum4 == "Y" :
                    scoreNum += 8
                elif playerNum4 == "Q" or playerNum4 == "X" or playerNum4 == "Z" :
                    scoreNum += 12
                print(scoreNum)

            def scoreAdd4b():
                global playerNum4b
                global scoreNum            
                if playerNum4b == "A" or playerNum4b == "E" or playerNum4b == "O" or playerNum4b == "T" :
                    scoreNum += 1
                elif playerNum4b == "D" or playerNum4b == "H" or playerNum4b == "I" or playerNum4b == "L" or playerNum4b == "N" or playerNum4b == "R" or playerNum4b == "S" :
                    scoreNum += 3
                elif playerNum4b == "C" or playerNum4b == "F" or playerNum4b == "G" or playerNum4b == "M" or playerNum4b == "U" or playerNum4b == "W" :
                    scoreNum += 6
                elif playerNum4b == "B" or playerNum4b == "J" or playerNum4b == "K" or playerNum4b == "P" or playerNum4b == "V" or playerNum4b == "Y" :
                    scoreNum += 8
                elif playerNum4b == "Q" or playerNum4b == "X" or playerNum4b == "Z" :
                    scoreNum += 12
                print(scoreNum)

            def scoreAdd5():
                global playerNum5
                global scoreNum
                if playerNum5 == "A" or playerNum5 == "E" or playerNum5 == "O" or playerNum5 == "T" :
                    scoreNum += 1
                elif playerNum5 == "D" or playerNum5 == "H" or playerNum5 == "I" or playerNum5 == "L" or playerNum5 == "N" or playerNum5 == "R" or playerNum5 == "S" :
                    scoreNum += 3
                elif playerNum5 == "C" or playerNum5 == "F" or playerNum5 == "G" or playerNum5 == "M" or playerNum5 == "U" or playerNum5 == "W" :
                    scoreNum += 6
                elif playerNum5 == "B" or playerNum5 == "J" or playerNum5 == "K" or playerNum5 == "P" or playerNum5 == "V" or playerNum5 == "Y" :
                    scoreNum += 8
                elif playerNum5 == "Q" or playerNum5 == "X" or playerNum5 == "Z" :
                    scoreNum += 12
                print(scoreNum)
                    
            def scoreAdd5b():
                global playerNum5b
                global scoreNum
                if playerNum5b == "A" or playerNum5b == "E" or playerNum5b == "O" or playerNum5b == "T" :
                    scoreNum += 1
                elif playerNum5b == "D" or playerNum5b == "H" or playerNum5b == "I" or playerNum5b == "L" or playerNum5b == "N" or playerNum5b == "R" or playerNum5b == "S" :
                    scoreNum += 3
                elif playerNum5b == "C" or playerNum5b == "F" or playerNum5b == "G" or playerNum5b == "M" or playerNum5b == "U" or playerNum5b == "W" :
                    scoreNum += 6
                elif playerNum5b == "B" or playerNum5b == "J" or playerNum5b == "K" or playerNum5b == "P" or playerNum5b == "V" or playerNum5b == "Y" :
                    scoreNum += 8
                elif playerNum5b == "Q" or playerNum5b == "X" or playerNum5b == "Z" :
                    scoreNum += 12
                print(scoreNum)

            def scoreAdd6():
                global playerNum6
                global scoreNum
                if playerNum6 == "A" or playerNum6 == "E" or playerNum6 == "O" or playerNum6 == "T" :
                    scoreNum += 1
                elif playerNum6 == "D" or playerNum6 == "H" or playerNum6 == "I" or playerNum6 == "L" or playerNum6 == "N" or playerNum6 == "R" or playerNum6 == "S" :
                    scoreNum += 3
                elif playerNum6 == "C" or playerNum6 == "F" or playerNum6 == "G" or playerNum6 == "M" or playerNum6 == "U" or playerNum6 == "W" :
                    scoreNum += 6
                elif playerNum6 == "B" or playerNum6 == "J" or playerNum6 == "K" or playerNum6 == "P" or playerNum6 == "V" or playerNum6 == "Y" :
                    scoreNum += 8
                elif playerNum6 == "Q" or playerNum6 == "X" or playerNum6 == "Z" :
                    scoreNum += 12
                print(scoreNum)

            def scoreAdd6b():
                global playerNum6b
                global scoreNum            
                if playerNum6b == "A" or playerNum6b == "E" or playerNum6b == "O" or playerNum6b == "T" :
                    scoreNum += 1
                elif playerNum6b == "D" or playerNum6b == "H" or playerNum6b == "I" or playerNum6b == "L" or playerNum6b == "N" or playerNum6b == "R" or playerNum6b == "S" :
                    scoreNum += 3
                elif playerNum6b == "C" or playerNum6b == "F" or playerNum6b == "G" or playerNum6b == "M" or playerNum6b == "U" or playerNum6b == "W" :
                    scoreNum += 6
                elif playerNum6b == "B" or playerNum6b == "J" or playerNum6b == "K" or playerNum6b == "P" or playerNum6b == "V" or playerNum6b == "Y" :
                    scoreNum += 8
                elif playerNum6b == "Q" or playerNum6b == "X" or playerNum6b == "Z" :
                    scoreNum += 12
                print(scoreNum)

            def scoreAdd7():
                global playerNum7
                global scoreNum
                if playerNum7 == "A" or playerNum7 == "E" or playerNum7 == "O" or playerNum7 == "T" :
                    scoreNum += 1
                elif playerNum7 == "D" or playerNum7 == "H" or playerNum7 == "I" or playerNum7 == "L" or playerNum7 == "N" or playerNum7 == "R" or playerNum7 == "S" :
                    scoreNum += 3
                elif playerNum7 == "C" or playerNum7 == "F" or playerNum7 == "G" or playerNum7 == "M" or playerNum7 == "U" or playerNum7 == "W" :
                    scoreNum += 6
                elif playerNum7 == "B" or playerNum7 == "J" or playerNum7 == "K" or playerNum7 == "P" or playerNum7 == "V" or playerNum7 == "Y" :
                    scoreNum += 8
                elif playerNum7 == "Q" or playerNum7 == "X" or playerNum7 == "Z" :
                    scoreNum += 12
                print(scoreNum)

            def scoreAdd7b():
                global playerNum7b
                global scoreNum
                if playerNum7b == "A" or playerNum7b == "E" or playerNum7b == "O" or playerNum7b == "T" :
                    scoreNum += 1
                elif playerNum7b == "D" or playerNum7b == "H" or playerNum7b == "I" or playerNum7b == "L" or playerNum7b == "N" or playerNum7b == "R" or playerNum7b == "S" :
                    scoreNum += 3
                elif playerNum7b == "C" or playerNum7b == "F" or playerNum7b == "G" or playerNum7b == "M" or playerNum7b == "U" or playerNum7b == "W" :
                    scoreNum += 6
                elif playerNum7b == "B" or playerNum7b == "J" or playerNum7b == "K" or playerNum7b == "P" or playerNum7b == "V" or playerNum7b == "Y" :
                    scoreNum += 8
                elif playerNum7b == "Q" or playerNum7b == "X" or playerNum7b == "Z" :
                    scoreNum += 12
                print(scoreNum)

            def scoreAdd8():
                global playerNum8
                global scoreNum
                if playerNum8 == "A" or playerNum8 == "E" or playerNum8 == "O" or playerNum8 == "T" :
                    scoreNum += 1
                elif playerNum8 == "D" or playerNum8 == "H" or playerNum8 == "I" or playerNum8 == "L" or playerNum8 == "N" or playerNum8 == "R" or playerNum8 == "S" :
                    scoreNum += 3
                elif playerNum8 == "C" or playerNum8 == "F" or playerNum8 == "G" or playerNum8 == "M" or playerNum8 == "U" or playerNum8 == "W" :
                    scoreNum += 6
                elif playerNum8 == "B" or playerNum8 == "J" or playerNum8 == "K" or playerNum8 == "P" or playerNum8 == "V" or playerNum8 == "Y" :
                    scoreNum += 8
                elif playerNum8 == "Q" or playerNum8 == "X" or playerNum8 == "Z" :
                    scoreNum += 12
                print(scoreNum)


            def scoreAdd8b():
                global playerNum8b
                global scoreNum            
                if playerNum8b == "A" or playerNum8b == "E" or playerNum8b == "O" or playerNum8b == "T" :
                    scoreNum += 1
                elif playerNum8b == "D" or playerNum8b == "H" or playerNum8b == "I" or playerNum8b == "L" or playerNum8b == "N" or playerNum8b == "R" or playerNum8b == "S" :
                    scoreNum += 3
                elif playerNum8b == "C" or playerNum8b == "F" or playerNum8b == "G" or playerNum8b == "M" or playerNum8b == "U" or playerNum8b == "W" :
                    scoreNum += 6
                elif playerNum8b == "B" or playerNum8b == "J" or playerNum8b == "K" or playerNum8b == "P" or playerNum8b == "V" or playerNum8b == "Y" :
                    scoreNum += 8
                elif playerNum8b == "Q" or playerNum8b == "X" or playerNum8b == "Z" :
                    scoreNum += 12
                print(scoreNum)

            def scoreAddSet():
                global scoreNum
                global scoreNum2
                global gameSpeed
                global scoreMult
                scoreNum2 = scoreNum
                if gameSpeed <= 4:
                    scoreMult = 1
                elif gameSpeed == 5:
                    scoreMult = 1.25
                elif gameSpeed == 6:
                    scoreMult = 1.5
                elif gameSpeed == 8 :
                    scoreMult = 2
                elif gameSpeed == 10 :
                    scoreMult = 3
                elif gameSpeed >= 13 :
                    scoreMult = 5

                 


                

            if gameStop == False:
                gameScreen.blit(MAIN_HEADER, (0, 0))
                gameScreen.blit(MAIN_FOOTER, (0, 520))
            gameScreen.blit(newLabel, (selectPos[0], selectPos[1]))
            gameScreen.blit(newLabel2, (select2Pos[0], select2Pos[1]))
            gameScreen.blit(newLabel3, (select3Pos[0], select3Pos[1]))
            gameScreen.blit(newLabel4, (select4Pos[0], select4Pos[1]))
            gameScreen.blit(newLabel5, (select5Pos[0], select5Pos[1]))
            gameScreen.blit(newLabel6, (select6Pos[0], select6Pos[1]))
            gameScreen.blit(newLabel7, (select7Pos[0], select7Pos[1]))
            gameScreen.blit(newLabel8, (select8Pos[0], select8Pos[1]))
            gameScreen.blit(newLabel9, (select9Pos[0], select9Pos[1]))
            gameScreen.blit(newLabel10, (select10Pos[0], select10Pos[1]))
            gameScreen.blit(newLabel11, (select11Pos[0], select11Pos[1]))
            gameScreen.blit(newLabel12, (select12Pos[0], select12Pos[1]))
            gameScreen.blit(strikesLabel, (strikesPos[0], strikesPos[1]))
            gameScreen.blit(foundLabel, (foundPos[0], foundPos[1]))
            gameScreen.blit(scoreLabel, (scorePos[0], scorePos[1]))
            gameScreen.blit(scoreUp, (scorePos[0], scorePos[1]+18))
            gameScreen.blit(scoreUpb, (scorePos[0], scorePos[1]+36))
            gameScreen.blit(scoreUpc, (gameWidth*.35, gameHeight/2))
            gameScreen.blit(boostUp, (gameWidth*.3, gameHeight/3))
            gameScreen.blit(lettersUp, (gameWidth*.02, gameHeight*.75))
            gameScreen.blit(shieldLabel, (shieldPos[0], shieldPos[1]))
            gameScreen.blit(lettersLabel, (lettersPos[0], lettersPos[1]))
            gameScreen.blit(speedLabel, (speedPos[0], speedPos[1]))
            gameScreen.blit(wordLabel, (wordLabelPos[0], wordLabelPos[1]))
            gameScreen.blit(lettersTextLabel, (lettersTextLabelPos[0], lettersTextLabelPos[1]))
            gameScreen.blit(coinLabel, (coinPos[0], coinPos[1]))


            

                
            pygame.display.update()


            
            
            clock.tick(30)

        return Fl 
            
if __name__ == '__main__':
    app = MainApp()
    app.run()

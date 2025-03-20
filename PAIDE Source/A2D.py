import pygame
import datetime
import pathlib
import wx
from colorama import Fore as TextColour
from time import sleep as Wait

ObjectList = []
PlayerList = []

def Error(text):
    print(f"{TextColour.RED}{text}{TextColour.RESET}")
    exit()

def Info(text):
    print(f"{TextColour.MAGENTA}{text}{TextColour.RESET}")

def Warn(text):
    print(f"{TextColour.YELLOW}{text}{TextColour.RESET}")

class Images():
    def __init__(self):

        self.BaseImages = { # Name : FilePath

            "Player" : "Assets\Images\Players\Player.png",
            "Enemy" : "Assets\Images\Enemy\Enemy.png",
            "Boss" : "Assets\Images\Enemies\Boss.png",
            "Robot" : "Assets\Images\Friendly\Good_Robot.png",
            "UpArrow": "Assets\Images\Objects\Arrow_Up.png",
        }

class Events():
    def __init__(self):

        self.events = ["quit", ]

class Instance():
    def __init__(self, Name:str = None, IsFullScreen:bool = False, Width:int = 400, Height:int = 400):
        
        self.External = wx.App(False)
        
        Info("""
Welcome to PAIDE
Doccumentation Can be Found at: <https://Insert-Link-Here.com>""")
        self.Init = pygame.init()
        self.Running = True
        self.ScreenHeight = Height
        self.ScreenWidth = Width
        
        self.Events = []
        
        if Name == None or Name.strip() == "":
            Error("Error: Instance must Require a Name")

        if IsFullScreen == True:

            self.ScreenWidth, self.ScreenHeight = wx.GetDisplaySize()
        
        pygame.display.set_mode((self.ScreenWidth,self.ScreenHeight))
        pygame.display.set_caption(str(Name))

    def EventRunner(self):
        for each in self.Events:
            try:
                eval(f"{each}()")
            except:
                print(f"Log: {datetime.datetime.now.strftime("%H:%M:%S")}, could not find '{each}' ")

    def Display(self):
        pygame.display.flip()
            
    
    def Leave(self):
        pygame.quit()
        exit()
        

class Player():
    def __init__(self, Name:str = "Player 1", Size:int = 2, MovementSpeed:int = 5, StartPositon:list = [100,100], MovementBinds:list = [pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_s], IsAnimated:bool = False):
        
        self.UserName = Name
        self.Position = StartPositon
        self.Size = Size
        self.Speed = MovementSpeed
        self.Binds = MovementBinds
        self.LastDirection = None

        self.Animated = IsAnimated

        self.FallBackImage = ""

        self.CurrentAnimationPoint = [None, 0]

        self.UpImages = []
        self.LeftImages = []
        self.RightImages = []
        self.DownImages = []

        PlayerList.append(str(self))
    
    def MovementQue(self):

        self.LastDirection = None

        if pygame.key.get_pressed() == self.Binds[0]: # UP
            self.LastDirection = "UP"

            if self.CurrentAnimationPoint[0] == "UP" and self.Animated:
                if self.CurrentAnimationPoint[1] == len(self.UpImages) - 1:
                    self.CurrentAnimationPoint[1] = 0
                else:
                    self.CurrentAnimationPoint[1] += 1
            else:
                self.CurrentAnimationPoint = ["UP", 0]
        
        if pygame.key.get_pressed() == self.Binds[1]: # LEFT
            self.LastDirection = "LEFT"

            if self.CurrentAnimationPoint[0] == "LEFT" and self.Animated:
                if self.CurrentAnimationPoint[1] == len(self.LeftImages) - 1:
                    self.CurrentAnimationPoint[1] = 0
                else:
                    self.CurrentAnimationPoint[1] += 1
            else:
                self.CurrentAnimationPoint = ["LEFT", 0]

        if pygame.key.get_pressed() == self.Binds[2]: # RIGHT
            self.LastDirection = "RIGHT"

            if self.CurrentAnimationPoint[0] == "RIGHT" and self.Animated:
                if self.CurrentAnimationPoint[1] == len(self.RightImages) - 1:
                    self.CurrentAnimationPoint[1] = 0
                else:
                    self.CurrentAnimationPoint[1] += 1
            else:
                self.CurrentAnimationPoint = ["RIGHT", 0]

        if pygame.key.get_pressed() == self.Binds[3]: # DOWN
            self.LastDirection = "DOWN"

            if self.CurrentAnimationPoint[0] == "DOWN" and self.Animated:
                if self.CurrentAnimationPoint[1] == len(self.DownImages) - 1:
                    self.CurrentAnimationPoint[1] = 0
                else:
                    self.CurrentAnimationPoint[1] += 1
            else:
                self.CurrentAnimationPoint = ["DOWN", 0]

        if self.LastDirection == "UP" and self.Animated:
            Wait(1)




class Object():
    def __init__(self, CollisionType:str = None, Width:int = 5, Height:int = 5, Texture:str = None):
        pass
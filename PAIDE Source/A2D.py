###################################
# Imports
import pygame
import datetime
import pathlib
import os
from subprocess import run 
import json
import wx
from colorama import Fore as TextColour
from time import sleep as Wait
import webbrowser
###########################################





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

        self.Events = ["quit"]
        self.CurrentEventID = ""
    
    def SendEvent(self, EventName:str = ""):
        self.CurrentEventID = str(EventName)

class Player():
    def __init__(self, Name:str = f"NewPlayer", Size:int = 2, MovementSpeed:int = 5, StartPositon:list = [100,100], MovementBinds:list = [pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_s], IsAnimated:bool = False):
        
        self.DisplayName = Name
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




class Instance():
    def __init__(self, Name:str = None, IsFullScreen:bool = False, Width:int = 400, Height:int = 400):
        
        self.External = wx.App(False)
        
        ConfigFile = pathlib.Path("Assets\cfg\cfg.json")
        try:
            Test = open(ConfigFile)
            Test.close()
        except:
            Error("Error: Configuration file could not be found")

        with open(ConfigFile, "r+") as NewConfig:
            self.Configs = json.load(NewConfig)

            Info("""
Welcome to PAIDE
Doccumentation Can be Found at: <https://Insert-Link-Here.com>""")
        
            if self.Configs["IsNewStartup"] == True:
                Warn("We will need to install the Python interpreter as it is your first time using this program")
                #run("Dependancies\PySource.exe") # change this to open the python download menu instead
                webbrowser.open_new_tab("https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe")
                self.Configs.update({"IsNewStartup" : False})
        
        os.remove(ConfigFile)
            
        with open(ConfigFile, "x") as NewConfig: 
            json.dump(self.Configs, NewConfig, indent = 4)
                
        
        self.Init = pygame.init()
        self.Running = True
        self.ScreenHeight = Height
        self.ScreenWidth = Width

        
        
        self.Events = []
        self.ObjectList = []
        self.PlayerList = []
        
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
                Warn(f"Log: {datetime.datetime.now.strftime("%H:%M:%S")}, could not find '{each}' ")

    def Display(self, PlayerList:list = None):
        if type(PlayerList) != list:
            Error("Error: PlayerList is not a list type")
        for each in self.PlayerList:
            pygame.draw.circle(radius=each.Size, centre = each.Position, color= "#FF0000") 
        Wait(1)
        pygame.display.flip()
            
    
    def Leave(self):
        pygame.quit()
        exit()
        


class Object():
    def __init__(self, CollisionType:str = None, Width:int = 5, Height:int = 5, Texture:str = None):
        pass

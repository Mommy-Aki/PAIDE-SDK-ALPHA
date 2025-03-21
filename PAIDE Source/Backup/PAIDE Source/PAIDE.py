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

PlayersCreated = 1

def Error(text):
    if str(text).strip() != "":
        print(f"{TextColour.RED}{text}{TextColour.RESET}")
    
    try:
        os.remove("SourceScriptCopy.py")
    except:
        pass
    exit()

def Info(text):
    print(f"{TextColour.MAGENTA}{text}{TextColour.RESET}")

def Warn(text):
    print(f"{TextColour.YELLOW}{text}{TextColour.RESET}")

class Images():
    BaseImages = { # Name : FilePath

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

class PlayerManager():
    Players = []
    
        
        
    
    def AddPlayer(self, Name:str = f"Player_{PlayersCreated}", HitboxRadius:int = 5, DisplayImage:str = Images.BaseImages.get("Player", None), Movebinds:dict = {"Up" : pygame.K_w, "Down" : pygame.K_s, "Left" : pygame.K_a, "Right" : pygame.K_d}, MovementSpeed:int = 2):
        try:
            pass
        except:
            Warn(f"Could not create client '{Name}'")
        pass
    def KickPlayer(self, Player):
        try:
            self.Players.remove(str(Player))
        except:
            Warn(f"There are no clients called '{Player}' in the current session")

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
        self.NameLimit = 2

        
        
        self.Events = []
        
        try:
            if Name == None or Name.strip() == "" or len(str(Name)) < self.NameLimit:
                Error(f"Error: Instance must Require a Name with at least {self.NameLimit} characters present")
        except AttributeError:
            Error("Error: Invalid Name entered for Instance")

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

    def Display(self):
        if type(PlayerManager.Players) != list:
            Error("Error: PlayerList is not a list type")
        for each in PlayerManager.Players:
            Info(each)
            pygame.draw.circle(radius=eval(each)['Size'], centre = eval(each)['StartPositon'], color= "#FF0000") 
        pygame.display.flip()
            
    
    def Leave(self):
        pygame.quit()
        Error()
        


class Object():
    def __init__(self, CollisionType:str = None, Width:int = 5, Height:int = 5, Texture:str = None):
        pass

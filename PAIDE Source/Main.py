from PAIDEv2 import *

GameService.SetupGame()

while GameService.Game.get("Running"):
    GameService.RunEvents()
    GameService.Display.DisplayInstance()
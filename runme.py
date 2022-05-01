# RazPlay

# Imports
from guizero import *
import time

# Defintions
def games():
    import games
# Script
print("RazPlay RVM Developer Edition RPDE01")
print("Started with 0 RVMs")
app = App(title="RazPlay RVM [Developer Edition]")
welcome_message = Text(app, text="Welcome to RazPlay RVM Dev Edition RPDE01")
games = PushButton(app, command=games, text="Games")
app.display()

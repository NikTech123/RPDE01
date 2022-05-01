# Start
print("RVM System Ready to Launch Games [Games.PY internal ROM]")
print("Please ignore the warning. If you see the warning the app is working correctly.")
# Imports
from guizero import *
import time
# Script
app = App(title="RazPlay RVM Games Menu [Developer Edition]")
welcome_message = Text(app, text="Games Menu")
app.display()

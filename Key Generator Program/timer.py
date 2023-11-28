import os
import time
from replit import db



class Timer:
  def start(self):
    seconds = 600 #Set this to the amount of time you want to have the key be available.
    counter = 0
    while counter <= seconds:
      os.system("clear")
      counter += 1
      print("Your key is:")
      print(db["key"])
      print("\n\n")
      print(f"You have {seconds - counter} Seconds until key expires.")
      time.sleep(1)
    db["key"] = ""
    print("\n\n")
    print("Key deleted.")

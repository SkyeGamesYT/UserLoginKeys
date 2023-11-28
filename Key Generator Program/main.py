from replit import db
from keygen import Key
from timer import Timer
import time

print("Welcome to your account creation...")
print("\n\n")
username = input("create a username (ALL LOWERCASE): ")
print("\n")
password = input("create a password (ALL LOWERCASE): ")

db["username"] = username.lower()
db["password"] = password.lower()

print("Account creation complete. Generating Auth Key.")
print("\n\n")


print("Generating key... This may take a bit.")
local_key = Key().key.upper()
db["PermaKeys"] = ["test", "test2"]
db["key"] = local_key
print("Your key is:")
print(db["key"])
print("\n")
print("This key will expire in 10 Minutes and 30 seconds.")
time.sleep(30)
Timer().start()




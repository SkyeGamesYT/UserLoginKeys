from replit import db
#Connects database
db.db_url = "WEB URL OF CONNECTOR"

##Login

username = input("What is your username? ")
print("\n\n")
password = input("What is your password? ")
print("\n\n")
if username == db["username"] and password == db["password"]:
 print("Access Granted. Please enter generated Key.")
 print("\n\n")
else:
  print("Invalid Login.")






##Key

key1 = input("What is your generated key? ")

if key1 == db["key"]:
  print("Key Approved!")
elif key1 in db["PermaKeys"]:
  print("Perm key approved.")
elif db["key"] == "":
  print("Key Expired.")
else:
  print("Invalid Key.")

del db["username"] #Remove this line to forever keep usernames + passwords
del db["password"] #Remove this line to forever keep usernames + passwords

print("\n\n")
print("Deleted Login. Login success.") #Remove this line to forever keep usernames + passwords

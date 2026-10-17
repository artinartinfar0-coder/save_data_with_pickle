import pickle
import os
contacts = {}
if os.path.exists("phonebook.txt"):
    f = open("phonebook.txt","rb")
    b = f.read()
    f.close()
    contacts = pickle.loads(b)
    print(f"Loaded {len(contacts)}contacts.")
while True:
    name = input("user name:")
    if name == "":
        break
    phone = input("phone number:")
    contacts[name] = phone
b = pickle.dumps(contacts)
f = open("phonebook.txt","wb")
f.write(b)
f.close()
print("Contacts saved successfully!")
targets = input("Enter your target process: ")
token = input("Enter your bot's token: ")
chat_id = input("Enter your chat_id: ")
with open('data.txt', 'w') as f:
    f.write(f'{targets}|&|{token}|&|{chat_id}')
print("Your data is successfully saved, write: \npython3 procMain.py - to start controlling")

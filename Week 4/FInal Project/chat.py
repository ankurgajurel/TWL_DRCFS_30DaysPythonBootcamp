from post_req import post
from get_req import get

while True:
    print(get())
    msg = input("You > ")
    if msg == ":q":
        break
    else:
        post(msg)
        

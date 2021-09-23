import base64
import time
import urllib.request

print("Idle Breakout Save Code Generator by Gage")
print("Loading...")
time.sleep(3)
print("Loaded!")
time.sleep(3)
print("Hello!")
time.sleep(1)

# TODO prestige modification

print("What level do you want to be at?")
level = input()

print("How much money do you want")
money = input()

print("How much gold do you want")
gold = input()

print("How many Black Boxes?")
bb = input()

print("How many skillpoints")
sp = input()

s = f"{level},{money},{gold},2,0,0,0,0,0,0,0,1,1,0,43595.78,999999,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,{bb},0,0,0,1,{sp},1,0,0,Made By Gage"
b = s.encode("UTF-8")
e = base64.b64encode(b)
print("Testing Servers....")
time.sleep(3)
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
# test
print( "Connected to Internet" if connect() else "You do not have internet!" )

time.sleep(2)
print("Finding Fastest Connection....")
time.sleep(1)
print("Conecting to server....")
time.sleep(3)
print("Loading generator....")
time.sleep(4)
print("Generating Code....")
time.sleep(5)
print("Encoding...")
time.sleep(2)
print("Process Complete!")
time.sleep(1)
print(e)
print("\nCopy whats INSIDE the quotes\n")
print("CTR+C does not work, use right click and copy\n")
print("WARNING! MAKE SURE YOU HAVE YOUR OLD CODE WRITTEN DOWN IF YOU ARE GOING TO WANT TO HAVE YOUR OLD SAVE!")
end = 1
while end == 1:
    print("\nOnce copied you may exit the program.")
    input()

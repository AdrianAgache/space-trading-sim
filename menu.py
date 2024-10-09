from time import sleep
from os import *
ans = True
while ans == True:
    print("<SHIP LOADING>")
    sleep(0.5)
    for i in range(0, 101):
      system("clear")
      print("<SHIP LOADING: ", i, "%>")
      sleep(0.08 / ((i+1*360)/100))
    print("<Welcome Captain>")
    ans=input("What would you like to do?\n")
    if ans=="1": 
      print("") 
    elif ans=="2":
      print("") 
    elif ans=="3":
      print("") 
    elif ans=="4":
      print("") 
    else:
      print("")

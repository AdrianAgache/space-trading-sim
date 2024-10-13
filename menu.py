from time import sleep
import os
ans = True
while ans == True:
    print("<SHIP LOADING>")
    sleep(0.5)
    for i in range(0, 101):
      os.system("clear")
      print("<SHIP LOADING: ", i, "%>")
      sleep(0.08 / ((i+1*360)/100))
    j = open("save.txt", "r")
    capnam = str(j.readline())
    print("<Welcome " + capnam + ">")
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

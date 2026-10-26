import os
import time
import random
def start():
  os.system("clear")
  print("""
************************************
*██████╗ ██╗   ██╗██████╗ ██╗   ██╗*
*██╔══██╗██║   ██║██╔══██╗╚██╗ ██╔╝*
*██████╔╝██║   ██║██████╔╝ ╚████╔╝ *
*██╔══██╗██║   ██║██╔══██╗  ╚██╔╝  *
*██║  ██║╚██████╔╝██████╔╝   ██║   *
*╚═╝  ╚═╝ ╚═════╝ ╚═════╝    ╚═╝   *
************************************
""")
  question = input("(r)uby, or (f)inder, or (c)ng, or (h)elp?: ")
  if question == "r":
    os.system("clear")
    ruby()
    
  if question == "f":
    os.system("clear")
    finder()

  if question == "c":
    os.system("clear")
    cng()
    
  if question == "h":
    os.system("clear")
    help()

def help():
  question = input("(r)uby, or (f)inder, or (c)ng?: ")
  if question == "r":
    os.system("clear")
    num = 5
    while num != 1:
      print("Ruby is a people database creator for investigators. [" + str(num) + "]")
      time.sleep(1)
      os.system("clear")
      num -= 1
    start()
  if question == "f":
    os.system("clear")
    num = 5
    while num != 1:
      print("Finder redirects you to people finder sites with the data you give it. [" + str(num) + "]")
      time.sleep(1)
      os.system("clear")
      num -= 1
    start()
  if question == "c":
    os.system("clear")
    num = 5
    while num != 1:
      print("Case Number Generator helps create case numbers. [" + str(num) + "]")
      time.sleep(1)
      os.system("clear")
      num -= 1
    start()
    
def finder():
  firstname = input("What is this person's first name?: ")
  middlename = input("What is this person's middle name?: ")
  lastname = input("What is this person's last name?: ")
  state = input("What is this person's state?: ")
  city = input("What is this person's city?: ")
  zip = input("What is this person's zip code?: ")
  question = input("(t)hatsthem, (tr)uepeoplesearch, (w)hitepages: ")
  if question == "t":
    url = "https://thatsthem.com/name/" + firstname + "-" + middlename + "-" + lastname + "/" + city + "-" + state
    os.system("xdg-open " + url)
  
  if question == "tr":
    url = "http://www.truepeoplesearch.com/results?name=" + firstname + "+" + lastname + "&citystatezip=" + city + "+" + state + "+" + zip
    os.system("xdg-open " + "'" + url + "'")
    
  if question == "w":
      url = "https://www.whitepages.com/name/" + firstname + "-" + middlename + "-" + lastname + "/" + city + "-" + state + "?fs=1&searchedname=" + firstname + "%20" + middlename + "%20" + lastname + "searchedLocation=" + city + "%20" + state
      os.system("xdg-open " + "'" + url + "'")

def ruby():
  firstname = input("What is this person's first name?: ")
  middlename = input("What is this person's middle name?: ")
  lastname = input("What is this person's last name?: ")
  nickname = input("What is this person's nickname?: ")
  state = input("What is this person's state?: ")
  city = input("What is this person's city?: ")
  zip = input("What is this person's zip code?: ")
  address = input("What is this person's address?: ")
  ec = input("What is this person's eye color?: ")
  hc = input("What is this person's hair color?: ")
  r = input("What is this person's race?: ")
  eb = input("What is this person's ethnic background?: ")
  notes = ("Please type in any notes, or leave this blank.: ")
  saveas = input("What do you want to save the file name as?: ")
  if (os.path.isfile(saveas)):
    print("File exists already, please choose a different name.")
    return ruby()
  else:
     with open(saveas + ".txt", "w") as f:
        f.write("""""" + 
"""POI: """ + firstname + " " + middlename + " " + lastname + """
POI Nickname: """ + nickname + """
POI State: """ + state + """
POI City: """ + city + """
POI Zip Code: """ + zip + """
POI Address: """ + address + """
POI Eye Color: """ + ec + """
POI Hair Color: """ + hc + """
POI Race: """ + r + """
POI Ethnic Background: """ + eb + """
Notes: """ + notes)
     with open(saveas + ".txt", "r") as f:
       os.system("clear")
       print("""Wrote the following text to " + """ + saveas + """.txt:
       """ + f.read())

def cng():
  os.system("clear")
  number = random.randint(1, 9)
  initial = input("Please input the first, middle, and last initial of the POI (e.g. pcp): ")
  os.system("clear")
  state = input("Please input the state of the POI (e.g. KS): ")
  file = os.getcwd() + "/casenumber.txt"
  if os.path.isfile(file):
    with open(file, "r") as f:
      current_number = f.read()
      new_number = int(current_number)
      new_number += 1
      os.system("clear")
      print("Your case number is: " + initial + "-" + state + "-" + str(new_number))
      f.close()
    with open(file, "w") as f:
      f.write("" + str(new_number))
  else:
    with open(file, "w") as f:
      number = f.write("1")
      os.system("clear")
      print("Your case number is: " + initial + "-" + state + "-1")
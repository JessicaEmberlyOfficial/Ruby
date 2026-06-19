import os
import time
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
  question = input("(r)uby, or (f)inder, or (h)elp?: ")
  if question == "r":
    os.system("clear")
    ruby()
    
  if question == "f":
    os.system("clear")
    finder()
    
  if question == "h":
    os.system("clear")
    help()

def help():
  question = input("(r)uby, or (f)inder?: ")
  if question == "r":
    os.system("clear")
    print("Ruby is a people database creator for investigators. [5]")
    time.sleep(1)
    os.system("clear")
    print("Ruby is a people database creator for investigators. [4]")
    time.sleep(1)
    os.system("clear")
    print("Ruby is a people database creator for investigators. [3]")
    time.sleep(1)
    os.system("clear")
    print("Ruby is a people database creator for investigators. [2]")
    time.sleep(1)
    os.system("clear")
    print("Ruby is a people database creator for investigators. [1]")
    time.sleep(1)
    start()
  if question == "f":
    os.system("clear")
    print("Finder redirects you to people finder sites with the data you give it. [5]")
    time.sleep(1)
    os.system("clear")
    print("Finder redirects you to people finder sites with the data you give it. [4]")
    time.sleep(1)
    os.system("clear")
    print("Finder redirects you to people finder sites with the data you give it. [3]")
    time.sleep(1)
    os.system("clear")
    print("Finder redirects you to people finder sites with the data you give it. [2]")
    time.sleep(1)
    os.system("clear")
    print("Finder redirects you to people finder sites with the data you give it. [1]")
    time.sleep(1)
    os.system("clear")
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
  state = input("What is this person's state?: ")
  city = input("What is this person's city?: ")
  zip = input("What is this person's zip code?: ")
  address = input("What is this person's address?: ")
  saveas = input("What do you want to save the file name as?: ")
  if (os.path.isfile(saveas)):
    print("File exists already, please choose a different name.")
    return ruby()
  else:
     with open(saveas + ".txt", "w") as f:
        f.write("""""" + 
"""POI: """ + firstname + " " + middlename + " " + lastname + """
POI State: """ + state + """
POI City: """ + city + """
POI Zip Code: """ + zip + """
POI Address: """ + address)
     with open(saveas + ".txt", "r") as f:
       os.system("clear")
       print("""Wrote the following text to " + """ + saveas + """.txt:
       """ + f.read())
# write code to implement a turnstile




state = "Locked"

def Locked():
    state = input ("Turnstile is currently Locked. Would you like to Push or Coin.  ")
    if state == "Push":
        print ("Turnstile is Locked. Please insert coin.  ")
        state = "Locked"
        Locked()
    elif state == "Coin":
        print ("Coin has been deposited. Turnstile is now Unlocked.  ")
        state = "Unlocked"
        Unlocked()

def Walked():
    print ()

def Unlocked():
    state = input ("Turnstile is currently Unlocked. Would you like to Push or Coin.  ")
    if state == "Push":
        print ("You have walked through the Turnstile. Have a good day.  ")
        state = "Walked"
        Walked()
    elif state == ("Coin"):
        print("You have already inserted a coin dummy. Please walk through.  ")
        state = "Unlocked"
        Unlocked()


Locked()
# while state != "Walked":
#     while state == "Locked":
#         state = input ("Turnstile is currently Locked. Would you like to Push or Coin.  ")
#         if state == "Push":
#             print ("Turnstile is Locked. Please insert coin.  ")
#             state = "Locked"
#         elif state == "Coin":
#             print ("Coin has been deposited. Turnstile is now Unlocked.  ")
#             state = "Unlocked"
#     while state == "Unlocked":
#         state = input ("Turnstile is currently Unlocked. Would you like to Push or Coin.  ")
#         if state == "Push":
#             print ("You have walked through the Turnstile. Have a good day.  ")
#             state = "Walked"
#         elif state == ("Coin"):
#             print("You have already inserted a coin dummy. Please walk through.  ")
#             state = "Unlocked"
            
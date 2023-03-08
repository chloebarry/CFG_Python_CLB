# Recipe Finder Programme
import helper_functions

while (helper_functions.isRunning):
  # Welcome message
  print(
    "Welcome to our recipe finder, so you can chooose a meal to cook within seconds! No more dinner blues! \n"
  )

  helper_functions.user_input()

  

  valid_input = False

  while (valid_input == False):
    escape = input("Do you want to search again? Type 'y' for Yes and 'n' for No" + '\n')
    if escape == "n":
      helper_functions.isRunning = False
      valid_input = True
    elif (escape == "y"):
      valid_input = True
    else:
      print("Invalid input, please try again"  + '\n')
      valid_input = False

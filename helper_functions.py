import requests

isRunning = True


# Recipe search function
def recipe_search(ingredient, meal_type, cuisine_type):

  # Register to get an APP ID and key https://developer.edamam.com/
  # Added app_id and app_key from Edamam API
  app_id = '3a2b8157'
  app_key = '4a9218c1312b78152b102056f6911d93'
  result = requests.get(         
    'https://api.edamam.com/search?q={}&app_id={}&app_key={}&mealType={}&cuisineType={}'.format(ingredient, app_id, app_key, meal_type, cuisine_type))

  data = result.json()
  return data['hits']


# Ask user to enter their ingredient, meal type, cuisine type and exclusions
def user_input():
  # Prompt user for main ingredient
  ingredient = input('What is your main ingredient? \n')
  print('\n')

  # Prompt user for meal type
  meal_type = input(
    'What meal are you cooking, for example: breakfast, lunch, dinner? \n') 

  print('\n')
  # Prompt user for cuisine type
  cuisine_type = input(
    'What cuisine do you want to cook tonight, for example: british, french, asian? \n'
  )
  print('\n')
  
  # Get results from API
  results = recipe_search(ingredient, meal_type, cuisine_type)

  File_results = ""
  for result in results:
    recipe = result['recipe']

    # ingredient = result[''] this seems to be causing an error so I've noted it. Wondering what it was meant to mean though - M
    print(recipe['label'])
    print(recipe['uri'])
    print()
    File_results = File_results + recipe['label'] + recipe['uri'] + '\n\n'

    # File export to txt
  with open('Recipe_result.txt', 'w+') as file:
    file.write(File_results)
    file.close()

## display the menu options of the applicatin to the user
def display_menu():
  print('=' * 50)
  print('NEO - AI Study System'.center(50, ' '))
  print('=' * 50)

  print(' ' * 50)
  print('What would you like to do?')
  print(' ' * 50)

  for num, values in MENU_FEATURES.items():
    for keys, function in values.items():
      print(f'{num}. {keys}')


## lets the user choose from the menu options on the display menu
def menu_selection():
  selection = input('Enter a number to choose an option: ')

  for num, values in MENU_FEATURES.items():
    for keys, function in values.items():
      if selection == num:
        return function()
        
  return 'Feature Not Found'


## lets the user import notes
def import_notes():
  return 'IMPORT NOTES'

## shows the user the available note sets
def available_notes():
  return 'AVAILABLE NOTES'


## lets the user generate study material
def study_materials():
  return 'STUDY MATERIALS'


## lets the user review summaries and flashcards
def summary_flashcards():
  return 'SUMMARY FLASHCARDS'


## let the user practice flash cards
def practice_flashcards():
  return 'PRACTICE FLASHCARDS'


## lets the user track study progress
def study_progress():
  return 'STUDY PROGRESS'


## lets the user exit the program
def exit_program():
  return 'EXIT PROGRAM'

## menu features
MENU_FEATURES = {
  '1': {'Import notes': import_notes},
  '2': {'View available note sets': available_notes},
  '3': {'Generate study materials': study_materials},
  '4': {'Review summaries and flashcards': summary_flashcards},
  '5': {'Practice flashcards': practice_flashcards},
  '6': {'View study progress': study_progress},
  '7': {'Exit': exit_program}
  }

## calls the functions of the application
display_menu()
menu_selection()
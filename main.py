## display the menu options of the applicatin to the user
def display_menu():
  ## format for title string
  print('=' * 50)
  print('NEO - AI Study System'.center(50, ' '))
  print('=' * 50)

  print('\nWhat would you like to do?\n')

  ## prints and nums the name of features in MENU_FEATURES
  for num, (label, func) in MENU_FEATURES.items():
    print(f'{num}. {label}')


## lets the user choose from the menu options and checks if it exists
def menu_selection():
  while True:
    ## gets the choice input from the user
    selection = input('\nEnter a number to choose an option: ').strip()

    ## checks if the users input exists
    if selection in MENU_FEATURES:
      MENU_FEATURES[selection][1]()
      break
    else:
      print('\nEnter a number BETWEEN 1 AND 7.')


## lets the user import notes
def import_notes():
  ## formats and displays title of the feature
  print('=' * 50)
  print('IMPORT NOTES'.center(50, ' '))
  print('=' * 50)
  ## tells the user they can exit out of the current feature
  print('type "exit" anytime to cancel')

  while True:
    ## gets the path of a note from the user
    path = input('\nEnter the path of your note: ').strip()
    path_exit = path.lower()
    
    ## checks if the user wants to exit the program
    if path_exit == 'exit':
      print('Import Cancelled\n')
      return
    else:
      ## a try and except block to handle file ERRORS
      try:
        ## opens the note and stores what the note contains
        with open(path, encoding='utf-8') as notes:
          read_notes = notes.read()
          
          ## checks if the file is empty
          if not read_notes.strip():
            print('File is EMPTY.')
            continue

          print(f'imported {len(read_notes)} characters')
          break
      except FileNotFoundError:
        print('Error: The file does not exist.')


## shows the user the available note sets
def available_notes():
  print('AVAILABLE NOTES')


## lets the user generate study material
def study_materials():
  print('STUDY MATERIALS')


## lets the user review summaries and flashcards
def summary_flashcards():
  print('SUMMARY FLASHCARDS')


## let the user practice flash cards
def practice_flashcards():
  print('PRACTICE FLASHCARDS')


## lets the user track study progress
def study_progress():
  print('STUDY PROGRESS')


## lets the user exit the program
def exit_program():
  print('EXIT PROGRAM')

## menu features
MENU_FEATURES = {
  '1': ('Import notes', import_notes),
  '2': ('View available note sets', available_notes),
  '3': ('Generate study materials', study_materials),
  '4': ('Review summaries and flashcards', summary_flashcards),
  '5': ('Practice flashcards', practice_flashcards),
  '6': ('View study progress', study_progress),
  '7': ('Exit', exit_program)
}

## calls the functions of the application
display_menu()
menu_selection()
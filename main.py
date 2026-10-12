## display the menu to the user
## the user can see their menu options/application features

def display_menu():
  print('=' * 50)
  print('NEO - AI Study System'.center(50, ' '))
  print('=' * 50)

  print(' ' * 50)
  print('What would you like to do?')
  print(' ' * 50)

  menu_features = ['Import notes', 'View available note sets', 'Generate study materials', 'Review summaries and flashcards', 'Practice flashcards', 'View study progress', 'Exit']

  for num, menu in enumerate(menu_features, 1):
    print(f'{num}. {menu}')

display_menu()
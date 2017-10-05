"""
Written by : Nathan Payton- McCauslin,
             Daniel Williamson,
             Garrett Gray

Date Written: October 22, 2015

Description: This program is a gameshow where the user is given a famous quote
        and must identify who said it. The questions are given in random order
        and there is a menu system implemented.
"""

import random
# Setup Variables for score tracking
score_count = 0
total_quest = 0
# create data structure for holding Q and A
questions_list = [
    {'question': 'One small step for man, one giant leap for mankind.',
     'answers': [
         'Neil Armstrong',
         'Lance Armstrong',
         'Buzz Aldrin',
         'Richard Nixon'],
     'correct': '1'},

    {'question': 'I was born to make mistakes, not to fake perfection.',
     'answers': [
         'Nicki Minaj',
         'Lil Wayne',
         'Tupac',
         'Drake'],
     'correct': '4'},

    {'question': 'You miss 100% of the shots you dont take.',
     'answers': [
         'Michael Jordan',
         'Wayne Gretzky',
         'Steve Nash',
         'Sidney Crosby'],
     'correct': '2'},

    {'question': 'The most difficult thing is the decision to act, \
the rest is merely tenacity.',
     'answers': [
         'Charlie Chaplin',
         'Charles Lindbergh',
         'Amelia Earhart',
         'Eleanor Roosevelt'],
     'correct': '3'},

    {'question': 'Life is what happens to you while youre \
busy making other plans.',
     'answers': [
         'John Lennon',
         'Brian Johnson',
         'Paul McCartney',
         'Bret Michaels'],
     'correct': '1'},

    {'question': 'The mind is everything. What you think you become.',
     'answers': [
         'Dalai Lama',
         'Buddha',
         'Gandhi',
         'Heinrich Harrer'],
     'correct': '2'},

    {'question': 'An unexamined life is not worth living.',
     'answers': [
         'Confucius',
         'Aristotle',
         'Plato',
         'Socrates'],
     'correct': '4'},

    {'question': 'Every child is an artist. The problem is how to \
remain an artist once he grows up.',
     'answers': [
         'Pablo Picasso',
         'Vincent van Gogh',
         'Salvador Dali',
         'Leonardo da Vinci'],
     'correct': '1'},

    {'question': 'Whether you think you can or you think you \
cant, youre right.',
     'answers': [
         'Thomas Edison',
         'John D. Rockefeller',
         'Henry Ford',
         'Nikola Tesla'],
     'correct': '3'},

    {'question': 'If youre going through hell, keep going.',
     'answers': [
         'Franklin D. Roosevelt',
         'Winston Churchill',
         'Joseph Stalin'],
     'correct': '2'}]

print('Welcome to our CS126 Trivia Game')
print('Match each famous quote with who said it and you could')
print('Win NOTHING!!')
print("")
# Give menu options
main_menu = input('(1) = Play, (2) = View Credits, (3) = Quit: ')
while main_menu == '1':
    random.shuffle(questions_list)  # choose random order of questions
    for question_dict in questions_list:  # Asks one of the above questions
        print(question_dict['question'])
        for i, choice in enumerate(question_dict['answers']):
            print(str(i+1) + '. ' + choice)
        answer = int(input('Choose an answer 1-4: '))
        # Loop checks that the user inputs an option for an answer
        while answer not in range(1, len(question_dict['answers'])+1):
            answer = int(input('Choose an answer 1-4: '))
        total_quest += 1
        if answer == int(question_dict['correct']):
            score_count += 1
            print('Good job.')
        else:
            print('Not correct.')
        print("Your score is:", score_count, "/", total_quest)
        print("")
    main_menu = input('(1) = Play, (2) = View Credits, (3) = Quit: ')

# Credits
while main_menu == '2':
    print('Written by: Nathan Payton- McCauslin,')
    print('            Daniel Williamson,')
    print('            Garrett Gray')
    break
# Exit program
while main_menu == '3':
    print('Thank you for playing.')
    break

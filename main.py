from random import randint
player = input('rock(r), paper(p) or scissors(s) ')

if player == 'r':
  print('0',end=' ')

elif player == 'p':
  print('_',end=' ')

elif player == 's':
  print('8<',end=' ')

print ('vs', end=' '  )

chosen = randint(1,3)

if chosen == 1:
    computer = 'r'
    print('0')
elif chosen == 2:
    computer = 'p'
    print('_')
else:
    computer = 's'
    print('8<')


if player == computer:
  print('DRAW!')
elif player == 'r' and computer == 's':
  print('Player wins!')

elif player == 'r' and computer == 'p':
  print('Computer wins!')

elif player == 'p' and computer == 'r':
  print('Player wins!')

elif player == 'p' and computer == 's':
  print('Computer wins!')

elif player == 's' and computer == 'p':
  print('Player wins!')

elif player == 's' and computer == 'r':
  print('Computer wins!')
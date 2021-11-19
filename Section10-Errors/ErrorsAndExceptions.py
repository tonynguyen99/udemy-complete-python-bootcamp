# Problem 1

try:
  for i in ['a', 'b', 'c']:
    print(i**2)
except TypeError:
  print('You can only square intergers!')
else:
  print('I will never run!')
finally:
  print('All done!')
  
# Problem 2

x = 5
y = 0
try:  
  z = x/y
except ZeroDivisionError:
  print('You cannot divide a number by 0!')
else:
  print('I will never run!')
finally:
  print('All done!')
  
# Problem 3

def ask():
  
  while True:
    
    try:
      number = int(input('Enter a number to square!: '))
    except:
      print('An error occurred! Please try again')
    else:
      print('Thank you, your number square is: ' + str(number**2))
      break
      
ask()
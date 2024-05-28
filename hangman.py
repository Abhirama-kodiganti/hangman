
import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / ` | ' \ / ` | ' ` _ \ / ` | ' \ 
| | | | (| | | | | (| | | | | | | (_| | | | |
|| ||\,|| ||\, || || ||\,|| |_|
                    __/ |                      
                   |_/    '''
                   
                   
print(logo)
words = ["soti","moti", "chati","matti"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
stages.reverse()
y = random.choice(words)
z=[]
for i in y:
    z.append("_")
a = len(y)
draw_count=0
print(z)

while (draw_count<7):
    
    x = input("what's your letter")
    
    if x in z:
            print("already there")
                
    if x in y:
        count=0
        for i in y:
            if x==i:
                z[count]=x
            
            count = count+1
        x = ''.join(z)
        print(x)
    else:
        print(stages[draw_count])
        draw_count+=1
    if '_' not in z: 
       print("SUCCESS")
       break
            
    
if(draw_count==7):
    print("you lost the game")
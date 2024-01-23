                                   
print('''

                                   ___
                               ,-""   `.
                             ,'  _   e )`-._
                            /  ,' `-._<.===-'
                           /  /
                          /  ;
              _          /   ;
 (`._    _.-"" ""--..__,'    |
 <_  `-""                     \
  <`-                          :
   (__   <__.                  ;
     `-.   '-.__.      _.'    /
        \      `-.__,-'    _,'
         `._    ,    /__,-'
            ""._\__,'< <____
                 | |  `----.`.
                 | |        \ `.
                 ; |___      \-``
                 \   --<
                  `.`.<
                    `-'
''')

print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")

if input("You're at a crossroad, where do you want to go? Type \"left\" or \"right\". ").lower() == "left" or "l":
  if input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ").lower() == "wait":
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you want to choose? ").lower()
    if door == "red":
      print(f"Burned by fire.\nGame Over")
    elif door == "yellow":
      print("You Win!")
    elif door == "blue":
      print(f"Eaten by beasts.\nGameOver")
  else:
    print(f"Attacked by trout.\nGame Over.")
else:
  print("Fall into a hole.\n Game Over.")
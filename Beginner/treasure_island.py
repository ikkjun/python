                                   
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

if input("left or right? ").lower() == "left" or "l":
  if input("swim or wait? ").lower() == "wait":
    door = input("Which door?").lower()
    if door == "red":
      print(f"Burned by fire. \n Game Over")
    elif door == "yellow":
      print("You Win!")
    elif door == "blue":
      print(f"Eaten by beasts. \n GameOver")
  else:
    print(f"Attacked by trout.\n Game Over.")
else:
  print("Fall into a hole.\n Game Over.")
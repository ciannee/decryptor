# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# Assignment 3: Redo Problem 2 with multiple github commits (Decryption)

# looping
decryption_str = ""
while decryption_str != "no":
  
# ask for user's input
    import pyfiglet
    name = input("\n\033[91m ♡˗ˏ✎*ೃ˚: Hi! Please enter your nickname:  ")
    hello = "Hello"

    import time
    time.sleep(3)
    name_art = pyfiglet.figlet_format(hello + name,font='graffiti')
    print(name_art)

    input_str = input("\n\033[95mPlease enter a string: ")
    output_str = ""

    # check each character
    for i in range(len(input_str)):
    #   if a, change to *
        if input_str[i] == "a":
            output_str += "*"
    #   if e, change to &
        elif input_str[i] == "e":
            output_str += "&"
    #   if i, change to #
        elif input_str[i] == "i":
            output_str += "#"
    #   if o, change to +
        elif input_str[i] == "o":
            output_str += "+"
    #   if u, change to !  
        elif input_str[i] == "u":
            output_str += "!"    
        else:
            output_str += input_str[i]

    # print output and loading screen 
    import time
    print("\n⋘  Processing.......... ⋙")
    time.sleep (3)
    print("\n██ 20% *___*")
    time.sleep(1)
    print("\n███ 40% *___*")
    time.sleep(1)
    print("\n████ 60% *___*")
    time.sleep(1)
    print("\n█████ 80% *___*")
    time.sleep(1)
    print("\n██████ 100% *___*")
    time.sleep(3)

    print("\nYour encrypted text will be:", output_str)

    import time
    time.sleep (3)

    # decryption

    print("\nDecrypting your string..........")

    import time
    print("\n⋘  Processing.......... ⋙")
    time.sleep (3)
    print("\n██ 20% *___*")
    time.sleep(1)
    print("\n███ 40% *___*")
    time.sleep(1)
    print("\n████ 60% *___*")
    time.sleep(1)
    print("\n█████ 80% *___*")
    time.sleep(1)
    print("\n██████ 100% *___*")
    time.sleep(3)

    # print output
    print("\nYour decrypted string will be: \n", input_str, "\n")
   
    # looping
    decryption_str = input("Do you want to try again? (YES or NO): ")
    if decryption_str == "YES" :
        print("BEGIN AGAIN.")
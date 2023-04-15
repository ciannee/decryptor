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
        
    #   if u, change to !  
        
    # print output and loading screen 
   
    # decryption

    # print output

    # import pyfiglet module
   
    # looping
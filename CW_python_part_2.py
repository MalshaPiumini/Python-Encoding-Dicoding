ALPHABET=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#main function
def run():
    global a
    global key
    global messege_decode
    a= 1#to enter the while loop i use this variable a
    while a>0:
        global command
        print("""If you want to encode enter'e' for the command
If you want to decode enter'd' for the command
If you want to analyse enter'a' for the command
If you want to quite enter'q' for the command""")
        command= input("Input command : ")
        if command=='e':        
            encoding()
            try:
                a=int(input("If you want to quiet the program input positive number,else input negetive number : "))
            except:
                print("You entered a wrong value")
            continue
        elif command=='d':
            try:
                key = int(input("Input a key between 1 and 25 : "))
                if key<0 or key>25:
                    print("Key is not in range")
                    continue
                else:
                    messege_decode=input("Enter the message you want to decode : ")
                    decoding()
            except:
                print("You entered a wrong key")
                
            
            try:
                a=int(input("If you want to quiet the program input positive number,else input negetive number : "))
            except:
                print("You entered a wrong value")
            continue
        elif command=='a':
            analysing()
            try:
                a=int(input("If you want to quiet the program input positive number,else input negetive number : "))
            except:
                print("You entered a wrong value")
            continue
        elif command == 'q':
            return
        else:
            print("Enter a proper command")
            continue

#function for decoding      
def encoding():
    global key
    global encoded_msg
    global temp
    global position
    message_e=input("Enter the message you want to encode : ")
    try:
        key = int(input("Input a key between 1 and 25 : "))
        if key>0 and key<26:
            encoded_msg=""
            for x in message_e:
                temp=0#temporary variable
                for y in ALPHABET:
                    temp+=1
                    if x==y:
                        position=ALPHABET.index(y)
                        if (position+key)<=25:
                            encoded_msg=encoded_msg+ALPHABET[position+key]
                            break #this  makes the code speed 
                        elif (position+key)>25:
                            x=(position+key)-26
                            encoded_msg=encoded_msg+ALPHABET[x]
                            break#this  makes the code speed
                    elif(temp==26):
                        encoded_msg=encoded_msg+x
                        break#this  makes the code speed
                        
            print("Encoded message :",encoded_msg)
        else:
            print("Key is not in range")
            return        
    except:
        print("You entered a wrong key")
        return
def decoding():
    global decoded_msg
    global messege_decode
    global key
    decoded_msg=""       
    process_decoding()
    print("Decoded message :",decoded_msg)

#this function contains the process of decording    
def process_decoding():
    global temp
    global messege_decode
    global position
    global decoded_msg
    global key
    for x in messege_decode:
        temp=0#temporary variable
        for y in ALPHABET:
            temp+=1
            if x==y:
                position=ALPHABET.index(y)
                if (position-key)<=25:
                    decoded_msg=decoded_msg+ALPHABET[position-key]
                    break #this  makes the code speed 
                elif (position-key)<0:
                    x=(position-key)+26
                    decoded_msg=decoded_msg+ALPHABET[x]
                    break
            elif(temp==26):
                decoded_msg=decoded_msg+x
                break
 
def analysing():
    try:
        global key
        global messege_decode
        global messege_to_analyse
        global plain_test
        global a#this a refers to the index of messege_to_analyse
        global b#this b variable refers to index of the charater of plain_test
        global decoded_msg
        messege_to_analyse=input("Enter the messege you want to analyse :")
        #if user didn't enter any value
        if messege_to_analyse=="":
            print("INVALID, you didn't enter a value")
            return
        plain_test=input("Enter part of plain test :")
        #if user didn't enter any value
        if plain_test=="":
            print("INVALID, you didn't enter a value")
            return
        index_of_messege_to_analyse()
        index_of_plain_test()
        key=a-b
        print("Key is :",key)
        messege_decode=messege_to_analyse
        decoding()
    except:
        print("ENTERED VALUES ARE NOT VALIED")
        return
        
# to get the index of variable messege_to_analyse     
def index_of_messege_to_analyse():
    try: 
        global a#this a refers to the index of messege_to_analyse
        global messege_to_analyse
        for x in messege_to_analyse:
            for y in ALPHABET:
                if x==y:
                    a=ALPHABET.index(y)
    ##                print(ALPHABET.index(y))
                    return
                else:
                    continue
    except:
        print("Entered message you want to analyse is not valid")
# to get the index of variable                  
def index_of_plain_test():
    try:
        global plain_test
        global b #this b variable refers to index of the charater of plain_test
        for x in plain_test:
            for z in ALPHABET:
                if x==z:
                    b=ALPHABET.index(z)
    ##                print(ALPHABET.index(z))
                    return
                else:
                    continue
    except:
        print("Entered plain text is not valid")
        
            
    
run()             

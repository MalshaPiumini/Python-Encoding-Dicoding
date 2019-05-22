#PYTHON COURSE WORK 01 - 2018443 - R.M.Malsha Piumini-W1742126
#--------------------------------------------------------------

arr0=[]#to store data between 0-30
arr30=[]#to store data between 30-40
arr40=[]#to store data between 40-70
arr70=[]#to store data between 70-100
no_of_marks=0#no of marksyou input
no_of_pass_students=0#students who took marks over 40
input_data=0#marks you going to enter
max_marks=0 #highest marks
min_marks=100#lowestmarks
total=0#total sum of the marks
max_array=0#maximum length of the array

#if you make a global variable you can use them out of the loop
#The return keyword is to exit a function and return a value
#functions are like methods in java

def compute():
    global no_of_marks
    global no_of_pass_students
    global input_data
    global max_marks
    global min_marks
    global total
    while input_data>=0:
        try:
            input_data=int(input("INPUT marks,If you want end inputting,Enter a NEGETIVE value :\n"))#getting marks from the keyboard
        except:
            print("Invalid INPUT")
            continue#if you mistakenly enter a null value or an alphabatical letters
                
        if input_data<0:
            printing()
            print()
            vertical_histogram()
            return 
        if input_data >=0 and input_data <=100:
            total=total+input_data
            no_of_marks=no_of_marks+1
            if max_marks<input_data:#Finding the max marks
                max_marks=input_data
            if min_marks>input_data:#finding the min marks
                min_marks=input_data
            if input_data>=40:#finding the studets who passed
                no_of_pass_students=no_of_pass_students+1   
            if input_data>=70:#marks between 70-100
                arr70.append(input_data)
            elif input_data>=40:#marks between 40-70
                arr40.append(input_data)
            elif input_data>=30:#marks between 30-40
                arr30.append(input_data) 
            else:#marks between 0-30
                arr0.append(input_data)
        elif input_data>100:
              print("marks are over 100")
              continue

#print horizontal program,average marks,higest marks,lowest     
def printing():
    global no_of_marks  
    global no_of_pass_students
    global input_data
    global max_marks
    global min_marks
    global total
    print("")
    
#printing stars method 1
##    print("Marks between 0-29","  ",end="")
##    print("*"*(len(arr0)))
##    print("\nMarks between 30-39"," ",end="")
##    print("*"*(len(arr30)))
##    print("\nMarks between 40-69"," ",end="")
##    print("*"*(len(arr40)))
##    print("\nMarks between 70-100","",end="")
##    print("*"*(len(arr70)))

#printing stars method 2 by using loops      
    print("Marks between 0-30","  ",end="")
    stars(len(arr0))

    print("\nMarks between 30-40"," ",end="")
    stars(len(arr30))

    print("\nMarks between 40-70"," ",end="")
    stars(len(arr40))
        
    print("\nMarks between 70-100","",end="")
    stars(len(arr70))

#calculating the average marks
    average_mark=total/no_of_marks
#printing other data
    print("")
    print("\nYou entered ",no_of_marks,"values" if no_of_marks>1 else "value")
    print("Highest mark :",max_marks)
    print("Lowest mark :",min_marks)
    print("Number of students who pass the exam :",no_of_pass_students)
    print("Average mark of above :",average_mark)

def stars(x):
    for a in range(0,x):
        print(" * ",end="")

        
#as cw says make use of loops;    
def vertical_histogram():
    global max_array
    max_array=0
    
#to find the maximum length array
    
    if len(arr0)> max_array:
        max_array=len(arr0)
    if len(arr30)>max_array:
        max_array=len(arr30)
    if len(arr40)>max_array:
        max_array=len(arr40)
    if len(arr70)>max_array:
        max_array=len(arr70)
        
#to get the other array lengths also equals to max_length 
    for a in range(0,max_array+1):
        arr0.append(' ')
    for b in range(0,max_array+1):
        arr30.append(' ')
    for c in range(0,max_array+1):
        arr40.append(' ')
    for d in range(0,max_array+1):
        arr70.append(' ')
    for x in range(0,max_array+1):
        if x==0:
            print("0-29","","30-39","","40-69","","70-100")
        if arr0[x]!=' ' :
            arr0[x]="*"
        if arr30[x]!=' ' :
            arr30[x]="*"
        if arr40[x]!=' ' :
            arr40[x]="*"
        if arr70[x]!=' ' :
            arr70[x]="*"
        print(" ",arr0[x],"    ",arr30[x],"   ",arr40[x],"    ",arr70[x])
#calling function       
compute()



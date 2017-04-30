
'''**************************************************************************
            Pick which HW challenge you want
            By: Anthony Tennenbaum
**************************************************************************'''
#function for lottery generator
def lottery_number_generator(event):
    import random
    lottoNumber = []

    for i in range(0,7):
        randNum = random.randint(0,9)
        lottoNumber.append(randNum)

    for i in range(0,7):
        print (lottoNumber[i]),
    time.sleep(5)
    os.system("CLS")
    


#function for number analysis
def number_analysis(event):
    total = 0.0
    average = 0.0
    numberInput = 0.0
    numbers = []

    print("Enter in a series of 20 numbers\n")

    for i in range(20):
        numberInput = int(input("Enter your %s number: " % (i+1)))
        numbers.append(numberInput)
        total += numberInput
    average = total / 20

    print ("\nThe highest number is %.2f: " % max(numbers))
    print ("The lowest number is %.2f: " % min(numbers))
    print ("Your total is %.2f: " % total)
    print ("Your average is %.2f: " %average)
    time.sleep(8)
    os.system("CLS")

#function for rainfall calculator
def rainfall(event):
    totRain = 0.0
    average = 0.0
    totalRain = 0.0
    months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    rainFall = []
    for i in range(0,12):
        monthRain = input("Enter rainfall inches for %s: " % months[i])
        rainFall.append(monthRain)
        totalRain += monthRain

    average = float(totalRain / 12)

    for i in range(0,12):
        print ('')
        print("Rainfall for %s is %i" %(months[i],rainFall[i]))

    print ("\nThe total rainfall was %.2f: " % totalRain)
    print ("The average rainfall is %.2f" % average)
    print ("The highest amount of rainfall was %.2f "% max(rainFall))
    print ("The lowest amount of rainfall was %.2f "% min(rainFall))
    time.sleep(9)
    os.system("CLS")

#function for total sales
def total_sales():
    day = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    dailySales = []
    sales = 0.0
    totalSales = 0.0

    for i in range(0,7):
        sales = input("Enter sales for %s " % day[i])
        dailySales.append(sales)
        totalSales += sales    
    
    for i in range(0,7):
        print ("Sales for %s is %.2f:" % (day[i],dailySales[i]))
    print ("For a total of %.2f: \n" % totalSales)
    time.sleep(5)
    os.system("CLS")
#function for the menu
def menu():
    print ("Welcome, Please select which HW assignment you would like to view:\nPlease select which HW assignment to play by pushing the number.\n")
    print ("1. Play lottery number generator.\n2. Play number analysis.\n3. Play rainfall calculator.\n4. Play total sales calculator.\n5. Exit/Quit.")
    return input()
#function for main that checks choice and calls functions
def main():
    while True:
        choice = menu()
        if choice == 1:
            lottery_number_generator()
        elif choice == 2:
            number_analysis()
        elif choice == 3:
            rainfall()
        elif choice == 4:
            total_sales()
        elif choice == 5:
            sys.exit(0)
        else:
            print ("\n Not a valid choice try AGAIN.")
            time.sleep(2)
            os.system("CLS")
    
#start of program importing different libraries
import time
import os
import sys



from tkinter import *
root = Tk()
root.title("First GUI")
#making the top frame for the title, making title and putting it in titleFrame
titleFrame = Frame(root,height=5)
titleFrame.pack(side=TOP,fill=X)
title = Label(titleFrame, text="Welcome to pick your HW assignment",bg="black",fg="white")
title.grid(row=1,column=1,columnspan=4)
#making the left frame for the menu buttons
menuFrame =Frame(root)
menuFrame.pack(side=LEFT)
#making my buttons for the menu
lottery_button =Button(menuFrame,text="Play lottery number generator")
lottery_button.bind("<Button-1>", lottery_number_generator)
numberAnalysis_button =Button(menuFrame,text="Play number analysis")
numberAnalysis_button.bind("<Button>", number_analysis)
rainFall_button =Button(menuFrame, text="Play rainfall")
rainFall_button.bind("<Button>", rainfall)
totalSales_button =Button(menuFrame,text="Play total sales", command=total_sales)
quitButton = Button(menuFrame,text="Quit",command=menuFrame.quit)
#placing the buttons
lottery_button.grid(row=0,sticky=W)
numberAnalysis_button.grid(row=1,sticky=W)
rainFall_button.grid(row=2,sticky=W)

totalSales_button.grid(row=3,sticky=W)
quitButton.grid(row=4,sticky=W)



root.mainloop()

        

        

    


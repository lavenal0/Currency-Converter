#==================================CURRENCY CONVERSION=============================================
def currency():
    curr=0
    total=0
    print("-------------------- CURRENCY CONVERSION --------------------")
    print("\n\t1.Rupees \n\t2.Dollar \n\t3.Euro \n\t4.Dinar \n\t5.Back \n\t6.Exit")
    print("--------------------------------------------------------------")
    x1 = int(input("Enter your choice: "))    
    print("-----------------------------------------------------------")
#----------------------------------RUPEES---------------------------------------------
    if x1 == 1:
        curr = int(input("Enter Amount: "))
        print("----------------------------------------------------------")
        print("\t1.Rupees \n\t2.Dollar \n\t3.Euro \n\t4.Dinar \n\t5.Back \n\t6.Exit")
        print("----------------------------------------------------------")
        x2 = int(input("Enter second choice: "))
#Rupees        
        if x2 == 1:
            total=curr
            print("----------------------------------------------------")
            print(curr,"Rupees=",total,"Rupees")
            print("----------------------------------------------------")
            print("\t1.Continue\n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        

#Dollar
        if x2 == 2:
            total=curr*0.0128
            print("----------------------------------------------------")
            print(curr,"Rupees=",total,"Dollar")
            print("--------------------------------------------------------")
            print("\t1.Continue\n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))            
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        

#Euro
        if x2 == 3:
            total=curr*0.0123
            print("--------------------------------------------------------")
            print(curr,"Rupees=",total,"Euro")
            print("--------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        

#Dinar
        if x2 == 4:
            total=curr*0.0048
            print("--------------------------------------------------------")
            print(curr,"Rupees=",total,"Dinar")
            print("--------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        else:
            print("Invalid input")
            currency()
        
        

#----------------------------------DOLLAR---------------------------------------

    if x1 == 2:
        curr = int(input("Enter Amount: "))
        print("----------------------------------------------------------")
        print("\t1.Rupees \n\t2.Dollar \n\t3.Euro \n\t4.Dinar \n\t5.Back \n\t6.Exit")
        print("----------------------------------------------------------")
        x2 = int(input("Enter second choice: "))
#Rupees        
        if x2 == 1:
            total=curr*78.1561
            print("----------------------------------------------------")
            print(curr,"Dollar=",total,"Rupees")
            print("----------------------------------------------------")
            print("\t1.Continue\n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        

#Dollar
        if x2 == 2:
            total=curr
            print("----------------------------------------------------")
            print(curr,"Dollar=",total,"Dollar")
            print("--------------------------------------------------------")
            print("\t1.Continue\n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))            
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        

#Euro
        if x2 == 3:
            total=curr*0.9628
            print("--------------------------------------------------------")
            print(curr,"Dollar=",total,"Euro")
            print("--------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        

#Dinar
        if x2 == 4:
            total=curr*0.377
            print("--------------------------------------------------------")
            print(curr,"Dollar=",total,"Dinar")
            print("--------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        else:
            print("Invalid input")
            currency()
        

#-------------------------------------EURO----------------------------------------

    if x1 == 3:
        curr = int(input("Enter Amount: "))
        print("----------------------------------------------------------")
        print("\t1.Rupees \n\t2.Dollar \n\t3.Euro \n\t4.Dinar \n\t5.Back \n\t6.Exit")
        print("----------------------------------------------------------")
        x2 = int(input("Enter second choice: "))
#Rupees        
        if x2 == 1:
            total=curr*81.1807
            print("----------------------------------------------------")
            print(curr,"Euro=",total,"Rupees")
            print("----------------------------------------------------")
            print("\t1.Continue\n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        

#Dollar
        if x2 == 2:
            total=curr*1.0387
            print("----------------------------------------------------")
            print(curr,"Euro=",total,"Dollar")
            print("--------------------------------------------------------")
            print("\t1.Continue\n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))            
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        

#Euro
        if x2 == 3:
            total=curr
            print("--------------------------------------------------------")
            print(curr,"Euro=",total,"Euro")
            print("--------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        

#Dinar
        if x2 == 4:
            total=curr*0.3916
            print("--------------------------------------------------------")
            print(curr,"Euro=",total,"DInar")
            print("--------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        else:
            print("Invalid input")
            currency()
        

#----------------------------------DINAR---------------------------------------------

    if x1 == 4:
        curr = int(input("Enter Amount: "))
        print("----------------------------------------------------------")
        print("\t1.Rupees \n\t2.Dollar \n\t3.Euro \n\t4.Dinar \n\t5.Back \n\t6.Exit")
        print("----------------------------------------------------------")
        x2 = int(input("Enter second choice: "))
#Rupees        
        if x2 == 1:
            total=curr*207.309
            print("----------------------------------------------------")
            print(curr,"Dinar=",total,"Rupees")
            print("----------------------------------------------------")
            print("\t1.Continue\n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        

#Dollar
        if x2 == 2:
            total=curr*2.65
            print("----------------------------------------------------")
            print(curr,"Dinar=",total,"Dollar")
            print("--------------------------------------------------------")
            print("\t1.Continue\n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))            
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        

#Euro
        if x2 == 3:
            total=curr*2.55
            print("--------------------------------------------------------")
            print(curr,"Dinar=",total,"Euro")
            print("--------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        

#Dinar
        if x2 == 4:
            total=curr
            print("--------------------------------------------------------")
            print( curr,"Dinar=",total,"Dinar")
            print("--------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------")
            exi=int(input("Enter your choice: "))
            if exi==1:
                currency()
            elif exi==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif x2==5:
            currency()
        elif x2==6:
            exit()
        else:
            print("Invalid input")
            currency()
        
#-------------------------------------------------------------------------------
              
        
    if x1 == 5:
        calculator()
    elif x1 == 6:
        print("Good Bye")
        exit()
    else:
        print("Invalid Input")
        calculator()
    print("--------------------------------------------------------------")

#==========================CURRENCY CONVERSIONCLOSED===================================================

#==============================LENGTH CONVERSION==================================================
def distance():
    length=0
    measure=0
    print("-------------------------LENGTH CONVERSION-----------------------")
    print("\t1- Decimeter")
    print("\t2- Millimeter")
    print("\t3- Centimeter")
    print("\t4- Meter")
    print("\t5- Inches")
    print("\t6- Foot")
    print("\t7- Kilometer")
    print("\t8- Back")
    print("\t9- Exit\n")
    print("----------------------------------------------------------------")
    l = int(input("Enter your choice: "))
    print("----------------------------------------------------------------")

#------------------------------------------------------DECIMETER----------------------------------------------------------------------------------------------
    
    if l == 1:
        length=int(input("Enter length: "))
        print("-----------------------------------------------------------")
        print("\t1- Decimeter")
        print("\t2- Millimeter")
        print("\t3- Centimeter")
        print("\t4- Meter")
        print("\t5- Inches")
        print("\t6- Foot")
        print("\t7- Kilometer")
        print("\t8- Back")
        print("\t9- Exit\n")
        print("----------------------------------------------------------------")
        l2 = int(input("Enter your choice: "))
        print("----------------------------------------------------------------")

#DECIMETER

        if l2==1:
            measure=length
            print(length,"Decimeter= ",measure,"Decimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#MILLIMETER      

        if l2==2:
            measure=length*100
            print(length,"Decimeter= ",measure,"Millimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
            
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#CENTIMETER
            
        if l2==3:
            measure=length*10
            print(length,"Decimeter= ",measure,"Centimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#METER
            
        if l2==4:
            measure=length*0.1
            print(length,"Decimeter= ",measure,"Meter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#INCHES
            
        if l2==5:
            measure=length*3.93
            print(length,"Decimeter= ",measure,"Inches")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#FOOT
            
        if l2==6:
            measure=length*0.328
            print(length,"Decimeter= ",measure,"Foot")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#KILOMETER
            
        if l2==7:
            measure=length*0.0001
            print(length,"Decimeter= ",measure,"Kilometer")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()
        else:
            print("Invalid input")
            distance()
    
#-----------------------------------------------------MILLIMETER------------------------------------------------------------------------------------------------

    if l == 2:
        unit="Millimeter"
        length=int(input("Enter length: "))
        print("-----------------------------------------------------------")
        print("\t1- Decimeter")
        print("\t2- Millimeter")
        print("\t3- Centimeter")
        print("\t4- Meter")
        print("\t5- Inches")
        print("\t6- Foot")
        print("\t7- Kilometer")
        print("\t8- Back")
        print("\t9- Exit\n")
        print("----------------------------------------------------------------")
        l2 = int(input("Enter your choice: "))
        print("----------------------------------------------------------------")

#DECIMETER

        if l2==1:
            measure=length*0.01
            print(length,unit," = ",measure,"Decimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#MILLIMETER      

        if l2==2:
            measure=length
            print(length,unit," = ",measure,"Millimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
            
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#CENTIMETER
            
        if l2==3:
            measure=length*0.01
            print(length,unit," = ",measure,"Centimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#METER
            
        if l2==4:
            measure=length*0.001
            print(length,unit," = ",measure,"Meter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#INCHES
            
        if l2==5:
            measure=length*0.0393
            print(length,unit," = ",measure,"Inches")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#FOOT
            
        if l2==6:
            measure=length*0.00328
            print(length,unit," = ",measure,"Foot")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#KILOMETER
            
        if l2==7:
            measure=length*0.000001
            print(length,unit," = ",measure,"Kilometer")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()
        else:
            print("Invalid input")
            distance()

#--------------------------------------CENTIMETER-------------------------------------------------------------------------------------------------------------

    if l == 3:
        unit="Centimeter"
        length=int(input("Enter length: "))
        print("-----------------------------------------------------------")
        print("\t1- Decimeter")
        print("\t2- Millimeter")
        print("\t3- Centimeter")
        print("\t4- Meter")
        print("\t5- Inches")
        print("\t6- Foot")
        print("\t7- Kilometer")
        print("\t8- Back")
        print("\t9- Exit\n")
        print("----------------------------------------------------------------")
        l2 = int(input("Enter your choice: "))
        print("----------------------------------------------------------------")

#DECIMETER

        if l2==1:
            measure=length*0.1
            print(length,unit," = ",measure,"Decimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#MILLIMETER      

        if l2==2:
            measure=length*10
            print(length,unit," = ",measure,"Millimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
            
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#CENTIMETER
            
        if l2==3:
            measure=length
            print(length,unit," = ",measure,"Centimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#METER
            
        if l2==4:
            measure=length*0.01
            print(length,unit," = ",measure,"Meter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#INCHES
            
        if l2==5:
            measure=length*0.393
            print(length,unit," = ",measure,"Inches")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#FOOT
            
        if l2==6:
            measure=length*0.0328
            print(length,unit," = ",measure,"Foot")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#KILOMETER
            
        if l2==7:
            measure=length*0.00001
            print(length,unit," = ",measure,"Kilometer")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()
        else:
            print("Invalid input")
            distance()

#------------------------------------------METER---------------------------------------------------------------------------------------------------------

    if l == 4:
        unit="Meter"
        length=int(input("Enter length: "))
        print("-----------------------------------------------------------")
        print("\t1- Decimeter")
        print("\t2- Millimeter")
        print("\t3- Centimeter")
        print("\t4- Meter")
        print("\t5- Inches")
        print("\t6- Foot")
        print("\t7- Kilometer")
        print("\t8- Back")
        print("\t9- Exit\n")
        print("----------------------------------------------------------------")
        l2 = int(input("Enter your choice: "))
        print("----------------------------------------------------------------")

#DECIMETER

        if l2==1:
            measure=length*10
            print(length,unit," = ",measure,"Decimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#MILLIMETER      

        if l2==2:
            measure=length*1000
            print(length,unit," = ",measure,"Millimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
            
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#CENTIMETER
            
        if l2==3:
            measure=length*100
            print(length,unit," = ",measure,"Centimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#METER
            
        if l2==4:
            measure=length
            print(length,unit," = ",measure,"Meter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#INCHES
            
        if l2==5:
            measure=length*39.37
            print(length,unit," = ",measure,"Inches")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#FOOT
            
        if l2==6:
            measure=length*3.280
            print(length,unit," = ",measure,"Foot")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#KILOMETER
            
        if l2==7:
            measure=length*0.001
            print(length,unit," = ",measure,"Kilometer")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()
        else:
            print("Invalid input")
            distance()

#------------------------------------------INCHES-------------------------------------------------------------------------------------

    if l == 5:
        unit="Inches"
        length=int(input("Enter length: "))
        print("-----------------------------------------------------------")
        print("\t1- Decimeter")
        print("\t2- Millimeter")
        print("\t3- Centimeter")
        print("\t4- Meter")
        print("\t5- Inches")
        print("\t6- Foot")
        print("\t7- Kilometer")
        print("\t8- Back")
        print("\t9- Exit\n")
        print("----------------------------------------------------------------")
        l2 = int(input("Enter your choice: "))
        print("----------------------------------------------------------------")

#DECIMETER

        if l2==1:
            measure=length*0.254
            print(length,unit," = ",measure,"Decimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#MILLIMETER      

        if l2==2:
            measure=length*25.40
            print(length,unit," = ",measure,"Millimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
            
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#CENTIMETER
            
        if l2==3:
            measure=length*2.540
            print(length,unit," = ",measure,"Centimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#METER
            
        if l2==4:
            measure=length*0.0254
            print(length,unit," = ",measure,"Meter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#INCHES
            
        if l2==5:
            measure=length
            print(length,unit," = ",measure,"Inches")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#FOOT
            
        if l2==6:
            measure=length*0.0833
            print(length,unit," = ",measure,"Foot")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#KILOMETER
            
        if l2==7:
            measure=length*0.0000254
            print(length,unit ," = ",measure,"Kilometer")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()
        else:
            print("Invalid input")
            distance()

#---------------------------------------FOOT------------------------------------------------------------------------------------------------ 

    if l == 6:
        length=int(input("Enter length: "))
        print("-----------------------------------------------------------")
        print("\t1- Decimeter")
        print("\t2- Millimeter")
        print("\t3- Centimeter")
        print("\t4- Meter")
        print("\t5- Inches")
        print("\t6- Foot")
        print("\t7- Kilometer")
        print("\t8- Back")
        print("\t9- Exit\n")
        print("----------------------------------------------------------------")
        l2 = int(input("Enter your choice: "))
        print("----------------------------------------------------------------")

#DECIMETER

        if l2==1:
            unit="Inches"
            measure=length*3.04
            print(length,unit," = ",measure,"Decimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#MILLIMETER      

        if l2==2:
            measure=length*304.79
            print(length,unit," = ",measure,"Millimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
            
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#CENTIMETER
            
        if l2==3:
            measure=length*30.479
            print(length,unit, " = ",measure,"Centimeter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#METER
            
        if l2==4:
            measure=length*0.304
            print(length,unit," = ",measure,"Meter")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#INCHES
            
        if l2==5:
            measure=length*11.99
            print(length,unit," = ",measure,"Inches")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#FOOT
            
        if l2==6:
            measure=length
            print(length,unit," = ",measure,"Foot")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#KILOMETER
            
        if l2==7:
            measure=length*0.000304
            print(length,unit," = ",measure,"Kilometer")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()
        else:
            print("Invalid input")
            distance()


#----------------------------------KILOMETER----------------------------------------------------------------------------------------------------- 

    if l == 7:
        unit="Kilometer"
        length=int(input("Enter length: "))
        print("-----------------------------------------------------------")
        print("\t1- Decimeter")
        print("\t2- Millimeter")
        print("\t3- Centimeter")
        print("\t4- Meter")
        print("\t5- Inches")
        print("\t6- Foot")
        print("\t7- Kilometer")
        print("\t8- Back")
        print("\t9- Exit\n")
        print("-----------------------------------------------------------")
        l2 = int(input("Enter your choice: "))
        print("-----------------------------------------------------------")

#DECIMETER

        if l2==1:
            measure=length*10000
            print(length,unit," = ",measure,"Decimeter")
            print("-------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("---------------------------------------------------")
                print("\nInvalid input")
                print("---------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#MILLIMETER      

        if l2==2:
            measure=length*1000000
            print(length,unit," = ",measure,"Millimeter")
            print("-------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("---------------------------------------------------")
                print("\nInvalid input")
                print("---------------------------------------------------")
                calculator()
            
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#CENTIMETER
            
        if l2==3:
            measure=length*100000
            print(length,unit," = ",measure,"Centimeter")
            print("-------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("---------------------------------------------------")
                print("\nInvalid input")
                print("---------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#METER
            
        if l2==4:
            measure=length*1000
            print(length,unit," = ",measure,"Meter")
            print("-------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#INCHES
            
        if l2==5:
            measure=length*39370.07
            print(length,unit," = ",measure,"Inches")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#FOOT
            
        if l2==6:
            measure=length*3280.839
            print(length,unit," = ",measure,"Foot")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()

#KILOMETER
            
        if l2==7:
            measure=length
            print(length,unit," = ",measure,"Kilometer")
            print("-----------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-----------------------------------------------------------")
            exil=int(input("Enter your Choice: "))
            if exil==1:
                distance()
            elif exil==2:
                exit()
            else:
                print("------------------------------------------------------")
                print("\nInvalid input")
                print("------------------------------------------------------")
                calculator()
        elif l2==8:
            distance()
        elif l2==9:
            exit()
        else:
            print("Invalid input")
            distance()

#---------------------------------------------------------------------------------------------------------------------------------------

    elif l==8:
        converter()
    elif l==9:
        exit()
    else:
        print("----------------------------------------------------------------")
        print("Invalid  Input")
        print("----------------------------------------------------------------")
        distance()

#===========================LENGTH CONVERSION CLOSED=====================================================================

#===============================WEIGHT CONVERSION========================================================================

def weight():
    measur=0
    load=0
    print("-------------------------WEIGHT CONVERSION------------------------")
    print("\t1.Gram \n\t2.Kilogram \n\t3.Quintal \n\t4.Tonne \n\t5.Pound \n\t6.Back \n\t7.Exit")
    print("----------------------------------------------------------------------")
    w=int(input("Enter your choice: "))
    print("---------------------------------------------------------------------")
    
#--------------------------------------GRAM------------------------------------------------------------

    if w == 1:
        load=int(input("Enter weight: "))
        print("-------------------------------------------------------------")
        print("\t1.Gram \n\t2.Kilogram \n\t3.Quintal \n\t4.Tonne \n\t5.Pound \n\t6.Back \n\t7.Exit")
        print("-------------------------------------------------------------")
        w2=int(input("Enter your choice: "))
        print("-------------------------------------------------------------")
#Gram
        if w2==1:
            measure=load
            print(load,"Gram = ",measure,"Gram")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#kilogram
        if w2==2:
            measure=load*0.001
            print(load,"Gram = ",measure,"Kilogram")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#Quintal
        if w2==3:
            measure=load*0.00001
            print(load,"Gram = ",measure,"Quintal")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#Tonne
        if w2==4:
            measure=load*0.000001
            print(load,"Gram = ",measure,"Tonne")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#Pound
        if w2==5:
            measure=load*0.00220
            print(load,"Gram = ",measure,"Pound")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()
        if w2==6:
            weight()
        if w2==7:
            exit()
        else:
            print("Invalid Input")
            weight()

#--------------------------------------KILOGRAM------------------------------------------------------------

    if w == 2:
        load=int(input("Enter weight: "))
        print("-------------------------------------------------------------")
        print("\t1.Gram \n\t2.Kilogram \n\t3.Quintal \n\t4.Tonne \n\t5.Pound \n\t6.Back \n\t7.Exit")
        print("-------------------------------------------------------------")
        w2=int(input("Enter your choice: "))
        print("-------------------------------------------------------------")
#Gram
        if w2==1:
            measure=load*1000
            print(load,"Kilogram = ",measure,"Gram")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#kilogram
        if w2==2:
            measure=load
            print(load,"Kilogram = ",measure,"Kilogram")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#Quintal
        if w2==3:
            measure=load*0.01
            print(load,"Kilogram = ",measure,"Quintal")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#Tonne
        if w2==4:
            measure=load*0.001
            print(load,"Kilogram = ",measure,"Tonne")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#Pound
        if w2==5:
            measure=load*2.2046
            print(load,"Kilogram = ",measure,"Pound")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()
        if w2==6:
            weight()
        if w2==7:
            exit()
        else:
            print("Invalid Input")
            weight()
#--------------------------------------QUINTAL------------------------------------------------------------

    if w == 3:
        load=int(input("Enter weight: "))
        print("-------------------------------------------------------------")
        print("\t1.Gram \n\t2.Kilogram \n\t3.Quintal \n\t4.Tonne \n\t5.Pound \n\t6.Back \n\t7.Exit")
        print("-------------------------------------------------------------")
        w2=int(input("Enter your choice: "))
        print("-------------------------------------------------------------")
#Gram
        if w2==1:
            measure=load*100000
            print(load,"Quintal = ",measure,"Gram")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#kilogram
        if w2==2:
            measure=load*100
            print(load,"Quintal = ",measure,"Kilogram")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#Quintal
        if w2==3:
            measure=load
            print(load,"Quintal = ",measure,"Quintal")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#Tonne
        if w2==4:
            measure=load*0.1
            print(load,"Qiuntal= ",measure,"Tonne")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#Pound
        if w2==5:
            measure=load*220.462
            print(load,"Quintal = ",measure,"Pound")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()
        if w2==6:
            weight()
        if w2==7:
            exit()
        else:
            print("Invalid Input")
            weight()

#--------------------------------------TONNE------------------------------------------------------------

    if w == 4:
        load=int(input("Enter weight: "))
        print("-------------------------------------------------------------")
        print("\t1.Gram \n\t2.Kilogram \n\t3.Quintal \n\t4.Tonne \n\t5.Pound \n\t6.Back \n\t7.Exit")
        print("-------------------------------------------------------------")
        w2=int(input("Enter your choice: "))
        print("-------------------------------------------------------------")
#Gram
        if w2==1:
            measure=load*1000000
            print(load,"Tonne = ",measure,"Gram")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#kilogram
        if w2==2:
            measure=load*1000
            print(load,"Tonne = ",measure,"Kilogram")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#Quintal
        if w2==3:
            measure=load*10
            print(load,"Tonne = ",measure,"Quintal")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#Tonne
        if w2==4:
            measure=load
            print(load,"Tonne = ",measure,"Tonne")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#Pound
        if w2==5:
            measure=load*2204.622
            print(load,"Tonne = ",measure,"Pound")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()
        if w2==6:
            weight()
        if w2==7:
            exit()
        else:
            print("Invalid Input")
            weight()

#--------------------------------------Pound------------------------------------------------------------

    if w == 2:
        load=int(input("Enter weight: "))
        print("-------------------------------------------------------------")
        print("\t1.Gram \n\t2.Kilogram \n\t3.Quintal \n\t4.Tonne \n\t5.Pound \n\t6.Back \n\t7.Exit")
        print("-------------------------------------------------------------")
        w2=int(input("Enter your choice: "))
        print("-------------------------------------------------------------")
#Gram
        if w2==1:
            measure=load*453.592
            print(load,"Pound = ",measure,"Gram")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#kilogram
        if w2==2:
            measure=load*0.453
            print(load,"Pound = ",measure,"Kilogram")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#Quintal
        if w2==3:
            measure=load*0.00453
            print(load,"Pound = ",measure,"Quintal")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#Tonne
        if w2==4:
            measure=load*0.000453
            print(load,"Pound = ",measure,"Tonne")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()

#Pound
        if w2==5:
            measure=load
            print(load,"Pound = ",measure,"Pound")
            print("-------------------------------------------------------------")
            print("\t1.Continue \n\t2.Exit")
            print("-------------------------------------------------------------")
            w3=int(input("Enter your choice: "))
            print("-------------------------------------------------------------")
            if w3==1:
                weight()
            elif w3==2:
                exit()
            else:
                print("Invalid Input")
                converter()
        if w2==6:
            weight()
        if w2==7:
            exit()
        else:
            print("Invalid Input")
            weight()


#-----------------------------------------------------------------------------------------------------------
    if w==6:
        converter()
    if w==7:
        exit()
    else:
        print("Invalid Input")
        converter()

#===============================WEIGHT CONVERSION CLOSED================================================================
def converter():
    print("--------------------------------------------------------------")
    print("\nALL IN ONE CALCULATOR\n")
    print("\t1- Currency Conversion")
    print("\t2- Length Conversion")
    print("\t3- Weight Conversion")
    print("\t4- Exit\n")
    print("--------------------------------------------------------------")
    x = int(input("Enter your choice: "))
    print("--------------------------------------------------------------")
    if x==1:
        currency()
    elif x==2:
        distance()
    elif x==3:
        weight()
    elif x==4:
        exit()
converter()

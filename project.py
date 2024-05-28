#Project
def my_Line():
    print("_______________________________________________________________________________________________________")


SSR = ["Asuka","Azucena","Bryan","Dragunov","Jin","Jun","King","Kuma","Panda","Leo","Nina","Paul","Shaheen","Victor"]

while True:
    my_Line()
    print("\t\tHi What do you want to know?\n1.SS of Character\n2.Character Anti\n3.Exit")
    choice = input("Choose: ")
    my_Line()
    if choice == "1":
        
        while True:
            c = input("Which character do want to know : ")
            Char = c[0].upper() + c[1:].lower() 

            if Char in SSR:
                my_Line()
                print("\n"+Char,"= SSR\n\nif you want to exit press 2\n")
                my_Line()
                
            elif Char == "2":
                break
            else :
                my_Line()
                print("\n"+Char,"= SSL\n\nif you want to exit press [2]\n")
                my_Line()
            

    elif choice == "2":
        while True:
            anti = input("Which character do want to know : ")
            if anti == "1":
                break
            else: 
                try:
                    readfile = open(f"C:\Programing\/tekken_project\AntiGuide\{anti}_anti.txt", "r") #Use f เพื่อนำค่าอื่นมาใส่ใส่ตรงช่องปีกกา
                    print(readfile.read())
                    my_Line()
                    print("\nIf you want to main menu press 1")
                    my_Line()
                    print("")
                except:
                    my_Line()
                    print("Don't have file this name\n")
                    print("If you want to main menu press 1")
                    my_Line()
                
    elif choice == "3":
        break
    
    else: 
        print("\t\t\tChoose something again")

          #Project เช็คว่าอยากรู้ssไหม แค่พิม y จบ =============================================================================



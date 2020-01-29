# class 5
def HDL_anaysis(HDL_level):
    print("Here")
    if HDL_level>=60:
        return "Normal"
    elif 40<=HDL_level<60:
        return "Borderline low"
    else:
        return "Low"
def LDL_anaysis(LDL_level):
    print("Here")
    if LDL_level<130:
        return "Normal"
    elif 130<=LDL_level<159:
        return "Borderline low"
    elif 159<=LDL_level<189:
        return "High"
    else:
        return "Very High"

def new_feature():
    pass #run the blank code

def Cholestrol_analysis():
    print("Cholestrol analysis")
    HDLinput = input("Enter test result:")
    test_info = HDLinput.split('=')
    if test_info[0] == "HDL":
        answer = HDL_anaysis(int(test_info[1]))
        print("The level is {}".format(answer))
    if test_info[0] == "LDL":
        answer = LDL_anaysis(int(test_info[1]))
        print("The level is {}".format(answer))

def interface():
    while True:
#    choice = 0
#    while choice != 9:
        print("Cholestrol calculator")
        print("options:")
        print("1 -do analysis")
        print("9 - quit")
        choice = input('ENter you option:')
        if choice == '9':
            return
        elif choice == "1":
            Cholestrol_analysis()

if __name__=="__main__":
    interface()

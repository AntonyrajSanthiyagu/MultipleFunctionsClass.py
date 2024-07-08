class Multiplefunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        List=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for i in List:
            print(i)

    def oddEven():
            num=int(input("Enter the number"))
            if((num % 2)== 0):
                print(num,"is even number")
            else:
                print(num,"is odd number")

    def MarriageEligibility():
        Gender=input("Enter the Gender")
        Age=int(input("Enter the Age"))
        if ((Gender=="Male") & (Age>=21)):
            print("ELIGIBLE")
        elif ((Gender=="Female") & (Age>=18)):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
            Subject1=int(input("Enter the sub1"))
            Subject2=int(input("Enter the sub2"))
            Subject3=int(input("Enter the sub3"))
            Subject4=int(input("Enter the sub4"))
            Subject5=int(input("Enter the sub5"))
            Total=Subject1+Subject2+Subject3+Subject4+Subject5
            print("Total:",Total)
            percentage=Total/5
            print("percentage:",percentage)

    def triangle():
            Height=int(input("Height1"))
            Breadth=int(input("Breadth1"))
            AreaFormula=(Height*Breadth)/2
            print("AreaFormula:(Height*Breadth)/2")
            print("Area of Triangle:",AreaFormula)
            Height2=int(input("Height1"))
            Height3=int(input("Height2"))
            Breadth2=int(input("Breadth"))
            PerimeterFormula=Height2+Height3+Breadth2
            print("PerimeterFormula:Height1+Height2+Breadth")
            print("Perimeter of Triangle:",PerimeterFormula)


hotels=["A2b","sangeetha","dindugal thalapakkatti","sundhara vilas"]

rating=[4,4.5,3,5]

h_type=("veg","veg","non-veg","non-veg")

h_area=["tnagar","perungudi","mylapore","santorium"]
order=[{"tnagar":"the food available are: idly,dosa,poori,pongal"},{"perungudi":"the food available are: brinji,naan,poori,rasamalai"},{"mylapore":"the food available are:chicken briyani, mutton chukka, chicken 65"}
,{"santorium":"the food available are: mutton chukka,chicken fried rice,butter masala , prawn"}]


print                                      ( "********** Welcome to swiggy *************")

class swiggy:

    def __init__(self):

        self.__name= input("enter your name")

        if isinstance(self.__name,str):

            print("welcome!")

        else:
            print("enter a valid name")

        self.__area= input("enter your area- the available areas are ---> tnagar,perungudi,mylapore,santorium:")

        if self.__area =="tnagar":

            print("the hotel served in this location is: A2b")

    

        if self.__area=="perungudi":


            print("the hotel served in this location is: sangeetha")

        


        if self.__area=="mylapore":

            print("the hotel served in this location is: dindugal thalapakkati")

     

        if self.__area=="santorium":

            print("the hotel served in this location is :sundhara vilas")

    def details(self):

        self.__phonenumber=input("enter your phone number")

        if (len(self.__phonenumber))==10:
            print("number is saved")

        else:
            raise ValueError("enter a valid number")
            return


        self.__areas= ["tnagar" or "perungudi" or "mylapore" or
                       "santorium"]

        self.__order= input("enter your area")

            
        if self.__order=="tnagar":
            print("the food available are: idly-25rs,dosa-30rs,poori-50rs,pongal-40rs")

        if self.__order=="perungudi":
            print("the food available are: brinji-110rs,naan-125rs,poori-50rs,rasamalai-90rs")

        if self.__order=="santorium":
            print("the food available are: mutton chukka-150rs,chicken fried rice-200rs,butter masala-150rs , prawn-100rs")

        if self.__order=="mylapore":
            print("the food available are:chicken briyani-100rs, mutton chukka-200rs, chicken 65-250rs")
            

        elif print("none"):

            return

               

            
          
    
customer=swiggy()
customer.details()



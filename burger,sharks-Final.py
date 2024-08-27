import time         #To be able to use time.sleep()
class Restaurant:
    name= 'Burger Sharks'
    phone = '0115532'
    address = '105st,ELMaadi'
        
    def ContactUs(self): #only print the info of the restaurant
        print("Restaurant : ",self.name)
        print("Phone number : ",self.phone)
        print("Address : ",self.address)
#-----------------------------------------------------------------------------------------------
class Orders(Restaurant):
    def __init__(self,RestaurantName,cart=[],TotalPrice=0):
        self.RestaurantName = RestaurantName
        self.cart=[]
        self.TotalPrice= 0
        self.menu = [["Beef Burger",100],["Chicken Burger",75],["Fries",30],["Salad",30],["Cola",20]]

    def ShowMenu(self): #only display the menu to the user 
        for i in range(0,len(self.menu)):
            time.sleep(0.3)
            print(f"{i+1}.{self.menu[i][0]} {self.menu[i][1]}LE")   #formatted string to print (number . 1st part of the list"string" , price)
        print(f"{len(self.menu)+1}.I am full")  #to make sure "I am full" is under the menu no matter how big the menu"

    def AddToCart(self,order): #add items to cart
        self.cart.append(order)
        self.TotalPrice+= order[1]

    def ShowCart(self): #SHOW cart items 
        print("Cart: ")
        for i in range(0,len(self.cart)):
            print(f"{self.cart[i][0]} , {self.cart[i][1]}LE")
        print("Total price = ",self.TotalPrice) 
        print("All prices are VAT included")  
         

#the main program 


restaurant = Restaurant()
order=Orders("Burger sharks")
print (f"Welcome To {Restaurant.name}\nHow Can i help you ")
time.sleep(1)
while True:
    print("1.Order")
    time.sleep(0.5)
    print("2.Show Cart")
    time.sleep(0.5)
    print("3.Contact Us")
    time.sleep(0.5)
    print("4.Exit")
    choice1=int(input("Enter your choice please : "))
    
    if choice1!= 1 and  choice1 !=2 and choice1 !=3 and choice1 !=4 :
        print("invalid number please try again")
        continue
    while choice1 == 1: #loop to make sure user stay in ordering menu until he is done
        order.ShowMenu()
        choice2= int(input("Enter your order please : "))
        if choice2 not in  range(1,len(order.menu)+2):
            print("Invalid number please try again")
        elif choice2 == len(order.menu)+1 :
            break
        else:
            order.AddToCart(order.menu[choice2-1])
    
    if choice1 == 2:
        order.ShowCart()
    
    elif choice1== 3:            
        restaurant.ContactUs()

    else:
        break    
order.ShowCart()
time.sleep(1)            
print("We wish To visit Us Again ")  # :)  



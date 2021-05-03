# Write a python program (with class concepts) to find the area of a triangle using below formula
# area = (s(s-a)*(s-b)*(s-c))**0.5
# Function to take the lenght of traingle from user should be defined in the parent class and 
# function to calculate the area should be defined in subclass.

class Length:
    def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
a= int(input("Enter the value of a : "))
b= int(input("Enter the value of b : "))
c= int(input("Enter the value of c : "))

class Triangle(Length):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)

    def Area(self):
        s = (a + b + c)/2
        return (s*(s-a)*(s-b)*(s-c))**0.5        


T = Triangle(a,b,c)
print("Area of a Triangle is : {}".format(T.Area()))            
    
# Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n    


lst = (input("Enter the list of words : ").split())
n=int(input("Enter a integer : "))

def filter_long_words(lst,n):
    print([word for word in lst if len(word) > n])

       
filter_long_words(lst,n)


# Write a python program using function concept that maps list of words into a list of
# integers representing the lengths of the corresponding words 


lst1=(input(list("Enter the words : ").split()))
print(lst1)
def w_to_n(lst1):
    print([len(word) for word in lst1])
    
w_to_n(lst1)  



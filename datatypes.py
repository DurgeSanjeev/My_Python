"""Data Types"""
"""1)None = if a variable is not assigned without any value in other languages its called null
   2)Numeric = there are 4 types in numeric a)int
                                            b)float
                                            c)complex = form of 'a+bj' where j=squareroot of -1
                                            d)bool=returns true or false 
   3)sequences                                    
              a)List = []
              b)Tuple = ()
              c)Set = {}
              d)String = ""                  #there is no char datatype in python  it comes under string
              e)Range = range(parameter)     #used to print range
   4)Dictionary/Mapping"""

a=6+7j
print(type(a))
b=4
c=9
d=complex(b,c)
print(d)
e=c>b
print(e) #returns true or false
print(type(e))

j=list(range(10))                #range is keyword to get range
print(j)
n=list(range(2,10,2))            #to get different range as needed we write syntax as range(starting pt.,ending pt.,differnce)
print(n)


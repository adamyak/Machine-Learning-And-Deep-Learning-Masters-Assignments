# Write a python program to impliment your own myreduce() function which works exactly like
# python built-in function reduce().

# functools.reduce(myfunction, iterable, initializer)
    

def myreduce(func,iterable,initializer=None):
    i=iter(iterable)
    if initializer is None:
        num1=next(i)
    else:
        num1= initializer
    for num2 in i:
        num1=func(num1,num2)
    return(num1)
         


# Write a python program to impliment your own myfilter() function which works exactly like
# python built-in function filter().+


# filter(function, iterable)



def myfilter(function,iterable):
    return[value for value in iterable if function(value)]
                
 # Impliment list comprehensions to produce following list    
    


a=[ i*j for i in 'xyz' for j in range(1,5)]
print(a)

# ["x","xx","xxx","xxxx","y","yy","yyy","yyyy","z","zz","zzz","zzzz"]


b=[ i*j for i in range(1,5) for j in 'xyz']
print((b))

#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

c=[ [i+j] for i in range(1,4) for j in range(1,4) ]
d=[ [i+j for i in range(1,5)] for j in range(1,5) ]
print("{} {}".format(c,d))

#[[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]


e=[ (i,j)  for j in range(1,4) for i in range(1,4) ]
print(e)

#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

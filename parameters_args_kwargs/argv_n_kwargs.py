
# # example from https://www.geeksforgeeks.org/args-kwargs-python/


# Python program to illustrate
# *args with first extra argument
def myFun(arg1, *argv):
    print ("First argument :", arg1)
    print(type(argv))  ## tuple
    for arg in argv:
        print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

print('\n\nkwargs \n')
# Python program to illustrate
# *kargs for variable number of keyword arguments


def myFun(**kwargs):
    print(type(kwargs))  ## dictionary
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))


myFun(first ='Geeks', mid ='for', last='Geeks')


print('\n\nMixed plus\n')


# ## note: chease and blue can't be after **kwargs
def myFun(first,*args,cheese,blue, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
    print("cheese: ", cheese)
    print("blue: ", blue)
    print("first: ", first)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('first','geeks','for','geeks',blue='blueVar',first="Geeks",mid="for",last="Geeks",cheese='hey')



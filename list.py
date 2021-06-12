'''Tuple is the datastructure in python.
Tuple is non-mutable, ordered collection of items that allows duplicates
data are kept inside parenthesis 
tuple item can be access like we access in string i.e.  by giving index
it accept multiple data type inside single collection'''

#Example
newtuple = ("apple", "cherry ", "cuba", "mango")
print(len(newtuple))
#merging two tuple
oldtup = ("orange","banana", "dragon fruit")
mergetup = newtuple+oldtup
print(mergetup)

#print two tuple
print(newtuple,oldtup)

#repeating tuple

print(newtuple*3)

#min and max function

numtup = (1,2,3,4,5,6)
print(max(numtup))
print(min(numtup))
print(sorted(numtup))

if "apple" in newtuple:
    print("apple","lies here")

#change tuple value

changedval  =  list(newtuple)
changedval.append("berry")
print(tuple(changedval))




#deleting tuple
del newtuple
print(newtuple)



x= 5
print(x)

# to print type
print (type(x))  

#  mutiple assignment 
x,y,z = 5,'six',7.0



print(x,y,z)

# unpacking collectiond assignment from tuple or list
list =['natty','fekadu','gebre']
me,father,gfather =  list

print(me,father,gfather)

#  global vaiable
def testfunc():
    global globalx 
    globalx =  'global x'
    localx =  'local x'

testfunc()
print(globalx)


"""
 this is multiple line comment 

"""
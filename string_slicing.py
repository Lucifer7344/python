# slicing is the term which is used for the breakdown of string into parts and use it and this is used in very large no in ML.
""" str[starting_idx : ending_idx] """ # ending idx is not included in this.
str="harshit katiyar "
print(str[2:5])
print(str[:5])  # when we miss at the start it automatically start from 0 index.
print(str[8:15]) # all 3 below method to  representation are same because we are printing till end the string.
print(str[8:len(str)]) #we can also use len(str) for the use of element till end.
print(str[8:])  # when we miss the output then the interpreter automatically detect and make it till end.


#negative indexing we can use negative indexing in the python
print(str[-8:-1])
print(str[-8:])
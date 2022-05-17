#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".
var_int = 1357
x = 0
x += var_int % 2
var_int //= 10

x += var_int % 2
var_int //= 10

x += var_int % 2
var_int //= 10

x += var_int % 2
var_int //= 10

print(x)
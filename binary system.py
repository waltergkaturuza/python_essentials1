#a = 23477
#b= 31213
#print(bin(a)[2:])
#print(bin(b)[2:])
#c= a | b
#print(bin(c)[2:])

#d= a & b
#print(bin(d)[2:])

#e= a ^ b
#print("0"+bin(e)[2:])

#f = ~a
#print(bin(f))


#& | ~ ^ << >> means AND, OR, negation, XOR 

# AND (&) =>>> 1 AND 1 = 1 else ==0
# OR (|) =>>> 0 AND 0 == 0 else 1
# XOR (^)=>>> 0 AND 0 and 1 AND 1 ==0 else =1
#NOT (~)=>>> 
#shifts
number = 20
print(bin(number)[2:])
#shifting to the left by 1 means and add 0 to the end
#number <<=1
#print(bin(number)[2:])
#shifting to the right 2 means multiplying and dividing by two (remove last two numbers)
number >>=2
print(bin(number))
number >>=1
print(bin(number))

#Practical Uses of Bitwise
#example one
NEURAL_READ= 0b1000
NEURAL_WRITE=0b0100
NEURAL_EXEC =0b0010
NEURAL_CHANGE=0b0001

def myfunction(permission):
    print(bin(permission))

myfunction(NEURAL_READ | NEURAL_WRITE)

#example 2: swapping values of variable

var_a = 10
var_b = 20

var_a ^= var_b
var_b ^= var_a
var_a ^= var_b

print(var_a)
print(var_b)


#check if a number is odd or even
somenumber = 784476474843
if somenumber & 1 ==0:
    print("even")
else:
    print("odd")
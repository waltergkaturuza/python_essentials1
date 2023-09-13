def print_vector(x,y,z):
    print('<%s, %s,%s>' % (x,y,z))
    
print_vector(0,1,0)

list_vec = [3,5,7]

tuple_vec =(9,2,4)

print_vector(*list_vec)
print("Unpacking tuple", tuple_vec)

gen_expr = (x * x for x in list_vec)
print(*gen_expr) #using print function

gen = (x*x for x in range(3))

print_vector(*gen)

#dictionary unpacking using **

dic_vec = {
    'x':1,
    'y':2,
    'z':5
}

print_vector(**dic_vec)
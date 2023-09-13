class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self) -> str:
        return 'a {self.color}car'.format(self=self)
        
        
my_car = Car('red', 34455)
print(my_car.color, my_car.mileage)


blocks = int(input("Enter number of blocks: "))

height= 0

current_layer = 1
 
for block in range(1, blocks + 1):
    if blocks >= current_layer:
        blocks-=current_layer
        current_layer += 1
        height+=1
    else:
        break
    """
while blocks >= current_layer:
    blocks-= current_layer
    current_layer+=1
    height+=1
"""
print("The height is",height)
print("on the current layer number",current_layer) 


c0 = int(input("Enter a non-negative"))
steps = 0

while c0!=1:
    if c0% 2==0:
        c0=c0//2
    else:
        c0=3 * c0 +1
    steps +=1
    
print(steps)


s = "abcd"

print(s.split('c'))

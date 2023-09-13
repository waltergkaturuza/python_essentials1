# Step 1: Create an empty list named beatles
beatles = []

# Step 2: Add John Lennon, Paul McCartney, and George Harrison to the list
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Step 3: Prompt the user to add Stu Sutcliffe and Pete Best
new_member = 2
while new_member > 2:
    for _ in range(2):
        new_member = input("Enter a new member of the Beatles: ")
        beatles.append(new_member)
    

# Step 4: Remove Stu Sutcliffe and Pete Best from the list
del beatles[3:5]

# Step 5: Add Ringo Starr to the beginning of the list
beatles.insert(0, "Ringo Starr")

# Print the updated list
print(beatles)

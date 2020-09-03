# This is the title of my calculator
print("Ultimate human to dog years age converter")
#I now convert age into an int to be able to multiply it by another int(dog years in a human year)
#I created an input so the user can enter their age and I declare age afterwards
age=int(input("How old are you? "))
print(f"You are {(age* 7)} years old in dog years")
#same as line 5
pet=input("Do you have a pet?")
#neat little trick my neighbor taught me
#pet.lower makes any 
pet = pet.lower()
if pet == "yes":
    dog=int(input("How old is your pet in human years? "))
    print(f"Your pet is {(int(dog)* 7)} years old in dog years.")
    print("You and your pet are pretty old in dog years.")
elif pet=="no":
    print("Well, then get a pet so it can grow old with you.")
#Now I do the same for thing but it only applies to those with dogs


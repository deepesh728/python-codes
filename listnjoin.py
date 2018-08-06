mylist = ["a", "b", "c", "d"]
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
newstring = "_".join(mylist)
newstring1 = ("-").join(letters)
newstring2 = " and only, ".join(numbers)
print("\n"+ newstring)
print("\n"+ newstring1)
print("\n"+ newstring2)

harry={"title": "chamber of secret",
      "name": "harry potter",
      "parts": "prisoner of azkaban"}
       
print(harry)

dracula={"vampire": "edward", 
         "wolf": "jacob",}

print(dracula) 
dracula.update(harry)
print(dracula)
print(harry.update(dracula))
print(harry)
newone=harry.copy()
newone.update(dracula)
print(newone)

farm_animals={"sheep","cow","hen"}
print(farm_animals)
for animal in farm_animals:
    print(animal)

print("="*40)    
    
wild_animals = {"lion","panther","tiger","hare","elephant"}
print(wild_animals)
for animal in wild_animals:
    print(animal)

farm_animals.add("dog")
wild_animals.add("dog")
print(farm_animals)
print(wild_animals)
wild_animals.pop() = "lion"
print(wild_animals)

# empty_set = set()
# empty_set2 = set()
# empty_set.add("drac")
# empty_set2.add("dee")
# print(empty_Set)
# print(empty_set2)
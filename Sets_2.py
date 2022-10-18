# Q.   A pet store keeps track of the purchases of customers over a four-hour period. The store manager classifies purchases as containing a dog product, a cat product, a fish product, or product  for a different kind of pet. She found.

# a.   83 purchased a dog product 
# b.   101 purchased a cat product 
# c.   22 purchased a fish product
# d.   31 purchased a dog and a cat product 
# e.   8 purchased a dog and a fish product 
# f.    10 purchased a cat and a fish product
# g.   6 purchased a dog, a cat and a fish product
# h.   34 purchased a product for a pet other than a dog, cat or a fish.

# i.   How many purchases were for a dog product only?
# ii.   How many purchases were for cat product only? 
# iii.   How many purchases for a dog or a fish product? 
# iv.   How many purchases were there in total?


# Code




dog = set(range(1, 84))
cat = set(range(47, 148))
fish = set(range(72, 78)) | (set(range(138, 154))) | set(range(1, 9))
other = set(range(155, 189))
onlydog = dog - (cat | fish)
onlycat = cat - (dog | fish)
onlyfish = fish - (dog | cat)
total = dog | fish | cat | other
onlycatndog = (cat & dog) - fish
onlycatnfish = (cat & fish) - dog
onlydognfish = (dog & fish) - cat
allthree = cat & fish & dog
print("{:^40}".format("THE GIVEN DATA"))
data = {"dog product": len(dog), "cat product": len(cat), "fish product": len(fish),
        "a cat and a dog product": len(onlycatndog), "a dog and a fish product": len(onlydognfish),
        "a cat and a fish product": len(onlycatnfish), "a cat, a fish and a dog product": len(allthree),
        "a product other than a cat, dog and a fish product": len(other)}
for i, j in data.items():
    print("People who purchased", i, "=", j)
print("{:^40}".format("ANSWERS"))
print("People who purshased only dog product:", len(onlydog))
print("People who purshased only cat product:", len(onlycat))
print("People who purshased a dog or a fish product:", len(onlyfish | onlydog))
print("Total purchases=", len(total))

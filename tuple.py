my_tuple = ()
print(my_tuple)

my_tuple = (1,2,3)
print(my_tuple)

my_tuple = (1, "hello", 3.4)
print(my_tuple)

my_tuple = ("mouse", [8,4,7], (3,1,2))
print(my_tuple)

my_tuple = ('p','u','y','d','q','w','t')
print(my_tuple[0])
print(my_tuple[5])

n_tuple = ("mouse", [8,4,7], [3,1,2])

print(n_tuple[0][3])
print(n_tuple[1][1])

print("sliced : ", my_tuple[1:4])

for letter in (my_tuple):
    print("hello", letter)
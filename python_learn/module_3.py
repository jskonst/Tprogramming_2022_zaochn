def say_hello():
    print("Hello")
    print("more actions in function....")



print("Functions...")
say_hello()
print("-------")
say_hello()
print("end")

def summ(a, b):
    b += 1
    print(a + b)
    print(f"b in function = {b}")

summ(4, 6)
c = 5
b = 9
summ(c, b)
print(f"b after function = {b}")
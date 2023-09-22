def suma(a,b):
  x = a + b
  return x

def resta (a,b):
   x = a - b
   return x

print("Dame el primer número:")
a = int(input()) 
print("Dame el segundoo número")
b = int(input())
print ("La suma da",suma(a,b), "y la resta da", resta(a,b))

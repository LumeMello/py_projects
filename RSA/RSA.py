def cript(b,n,e):
  return (b**e)%n

def decript(a,n,d):
  return (a**d)%n

vector = [18, 22, 99, 28, 14, 23, 25, 10, 18]

for i in range(len(vector)):
  vector[i] = cript(vector[i],851,5)

print(vector)

for i in range(len(vector)):
  vector[i] = decript(vector[i],851,317)

print(vector)

#Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

final = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if  i+j+k != n]


## Giving multiple inputs together
x, y, z, n = (int(input()) for _ in range(4))

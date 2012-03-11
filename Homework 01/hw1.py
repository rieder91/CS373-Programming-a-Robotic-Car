# Histogramm based localization in a 2d world (like colored flatland)
# Thomas Rieder
#


colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

size_h = len(colors[0])
size_v = len(colors)

start_p = 1.0 / (size_h * size_v)

# uniform distribution
p = [[start_p for column in range(size_h)] for row in range(size_v)]

# sense function
def sense(p, Z):
    # initialize array
    q = [[0 for column in range(size_h)] for row in range(size_v)]    
    # calculate probabilities
    for i in range(size_v):
        for j in range(size_h):
            hit = colors[i][j] == Z
            q[i][j] = p[i][j] * (hit * sensor_right + (1 - hit) * (1 - sensor_right))                 
    # normalize
    pSum = sum(sum(i) for i in q)
    for i in range(size_v):
        for j in range(size_h):
            q[i][j] = q[i][j] / pSum
    return q

# move function
def move(p, U):
    # initialize array
    q = [[0 for column in range(size_h)] for row in range(size_v)]
    # execute move
    for i in range(size_v):
        for j in range(size_h):
            s = p_move * p[(i - U[0]) % size_v][(j - U[1]) % size_h]
            s += (1 - p_move) * p[i][j]
            q[i][j] = s
    return q


# move/sense-loop
for i in range(len(measurements)):
    p = move(p, motions[i])
    p = sense(p, measurements[i])

#Your probability array must be printed 
#with the following code.

show(p)





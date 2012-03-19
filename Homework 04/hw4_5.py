# dynamic programming exercise
# Thomas Rieder
#

# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# takes no input and RETURNS two grids. The
# first grid, value, should contain the computed
# value of each cell as shown in the video. The
# second grid, policy, should contain the optimum
# policy for each cell.
#
# Stay tuned for a homework help video! This should
# be available by Thursday and will be visible
# in the course content tab.
#
# Good luck! Keep learning!
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.
#
# NOTE: Please do not modify the values of grid,
# success_prob, collision_cost, or cost_step inside
# your function. Doing so could result in your
# submission being inappropriately marked as incorrect.

# -------------
# GLOBAL VARIABLES
#
# You may modify these variables for testing
# purposes, but you should only modify them here.
# Do NOT modify them inside your stochastic_value
# function.

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
       
goal = [0, len(grid[0])-1] # Goal is in top right corner


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

success_prob = 0.5                      
failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
collision_cost = 100                    
cost_step = 1        
                     

############## INSERT/MODIFY YOUR CODE BELOW ##################
#
# You may modify the code below if you want, but remember that
# your function must...
#
# 1) ...be called stochastic_value().
# 2) ...NOT take any arguments.
# 3) ...return two grids: FIRST value and THEN policy.

def stochastic_value():
    value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    
    progress = True
    while progress:
        progress = False
        
        # columns
        for x in range(len(grid)):
            # rows
            for y in range(len(grid[0])):
                # check if goal reached
                if goal[0] == x and goal[1] == y:
                    # check if obstacle
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y] = '*'
                        progress = True
                # no obstacle
                elif grid[x][y] == 0:
                    # iterate through all movements
                    for i in range(len(delta)):
                        xNew_1 = x + delta[i][0]
                        yNew_1 = y + delta[i][1]

                        xNew_2 = x + delta[i - 1][0]
                        yNew_2 = y + delta[i - 1][1]
                        
                        xNew_3 = x + delta[(i + 1) % len(delta)][0]
                        yNew_3 = y + delta[(i + 1) % len(delta)][1]

                        valueNew = 0
                        
                        # check if valid for 1st
                        valid = xNew_1 >= 0 and xNew_1 < len(grid) and yNew_1 >= 0 and yNew_1 < len(grid[0])
                        if not valid:
                            valueNew = collision_cost * success_prob
                        else:
                            if grid[xNew_1][yNew_1] == 0:
                                valueNew = value[xNew_1][yNew_1] * success_prob
                            else:
                                valueNew = collision_cost * success_prob
                        
                        # check if valid for 2nd
                        valid = xNew_2 >= 0 and xNew_2 < len(grid) and yNew_2 >= 0 and yNew_2 < len(grid[0])
                        if not valid:
                            valueNew += collision_cost * failure_prob
                        else:
                            if grid[xNew_2][yNew_2] == 0:
                                valueNew += value[xNew_2][yNew_2] * failure_prob
                            else:
                                valueNew += collision_cost * failure_prob
                        
                        # check if valid for 3rd
                        valid = xNew_3 >= 0 and xNew_3 < len(grid) and yNew_3 >= 0 and yNew_3 < len(grid[0])
                        if not valid:
                            valueNew += collision_cost * failure_prob
                        else:
                            if grid[xNew_3][yNew_3] == 0:
                                valueNew += value[xNew_3][yNew_3] * failure_prob
                            else:
                                valueNew += collision_cost * failure_prob

                        valueNew += cost_step
                        # check if progress
                        if valueNew < value[x][y]:
                            progress = True
                            value[x][y] = valueNew
                            policy[x][y] = delta_name[i]
    return value, policy
   
r1, r2 = stochastic_value()
print r2
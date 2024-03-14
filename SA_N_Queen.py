import random
import numpy
import math

def newNode():
    res = []
    for i in range(8):
        res.append(random.randint(0,7))
    return res

# evaluate a resault
def evaluate(arr):
    fault = 0
    for i in range(0 , 8):
        for j in range(1 , 8):
            if(i+j<8):
                if(arr[i+j] == arr[i]):
                    fault += 1
                if(arr[i+j] == arr[i]+j):
                    fault +=1
                if(arr[i+j] == arr[i]-j):
                    fault +=1
    return fault
                
                


# define and init start node
current_node = newNode()

# define and init start node value
current_val = evaluate(current_node)
# define  and init Tempeture
tempeture = 1000000

# loop to find resault
while(tempeture>0):
    if(current_val == 0):
        break
    # define and init next node
    next_node = newNode()
    # define and init next node value
    next_val = evaluate(next_node)

    # calc delta E
    # need minima => current - next
    E = current_val - next_val

    # is it a better point ? choose it
    if(E>0):
        current_node = next_node
        current_val = next_val
    # maybe this is a local answer, try to change status
    else:
        # calculate chance of change node
        chance = math.pow(math.e,E/tempeture)
        rnd = random.random()*100
        # can choose this node with this chance?
        if(rnd<chance):
            current_node = next_node
            current_val = next_val

    # change tempeture
    tempeture -= random.randint(1,3)
    # tempeture -= 1


# print resault
print(current_node , "  :   ",current_val)
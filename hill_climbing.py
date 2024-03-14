import random as rnd

size =  8
# heuristic function , find number of faults
def heuristic(arr):
	faults = 0
	for index in range(size):
		for i in range(1,index+1):
			if((arr[index]-i == arr[index-i]) or (arr[index]+i == arr[index-i]) or (arr[index] == arr[index-i])):
				faults += 1
	return faults

# fill array randomly
def build(arr):
	nums = []
	temp = 0
	for i in range(size):
		nums.append(i)

	for i in range(size , 0 , -1):
		temp = rnd.randint(0,i-1)
		arr[i-1] = nums[temp]
		nums.remove(nums[temp])


min_res = [0 for i in range(size)] 
temp_res = [0 for i in range(size)];

build(min_res)
min_h = heuristic(min_res)

# do while find resault
while(min_h != 0):
    build(temp_res);
    temp_h = heuristic(temp_res)

    if(min_h > temp_h):

        min_h = temp_h
        for i in range(size):
            min_res[i] = temp_res[i];


# print resault
for i in range(size):
    print(temp_res[i] , end= "")

# map size
n = 8
# array of resaults
arr = [0 for i in range(n)]
# total resaults
res = []

# check is it a valid map
def evaluate(arr , index):
    for i in range(1 , index+1):
        if((arr[index]-i == arr[index-i]) or (arr[index]+i == arr[index-i])):
            return False
    return True

# calculate resault
def calc(arr, index , st):
    # array filled
    if(index == n):
        res.append(arr.copy())
    else:
        # fill next index
        for i in st:
            # makea copy of possible numbers
            st_prim = st.copy()
            st_prim.remove(i)
            arr[index] = i
            # is it ok?
            if(evaluate(arr,index)):
                calc(arr,index+1,st_prim)
# make possible numbers
st = []
for i in range(n):
    st.append(i)
# fill array from index 0
calc(arr,0,st)
# print resaults
print("Number of resaults : ",len(res))
for x in res:
    print(x)
# ## Read input as specified in the question.
# ## Print output as specified in the question.
# #Write your code here
# def sol(arr):
#     arr.sort()
#     sum=0
#     for i in range(len(arr)):
#         sum+=arr[i]
#     x=len(arr)-3
#     for i in range(x,0,-3):
#         sum-=arr[i]
#     return sum
# x=int(input())
# arr=[]
# for i in range(x):
#     y=int(input())
#     arr.append(y)
# print(sol(arr))
## Read input as specified in the question.
## Print output as specified in the question.

def findMaxSquareWithAllZeros(arr):
    row = len(arr)
    col = len(arr[0])

    storage = [[0 for i in range(col+1)] for j in range(row+1)]

    for i in range(row,-1,-1):
        for j in range(col,-1,-1):
            storage[i][j] = min(storage[i+1][j], storage[i][j+1])
            maximum = storage[i][j]

            if max(row-i, col-j)<=maximum:
                continue

            foundOne = True

            for p in range(0, maximum+1):
                for q in range(0, maximum+1):
                    if arr[i+p][j+q]==1:
                        foundOne = True
                        break
                if foundOne:
                    break

            if foundOne==False:
                storage[i][j] += 1

    return storage[i][j]


    
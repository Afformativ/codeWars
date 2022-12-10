def sum_of_differences(arr):
    count=0
    if len(arr)==0:
        return 0
    arr.sort(reverse=True)
    for i in range(len(arr)-1):
        diff=arr[i]-arr[i+1]
        count+=diff
    return count  

def selection_sort(arr:list) -> list :
    for i in range(len(arr)):
    
        min_index = i
        
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
            
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
        

    return arr

test_cases = [
    [6,9,5,1,0,8,20,24,14,3],
    [1,4,6,0,4,9,2,5,9],
    [0,2,2,2,4,5,6,9,1]
]

for case in test_cases:
    print(selection_sort(case))
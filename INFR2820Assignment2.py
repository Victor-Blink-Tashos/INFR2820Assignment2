
# there is a chance playsound doesn't work, so just comment or delete them out so the rest of the code at least works 
from playsound import playsound

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx = right_idx = 0
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
            
            playsound("C:\This PC\Documents\PythonCode\Assignment2\Assignment2\Taco Bell Bong.mp3")  
    
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    
    return merged

# Example usage:
def main():
    arr = []
    n = int(input("Enter the number of elements in the array: "))
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        arr.append(element)
    
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
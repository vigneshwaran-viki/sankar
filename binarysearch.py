num = [13,17,29,31,47,57,69,73,93,101,127]
left = 0
right = len(num)-1
val = 101
flag =0

while left < right:
    mid  = (left+right)//2
    if(num[mid]==val):
        flag=1
        print("found at %d"%mid)
        break
    elif num[mid]>val:
        right = mid-1
    else:
        left = mid+1
if(flag==0):
    print("Value not Found")
        
            
        
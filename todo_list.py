def addlist(todo):
    task = input("Enter the task:");
    priority = int(input("Enter the priority in range 1-10(1 is Highest):"))
    todo.append((priority,task))

def displaylist(todo):
    p=1
    sorted_list = sorted(todo,key=lambda x : x[0])
    for i in sorted_list:
        m=f"{p} . TASK ---> {i[1]}"
        #print("{q}TASK --->",p,i[1])
        print(m)
        p+=1
        
def main():
    todo = []
    while True:
        choice = input("Enter 1 for add in list\nEnter 2 for view list\nEnter 3 for exit\n")
        if choice == '1':
            addlist(todo)
        elif choice == '2':
            displaylist(todo)
            break;
        elif choice == '3':
            break
        else:
            print("Enter valid value")
            
if __name__ == "__main__":
    main()        
    
    
    
    
    
    
    
    
    
    
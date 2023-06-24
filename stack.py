stc=[]
#push
def push_element():
    if (len(stc)==n):
        print("stack is full")
    else:
        element=input("enter the element")
        stc.append(element)
        print(stc)
def pop_element():
    if (len(stc)==0):
        print("stack is empty")
    else:
        e=stc.pop()
        print(e,"removed")
        print(stc)
n=int(input("enter the size of the stack"))
while True:
    choice=int(input("enter your choice 1. PUSH 2.POP 3.END"))
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter the correct choice")
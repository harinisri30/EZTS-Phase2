queue=[]
def enqueue():
    if (len(queue)==n):
        print("queue is full")
    else:
        element=input("enter the element")
        queue.append(element)
        print(queue)
def dequeue():
    if (len(queue)==0):
        print("queue is empty")
    else:
        e=queue.pop(0)
        print(e,"removed")
        print(queue)
        
n=int(input("enter the size of the queue"))
while True:
    choice=int(input("enter your choice 1. ENQUEUE 2.DEQUEUE 3.END"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        break
    else:
        print("Enter the correct choice")

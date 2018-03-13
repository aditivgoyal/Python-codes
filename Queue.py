class Queue:
    def __init__(self):
        self.items=[]
    def Push(self, T):
        self.items.insert(0,T)
    
    def Pop(self):
        return self.items.pop()
    
    def Size(self):
        return len(self.items)
    
    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False
        
q=Queue()

def Dequeue(r):
    while not r.isEmpty():
        r.Pop()

def Enqueue(r,T):
    r.Push(T)

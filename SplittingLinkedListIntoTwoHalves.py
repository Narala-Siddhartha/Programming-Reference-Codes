class Node:
    def __init__(self,d):
        self.link=None
        self.d=d
class LinkedList:
    def __init__(self):
        self.start=None
        self.end=None
        self.start2=None
    def Create(self,n):
        i=0
        while i<n:
            d=int(input())
            nodeobj= Node(d)
            if self.start==None:
                self.start=nodeobj
                self.end=nodeobj
            else:
                self.end.link=nodeobj
                self.end = nodeobj
            i+=1
    def Show(self,beg):
        t=beg
        while t:
            print(t.d,end=" ")
            t=t.link
    def Split(self):
        if self.start:
            fast=self.start
            slow=self.start
            while fast.link:
                fast=fast.link
                if fast.link:
                    fast=fast.link
                    slow=slow.link
            self.start2=slow.link
            slow.link=None
            print("\nFirst\n")
            self.Show(self.start)
            print("\nSecond\n")
            self.Show(self.start2)
n=int(input("Number:"))
Obj=LinkedList()
Obj.Create(n)
Obj.Show(Obj.start)
Obj.Split()
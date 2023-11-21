class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

class DlinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data,None,None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None,itr)

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)
            if itr.next:
                llstr += ' --> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr.next:
            itr = itr.next
        while itr:
            llstr += str(itr.data)
            if itr.prev:
                llstr += ' --> '
            itr = itr.prev
        print(llstr)



    def insert_values(self,itemslist):
        for i in itemslist:
            self.insert_at_end(i)

if __name__ == '__main__':
    ll = DlinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()



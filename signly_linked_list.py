class Node(object):
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class SinglyLinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = Node(data=head)

    def __str__(self) -> str:
        if self.head is None:
            return "Linked list is empty."
        else:
            return_str = ''
            nxt_itm = self.head
            while nxt_itm:
                return_str += str(nxt_itm.data) + '-->'
                nxt_itm = nxt_itm.next
            return return_str

    def lenght(self):
        if self.head == None:
            return 0
        else:
            count = 0
            nxt_item = self.head
            while nxt_item:
                nxt_item = nxt_item.next
                count += 1
            return count
        
    def appendleft(self, data):
        head = self.head
        new_data = Node(data, head)
        self.head = new_data
        return

    def popleft(self):
        head = self.head
        next = head.next
        self.head = next
        return

    def append(self, data):
        if self.head is None:
            self.head = Node(data=data)
        else:
            nxt_item = self.head
            while nxt_item:
                if not nxt_item.next:
                    nxt_item.next = Node(data=data)
                    break
        return
    
    def pop(self):
        if self.head is None:
            return "Linked list is empty"
        else:
            prev_item = self.head
            nxt_item = prev_item.next
            if nxt_item is None:
                prev_item = None
                return
            while nxt_item:
                if nxt_item.next == None:
                    prev_item.next = None
                    break
                else:
                    nxt_item = prev_item.next
            return


    def create_linked_list(self, ip_list):
        for x in range(ip_list) - 2:
            itm = ip_list[x]
            nxt_itm = ip_list[x + 1]
            node = Node(itm, nxt_itm)
            if self.head == None:
                self.head = node
            else:
                return


ll = SinglyLinkedList('apple')
ll.appendleft('ball')
print(ll)
ll.popleft()
print(ll)
ll.append('cat')
print(ll)
ll.pop()
print(ll)
print(ll.lenght())
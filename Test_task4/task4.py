class Node:
    def __init__(this, item=None):
        this.item = item
        this.prev = None
        this.next = None

class LinkedList:
    def __init__(this):
        this.head = None
        this.tail = None

    def push(this, item):
        new_node = Node(item)
        if not this.head:
            this.head = new_node
            this.tail = new_node
        else:
            new_node.prev = this.tail
            this.tail.next = new_node
            this.tail = new_node

    def pop(this):
        if not this.tail:
            return None
        elif this.head == this.tail:
            item = this.tail.item
            this.head = None
            this.tail = None
            return item
        else:
            item = this.tail.item
            this.tail = this.tail.prev
            this.tail.next = None
            return item

    def shift(this):
        if not this.head:
            return None
        elif this.head == this.tail:
            item = this.head.item
            this.head = None
            this.tail = None
            return item
        else:
            item = this.head.item
            this.head = this.head.next
            this.head.prev = None
            return item

    def unshift(this, item):
        new_node = Node(item)
        if not this.head:
            this.head = new_node
            this.tail = new_node
        else:
            new_node.next = this.head
            this.head.prev = new_node
            this.head = new_node
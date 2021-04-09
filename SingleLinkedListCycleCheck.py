def checker(nodes):
    size = len(nodes)
    for node in nodes:
        secondaryNode = node
        for i in range(size):
            secondaryNode = secondaryNode.nextNode
        if node != secondaryNode:
            return False
    return True

class SingleLinkedListCycleCheck:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

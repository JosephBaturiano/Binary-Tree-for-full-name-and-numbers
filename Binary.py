class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    name = ["J", "O", "S", "E", "P", "H", "Z", "B",
            "A", "T", "U", "R", "I", "A", "N", "O", "O"]
    numbers = [24, 21, 52, 15, 12, 7, 14, 27, 20, 23, 8, 7, 24]

name_tree = build_tree(name)
print("\t\t\t", "-"*30)
print("\t\t\tBINARY TREE FOR LETTERS OF NAME")
print("Letters of my full name:", name)
print("\nMinimum value:", name_tree.find_min())
print("Maximum value:", name_tree.find_max())
print("Is the letter P included in the list?:", name_tree.search("P"))
print("Is the letter Q included in the list?:", name_tree.search("Q"))
name_tree.delete("A")
print("After deleting letter A, The current list of letters was now being shown in order traversal:\n",
      name_tree.in_order_traversal())
name_tree.delete("R")
print("After deleting letter R, The current list of letters was now being shown in order traversal:\n",
      name_tree.in_order_traversal())
name_tree.delete("H")
print("After deleting letter H, The current list of letters was now being shown in order traversal:\n",
      name_tree.in_order_traversal())
print("\nIn order traversal of the list:", name_tree.in_order_traversal())
print("Pre order traversal of the list:", name_tree.pre_order_traversal())
print("Post order traversal of the list:", name_tree.post_order_traversal())

numbers_tree = build_tree(numbers)
print('\n')
print("\t\t\t", "-"*24)
print("\t\t\tBINARY TREE FOR NUMBERS")
print("Some random numbers:\n", numbers)
print("\nMinimum value:", numbers_tree.find_min())
print("Maximum value:", numbers_tree.find_max())
print("Is the number 8 included in the list?:", numbers_tree.search(8))
print("Is the number 99 included in the list?:", numbers_tree.search(99))
numbers_tree.delete(23)
print("After deleting number 23, The current list for numbers was now being shown in order traversal:\n",
      numbers_tree.in_order_traversal())
numbers_tree.delete(7)
print("After deleting number 7, The current list for numbers was now being shown in order traversal:\n",
      numbers_tree.in_order_traversal())
numbers_tree.delete(12)
print("After deleting number 12, The current list for numbers was now being shown in order traversal:\n",
      numbers_tree.in_order_traversal())
print("\nSum of all numbers:", numbers_tree.calculate_sum())
print("In order traversal of the list:", numbers_tree.in_order_traversal())
print("Pre order traversal of the list:",
      numbers_tree.pre_order_traversal())
print("Post order traversal of the list:",
      numbers_tree.post_order_traversal())

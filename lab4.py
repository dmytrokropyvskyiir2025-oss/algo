class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None


class BinaryTreePriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if self.root is None:
            self.root = new_node
        else:
            self.root = self._insert(self.root, new_node)
        print(f"  [+] Додано: '{value}' | пріоритет: {priority}")

    def _insert(self, current, new_node):
        if current is None:
            return new_node
        if new_node.priority > current.priority:
            new_node.right = current
            return new_node
        else:
            current.left = self._insert(current.left, new_node)
            return current

    def delete_max(self):
        if self.root is None:
            print("  [!] Черга порожня")
            return None
        max_node = self.root
        self.root = self._merge(self.root.left, self.root.right)
        print(f"  [-] Видалено: '{max_node.value}' | пріоритет: {max_node.priority}")
        return max_node.value

    def _merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        if left.priority >= right.priority:
            left.right = self._merge(left.right, right)
            return left
        else:
            right.left = self._merge(left, right.left)
            return right

    def peek(self):
        if self.root is None:
            print("  [!] Черга порожня")
            return None
        print(f"  [*] Найвищий пріоритет: '{self.root.value}' | пріоритет: {self.root.priority}")
        return self.root.value

    def is_empty(self):
        return self.root is None

    def display(self):
        if self.root is None:
            print("  [!] Черга порожня")
            return
        self._display(self.root, 0)

    def _display(self, node, level):
        if node is None:
            return
        self._display(node.left, level + 1)
        print(f"{'  ' * level}  -> [{node.priority}] '{node.value}'")
        self._display(node.right, level + 1)


if __name__ == "__main__":
    queue = BinaryTreePriorityQueue()

    print("=" * 45)
    print("   ЧЕРГА З ПРІОРИТЕТАМИ | БІНАРНЕ ДЕРЕВО")
    print("=" * 45)

    print("\n>>> Вставка елементів")
    queue.insert("Завдання A", 3)
    queue.insert("Завдання B", 7)
    queue.insert("Завдання C", 1)
    queue.insert("Завдання D", 5)
    queue.insert("Завдання E", 9)
    queue.insert("Завдання F", 2)

    print("\n>>> Стан черги")
    queue.display()

    print("\n>>> Peek — дивимось без змін")
    queue.peek()

    print("\n>>> Видаляємо 3 елементи")
    queue.delete_max()
    queue.delete_max()
    queue.delete_max()

    print("\n>>> Стан черги після видалення")
    queue.display()

    print("\n>>> Додаємо ще один елемент")
    queue.insert("Завдання G", 6)
    queue.display()

    print("\n>>> Видаляємо все")
    while not queue.is_empty():
        queue.delete_max()

    print("\n>>> Спроба видалити з порожньої черги")
    queue.delete_max()

    print("\n" + "=" * 45)
    print("   КІНЕЦЬ РОБОТИ ПРОГРАМИ")
    print("=" * 45)
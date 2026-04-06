from lab4 import BinaryTreePriorityQueue

queue = BinaryTreePriorityQueue()

print("=" * 45)
print("   ТЕСТУВАННЯ ЧЕРГИ З ПРІОРИТЕТАМИ")
print("=" * 45)

# ── Тест 1: вставка ────────────────────────────────────────
print("\n[ТЕСТ 1] Вставка елементів:")
queue.insert("Завдання A", 3)
queue.insert("Завдання B", 7)
queue.insert("Завдання C", 1)
queue.insert("Завдання D", 5)
queue.insert("Завдання E", 9)
queue.insert("Завдання F", 2)

# ── Тест 2: peek ───────────────────────────────────────────
print("\n[ТЕСТ 2] Peek — перевіряємо найвищий пріоритет:")
result = queue.peek()
assert result == "Завдання E", f"Очікували 'Завдання E', отримали '{result}'"
print(f"  [OK] Найвищий пріоритет правильний: '{result}'")

# ── Тест 3: display ────────────────────────────────────────
print("\n[ТЕСТ 3] Відображення черги:")
queue.display()
print("  [OK] Черга відображена")

# ── Тест 4: delete_max повертає правильний елемент ─────────
print("\n[ТЕСТ 4] Видалення елементів за пріоритетом:")
deleted = queue.delete_max()
assert deleted == "Завдання E", f"Очікували 'Завдання E', отримали '{deleted}'"
print(f"  [OK] Перше видалення правильне: '{deleted}'")

deleted = queue.delete_max()
assert deleted == "Завдання B", f"Очікували 'Завдання B', отримали '{deleted}'"
print(f"  [OK] Друге видалення правильне: '{deleted}'")

deleted = queue.delete_max()
assert deleted == "Завдання D", f"Очікували 'Завдання D', отримали '{deleted}'"
print(f"  [OK] Третє видалення правильне: '{deleted}'")

# ── Тест 5: peek після видалень ────────────────────────────
print("\n[ТЕСТ 5] Peek після видалень:")
result = queue.peek()
assert result == "Завдання A", f"Очікували 'Завдання A', отримали '{result}'"
print(f"  [OK] Новий найвищий пріоритет: '{result}'")

# ── Тест 6: is_empty ───────────────────────────────────────
print("\n[ТЕСТ 6] Перевірка is_empty:")
assert not queue.is_empty(), "Черга має бути непорожньою"
print("  [OK] Черга не порожня — правильно")

# ── Тест 7: видаляємо все ──────────────────────────────────
print("\n[ТЕСТ 7] Видаляємо всі елементи що залишились:")
while not queue.is_empty():
    queue.delete_max()

assert queue.is_empty(), "Черга має бути порожньою"
print("  [OK] Черга порожня після видалення всього")

# ── Тест 8: операції на порожній черзі ────────────────────
print("\n[ТЕСТ 8] Операції на порожній черзі:")
result = queue.delete_max()
assert result is None, f"Очікували None, отримали '{result}'"
print(f"  [OK] delete_max повернув None")

result = queue.peek()
assert result is None, f"Очікували None, отримали '{result}'"
print(f"  [OK] peek повернув None")

# ── Тест 9: однаковий пріоритет ───────────────────────────
print("\n[ТЕСТ 9] Елементи з однаковим пріоритетом:")
queue.insert("Завдання X", 5)
queue.insert("Завдання Y", 5)
queue.insert("Завдання Z", 5)
result = queue.peek()
assert result is not None, "Черга не повинна бути порожньою"
print(f"  [OK] Peek з однаковими пріоритетами: '{result}'")
while not queue.is_empty():
    queue.delete_max()
print("  [OK] Видалили всі елементи з однаковим пріоритетом")

print("\n" + "=" * 45)
print("   ВСІ ТЕСТИ ПРОЙДЕНІ УСПІШНО ✓")
print("=" * 45)
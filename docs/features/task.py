tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Задача '{task}' добавлена.")

def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Задача '{removed}' удалена.")
    else:
        print("Неверный индекс.")
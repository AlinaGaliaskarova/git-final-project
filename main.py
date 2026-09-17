import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task():
    task = input("Введите задачу: ").strip()
    if not task:
        print("Задача не может быть пустой.")
        return
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Задача добавлена: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Список задач пуст.")
        return
    print("\nСписок задач:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("Список задач пуст.")
        return
    list_tasks()
    try:
        num = int(input("Введите номер задачи для удаления: "))
    except ValueError:
        print("Нужно ввести число.")
        return
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Удалена задача: {removed}")
    else:
        print("Задачи с таким номером нет.")

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Показать список")
        print("0. Выход")
        choice = input("Выберите пункт: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            list_tasks()
        elif choice == "0":
            break
        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    main()
    
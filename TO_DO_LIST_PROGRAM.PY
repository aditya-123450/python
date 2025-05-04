import json

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, description):
        self.tasks.append({"description": description, "completed": False})
        self.save_tasks()

    def list_tasks(self):
        for idx, task in enumerate(self.tasks, 1):
            status = "✔" if task["completed"] else "❌"
            print(f"{idx}. [{status}] {task['description']}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                self.tasks = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

def main():
    todo = ToDoList()
    
    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            desc = input("Enter task description: ")
            todo.add_task(desc)
        elif choice == "2":
            todo.list_tasks()
        elif choice == "3":
            idx = int(input("Enter task number to complete: ")) - 1
            todo.complete_task(idx)
        elif choice == "4":
            idx = int(input("Enter task number to delete: ")) - 1
            todo.delete_task(idx)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

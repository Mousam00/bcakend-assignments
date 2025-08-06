import json

class Task:
    def __init__(self, name, description, completed = False):
        self.name = name
        self.description = description
        self.completed=completed

    def __str__(self):
        return f"Task: {self.name},\n Description: {self.description},\n Completed: {self.completed}"
    
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "completed": self.completed
        }
    
    @staticmethod
    def from_dict(data):
        return Task(data['name'],data["description"],data["completed"])

class TodoList:
    def __init__(self, filename='tasks.json'):
        self.tasks = []
        self.filename=filename
        self.load_task()

    def add_task(self, task):
        for existing in self.tasks:
            if existing.name == task.name:
                print("Task with this name already exists.")
                return
        self.tasks.append(task)
        self.save_task()
    
    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

    def mark_completed(self, task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id].completed = True
            self.save_task()
            print("Task marked as completed.")
        else:
            print("Invalid task ID.")

    def mark_uncompleted(self, task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id].completed = False
            self.save_task()
            print("Task marked as uncompleted.")
        else:
            print("Invalid task ID.")

    def remove_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            removed_task = self.tasks.pop(task_id)
            self.save_task()
            print(f"Removed task: {removed_task.name}")
        else:
            print("Invalid task ID.")

        
    def save_task(self):
        with open(self.filename,'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)
        print("Tasks saved successfully.")
    

    def load_task(self):
        try:
            with open(self.filename,'r') as file:
                content=file.read().strip()
                if not content:
                    self.tasks=[]
                else:
                    data=json.loads(content)
                    self.tasks=[Task.from_dict(items) for items in  data]
        except FileNotFoundError:
            self.tasks=[]
        except json.JSONDecodeError:
            print("Error decoding JSON file. Please check the file format.")
            self.tasks=[]

def main():
    todo=TodoList()

    while True:
        print("\n")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Mark Task as Uncompleted")
        print("4. View Tasks")
        print("5. Remove Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            task = Task(name, description)
            todo.add_task(task)
            print("Task added successfully.")

        elif choice == "2":
            todo.display_tasks()
            try:
                index = int(input("\nEnter task ID: ")) - 1
                todo.mark_completed(index)
            except ValueError:
                print("Please enter a valid integer.")


        elif choice == "3":
            todo.display_tasks()
            try:
                index = int(input("\nEnter task ID: ")) - 1
                todo.mark_uncompleted(index)
            except ValueError:
                print("Please enter a valid integer.")


        elif choice == "4":
            todo.display_tasks()

        elif choice =="5":
            todo.display_tasks()
            try:
                index = int(input("\nEnter task ID to remove: ")) - 1
                confirm = input("Are you sure you want to delete this task? (y/n): ")
     
                if confirm.lower() == 'y':
                    todo.remove_task(index)
                else:
                    print("Deletion cancelled.")

            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting due to keyboard interrupt.")
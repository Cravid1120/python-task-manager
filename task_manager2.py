from datetime import datetime

class Task:
    def __init__(self, title: str, due_date: str, priority: str):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def complete(self):
        self.completed = True

    def uncomplete(self):
        self.completed = False


class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):

        print("\n==============================")
        print("       TASK MANAGER")
        print("==============================")

        if len(self.tasks) == 0:
            print("No tasks found.")
            return

        print("\nID  STATUS  TASK")
        print("--  ------  --------------------------------")

        for index, task in enumerate(self.tasks):

            if task.completed:
                continue
            else:
                status = "[ ]"

            if task.priority.lower() == "high":
                priority_icon = "🔥 HIGH"

            elif task.priority.lower() == "medium":
                priority_icon = "⚠ MEDIUM"

            else:
                priority_icon = "✅ LOW"

            due_date = datetime.strptime(
                task.due_date,
                "%Y-%m-%d"
            )

            today = datetime.today()

            if not task.completed and due_date < today:
                due_status = "⚠ OVERDUE ⚠"
            else:
                due_status = ""

            print(
                f"{index:<3} "
                f"{status:<6} "
                f"{task.title} "
                f"(Due: {task.due_date}) "
                f"{priority_icon} "
                f"{due_status}"
            )
                               
    def complete_task(self, index):
        self.tasks[index].complete()

    def delete_task(self, index):
        del self.tasks[index]

    def uncomplete_task(self, index):
        self.tasks[index].uncomplete()

    def edit_task(self, index, title, due_date):
        self.tasks[index].title = title
        self.tasks[index].due_date = due_date

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(
                    task.title + "|" +
                    task.due_date + "|" +
                    task.priority + "|" +
                    str(task.completed) + "\n"
                )

    def show_completed_tasks(self):

        print("\n==============================")
        print("         COMPLETED TAKS       ")
        print("==============================")

        found = False

        for task in self.tasks:

            if task.completed:

                found = True

                print(
                    f"{task.title} "
                    f"(Due: {task.due_date})"
                    f"[{task.priority}]"
                )

        if not found:
            print("No completed tasks found.")


    def show_dashboard(self):
        
        total = len(self.tasks)

        completed = 0 
        overdue = 0
        high = 0 
        medium = 0 
        low = 0 

        today = datetime.today().date()

        for task in self.tasks:

            if task.completed:
                completed += 1
                continue

            if task.priority.lower() == "high":
                high += 1

            elif task.priority.lower() == "medium":
                medium += 1

            else:
                low += 1
            
 

            due_date = datetime.strptime(
                task.due_date,
                "%Y-%m-%d"
            ).date()

            if not task.completed and due_date < today: 
                overdue += 1

        remaining = total - completed 

        print("\n==============================")
        print("            DASHBOARD          ")
        print("==============================")

        print(f"Total Tasks: {total}")
        print(f"Completed:   {completed}")
        print(f"Remaining:   {remaining}")
        print(f"Overdue:     {overdue}")
        
        print(f"🔥 High Priority:   {high}")
        print(f"⚠ Medium Priority: {medium}")
        print(f"✅ Low Priority:    {low}")


    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:

                    line = line.strip()

                    if not line:
                        continue

                    parts = line.split("|")

                    if len(parts) == 4:

                        title = parts[0]
                        due_date = parts[1]
                        priority = parts[2]
                        completed = parts[3]

                    else:

                        title = parts[0]
                        due_date = parts[1]
                        priority = "Medium"
                        completed = parts[2]

                                        
                    task = Task(title, due_date, priority)

                    if completed == "True":
                        task.complete()

                    self.tasks.append(task)

        except FileNotFoundError:
            pass


# Main Program

manager = TaskManager()

manager.load_tasks()

while True:

    manager.show_dashboard()

    print("\n==============================")
    print("       TASK MANAGER")
    print("==============================")

    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Edit Task")
    print("4. Complete Task")
    print("5. Uncomplete Task")
    print("6. Delete Task")
    print("7. Show Completed Tasks")
    print("8. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        title = input("Enter task title: ")
        while True:
            due_date = input("Enter due date (YYYY-MM-DD): ")
            
            priority = input("Enter priority (High/Medium/Low): ")

            if priority.lower() in [
                "high",
                "medium",
                "low"
            ]:
                break

            print("Please enter High, Medium, or Low")

            try:
                datetime.strptime(due_date, "%Y-%m-%d")
                break

            except ValueError:
                print(
                    "Invalid date format. "
                    "Please use YYYY-MM-DD"
                )

        task = Task(title, due_date, priority)

        manager.add_task(task)

        manager.save_tasks()

        print("Task added.")

    elif choice == "2":

        manager.show_tasks()

    elif choice == "3":

        manager.show_tasks()

        try:
            task_number = int(input("Enter task number: "))

            if 0 <= task_number < len(manager.tasks):

                new_title = input("Enter new title: ")
                new_due_date = input("Enter new due date (YYYY-MM-DD): ")

                manager.edit_task(
                    task_number,
                    new_title,
                    new_due_date
                )

                manager.save_tasks()

                print("Task updated.")

            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a number.")

    elif choice == "4":
        manager.show_tasks()

        try:
            task_number = int(input("Enter task number: "))

            if 0 <= task_number < len(manager.tasks):

                manager.complete_task(task_number)
                
                manager.save_tasks()

                print("Task completed.")

            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a number.")

    elif choice == "5":

        manager.show_tasks()

        try:
            task_number = int(input("Enter task number: "))

            if 0 <= task_number < len(manager.tasks):

                manager.uncomplete_task(task_number)

                manager.save_tasks()

                print("Task marked incomplete.")

            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "6":

        manager.show_tasks()

        try:
            task_number = int(input("Enter task number: "))

            if 0 <= task_number < len(manager.tasks):

                manager.delete_task(task_number)

                manager.save_tasks()

                print("Task deleted.")

            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "7":

        manager.show_completed_tasks()
            
    elif choice == "8":

        print("Goodbye!")
        break

    else:
        print("Invalid option.")


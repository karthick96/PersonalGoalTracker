import tkinter as tk
import datetime


class Goal:
    def __init__(self, master):
        self.master = master
        self.description = tk.StringVar()
        self.start_date = tk.StringVar()
        self.end_date = tk.StringVar()
        self.tasks = []
        self.progress = 0
        self.progress_scale = tk.Scale(
            self.master, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, command=self.update_progress)

        # create a frame to hold the widgets
        self.frame = tk.Frame(master, bg='#80c1ff')
        self.frame.pack(fill=tk.BOTH, expand=True)

        # create widgets for the UI
        self.goal_label = tk.Label(self.frame, text="Goal Tracker", font=(
            "Helvetica", 16), fg='white', bg='#80c1ff')
        self.goal_label.pack(pady=20)

        self.description_label = tk.Label(self.frame, text="Goal Description:", font=(
            "Helvetica", 14), fg='white', bg='#80c1ff')
        self.description_entry = tk.Entry(
            self.frame, textvariable=self.description, font=("Helvetica", 14), width=40)
        self.start_date_label = tk.Label(self.frame, text="Start Date:", font=(
            "Helvetica", 14), fg='white', bg='#80c1ff')
        self.start_date_entry = tk.Entry(
            self.frame, textvariable=self.start_date, font=("Helvetica", 14), width=40)
        self.end_date_label = tk.Label(self.frame, text="End Date:", font=(
            "Helvetica", 14), fg='white', bg='#80c1ff')
        self.end_date_entry = tk.Entry(
            self.frame, textvariable=self.end_date, font=("Helvetica", 14), width=40)
        self.create_button = tk.Button(
            self.frame, text="Create Goal", command=self.create_goal, bg='#80c1ff', font=("Helvetica", 14))

        # layout widgets in the UI
        self.description_label.pack()
        self.description_entry.pack()
        self.start_date_label.pack()
        self.start_date_entry.pack()
        self.end_date_label.pack()
        self.end_date_entry.pack()
        self.create_button.pack()

        self.task_frame = tk.Frame(self.frame, bg='#80c1ff')
        self.task_frame.pack(fill=tk.BOTH, expand=True)

        self.task_label = tk.Label(self.task_frame, text="Tasks:", font=(
            "Helvetica", 14), fg='white', bg='#80c1ff')
        self.task_list = tk.Listbox(
            self.task_frame, font=("Helvetica", 14), width=40)
        self.add_task_button = tk.Button(
            self.task_frame, text="Add Task", command=self.add_task, bg='#80c1ff', font=("Helvetica", 14))
        self.task_description_entry = tk.Entry(
            self.task_frame, font=("Helvetica", 14), width=40)

        self.task_label.pack(side=tk.TOP, pady=10)
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.add_task_button.pack(side=tk.RIGHT)
        self.task_description_entry.pack(side=tk.BOTTOM, pady=10)

        self.progress_label = tk.Label(self.frame, text="Progress:", font=(
            "Helvetica", 14), fg='white', bg='#80c1ff')
        self.progress_label.pack(pady=20)
        self.progress_scale.pack()

        self.completion_frame = tk.Frame(self.frame, bg='#80c1ff')
        self.completion_frame.pack(fill=tk.BOTH, expand=True)

        self.completion_label = tk.Label(self.completion_frame, text="Goal Completion:", font=(
            "Helvetica", 14), fg='white', bg='#80c1ff')
        self.completion_label.pack(side=tk.LEFT)
        self.completion_status = tk.Label(self.completion_frame, text="Incomplete", font=(
            "Helvetica", 14), fg='white', bg='#80c1ff')
        self.completion_status.pack(side=tk.RIGHT)

    def create_goal(self):
        # get the goal description and dates from the UI
        description = self.description.get()
        start_date = datetime.datetime.strptime(
            self.start_date.get(), "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(
            self.end_date.get(), "%Y-%m-%d").date()
        # create a new goal with the given information
        self.goal = Goal(description, start_date, end_date)
        # update the UI to show the tasks and progress for the new goal
        self.task_list.delete(0, tk.END)
        for task in self.goal.tasks:
            self.task_list.insert(tk.END, task)
        self.progress_scale.set(self.goal.progress)
        self.completion_status.configure(
            text="Incomplete" if not self.goal.is_complete() else "Complete")

    def add_task(self):
        # get the task description from the UI
        task_description = self.task_description_entry.get()
        # add the task to the goal
        self.goal.add_task(task_description)
        # update the UI to show the new task
        self.task_list.insert(tk.END, task_description)

    def update_progress(self, event):
        # get the new progress value from the UI
        progress = event

        # update the progress of the goal
        self.goal.update_progress(progress)

        # update the completion status label to show the new completion status of the goal
        self.completion_status.configure(
            text="Incomplete" if not self.goal.is_complete() else "Complete")

    def is_complete(self):
        return self.goal.is_complete()

    def create_task_window(self):
        # create the add task window
        self.add_task_window = tk.Toplevel(self.master)
        self.add_task_window.title("Add Task")
        self.add_task_window.geometry("400x200")
        self.add_task_window.configure(bg='#80c1ff')

        # create widgets for the add task window
        self.task_description_label = tk.Label(
            self.add_task_window, text="Task Description:", font=("Helvetica", 14), fg='white', bg='#80c1ff')
        self.task_description_entry = tk.Entry(
            self.add_task_window, font=("Helvetica", 14), bg='#f2f2f2')
        self.add_button = tk.Button(
            self.add_task_window, text="Add", font=("Helvetica", 14), command=self.add_task)
        self.cancel_button = tk.Button(
            self.add_task_window, text="Cancel", font=("Helvetica", 14), command=self.add_task_window.destroy)

        # layout widgets in the add task window
        self.task_description_label.pack(pady=20)
        self.task_description_entry.pack(pady=10)
        self.add_button.pack(side=tk.LEFT, padx=20)
        self.cancel_button.pack(side=tk.RIGHT, padx=20)

    def on_closing(self):
        # close the window
        self.master.destroy()

    def create_goal_window(self):
        # create the create goal window
        self.create_goal_window = tk.Toplevel(self.master)
        self.create_goal_window.title("Create Goal")
        self.create_goal_window.geometry("600x400")
        self.create_goal_window.configure(bg='#80c1ff')

        # create widgets for the create goal window
        self.description_label = tk.Label(
            self.create_goal_window, text="Goal Description:", font=("Helvetica", 14), fg='white', bg='#80c1ff')
        self.description_entry = tk.Entry(
            self.create_goal_window, font=("Helvetica", 14), bg='#f2f2f2')
        self.start_date_label = tk.Label(
            self.create_goal_window, text="Start Date:", font=("Helvetica", 14), fg='white', bg='#80c1ff')
        self.start_date_entry = tk.Entry(
            self.create_goal_window, font=("Helvetica", 14), bg='#f2f2f2')
        self.end_date_label = tk.Label(
            self.create_goal_window, text="End Date:", font=("Helvetica", 14), fg='white', bg='#80c1ff')
        self.end_date_entry = tk.Entry(
            self.create_goal_window, font=("Helvetica", 14), bg='#f2f2f2')
        self.create_button = tk.Button(
            self.create_goal_window, text="Create", font=("Helvetica", 14), command=self.create_goal)
        self.cancel_button = tk.Button(
            self.create_goal_window, text="Cancel", font=("Helvetica", 14), command=self.create_goal_window.destroy)

        # layout widgets in the create goal window
        self.description_label.pack(pady=20)
        self.description_entry.pack(pady=10)
        self.start_date_label.pack(pady=10)
        self.start_date_entry.pack(pady=10)
        self.end_date_label.pack(pady=10)
        self.end_date_entry.pack(pady=10)
        self.create_button.pack(side=tk.LEFT, padx=20)
        self.cancel_button.pack(side=tk.RIGHT, padx=20)

    def create_task_window(self):
        # create the create task window
        self.create_task_window = tk.Toplevel(self.master)
        self.create_task_window.title("Create Task")
        self.create_task_window.geometry("600x400")
        self.create_task_window.configure(bg='#80c1ff')

        # create widgets for the create task window
        self.description_label = tk.Label(
            self.create_task_window, text="Task Description:", font=("Helvetica", 14), fg='white', bg='#80c1ff')
        self.description_entry = tk.Entry(
            self.create_task_window, font=("Helvetica", 14), bg='#f2f2f2')
        self.due_date_label = tk.Label(
            self.create_task_window, text="Due Date:", font=("Helvetica", 14), fg='white', bg='#80c1ff')
        self.due_date_entry = tk.Entry(
            self.create_task_window, font=("Helvetica", 14), bg='#f2f2f2')
        self.create_button = tk.Button(
            self.create_task_window, text="Create", font=("Helvetica", 14), command=self.add_task)
        self.cancel_button = tk.Button(
            self.create_task_window, text="Cancel", font=("Helvetica", 14), command=self.create_task_window.destroy)

        # layout widgets in the create task window
        self.description_label.pack(pady=20)
        self.description_entry.pack(pady=10)
        self.due_date_label.pack(pady=10)
        self.due_date_entry.pack(pady=10)
        self.create_button.pack(side=tk.LEFT, padx=20)
        self.cancel_button.pack(side=tk.RIGHT, padx=20)

    def update_goal_window(self):
        # create the update goal window
        self.update_goal_window = tk.Toplevel(self.master)
        self.update_goal_window.title("Update Goal")
        self.update_goal_window.geometry("600x400")
        self.update_goal_window.configure(bg='#80c1ff')

        # create widgets for the update goal window
        self.description_label = tk.Label(
            self.update_goal_window, text="Goal Description:", font=("Helvetica", 14), fg='white', bg='#80c1ff')
        self.description_entry = tk.Entry(
            self.update_goal_window, font=("Helvetica", 14), bg='#f2f2f2')
        self.start_date_label = tk.Label(
            self.update_goal_window, text="Start Date:", font=("Helvetica", 14), fg='white', bg='#80c1ff')
        self.start_date_entry = tk.Entry(
            self.update_goal_window, font=("Helvetica", 14), bg='#f2f2f2')
        self.end_date_label = tk.Label(
            self.update_goal_window, text="End Date:", font=("Helvetica", 14), fg='white', bg='#80c1ff')
        self.end_date_entry = tk.Entry(
            self.update_goal_window, font=("Helvetica", 14), bg='#f2f2f2')
        self.update_button = tk.Button(
            self.update_goal_window, text="Update", font=("Helvetica", 14), command=self.update_goal)
        self.cancel_button = tk.Button(
            self.update_goal_window, text="Cancel", font=("Helvetica", 14), command=self.update_goal_window.destroy)

        # layout widgets in the update goal window
        self.description_label.pack(pady=20)
        self.description_entry.pack(pady=10)
        self.start_date_label.pack(pady=10)
        self.start_date_entry.pack(pady=10)
        self.end_date_label.pack(pady=10)
        self.end_date_entry.pack(pady=10)
        self.update_button.pack(side=tk.LEFT, padx=20)
        self.cancel_button.pack(side=tk.RIGHT, padx=20)

    def update_task_window(self):
        # create the update task window
        self.update_task_window = tk.Toplevel(self.master)
        self.update_task_window.title("Update Task")
        self.update_task_window.geometry("600x400")
        self.update_task_window.configure(bg='#80c1ff')

        # create widgets for the update task window
        self.description_label = tk.Label(
            self.update_task_window, text="Task Description:", font=("Helvetica", 14), fg='white', bg='#80c1ff')
        self.description_entry = tk.Entry(
            self.update_task_window, font=("Helvetica", 14), bg='#f2f2f2')
        self.due_date_label = tk.Label(
            self.update_task_window, text="Due Date:", font=("Helvetica", 14), fg='white', bg='#80c1ff')
        self.due_date_entry = tk.Entry(
            self.update_task_window, font=("Helvetica", 14), bg='#f2f2f2')
        self.update_button = tk.Button(
            self.update_task_window, text="Update", font=("Helvetica", 14), command=self.update_task)
        self.cancel_button = tk.Button(
            self.update_task_window, text="Cancel", font=("Helvetica", 14), command=self.update_task_window.destroy)

        # layout widgets in the update task window
        self.description_label.pack(pady=20)
        self.description_entry.pack(pady=10)
        self.due_date_label.pack(pady=10)
        self.due_date_entry.pack(pady=10)
        self.update_button.pack(side=tk.LEFT, padx=20)
        self.cancel_button.pack(side=tk.RIGHT, padx=20)

    def create_task(self):
        # get the task description and due date from the UI
        description = self.description_entry.get()
        due_date = datetime.datetime.strptime(
            self.due_date_entry.get(), "%Y-%m-%d").date()

        # create a new task with the given information
        task = Task(description, due_date)
        self.goal.add_task(task)

        # update the UI to show the new task
        self.task_list.insert(tk.END, task)

        # close the create task window
        self.create_task_window.destroy()

    def update_task(self):
        # get the updated task description and due date from the UI
        description = self.description_entry.get()
        due_date = datetime.datetime.strptime(
            self.due_date_entry.get(), "%Y-%m-%d").date()

        # get the selected task from the task list
        selected_task_index = self.task_list.curselection()[0]
        selected_task = self.task_list.get(selected_task_index)

        # update the task with the new information
        selected_task.description = description
        selected_task.due_date = due_date

        # update the UI to show the updated task
        self.task_list.delete(selected_task_index)
        self.task_list.insert(selected_task_index, selected_task)

        # close the update task window
        self.update_task_window.destroy()

    def mark_complete(self):
        # get the selected task from the task list
        selected_task_index = self.task_list.curselection()[0]
        selected_task = self.task_list.get(selected_task_index)

        # mark the task as complete
        selected_task.mark_complete()

        # update the UI to show the updated task
        self.task_list.delete(selected_task_index)
        self.task_list.insert(selected_task_index, selected_task)

        # update the progress of the goal
        self.goal.update_progress()
        self.progress_scale.set(self.goal.progress)


if __name__ == '__main__':
    # create the root window
    root = tk.Tk()
    root.title("Goal Tracker")
    root.geometry("800x600")

    # create the goal tracker app
    app = Goal(root)

    # start the event loop
    root.mainloop()

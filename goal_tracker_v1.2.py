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

        # create a frame to hold the widgets
        self.frame = tk.Frame(master, bg='#80c1ff')
        self.frame.pack(fill=tk.BOTH, expand=True)

        # create widgets for the UI
        self.description_label = tk.Label(
            self.frame, text="Goal Description:", fg='white', bg='#80c1ff')
        self.description_entry = tk.Entry(
            self.frame, textvariable=self.description)
        self.start_date_label = tk.Label(
            self.frame, text="Start Date:", fg='white', bg='#80c1ff')
        self.start_date_entry = tk.Entry(
            self.frame, textvariable=self.start_date)
        self.end_date_label = tk.Label(
            self.frame, text="End Date:", fg='white', bg='#80c1ff')
        self.end_date_entry = tk.Entry(self.frame, textvariable=self.end_date)
        self.create_button = tk.Button(
            self.frame, text="Create Goal", command=self.create_goal, bg='#80c1ff')
        self.task_label = tk.Label(
            self.frame, text="Tasks:", fg='white', bg='#80c1ff')
        self.task_list = tk.Listbox(self.frame)
        self.add_task_button = tk.Button(
            self.frame, text="Add Task", command=self.add_task, bg='#80c1ff')
        self.progress_label = tk.Label(
            self.frame, text="Progress:", fg='white', bg='#80c1ff')
        self.progress_scale = tk.Scale(
            self.frame, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, command=self.update_progress)

        # layout widgets in the UI
        self.description_label.grid(row=0, column=0, sticky=tk.W)
        self.description_entry.grid(row=0, column=1)
        self.start_date_label.grid(row=1, column=0, sticky=tk.W)
        self.start_date_entry.grid(row=1, column=1)
        self.end_date_label.grid(row=2, column=0, sticky=tk.W)
        self.end_date_entry.grid(row=2, column=1)
        self.create_button.grid(row=3, column=1, sticky=tk.E)
        self.task_label.grid(row=4, column=0, sticky=tk.W)
        self.task_list.grid(row=5, column=0, columnspan=2)
        self.add_task_button.grid(row=6, column=1, sticky=tk.E)
        self.progress_label.grid(row=7, column=0, sticky=tk.W)
        self.progress_scale.grid(row=7, column=1)

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

    def add_task(self):
        # get the task description from the UI
        task_description = self.task_description.get()
        # add the task to the goal
        self.goal.add_task(task_description)
        # update the UI to show the new task
        self.task_list.insert(tk.END, task_description)

    def update_progress(self, event):
        # get the new progress value from the UI
        progress = event
        # update the progress of the goal
        self.goal.update_progress(progress)

    def is_complete(self):
        return self.goal.is_complete()


if __name__ == '__main__':
    # create the root window
    root = tk.Tk()
    root.title("Goal Tracker")
    # create an instance of the Goal class
    app = Goal(root)
    # start the Tkinter event loop
    root.mainloop()

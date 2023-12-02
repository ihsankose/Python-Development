from sort_functions import *
import datetime

"""
   This application is a To Do App.
   It uses a Task class to define a Task class with properties like title, description, priority, and due_date
   And uses following features for better task handling.
        Create, update, and delete tasks
        Sort tasks by priority, due date, or creation date
        Option to mark tasks as complete
        Save and load tasks to/from a file
"""


class Task:
    def __init__(self, task_title, task_desc='TaskDescriptionGoesHere', task_prio=0, task_due=None,
                 task_create_date=None, is_task_complete =False):
        self.title = task_title
        self.desc = task_desc
        self.prio = task_prio
        self.due = datetime.date.today() if task_due is None else task_due
        self.created_at = datetime.datetime.now(
        ) if task_create_date is None else task_create_date
        self.isComplete = is_task_complete


class TaskBook:
    def __init__(self):
        self.book = []

    def add(self, task_name):
        self.book.append(task_name)

    def delete(self, task_name):
        self.book.remove(task_name)

    # def update(self, task_name, task_title, task_desc, task_prio, task_due, task_create_date):
    #     # index = next((i for i, obj in enumerate(self.book) if obj.title == task_name), None)
    #     self.book[self.book.index(task_name)].title = task_title
    #     self.book[self.book.index(task_name)].desc = task_desc
    #     self.book[self.book.index(task_name)].prio = task_prio
    #     self.book[self.book.index(task_name)].due = task_due
    #     self.book[self.book.index(task_name)].created_at = task_create_date

    def update(self, task_name, task_title=None, task_desc=None, task_prio=None, task_due=None, task_create_date=None):
    # Find the task with the matching title
        task_to_update = next((task for task in self.book if task.title == task_name), None)

        if task_to_update:
            # Update the task properties if a new value is provided
            if task_title is not None:
                task_to_update.title = task_title
            if task_desc is not None:
                task_to_update.desc = task_desc
            if task_prio is not None:
                task_to_update.prio = task_prio
            if task_due is not None:
                task_to_update.due = task_due
            if task_create_date is not None:
                task_to_update.created_at = task_create_date
        else:
            print(f"Task with title '{task_name}' not found.")



    def book_sort(self, attr, rev=False):
        self.book.sort(reverse=rev, key=attr)

    def display_book(self):
        print('Here is your To-Do List:')
        for i, taskNo in enumerate(self.book):
            print(f'{i+1}. {taskNo.title}: {taskNo.desc}, Priority: {taskNo.prio}, Due Date: {taskNo.due}, Created At: {taskNo.created_at}')


Task1 = Task('1st_Task', task_prio=2)
Task2 = Task('2nd_Task', task_prio=1)
Task3 = Task('3nd_Task', task_prio=1, task_due=datetime.date(2023, 12, 1))
Task4 = Task('4th_Task', task_prio=1, task_due=datetime.date(2023, 10, 1))

my_task_book = TaskBook()
my_task_book.add(Task1)
my_task_book.add(Task2)
my_task_book.add(Task3)
my_task_book.add(Task4)
my_task_book.delete(Task2)

my_task_book.book_sort(attr=sort_by_priority)

# for i, taskNo in enumerate(my_task_book.book):
#     print(f" task_book before sorting by priority: {taskNo.title}")


my_task_book.book_sort(rev=True, attr=sort_by_create_date)
my_task_book.book_sort(rev=True, attr=sort_by_due_date)

my_task_book.display_book()

my_task_book.update('1st_Task', '1st_Task_v2', task_create_date = datetime.datetime.now())

my_task_book.display_book()

# print(f"accessing task_book[all] after sorting: {my_task_book.book}")

to_do_list = []
while True:
    task = input("enter your task: ")
    if task == "delete":
        print(to_do_list)
        task_numbers =int(input("enter number of task?: "))
        to_do_list.pop(task_numbers - 1)
        print(to_do_list)
        continue
    if task == "show":
        print(to_do_list)
        continue
    if task == "done":
        print(to_do_list)
        break
    to_do_list.append(task)



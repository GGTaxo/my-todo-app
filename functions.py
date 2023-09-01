FILEPATH = 'todos.txt'


def get_todos(filepath_arg=FILEPATH):
    """ Read a text file and return the list of to-do items.
    :param filepath_arg:
    :return:
    """
    with open(filepath_arg, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# print(help(get_todos))

def write_todos(todos_arg, filepath_arg=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath_arg, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("hello from functions")

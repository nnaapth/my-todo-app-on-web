FILEPATH='members.txt'
def get_todos():
    """ Read a text file and return the list of
    to-do items.
    """
    with open('/Users/nnaap/Downloads/members.txt', 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg,filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
# no return bc we don't need anythings
print(__name__)
if __name__ == "__main__":
     print("hello from functions")
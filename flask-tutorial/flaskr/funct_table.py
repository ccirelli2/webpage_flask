from flask_table import Table, Col


class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')

# Get some objects
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description



if __name__ == "__main__":
    # Create Class of Table
    items = [Item('Name1', 'Description1'),
             Item('Name2', 'Description2'),
             Item('Name3', 'Description3')]
    # Populate the table
    table = ItemTable(items)
    # Print the html
    print(table.__html__())

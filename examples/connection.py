"""
Examples using a connection
"""
from pynamodax.connection import Connection

# Get a connection
conn = Connection(host='http://localhost:8000')
print(conn)

# List tables
print(conn.list_tables())

# Describe a table
print(conn.describe_table('Thread'))

# Get an item
print(conn.get_item('Thread', 'hash-key', 'range-key'))

# Put an item
conn.put_item('Thread', 'hash-key', 'range-key', attributes={'forum_name': 'value', 'subject': 'value'})

# Delete an item
conn.delete_item('Thread', 'hash-key', 'range-key')

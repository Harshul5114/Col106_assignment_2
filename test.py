from avl import *
import random as r
from bin import *
from object import *
from gcms import *

# Add bins to the GCMS (same as before)
gc = GCMS()

# Inserting bins into the GCMS
gc.add_bin(15, 50)    # Insert gc bin with id 15, capacity 50
gc.add_bin(20, 30)    # Insert gc bin with id 20, capacity 30
gc.add_bin(24, 40)    # Insert gc bin with id 24, capacity 40
gc.add_bin(10, 70)    # Insert gc bin with id 10, capacity 70
gc.add_bin(8, 60)     # Insert gc bin with id 8, capacity 60
gc.add_bin(12, 55)    # Insert gc bin with id 12, capacity 55
gc.add_bin(18, 25)    # Insert gc bin with id 18, capacity 25
gc.add_bin(6, 65)     # Insert gc bin with id 6, capacity 65
gc.add_bin(30, 35)    # Insert gc bin with id 30, capacity 35
gc.add_bin(25, 20)    # Insert gc bin with id 25, capacity 20
gc.add_bin(40, 45)    # Insert gc bin with id 40, capacity 45
gc.add_bin(35, 15)    # Insert gc bin with id 35, capacity 15
gc.add_bin(22, 75)    # Insert gc bin with id 22, capacity 75
gc.add_bin(28, 90)    # Insert gc bin with id 28, capacity 90
gc.add_bin(14, 10)    # Insert gc bin with id 14, capacity 10
gc.add_bin(5, 100)    # Insert gc bin with id 5, capacity 100
gc.add_bin(7, 85)     # Insert gc bin with id 7, capacity 85
gc.add_bin(9, 95)     # Insert gc bin with id 9, capacity 95
gc.add_bin(1, 110)    # Insert gc bin with id 1, capacity 110
gc.add_bin(3, 80)     # Insert gc bin with id 3, capacity 80
gc.add_bin(13, 20)    # Insert gc bin with id 13, capacity 20

print(gc.bins)
# List of all bin IDs with their exact capacities
bins_to_delete = [
    (15, 50), (20, 30), (24, 40), (10, 70), (8, 60), (12, 55),
    (18, 25), (6, 65), (30, 35), (25, 20), (40, 45), (35, 15),
    (22, 75), (28, 90), (14, 10), (5, 100), (7, 85), (9, 95),
    (1, 110), (3, 80), (13, 20)
]

# Define a DFS function that prints the balance of each node
def dfs_with_balance(node, tree):
    if node:
        dfs_with_balance(node.left, tree)
        print(f"Node {node.val.id} with capacity {node.val.capacity}, Balance: {tree._get_balance(node)}")
        dfs_with_balance(node.right, tree)

# Print the tree state and its size
print("Initial AVL Tree:")
dfs_with_balance(gc.bins.root, gc.bins)
print(f"Initial Size: {gc.bins.size}\n")

# Randomly delete bins one by one and print the state of the tree after each deletion
while bins_to_delete:
    # Randomly pick a bin to delete (both ID and capacity are used)
    bin_id, bin_capacity = r.choice(bins_to_delete)
    print(f"Deleting bin with ID: {bin_id}, Capacity: {bin_capacity}")
    
    # Delete the bin from the AVL tree
    gc.bins.delete(Bin(bin_id, bin_capacity))  # Now using both ID and capacity for the delete
    
    # Perform DFS to print the tree structure and balance factors
    print("\nTree after deletion:")
    dfs_with_balance(gc.bins.root, gc.bins)
    
    # Print the updated size of the tree
    print(f"Updated Size: {gc.bins.size}\n")
    
    # Remove the deleted bin (ID, capacity) from the list
    bins_to_delete.remove((bin_id, bin_capacity))

from linkedlist_api import LinkedList, Node
import csv
import sys

orig_stdout = sys.stdout
f = open('output.txt', 'w')
sys.stdout = f
line_count = 0

with open('data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print("{}:{}".format(line_count,','.join(str(item) for item in row)))
        command = row[0]
        if command == 'CREATE':
                linked_list = LinkedList()
        elif command == 'DEBUG':
                linked_list.debug_print()
        elif command == 'ADD':
                linked_list.add(row[1])
        elif command == 'GET':
                linked_list.get(int(row[1]))
        elif command == 'SET':
                linked_list.set(int(row[1]),row[2])
        elif command == 'INSERT':
                linked_list.insert(int(row[1]),row[2])
        elif command == 'DELETE':
                linked_list.delete(int(row[1]))
        elif command == 'SWAP':
                linked_list.swap(int(row[1]), int(row[2]))

        line_count += 1

sys.stdout = orig_stdout
f.close()

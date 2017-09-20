from linkedlist_api import LinkedList, Node

# create linked list
ll = LinkedList()
ll.head = Node('a')


ll.head.next = Node('b')
ll.head.next.next = Node('c')

ll.size = 3

# iterate through linked list
# n = ll.head
# for i in range(ll.size):
#     print(n)
#     n = n.next
#
# t = ll._get_node(1)
# print("....", t)
#
# ll.add('d')
#
# ll.size += 1
#
# n = ll.head
# for i in range(ll.size):
#     print(n)
#     n = n.next

ll.debug_print()


#
# class Processor(object):
#
#     def run(self, f):
#         '''Processes the given file stream.'''
#         for line_i, line in enumerate(f):
#             # get the line parts
#             line = line.rstrip()
#             print('{}:{}'.format(line_i, line))
#             parts = line.split(',')
#             # call this command's function
#             try:
#                 func = getattr(self, 'cmd_{}'.format(parts[0].lower()))
#                 func(*parts[1:])
#             except Exception as e:
#                 print('Error: {}'.format(e))
#
#     def cmd_debug(self, *args):
#         self.ar.debug_print()
#
#     def cmd_create(self, *args):
#         self.ar = Array()
#
#     def cmd_add(self, *args):
#         self.ar.add(args[0])
#
#     def cmd_insert(self, *args):
#         self.ar.insert(int(args[0]), args[1])
#
#     def cmd_set(self, *args):
#         self.ar.set(int(args[0]), args[1])
#
#     def cmd_get(self, *args):
#         print(self.ar.get(int(args[0])))
#
#     def cmd_delete(self, *args):
#         self.ar.delete(int(args[0]))
#
#     def cmd_swap(self, *args):
#         self.ar.swap(int(args[0]), int(args[1]))
#
#
#
# #######################
# ###   Main loop
#
# with open('data.csv', newline='') as f:
#     processor = Processor()
#     processor.run(f)

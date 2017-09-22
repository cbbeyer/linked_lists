from linkedlist_api import LinkedList, Node
#
# # create linked list
# ll = LinkedList()
# ll.add('a')
#
#
# # ll.head = Node('a')
# #
# #
# ll.add('b')
# ll.add('c')
# ll.add('d')
# #
# # ll.size = 3
#
# # iterate through linked list
# # n = ll.head
# # for i in range(ll.size):
# #     print(n)
# #     n = n.next
# #
# # t = ll._get_node(1)
# # print("....", t)
# #
# # ll.add('d')
# #
# # ll.size += 1
# #
# # n = ll.head
# # for i in range(ll.size):
# #     print(n)
# #     n = n.next
#
# # ll.debug_print()
# #
# # ll.get(0)
# # ll.get(1)
# # ll.get(2)
#
# # ll.delete(1)
# # ll.delete(0)
#
# # ll.set(1,'h')
#
# ll.insert(2, 'test1')
# ll.insert(2, 'test2')
# # print(ll.size)
#
# # ll.debug_print()
# #
# # print('>>>>>> List 1')
# #
# # ll.get(0)
# # ll.get(1)
# # ll.get(2)
# # ll.get(3)
# # ll.get(4)
# #
# # print('>>>>>> List 2')
#
# # ll.debug_print()
# #
# # ll.insert(0, 'hello')
# # ll.get(0)
# # ll.get(1)
# # ll.get(2)
# # ll.get(3)
# # ll.get(4)
# # ll.get(5)
# #
# # ll.debug_print()
#
# print('................ SWAP ...................')
#
# ll.debug_print()
# ll.swap(3,5)
# ll.debug_print()
# # ll.swap(3,5)
# # ll.debug_print()
# # ll.swap(0,3)
# # ll.debug_print()
# # ll.swap(4,3)
# # ll.debug_print()


class Processor(object):

    def run(self, f):
        '''Processes the given file stream.'''
        for line_i, line in enumerate(f):
            # get the line parts
            line = line.rstrip()
            print('{}:{}'.format(line_i, line))
            parts = line.split(',')
            # call this command's function
            try:
                func = getattr(self, 'cmd_{}'.format(parts[0].lower()))
                func(*parts[1:])
            except Exception as e:
                print('Error: {}'.format(e))

    def cmd_debug(self, *args):
        self.ll.debug_print()

    def cmd_create(self, *args):
        self.ll = LinkedList()

    def cmd_add(self, *args):
        self.ll.add(args[0])

    def cmd_insert(self, *args):
        self.ll.insert(int(args[0]), args[1])

    def cmd_set(self, *args):
        self.ll.set(int(args[0]), args[1])

    def cmd_get(self, *args):
        print(self.ll.get(int(args[0])))

    def cmd_delete(self, *args):
        self.ll.delete(int(args[0]))

    def cmd_swap(self, *args):
        self.ll.swap(int(args[0]), int(args[1]))



#######################
###   Main loop

with open('data.csv', newline='') as f:
    processor = Processor()
    processor.run(f)

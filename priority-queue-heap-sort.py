class PriorityQueue:

    def __init__(self, array):

        self.target = len(array)
        self.heap_size = len(array) - 1
        self.array = array


    # traverse subarray A[1..n-1] from top-bottom and run swim_up on each node
    def build_heap(self):
        counter = self.target
        for i in range(1, counter):
            self.swim_up(i)

        return self.array


    def swim_up(self, current_index):
        parent_index = (current_index + 1) / 2 - 1

        if (current_index >= 1 and
            self.array[current_index] > self.array[parent_index]):
            self.exchange(parent_index, current_index)
            self.swim_up(parent_index)

        return self.array


    # removes the maximum:
    # exchange key with root
    # sink_down
    def sink_down(self, parent_index):
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2
        largest = parent_index

        if (left_child_index <= self.heap_size and
            self.array[left_child_index] > self.array[parent_index]):
            largest = left_child_index

        if (right_child_index <= self.heap_size and
            self.array[right_child_index] > self.array[largest]):
            largest = right_child_index

        if largest != parent_index:
            self.exchange(parent_index, largest)
            self.sink_down(largest)

        return self.array


    def exchange(self, first_index, second_index):
        temp = self.array[first_index]
        self.array[first_index] = self.array[second_index]
        self.array[second_index] = temp


    def sort(self):
        self.build_heap()

        while self.heap_size >= 0:
            self.exchange(0, self.heap_size)
            self.heap_size -= 1
            self.sink_down(0)

        return self.array


array = [76,23,11,5799,2,1,3,0]
heap_array = PriorityQueue(array)
print heap_array.sort()





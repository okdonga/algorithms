class HeapSort:

  def __init__(self, array):
    self.target = len(array) - 1
    self.array = array

  def build_heap(self):
    counter = self.target/2

    for i in range(counter, -1, -1):
      self.max_heapify(i)

    return self.array

  # make root value greater than the child value
  def max_heapify(self, parent_index):

    left_child_index = 2 * parent_index + 1
    right_child_index = 2 * parent_index + 2
    largest = parent_index

    if (left_child_index <= self.target and
        self.array[left_child_index] > self.array[parent_index]):
      largest = left_child_index

    if (right_child_index <= self.target and
        self.array[right_child_index] > self.array[largest]):
      largest = right_child_index

    if largest != parent_index:
      self.exchange(parent_index, largest)
      self.max_heapify(largest);

    return self.array


  def exchange(self, first_index, second_index):
    temp = self.array[first_index]
    self.array[first_index] = self.array[second_index]
    self.array[second_index] = temp


  def sort(self):
    self.build_heap()

    while self.target >= 0:
      self.exchange(0, self.target)
      self.target -= 1
      self.max_heapify(0)

    return self.array


array = [6,5,3,1,8,7,2,4]
heap_array = HeapSort(array)
print heap_array.sort()





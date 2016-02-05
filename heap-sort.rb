class HeapSort

  def initialize(array)
    @target = array.length - 1
    @array = array
  end

  # traverse subarray A[0..n/2] from bottom-up and run max_heapify on each one
  def build_heap
    counter = @target/2
    while counter >= 0
      max_heapify(counter)
      counter -= 1
    end
    @array
  end

  # make root value greater than the child value
  def max_heapify(parent_index)

    left_child_index = 2 * parent_index + 1
    right_child_index = 2 * parent_index + 2
    largest = parent_index

    # left_child_index <= @target is checked to discard already sorted items
    if left_child_index <= @target && @array[left_child_index] > @array[parent_index]
      largest = left_child_index
    end

    if right_child_index <= @target && @array[right_child_index] > @array[largest]
      largest = right_child_index
    end

    if largest != parent_index
      exchange(parent_index, largest)
      max_heapify(largest);
    end

    @array
  end

  def exchange(first_index, second_index)
    temp = @array[first_index]
    @array[first_index] = @array[second_index]
    @array[second_index] = temp
  end

  def sort
    build_heap
    while @target >= 0
      exchange(0, @target)
      @target -= 1
      max_heapify(0)
    end
    @array
  end
end

array = [7,3,1444,2,1,78,3]
heap_array = HeapSort.new(array)
p heap_array.sort


=begin
Time complexity: O(n lg n)
* call to build_heap takes o(n) time
* each of the n-1 calls to max_heapify takes lg n time
=end


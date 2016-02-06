var swap = function(array, firstIndex, secondIndex) {
  var temp = array[firstIndex];
  array[firstIndex] = array[secondIndex]
  array[secondIndex] = temp
}

var insertionSort = function(array) {
  var i = 1;
  var j;

  for (i; i < array.length; i++) {
    j = i-1;
    for (j; j >= 0; j--) {
      if (array[i] >= array[j]) {
        break;
      } else {
        swap(array, i, j);
        i = j;
      }
    }
  }

  return array;
}

var array = [22, 11, 99, 88, 9, 7, 42];
console.log(insertionSort(array));


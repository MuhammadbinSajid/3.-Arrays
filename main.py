import array as arr

# create an array
array_num = arr.array('i', [1, 2, 3, 4, 5, 6])
print("Original array: "+str(array_num))

# count number of occurences
print("Number of occurences of the number 3 in the said array:"+str(array_num.count(3)))

# reverse the array
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))
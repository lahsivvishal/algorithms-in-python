# Naive method - O(n^2) time | O(1) space
"""
def twoNumberSum(array, target):
	result = []
	for i in range(len(array) - 1):
		for j in range(i+1, len(array)):
			if array[i] + array[j] == target:
				result.append((array[i], array[j]))
	return result

print(twoNumberSum([7,4,3,2,5,9,1,8,6], 7))
"""
########################################################################################################

# Hash table method - O(n) time | O(n) space

"""def twoNumberSum(array, target):
	nums = {}
	res = []
	for num in array:
		if target - num in nums:
			res.append((target-num, num))
		else:
			nums[num] = True

	return res

print(twoNumberSum([5,2,8,6,1,4,7,9,3], 10))
"""
########################################################################################################

# Pointer Method

def twoNumberSum(array, target):
	array.sort()
	left = 0
	right = len(array)-1
	while left != right:
		currentSum = array[left] + array[right]
		if currentSum == target:
			return [array[left], array[right]]
		elif currentSum < target:
			left += 1
		elif currentSum > target:
			right -= 1

	return []

print(twoNumberSum([6,2,9,4,8,1,7,5,3], 8))

# Steps and Explanation:

# 1. Sorting the Array:

nums.sort()
#The first step is to sort the array. Sorting helps simplify the logic of finding unique triplets and eliminates the need for explicitly handling duplicate combinations later.

#2. Iterating through the Array:

for i in range(0, len(nums) - 2):
#The outer loop iterates over each element in the array. The index i represents the first number in the triplet. The loop goes up to len(nums) - 2 because we need at least two other numbers (j and k) to form a triplet.

#3. Skipping Duplicates:

if i > 0 and nums[i] == nums[i - 1]:
    continue
#If the current element is the same as the previous element (nums[i] == nums[i-1]), we skip this iteration to avoid considering the same triplet multiple times. This ensures that the triplets are unique.

#4. Two Pointers Approach: After fixing the first element nums[i], we use two pointers to find the other two numbers:

#j: The pointer starts from the element just after i (i + 1).
#k: The pointer starts from the last element of the array (len(nums) - 1).
#The idea is to adjust these two pointers (j and k) to find two numbers such that the sum of nums[i] + nums[j] + nums[k] equals zero.

#4. Checking the Sum:

while j < k:
    threeSum = nums[i] + nums[j] + nums[k]
#The inner while loop runs as long as j is less than k. For each triplet (nums[i], nums[j], nums[k]), we calculate threeSum.

#If threeSum is less than 0, we need a larger number to reach 0, so we move the j pointer to the right.

if threeSum < 0:
    j = j + 1
    while nums[j] == nums[j - 1] and j < k:
        j = j + 1
#The inner while loop ensures that we skip over any duplicates by checking if nums[j] == nums[j-1].

#If threeSum is greater than 0, we need a smaller number to reach 0, so we move the k pointer to the left.

elif threeSum > 0:
    k = k - 1
    while nums[k] == nums[k + 1] and j < k:
        k = k - 1
#Similar to the j pointer, the inner while loop skips over duplicates for k.

#If threeSum == 0, we found a valid triplet. We add it to the result list res:

else:
    res.append([nums[i], nums[j], nums[k]])
    j = j + 1
    k = k - 1
    while nums[j] == nums[j - 1] and j < k:
        j = j + 1
    while nums[k] == nums[k + 1] and j < k:
        k = k - 1
#After finding a valid triplet, we move both pointers (j and k) to find more possible triplets. The inner while loops again handle skipping duplicates.

#Return the Result: Finally, after the loops complete, we return the list of triplets:


return res
#Key Points:
#Sorting: The array is sorted to simplify duplicate handling and enable the two-pointer approach.
#Two-Pointer Technique: This technique efficiently finds pairs that sum to a target by adjusting the two pointers (j and k).
#Duplicate Handling: The code ensures no duplicate triplets are included by checking adjacent elements during pointer shifts (j, k).
#Time Complexity: The time complexity of this approach is 
#𝑂(𝑛^2) where sorting is n log n and the two pointer technique is 0(n)


#This solution efficiently finds all unique triplets that sum to zero.

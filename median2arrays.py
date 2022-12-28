def find_median(nums1, nums2):
  # merge the two arrays into a single sorted array
  nums = []
  i = j = 0
  while i < len(nums1) and j < len(nums2):
    if nums1[i] < nums2[j]:
      nums.append(nums1[i])
      i += 1
    else:
      nums.append(nums2[j])
      j += 1
  nums.extend(nums1[i:])
  nums.extend(nums2[j:])
  
  # find the length of the merged array
  n = len(nums)
  
  # if the length is odd, return the middle element
  if n % 2 == 1:
    return nums[n // 2]
  
  # if the length is even, return the average of the two middle elements
  else:
    return (nums[n // 2] + nums[n // 2 - 1]) / 2

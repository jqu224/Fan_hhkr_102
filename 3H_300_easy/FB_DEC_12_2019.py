-----------------------------------------------------
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
```
[1 2 3 4]
left =     [ 1  1  2  6 24]
right = [24 24 12  4  1] 

LEFT DRAGON RIGHT RAINBOW
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_r = [1]
        right_l = [1] 
        for i in nums:
            left_r.append(left_r[-1]*i) 
        for i in nums[::-1]:
            right_l.append(right_l[-1]*i) 
        right_l = right_l[::-1]
        
        ret = []
        for i in range(len(nums)):
            ret.append(left_r[i]*right_l[i+1])
        return ret
	
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for i in range(len(nums))]
        
        # left pass
        prefix_left = 1
        for i in range(1, len(nums)):            
            prefix_left *= nums[i-1]
            result[i] = result[i]*prefix_left

	# right pass
        prefix_right = 1
        for i in range(len(nums)-2, -1, -1):
            prefix_right *= nums[i+1]
            result[i] = result[i]*prefix_right

        return result 

-----------------------------------------------------
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/
 
NOTE: TLE
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        left_r = [0, nums[0]]
        for i in nums[1:]:
            left_r.append(left_r[-1] + i) 
            
        cnt = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if left_r[j] - left_r[i] == k:
                    cnt += 1
        return cnt
	
USE HASHMAP:
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int: 
    
        map_ = defaultdict(int, {0:1}) 
        cnt = 0
        curr = 0
        for i in nums:
            curr += i 
            if curr - k in map_:
                cnt += map_[curr-k]
            map_[curr] += 1
        return cnt	 


---------------------------------------------
973. K Closest Points to Origin 
class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
	
	from heapq import *
	
	
class Solution(object):
    def kClosest(self, points, K):
        # points.sort(key = lambda P: P[0]**2 + P[1]**2)
        # return points[:K]
        pt = []
        heapify(pt)
        for (a, b) in points:
            heappush(pt, (a**2 + b**2, [a, b]))
        rt = []
        for i in range(K):
            rt.append(heappop(pt)[-1])
            
        return rt 

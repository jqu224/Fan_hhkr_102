------------------------------------------------------------------
1. Two Sum
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = sorted(nums)
        l = 0
        r = len(lst) - 1
        while l < r:
            if lst[l] + lst[r] > target:
                r -= 1
            elif lst[l] + lst[r] < target:
                l += 1
            else:
                ll = nums.index(lst[l])
                try:
                    rr = nums.index(lst[r], ll+1)
                except:
                    rr = nums.index(lst[r])
                   
                return [ll, rr]
        return []
            
```
278. First Bad Version
https://leetcode.com/problems/first-bad-version/
```
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
```
```
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l < r: 
            mid = l + (r-l)//2 
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid
                
        return l
```

35. Search Insert Position
https://leetcode.com/problems/search-insert-position/submissions/
```
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
```

953. Verifying an Alien Dictionary
```
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map_ = [0]*26
        for i, o in enumerate(order):
            map_[ord(o) - ord("a")] = i
        ret = [] 
        for word in words:
            temp = []
            for w in word:
                
                temp.append(map_[ord(w) - ord("a")])
            ret.append(tuple(temp))
        dict_1 = {i:r for i, r in enumerate(ret)}
        dict_2 = {i:r for i, r in enumerate(sorted(ret))}
        for k in dict_1:
            if dict_1[k] == dict_2[k]:
                pass
            else:
                break
        else:
            return True
        return False
        
```

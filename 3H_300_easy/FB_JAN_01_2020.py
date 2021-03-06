34. Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                start = end = mid
                while start >= 1 and nums[start] == nums[start-1]:
                    start -= 1
                while end+1 <= len(nums)-1 and nums[end] == nums[end+1]:
                    end += 1
                return [start,end]
            elif target > nums[mid]:
                left =  mid + 1
            else:
                right = mid - 1
        return [-1,-1]
      
 lower bound and upper bound
if upper:
  if nums[mid] == t and nums[mid+1] > t:
if lower:
  if nums[mid] == t and nums[mid11] < t:


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
71. Simplify Path
# Given an absolute path for a file

class Solution:
    def simplifyPath(self, p: str) -> str:
        p = p.split("/")
        ret = []
        for i in p: 
            if not i or i == ".":
                continue
            if i == "..":
                if ret:
                    ret.pop()
            else:
                ret.append(i)
        return "/" + "/".join(ret)
                
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
721. Accounts Merge
class Solution(object):
    def accountsMerge(self, accounts):
        em_to_name = {}
        graph = collections.defaultdict(set)
        for name, *acc in accounts: 
            for email in acc:
                graph[acc[0]].add(email)
                graph[email].add(acc[0])
                em_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for k,num in enumerate(nums):
            if num > 0:
                break

            
            if k > 0 and nums[k] == nums[k-1]: 
                continue
            
            i , j = k+1, len(nums) - 1
            while i < j:
                threeSum = num + nums[i] + nums[j]
                if threeSum > 0:
                    j -= 1
                elif threeSum < 0:
                    i += 1
                else:
                    res.append([num, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i-1] and i < j:
                        i += 1

        return res

            

            
        
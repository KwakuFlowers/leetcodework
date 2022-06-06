class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        # print(self.nums)
        self.target = target
        # print(self.target)
        self.ret = []
        self.currlen = len(self.nums)
        # print(self.currlen)

        if self.currlen >= 2 and self.currlen <= (10**4):
            self.maxind = self.currlen - 1
            for e in enumerate(self.nums):
                # print(e[0], e[1])
                for v in enumerate(self.nums):
                    # print(v[0], v[1])
                    if e[0] == self.maxind and v[0] == self.maxind and self.currlen > 2:
                        statement = "No matches found!"
                        return statement
                        break
                    if e[0] == v[0]:
                        continue
                    currval = self.nums[e[0]] + self.nums[v[0]]
                    # print(currval)
                    if currval == self.target:
                        self.ret = [e[0], v[0]]
                        return self.ret
                        break
                    else:
                        continue
                    break


S = Solution()
test = [3, 2, 4]

searchtest = 6
S.twoSum(test, searchtest)

# [3, 15, 3, 7]
# 6

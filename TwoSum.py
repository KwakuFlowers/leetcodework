class Solution(object):
    def findvalue(self, given, num, currind):
        for i in enumerate(num):
            if i[0] != currind:
                if i[1] == given:
                    return i[0]

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        # #print(self.nums)
        self.target = target
        # #print(self.target)
        self.ret = []
        self.currlen = len(self.nums)
        # #print(self.currlen)
        self.compare = {}
        if self.currlen >= 2 and self.currlen <= (10**4):
            self.compare = {k: val for val, k in enumerate(self.nums)}
            # print(self.compare)
            for i in enumerate(self.nums):
                currsearch = target - i[1]
                # print([i[0]])
                # print(currsearch)
                if currsearch in self.compare and self.compare[currsearch] != i[0]:
                    secind = self.compare[currsearch]
                    self.ret = [i[0], secind]
                    # print(self.ret)
                    return self.ret
                    break
                else:
                    continue


S = Solution()
test = [3, 2, 4]

searchtest = 6
print(S.twoSum(test, searchtest))

# [3, 15, 3, 7]
# 6

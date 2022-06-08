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
        # print(self.nums)
        self.target = target
        # print(self.target)
        self.ret = []
        self.currlen = len(self.nums)
        # print(self.currlen)

        if self.currlen >= 2 and self.currlen <= (10**4):
            self.maxind = self.currlen - 1
            for e in enumerate(self.nums):
                self.numlook = abs(target - e[1])
                # print(self.numlook)
                foundvalind = self.findvalue(self.numlook, self.nums, e[0])
                if isinstance(foundvalind, type(None)):
                    # print(foundvalind)
                    if e[0] == self.maxind:
                        break
                    continue
                else:
                    self.ret = [e[0], foundvalind]
                    break

            return self.ret


S = Solution()
test = [3, 2, 4]

searchtest = 6
print(S.twoSum(test, searchtest))

# [3, 15, 3, 7]
# 6

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.actnum = 0
        self.index = 0
        if len(s) >= 1 and len(s) <= 15:
            for i in s:
                if i == "I" or i == "i":
                    self.actnum = self.actnum + 1
                if i == "V" or i == "v":
                    self.actnum = self.actnum + 5
                    if self.index - 1 in range(0, 14):
                        if s[self.index - 1] == "I" or s[self.index - 1] == "i":
                            self.actnum = self.actnum - 2
                if i == "X" or i == "x":
                    self.actnum = self.actnum + 10
                    if self.index - 1 in range(0, 14):
                        if s[self.index - 1] == "I" or s[self.index - 1] == "i":
                            self.actnum = self.actnum - 2
                if i == "L" or i == "l":
                    self.actnum = self.actnum + 50
                    if self.index - 1 in range(0, 14):
                        if s[self.index - 1] == "X" or s[self.index - 1] == "x":
                            self.actnum = self.actnum - 20
                if i == "C" or i == "c":
                    self.actnum = self.actnum + 100
                    if self.index - 1 in range(0, 14):
                        if s[self.index - 1] == "X" or s[self.index - 1] == "x":
                            self.actnum = self.actnum - 20
                if i == "D" or i == "d":
                    self.actnum = self.actnum + 500
                    if self.index - 1 in range(0, 14):
                        if s[self.index - 1] == "C" or s[self.index - 1] == "c":
                            self.actnum = self.actnum - 200
                if i == "M" or i == "m":
                    self.actnum = self.actnum + 1000
                    if self.index - 1 in range(0, 14):
                        if s[self.index - 1] == "C" or s[self.index - 1] == "c":
                            self.actnum = self.actnum - 200
                self.index = self.index + 1
        print(self.actnum)


Ex = "MCMXCIV"
S = Solution()
S.romanToInt(Ex)
# s = "XIX"
# romanToInt(s)

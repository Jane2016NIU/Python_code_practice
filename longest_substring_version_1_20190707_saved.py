class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #temp string is 
        li = list(s)
        longest = 0
        dic = {}
        for j in range(len(li)):
            temp = []
            for k in range(j, len(li)):
                if li[k] not in temp:
                    temp.append(li[k])
                    # edge case: k in the end of list
                    if (k == len(li) - 1) & (longest < len(temp)):
                        longest = len(temp)
                        #print(temp, 'and longest = ', longest)
                        break
                    #print(temp, 'and longest = ', longest)

                        
                else:
                    #print(temp)
                    if longest < len(temp):
                        longest = len(temp)
                        #print('longest = ', longest)
                    break
            if longest >= len(li) - j - 1: 
                break         
        return longest

if __name__ == '__main__':
	s = 'bcabcbb'
	solution = Solution()
	print('longest substring length is: ', solution.lengthOfLongestSubstring(s))
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        #we start on one side and then  if we see a repeated character we start again, 
        # but we save the length of the prev IF  its is bigger. 
        # SO we save the first one to begin with 

        #edge case - empty string 
        i = 0
        it = set()
        largest_size = 0
        prev_size = 0
        x = len(s)

        if len(s) == 1:
            return 1
        while i < x:
            if s[i] not in it :
                it.add(s[i])
                print(it)
                largest_size +=1 
                print(largest_size)
                if prev_size <= largest_size:
                    prev_size = largest_size # prev = 3
            else:
                it.clear()
                it.add(s[i])
                if prev_size <= largest_size:
                    prev_size = largest_size # prev = 3
                #it.clear()
                largest_size = 1
                print(largest_size)
            i += 1
        return prev_size


      
#407/987 cases passed, Use sliding windows 

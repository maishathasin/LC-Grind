
#this is acc ok i think can be beter 
# 2do: think 

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

        if (numBottles == numExchange):
            return numBottles + 1
        
        fullBottles = numBottles
        emptyBottles = 0
        res = 0
        while fullBottles > 0:
            res += fullBottles
            emptyBottles += fullBottles 
            fullBottles = emptyBottles // numExchange
            emptyBottles = emptyBottles % numExchange
        
        return res
            
            
            
            
            
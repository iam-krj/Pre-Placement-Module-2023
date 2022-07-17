class Solution(object):
    def maxProfit(self, prices):
        mtn = prices[0]
        bp = 0
        for i in range(1, len(prices)):
            if bp < prices[i]-mtn:
                bp = prices[i]-mtn
            if mtn > prices[i]:
                mtn =prices[i]
        return bp
            
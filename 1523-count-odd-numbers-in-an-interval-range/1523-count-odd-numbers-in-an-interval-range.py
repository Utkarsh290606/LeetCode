class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # for n odd no. :(high+1)//2
        # for odd nos. b/w 1 to low-1 : (low//2)
        return (high+1)//2 - (low//2)

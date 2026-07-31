class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        return string == string[::-1]

# Approach 2: Reverse half of the number(Efficient):

# def isPalindrome(x:int) -> bool:
#     if x < 0 or (x % 10 == 0 and x != 0):
#         return False

#     reversed half = 0
#     while x > reversed_half:
#         reversed_half = reversed_half * 10 + x % 10
#         x //= 10

#     return x == reversed_half or x == reversed_half // 10
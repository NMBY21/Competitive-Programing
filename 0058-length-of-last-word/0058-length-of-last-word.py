class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        if not words:
            return 0
        last_word = words[-1]
        length = len(last_word)

        print("The last word is '{}' with length {}.".format(last_word, length))
        return length

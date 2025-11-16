from collections import Counter

class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        if s == "":
            return 0
            
        char_counts = Counter(s)
        
        if char_counts['a'] == 0 or char_counts['b'] == 0:
            return len(s)
        
        a_freq = char_counts['a']
        b_freq = char_counts['b']

        string = list(s)
        a_list = []
        b_list = []
        for i in range(len(string)):
            if string[i] == 'a':
                a_list.append(string[i])
            elif string[i] == 'b':
                b_list.append(string[i])
        
        for i in range(len(string)):
            a_list[i] = a_list[i].replace('a', "")
            a_freq -= 1
            b_list[i] = b_list[i].replace('b', "")
            b_freq -= 1
            if a_freq == 0 or b_freq == 0:
                a_list = "".join(a_list)
                b_list = "".join(b_list)
                break
        return len(a_list) + len(b_list)
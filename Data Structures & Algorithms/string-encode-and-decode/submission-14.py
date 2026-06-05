class Solution:

    '''5#Hello5#World'''
    def encode(self, strs: List[str]) -> str:
        if not strs: return ""
        output_str = ""
        for s in strs:
            length = len(s)
            output_str += str(length) + '#' + s

        return output_str

    def decode(self, s: str) -> List[str]:
        print(s)
        def len_finder(s: str, idx: int):
            length = 0
            idx_c = idx
            while s[idx_c] != '#':
                length += 1
                idx_c += 1
            # print(s[idx:idx + length])
            return int(s[idx:idx + length])
        list = []
        if s == "": return list
        length = len_finder(s, 0)
        length_char = len(str(length)) - 1
        pos = 2

        

        while pos <= len(s):
            start_idx = pos + length_char
            end_idx = start_idx + length
            list.append(s[start_idx:end_idx])

            pos = end_idx + 2
            if pos < len(s): 
                length = len_finder(s,end_idx)
                length_char = len(str(length)) - 1

        return list

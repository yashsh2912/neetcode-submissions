class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op = defaultdict(list)
        for char in strs:
            sortedStr = ''.join(sorted(char))
            op[sortedStr].append(char)
        return list(op.values())
        
        
        
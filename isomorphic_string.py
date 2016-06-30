class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        destimap , sourcemap= dict(), dict()
        for x in range(len(s)):
            dest   =  destimap.get(s[x])
            source = sourcemap.get(t[x])
            if dest is None and source is None:
                sourcemap[t[x]] = s[x]
                destimap[s[x]]= t[x]
            elif source != s[x] or dest != t[x]:
                return False
        return True

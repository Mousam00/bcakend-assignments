def longest_unique_substring(s):
    i=0
    longest=0
    sett=set()
    n=len(s)

    for r in range(n):
        while s[r] in sett:
            sett.remove(s[i])
            i+=1
        w = (r-i) + 1
        longest = max(longest,w)
        sett.add(s[r])
    return longest

print(longest_unique_substring("abcabcbb"))
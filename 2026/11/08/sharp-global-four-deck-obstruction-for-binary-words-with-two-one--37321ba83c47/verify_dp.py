"""Exact binary scattered 4-deck and two-run comparison, Python 3 stdlib.
Each n-bit word appears once as an integer from 0 to 2**n-1.
"""
from collections import defaultdict
from math import comb

FIRST = '01111100111110'
SECOND = '10101111110101'
EXPECTED = (1,5,15,30,15,50,85,140,5,25,50,100,30,100,140,210)

def runs(s):
    return (s[0]=='1') + sum(s[i-1]=='0' and s[i]=='1' for i in range(1,len(s)))

def deck(s):
    d = [[0]*(1<<j) for j in range(5)]
    d[0][0] = 1
    for bit in map(int,s):
        for j in range(4,0,-1):
            for prefix,ct in enumerate(d[j-1]):
                d[j][2*prefix+bit] += ct
    assert sum(d[4])==comb(len(s),4)
    return tuple(d[4])

def census(n):
    groups=defaultdict(list)
    for w in range(1<<n):
        s=format(w,f'0{n}b')
        groups[deck(s)].append(s)
    mixed=[]
    for group in groups.values():
        rs=[runs(s) for s in group]
        if min(rs)<=2 and max(rs)>2:
            mixed.append(group)
    return groups,mixed

def main():
    for n,expected_total in ((13,8176),(14,16328)):
        gs,mixed=census(n)
        assert len(gs)==expected_total,(n,len(gs))
        if n==13:
            assert mixed==[],mixed
        else:
            assert len(mixed)==1,mixed
            assert sorted(mixed[0])==sorted((FIRST,SECOND)),mixed
        print(f'n={n} total_words={1<<n} distinct_decks={len(gs)} mixed_decks={len(mixed)}')
    assert runs(FIRST)==2 and runs(SECOND)==5
    assert deck(FIRST)==deck(SECOND)==EXPECTED
    print('DP_EXHAUSTIVE_OK')

if __name__=='__main__':main()

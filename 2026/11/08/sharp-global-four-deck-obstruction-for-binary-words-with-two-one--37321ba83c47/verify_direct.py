"""Independent combinatorial subsequence enumeration; no DP recurrence."""
from itertools import combinations
from collections import defaultdict
from math import comb

X='01111100111110'
Y='10101111110101'
V=(1,5,15,30,15,50,85,140,5,25,50,100,30,100,140,210)

def deck(s):
    d=[0]*16
    for positions in combinations(range(len(s)),4):
        v=0
        for i in positions:
            v=(v<<1)+int(s[i])
        d[v]+=1
    assert sum(d)==comb(len(s),4)
    return tuple(d)

def runs(s):
    return int(s[0]=='1')+sum(s[i]=='1' and s[i-1]=='0' for i in range(1,len(s)))

def main():
    for w in (X,Y): assert deck(w)==V
    assert runs(X)==2 and runs(Y)==5
    groups={}
    for number in range(1<<13):
        s=format(number,'013b')
        key=deck(s)
        count=runs(s)
        if key not in groups: groups[key]=[False,False]
        groups[key][count<=2]=True
    assert len(groups)==8176,len(groups)
    assert all(not(all(types)) for types in groups.values())
    print('DIRECT_EXHAUSTIVE_N13_OK 8192 source words; witness 2x1001 direct subsequences')
if __name__=='__main__':main()

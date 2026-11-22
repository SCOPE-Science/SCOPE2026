from collections import defaultdict
from itertools import combinations

def right_extensions(w):
    s=w+'$'
    fs=defaultdict(set)
    for i in range(len(s)):
        for j in range(i,len(s)):
            fs[s[i:j]].add(s[j])
    return sorted(u+c for u,F in fs.items() if len(F)>=2 for c in F)

def direct_min(w):
    s=w+'$';E=right_extensions(w)
    req=(1<<len(E))-1
    cover=[]
    for j in range(len(s)):
        pre=s[:j+1]
        cover.append(sum(1<<i for i,e in enumerate(E) if pre.endswith(e)))
    best=len(s)+1;count=0
    for mask in range(1,1<<len(s)):
        pc=mask.bit_count()
        if pc>best:continue
        cv=0
        for j in range(len(s)):
            if mask>>j&1:cv|=cover[j]
        if cv==req:
            if pc<best:best=pc;count=0
            count+=1
    return best,count,len(E)

pairs=[('01111000111100','01111000110100'),('01111001111000','01111001101000'),('10000110000111','10000110010111'),('10000111000011','10000111001011')]
for lo,hi in pairs:
 print(lo,direct_min(lo));print(hi,direct_min(hi))

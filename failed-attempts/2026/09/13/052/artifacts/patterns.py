"""Break transposition-permutation symmetry + partition fixed-point types.
Count: distributes triples by #fixed points is invariant under permuting the
9 pairs and 3 fixed points. Classify orbits by (i,j,k fixed-pattern)."""
import sys
def sig(x): return x^1 if x<18 else x
def fp(t): return sum(1 for x in t if x>=18)
def is_fixed_pair(a,b):
    if a>b:a,b=b,a
    sa,sb=sig(a),sig(b)
    return (sa==a and sb==b) or (sa==b and sb==a)
from itertools import combinations
import collections
seen=set()
cnt=collections.Counter()
ex={}
for t in combinations(range(21),3):
    a,b,c=t
    if is_fixed_pair(a,b) or is_fixed_pair(a,c) or is_fixed_pair(b,c): continue
    st=tuple(sorted((sig(a),sig(b),sig(c))))
    if st==t: continue
    key=min(t,st)
    if key in seen: continue
    seen.add(key)
    # canonical pattern: for each point, f or pair-index
    def pat(x): return 'f' if x>=18 else ('p%d'% (x//2))
    p=tuple(sorted(pat(x) for x in key))
    cnt[p]+=1
    ex.setdefault(p,key)
print("num orbits:",len(seen))
for k in sorted(cnt): print(k,cnt[k],"ex",ex[k])
# fixed-point-type totals in any solution: count triples with fp=0,1,2 (fp=3 is the {18,19,20} block)
# total pairs with 0,1,2 fixed endpoints:
n0=sum(1 for a in range(21) for b in range(a+1,21) if a<18 and b<18)
n1=sum(1 for a in range(21) for b in range(a+1,21) if (a<18)!=(b<18))
n2=3
print("pairs by fp:",n0,n1,n2)

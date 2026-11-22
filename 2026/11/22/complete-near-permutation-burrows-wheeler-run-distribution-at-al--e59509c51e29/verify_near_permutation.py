from itertools import permutations
from math import factorial

def canon(s):
    n=len(s)
    return min(s[i:]+s[:i] for i in range(n))
def bwt(s):
    n=len(s)
    return tuple(row[-1] for row in sorted(s[i:]+s[:i] for i in range(n)))
def successors(s,a):
    n=len(s)
    p=[i for i,x in enumerate(s) if x==a]
    assert len(p)==2
    return tuple(sorted((s[(i+1)%n] for i in p)))
def run_count(s):return 1+sum(a!=b for a,b in zip(s,s[1:]))
for n in range(3,10):
    r=n-1
    counts=[0,0];pairs={};valid=0
    for a in range(r):
        pool=list(range(r))+[a]
        # avoid all (n)! duplicates of repeat
        seen=set()
        for s in permutations(pool):
            if s in seen: continue
            seen.add(s)
            if s!=canon(s):continue
            p=successors(s,a)
            bad=p[1]==p[0]+1
            B=bwt(s)
            actual=(run_count(B)<n)
            assert bad==actual,(n,s,p,B,bad,actual)
            counts[actual]+=1
            pairs[(a,p)]=pairs.get((a,p),0)+1
            valid+=1
    assert valid == r*factorial(r)//2
    assert counts[1]==factorial(r)
    assert counts[0]==factorial(r)*(r-2)//2
    assert len(pairs)==r*(r*(r-1)//2)
    assert set(pairs.values())=={factorial(r-2)}
    print(n, 'full_runs',counts[0],'one_pair',counts[1], 'uniform_successor_multiplicity',factorial(r-2), flush=True)

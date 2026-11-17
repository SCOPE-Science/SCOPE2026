"""Exact finite-support certificate for a heterogeneous Greenberg--Hastings graph map.

Only the standard Python library is required; all finite signatures are examined.
"""
from itertools import product
from collections import Counter
from math import factorial

CAPS = tuple(product(range(3), repeat=6))

def classify(sig):
    # Initial groups are the six monochromatic classes of the original coloring.
    # A group with multiplicity two represents any actual multiplicity >= 2.
    colors = tuple(j % 3 if sig[j] else -1 for j in range(6))
    seen = {}
    for t in range(10):
        if colors in seen:
            return seen[colors], t-seen[colors]
        seen[colors] = t
        excitation = [0,0]
        for j,v in enumerate(colors):
            if v == 1:
                excitation[j//3] = min(2, excitation[j//3]+sig[j])
        next_colors=[]
        for j,v in enumerate(colors):
            if v == -1:
                next_colors.append(-1)
            elif v == 1:
                next_colors.append(2)
            elif v == 2:
                next_colors.append(0)
            else:
                threshold = 1 if j<3 else 2
                next_colors.append(1 if excitation[1-j//3]>=threshold else 0)
        colors=tuple(next_colors)
    raise AssertionError('profile failed to recur by step nine')

def occupancy_weight(N,trip):
    c0,c1,c2=trip
    if sum(trip)!=N:return 0
    return factorial(N)//(factorial(c0)*factorial(c1)*factorial(c2))

def count_by_first_entry(m,n):
    out=Counter()
    for l in product(range(m+1),repeat=2):
        x,y=l
        z=m-x-y
        if z<0:continue
        lc=(x,y,z)
        w1=occupancy_weight(m,lc)
        for a in range(n+1):
            for b in range(n-a+1):
                c=n-a-b
                rc=(a,b,c)
                sig=tuple(min(2,s) for s in lc+rc)
                out[classify(sig)] += w1*occupancy_weight(n,rc)
    return out

def threshold_surjections(m):
    return sum(factorial(m)//(factorial(i)*factorial(j)*factorial(m-i-j))
               for i in range(2,m+1) for j in range(2,m-i+1) if m-i-j>=2)

def two_large(m):
    return sum(factorial(m)//(factorial(j)*factorial(m-j)) for j in range(2,m-1))

def run():
    table={sig:classify(sig) for sig in CAPS}
    assert len(table)==729
    hist=Counter(table.values())
    expected={
        (0,1):9,(0,3):8,(0,4):8,(1,1):72,(1,4):32,
        (2,1):234,(2,4):56,(3,1):178,(3,4):24,
        (4,1):68,(4,4):8,(5,1):32}
    assert dict(hist)==expected, (hist,expected)
    per3=[s for s,tp in table.items() if tp==(0,3)]
    assert len(per3)==8 and all(all(v==2 for v in s[:3]) and all(v>=1 for v in s[3:]) for s in per3)
    per4=[s for s,tp in table.items() if tp==(0,4)]
    assert len(per4)==8
    assert all((s[0]==2 and s[1]==0 and s[2]==2 and s[3]>=1 and s[4]>=1 and s[5]==0)
                or (s[0]==2 and s[1]==2 and s[2]==0 and s[3]>=1 and s[4]==0 and s[5]>=1) for s in per4)
    assert all(sum(s[:3])>=3 and sum(s[3:])>=2 for s,tp in table.items() if tp[0]==5)
    for m,n in [(1,1),(2,2),(3,1),(3,2),(3,3),(4,2),(4,3),(5,4),(6,3),(6,4),(7,6),(8,8)]:
        vals=count_by_first_entry(m,n)
        assert sum(vals.values())==3**(m+n)
        assert vals[(0,1)]==1
        assert vals[(0,3)]==threshold_surjections(m)*(3**n-3*2**n+3)
        assert vals[(0,4)]==2*two_large(m)*(2**n-2)
        assert (max(t for t,p in vals)==5)==(m>=3 and n>=2)
    print('EXHAUSTIVE_PROFILES',len(table))
    print('HISTOGRAM',sorted(hist.items()))
    print('RECURRING_PERIODS',[1,3,4])
    print('ALL_PARAMETER_CHECKED_PROFILES: terminal bound=5; sharp iff m>=3,n>=2')
    print('REPRODUCIBLE SAMPLE_COUNTS m=6 n=3:',sorted(count_by_first_entry(6,3).items()))
    print('PASS')

if __name__=='__main__':run()

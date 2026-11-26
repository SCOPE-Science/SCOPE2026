"""Finite reproducibility checks of flat strict-implication normal forms.
Run: python3 verify.py
"""
from itertools import product
from collections import Counter
from math import comb, factorial

def operation(rows):
    n=len(rows)
    up=[((1<<n)-1) ^ ((1<<p)-1) for p in range(n+1)]
    vals=[up[r] for r in rows]
    answer=[]
    for p,A in enumerate(up):
        for q,B in enumerate(up):
            good=[]
            for w in range(n):
                if all(((v & ~A)!=0 or (v & ~B)==0) for v in vals[w:]):
                    good.append(w)
            answer.append(n if not good else good[0])
    return tuple(answer)

def last_occ(rows):
    n=len(rows)
    return tuple(max([j for j,r in enumerate(rows) if r==p],default=-1) for p in range(n))

def op_formula(l):
    n=len(l)
    return tuple(0 if q<=p else 1+max(l[p:q]) for p in range(n+1) for q in range(n+1))

def fibre(l):
    S=[p for p,x in enumerate(l) if x>=0]
    ends=set(l[p] for p in S)
    m=1
    for j in range(len(l)):
        if j not in ends:
            m*=1+sum(l[p]>j for p in S)
    return m

def expected_rank(n,k):
    return comb(n,k)*factorial(n)//factorial(n-k)

for n in range(1,7):
    counts=Counter(); op_to_last={}; total=0
    for rows in product(range(n+1), repeat=n):
        last=last_occ(rows)
        actual=operation(rows)
        assert actual==op_formula(last), (n,rows,last,actual,op_formula(last))
        if actual in op_to_last:
            assert op_to_last[actual]==last
        else:op_to_last[actual]=last
        counts[last]+=1
        total+=1
    assert len(op_to_last)==sum(expected_rank(n,k) for k in range(n+1))
    observed_ranks=Counter(sum(x>=0 for x in l) for l in counts)
    for k in range(n+1):assert observed_ranks[k]==expected_rank(n,k)
    assert all(ct==fibre(l) for l,ct in counts.items())
    assert sum(counts.values())==(n+1)**n
    print('n=',n,'rows=',total,'operations=',len(counts),'by_rank=',dict(sorted(observed_ranks.items())),'fiber_sum=',sum(map(fibre,counts)))
print('VERIFY_OK')

"""Direct verification of fixed-pattern deletion-output counts (standard library)."""
from itertools import combinations
from collections import defaultdict, Counter
from math import comb

def choose(n,k):
    return comb(n,k) if n>=k>=0 else 0

def classify(q,u):
    A=set();B=set();C=set()
    for r in range(q):
        cyc=tuple((r+j)%q for j in range(q))
        for a in range(q):
            if a==r:A.add(cyc+(a,))
            elif r<a:B.add(cyc+(a,))
            else:C.add(cyc+(a,))
            if a==(r-1)%q:A.add((a,)+cyc)
            elif (r==0 and a<q-1) or (r>=1 and a<=r-2):B.add((a,)+cyc)
            else:C.add((a,)+cyc)
    assert len(A)==q and len(B)==len(C)==q*(q-1)
    assert not (A&B or A&C or B&C)
    return 'A' if u in A else 'B' if u in B else 'C' if u in C else '-'

def expected(q,n,u):
    k=q+1;d=sum(u[i]>=u[i+1] for i in range(k-1)); e=choose(n+q-d,k)
    cl=classify(q,u)
    delta={'A':(n-1)*(n-2),'B':choose(n-1,2),'C':choose(n-2,2),'-':0}[cl]
    return e-delta,delta,cl

parameter_rows=0; masks=0; word_profiles=0; repeated_fibers=0
for q,n in [(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(4,2),(4,3),(4,4),(4,5),(5,3),(5,4),(6,3)]:
    w=tuple(range(q))*n; t=q+1
    pairs=defaultdict(lambda:defaultdict(int))
    for idx in combinations(range(q*n),t):
        mask=set(idx)
        u=tuple(w[j] for j in idx)
        output=tuple(w[j] for j in range(q*n) if j not in mask)
        pairs[u][output]+=1; masks+=1
    for u,fiber in pairs.items():
        count,loss,cl=expected(q,n,u)
        assert count==len(fiber),(q,n,u,count,len(fiber))
        assert loss==sum(z-1 for z in fiber.values())
        counts=Counter(fiber.values());counts.pop(1,None)
        if cl=='A': want={n-1:n-1} if n>2 else {}
        elif cl=='B': want={j:1 for j in range(2,n)}
        elif cl=='C': want={j:1 for j in range(2,n-1)}
        else:want={}
        assert counts==want,(q,n,u,counts,want)
        repeated_fibers+=sum(counts.values());word_profiles+=1
    parameter_rows+=1
print('PASS direct_enumeration parameter_rows=',parameter_rows,'masks=',masks,'pattern_profiles=',word_profiles,'repeated_output_fibers=',repeated_fibers)

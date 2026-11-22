"""Direct trace-signature test of every candidate allowed by the mono-incidence bound."""
from itertools import combinations

def trace(v):
    return tuple((v[0]>=2,v[1]>=2,v[2]>=2,v[0]>0 and v[1]>0,v[0]>0 and v[2]>0,v[1]>0 and v[2]>0))

def valid(C):
    ss=[trace(x) for x in C]
    return len(C)==len(set(C)) and all(sum(s[i] for s in ss)<=4 for i in range(6))

for n in range(4,41):
    V=[(i,j,n-i-j) for i in range(n+1) for j in range(n+1-i)]
    U={v for v in V if sum(x>=2 for x in v)==1}
    D={v for v in V if sum(x>=2 for x in v)==2}
    assert len(U)==12
    counts=[0,0]
    for kept in combinations(sorted(U),11):
        if valid(kept):counts[0]+=1
    for kept in combinations(sorted(U),10):
        for z in D:
            if valid(kept+(z,)):counts[1]+=1
    assert counts==[3,12*n-39],(n,counts)
    if n in (4,5,6,10,20,40):print('n=%d T11=%d T10=%d total=%d'%(n,*counts,sum(counts)))
print('exhaustive structurally reduced census PASS')

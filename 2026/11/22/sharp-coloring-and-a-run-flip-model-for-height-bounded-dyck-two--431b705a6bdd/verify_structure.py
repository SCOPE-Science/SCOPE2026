"""Independent bit-interval graph enumeration and theorem checks."""
from itertools import combinations,product

def adj(a,b):
    bad=[i for i,(x,y) in enumerate(zip(a,b)) if x!=y]
    return bool(bad) and bad==list(range(bad[0],bad[-1]+1)) and len(set(a[bad[0]:bad[-1]+1]))==1

def run_lengths(a):
    out=[]
    for t in a:
        if out and out[-1][0]==t:out[-1]=(t,out[-1][1]+1)
        else:out.append((t,1))
    return [r for _,r in out]

for m in range(0,12):
    v=[''.join(t) for t in product('01',repeat=m)]
    e=0
    for i,a in enumerate(v):
        degree=sum(adj(a,b) for b in v)
        assert degree==sum(r*(r+1)//2 for r in run_lengths(a)),(m,a,degree)
        e+=degree
    assert e%2==0
    assert e//2==(m-1)*2**m+1 if m else e==0
    for a in v:
        assert all(not adj(a,b) for b in v if a.count('1')==b.count('1') and a!=b)
    clique=['0'*j+'1'*(m-j) for j in range(m+1)]
    assert all(adj(a,b) for a,b in combinations(clique,2))
    if m>=4:
        witness=['1111','1101','0101','0100','0000']
        witness=[t+'0'*(m-4) for t in witness]
        assert all(adj(witness[i],witness[(i+1)%5]) for i in range(5))
        assert all(not adj(witness[i],witness[(i+2)%5]) for i in range(5))
    print('m=%d vertices=%d edges=%d degree_max=%d OK'%(m,len(v),e//2,m*(m+1)//2))

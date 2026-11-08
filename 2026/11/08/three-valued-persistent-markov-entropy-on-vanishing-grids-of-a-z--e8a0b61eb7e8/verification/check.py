"""Exact rational tests of the finite grid Markov transition formula."""
from fractions import Fraction as F
from math import log

def matrix(N):
    h=F(1,N)
    P=[]
    for i in range(N):
        a=i*h
        b=(i+1)*h
        row={}
        u=min(b,F(3,10))
        if a<u:
            lo=F(3,5)-2*u
            hi=F(3,5)-2*a
            left=max(0,int(lo*N)-1)
            right=min(N-1,int(hi*N)+1)
            for j in range(left,right+1):
                image_overlap=max(F(0),min(hi,(j+1)*h)-max(lo,j*h))
                if image_overlap:
                    row[j]=row.get(j,F(0))+image_overlap/(2*h)
        if b>F(3,10):
            plateau_length=b-max(a,F(3,10))
            if plateau_length:
                row[0]=row.get(0,F(0))+plateau_length/h
        assert sum(row.values())==1,(N,i,row)
        P.append(row)
    return P

def check(N):
    P=matrix(N)
    m,r=divmod(3*N,5)
    target=(m-2,m-1,m)
    weights=(F(5-r,10),F(1,2),F(r,10))
    expected={j:w for j,w in zip(target,weights) if w}
    assert P[0]==expected,(N,P[0],expected)
    assert all(P[j]=={0:F(1)} for j in expected),(N,expected)
    reachable={0}
    while True:
        grown=reachable|{i for i in range(N) if any(j in reachable for j in P[i])}
        if grown==reachable:break
        reachable=grown
    assert len(reachable)==N,(N,sorted(set(range(N))-reachable))
    pi={0:F(1,2),**{j:w/2 for j,w in expected.items()}}
    for j in range(N):
        assert sum(pi[i]*P[i].get(j,F(0)) for i in pi)==pi.get(j,F(0))
    return (r,tuple(weights),len(reachable))

for N in range(10,201):
    check(N)
print('VERIFY_OK exact rational: N=10..200, all rows, unique closed class by global reachability, stationary weights')
for r in range(5):
    weights=((5-r)/10,1/2,r/10)
    h=-sum(p*log(p) for p in weights if p)/2
    print(f'residue r={r}  h_N={h:.15f}')

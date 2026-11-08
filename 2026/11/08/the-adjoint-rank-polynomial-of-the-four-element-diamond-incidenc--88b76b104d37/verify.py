"""Exact finite-field verification of the diamond incidence algebra adjoint-rank polynomial."""
from collections import Counter
from itertools import product
from math import comb

def rank(rows, p):
    a=[list(map(lambda v:v%p,row)) for row in rows]; rank=0
    for j in range(len(a[0])):
        k=next((i for i in range(rank,len(a)) if a[i][j]),None)
        if k is None: continue
        a[rank],a[k]=a[k],a[rank]
        inv=pow(a[rank][j],-1,p)
        a[rank]=[v*inv%p for v in a[rank]]
        for i in range(len(a)):
            if i!=rank and a[i][j]:
                c=a[i][j]
                a[i]=[(x-c*y)%p for x,y in zip(a[i],a[rank])]
        rank+=1
        if rank==len(a):break
    return rank

def formula(q):
    w=q-1
    P0=Counter({0:1,1:w,2:4*q*w,3:6*q*w*w,4:q*(4*w**3+w**4)})
    P1=Counter({2:q*q,3:q*q*w,4:2*w*q**3,5:w*w*q**3})
    P2=Counter({4:q**4,5:q**4*w})
    F=Counter({1:2*q,2:2*q*w+(q-2)*q*q})
    out=Counter()
    for C,k in ((P0,q),(P1,2*q*w),(P2,q*w*w)):
        for r,v in C.items():out[r]+=v*k
    for a,va in F.items():
        for b,vb in F.items():out[1+a+b]+=q*q*w*va*vb
    return out

def direct(q):
    out=Counter()
    for d0,d1,d2,d3,a,b,c,d,e in product(range(q),repeat=9):
        alpha=d0-d1;beta=d0-d2;gamma=d1-d3;delta=d2-d3;eta=d0-d3
        # Columns y0,y1,y2,y3, u01,v02,w13,z23,t03
        rows=[[-a,a,0,0,alpha,0,0,0,0],
              [-b,0,b,0,0,beta,0,0,0],
              [0,-c,0,c,0,0,gamma,0,0],
              [0,0,-d,d,0,0,0,delta,0],
              [-e,0,0,e,-c,-d,a,b,eta]]
        out[rank(rows,q)]+=1
    return out

if __name__=='__main__':
    for q in (2,3):
        got=direct(q);exp=formula(q)
        assert got==exp,(q,got,exp)
        assert sum(got.values())==q**9
        print(q,sorted(got.items()))
    for q in (2,3,4,5,7,11):
        assert sum(formula(q).values())==q**9
    print('VERIFY_OK')

#!/usr/bin/env python3
"""Standalone exhaustive fiber check for the minimal-nilpotent bracket theorem."""
from itertools import product
from collections import Counter

def ops(q):
    if q==4:  # GF(4) = F_2[a]/(a^2+a+1), encoded 0,1,a,a+1
        plus=lambda a,b:a^b
        def mul(a,b):
            out=0
            if b&1:out^=a
            if b&2:out^=a<<1
            if out&8:out^=(0b111<<1)
            if out&4:out^=0b111
            return out
        neg=lambda a:a
    else:
        plus=lambda a,b:(a+b)%q
        mul=lambda a,b:(a*b)%q
        neg=lambda a:(-a)%q
    return plus,mul,neg

def rank(A,n,q,add,mul,neg):
    t=[list(A[i*n:(i+1)*n]) for i in range(n)]
    row=0
    for col in range(n):
        piv=next((i for i in range(row,n) if t[i][col]),None)
        if piv is None:continue
        t[row],t[piv]=t[piv],t[row]
        p=t[row][col]
        inv=next(x for x in range(1,q) if mul(x,p)==1)
        for j in range(col,n):t[row][j]=mul(t[row][j],inv)
        for i in range(n):
            if i!=row and t[i][col]:
                a=t[i][col]
                for j in range(col,n):t[i][j]=add(t[i][j],neg(mul(a,t[row][j])))
        row+=1
        if row==n:break
    return row

def matmul(a,b,n,add,mul):
    return tuple(__import__('functools').reduce(add,(mul(a[i*n+k],b[k*n+j]) for k in range(n)),0) for i in range(n) for j in range(n))

def work(n,q,check_all=True):
    add,mul,neg=ops(q)
    vec=list(product(range(q),repeat=n))
    nonzero=[v for v in vec if any(v)]
    lines=[v for v in nonzero if v[next(i for i,x in enumerate(v) if x)]==1]
    dot=lambda v,w:__import__('functools').reduce(add,(mul(x,y) for x,y in zip(v,w)),0)
    factors=[]
    for u in lines:
        for ph in nonzero:
            if dot(u,ph)==0:factors.append((u,ph))
    N=len(factors)
    counts=Counter()
    zero=(0,)*(n*n)
    for u,ph in factors:
        for v,ps in factors:
            aa=dot(ph,v); bb=dot(ps,u)
            C=tuple(add(mul(aa,mul(u[i],ps[j])),neg(mul(bb,mul(v[i],ph[j])))) for i in range(n) for j in range(n))
            counts[C]+=1
    L=(q**n-1)//(q-1)
    assert N==L*(q**(n-1)-1)
    zero_pred=N*((q**(n-1)-1)+(((q**(n-1)-1)//(q-1))-1)*(q**(n-2)-1))
    one_pred=2*q**(n-1)*(q**(n-2)-1)
    two_pred=2*(q-1) if q%2 else q*(q*q-1)
    assert counts[zero]==zero_pred,(n,q,"zero",counts[zero],zero_pred)
    assert sum(counts.values())==N*N
    for C,c in counts.items():
        if C==zero:continue
        r=rank(C,n,q,add,mul,neg)
        if r==1:
            assert matmul(C,C,n,add,mul)==zero,(n,q,'non-nilpotent rank 1',C)
            assert c==one_pred,(n,q,'rank 1',C,c,one_pred)
        elif r==2:
            assert c==two_pred,(n,q,'rank 2',C,c,two_pred)
            C2=matmul(C,C,n,add,mul)
            if q%2:
                C3=matmul(C2,C,n,add,mul)
                assert any(C3==tuple(mul(mul(t,t),z) for z in C) for t in range(1,q)),(n,q,'odd quadratic',C)
            else:
                assert any(C2==tuple(mul(t,z) for z in C) for t in range(1,q)),(n,q,'even scalar',C)
        else:raise AssertionError(('unexpected output rank',n,q,r,C))
    if check_all:
        for C in product(range(q),repeat=n*n):
            if C==zero:expected=zero_pred
            else:
                r=rank(C,n,q,add,mul,neg)
                if r==1 and matmul(C,C,n,add,mul)==zero:expected=one_pred
                elif r==2 and __import__('functools').reduce(add,(C[i*n+i] for i in range(n)),0)==0:
                    C2=matmul(C,C,n,add,mul)
                    if q%2:
                        C3=matmul(C2,C,n,add,mul)
                        admissible=any(C3==tuple(mul(mul(t,t),z) for z in C) for t in range(1,q))
                    else:admissible=any(C2==tuple(mul(t,z) for z in C) for t in range(1,q))
                    expected=two_pred if admissible else 0
                else:expected=0
            assert counts.get(C,0)==expected,(n,q,'full target',C,counts.get(C,0),expected)
    hist=Counter((rank(C,n,q,add,mul,neg),c) for C,c in counts.items())
    print('PASS', 'n',n,'q',q,'nonzero factor count',N,'target count',len(counts),'pair count',N*N,'target multiplicity classes',sorted(hist.items()),'all-target',check_all)
if __name__=='__main__':
    for n,q in [(2,2),(2,3),(2,4),(2,5),(2,7),(3,2),(3,3),(3,4),(3,5),(4,2)]:
        work(n,q,check_all=(n,q)!=(3,5))
    print('ALL_MINIMAL_NILPOTENT_BRACKET_CHECKS_PASS')

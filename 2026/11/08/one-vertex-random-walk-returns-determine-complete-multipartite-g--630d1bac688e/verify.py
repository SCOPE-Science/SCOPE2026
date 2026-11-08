#!/usr/bin/env python3
"""Exact finite checks of one-vertex random-walk return reconstruction.
Requires Python >= 3.9 standard library only.
"""
from fractions import Fraction as F
from collections import defaultdict

def partitions(n, maximum=None):
    if n==0:
        yield ()
        return
    if maximum is None: maximum=n
    for k in range(min(n,maximum),0,-1):
        for rest in partitions(n-k,k):
            yield (k,)+rest

def transition(part):
    n=sum(part); labels=sum(([i]*s for i,s in enumerate(part)),[])
    P=[]
    for i in labels:
        P.append([F(int(i!=j),n-part[i]) for j in labels])
    return P, labels

def quot(part):
    n=sum(part)
    return [[F(part[j],n-part[i]) if j!=i else F(0) for j in range(len(part))]
            for i in range(len(part))]

def mult(A,b):
    return [sum(A[i][j]*b[j] for j in range(len(b))) for i in range(len(b))]

def signature(A, root, steps):
    v=[F(int(i==root)) for i in range(len(A))]
    answer=[]
    for t in range(steps+1):
        answer.append(v[root]);v=mult(A,v)
    return tuple(answer)

def inverse(A,b):
    # Gaussian elimination over rationals
    n=len(A); R=[row[:]+[b[i]] for i,row in enumerate(A)]
    for j in range(n):
        p=next(k for k in range(j,n) if R[k][j]); R[j],R[p]=R[p],R[j]
        q=R[j][j];R[j]=[x/q for x in R[j]]
        for k in range(n):
            if k!=j:
                q=R[k][j]
                if q:R[k]=[x-q*y for x,y in zip(R[k],R[j])]
    return [R[i][-1] for i in range(n)]

def resolvent_diag(A, root, z):
    n=len(A);L=[[(z if i==j else F(0))-A[i][j] for j in range(n)] for i in range(n)]
    return inverse(L,[F(int(i==root)) for i in range(n)])[root]

def check():
    checks=0
    for n in range(2,12):
        seen={}
        for part in partitions(n):
            if len(part)<2: continue
            P,lab=transition(part); Q=quot(part)
            # The kernel projector kills every partwise-constant transition.
            for u in range(n):
                for w in range(n):
                    # P applied to I - within-part block average equals zero.
                    val=sum(P[u][k]*(F(int(k==w)) -
                         (F(1,part[lab[k]]) if lab[k]==lab[w] else F(0))) for k in range(n))
                    assert val==0
                    checks+=1
            for a in set(part):
                i=part.index(a);root=lab.index(i)
                sig=signature(P,root,2*n-1)
                qs=signature(Q,i,2*n-1)
                assert sig[0]==1
                for t in range(1,2*n):
                    assert sig[t]==qs[t]/a, (n,part,a,t)
                    checks+=1
                other=seen.setdefault(sig,(part,a))
                assert other==(part,a),(n,part,a,other)
                checks+=1
                d=F(a,n-a)
                for z in (F(2),F(3)):
                    f=resolvent_diag(P,root,z)
                    g=resolvent_diag(Q,i,z)
                    X=sum((F(s,n-s)/(z+F(s,n-s)) for j,s in enumerate(part) if j!=i), F(0))
                    assert f==(1-F(1,a))/z+g/a
                    assert g==(1-X)/((z+d)*(1-X)-d)
                    B=z-F(1)/g
                    assert B/(d+B)==X
                    checks+=3
        print('N',n,'unique rooted signatures',len(seen))
    # fixed root part, unknown N: complete bipartite return ambiguity
    for a in (1,2,3,5):
        sigs=[]
        for b in (1,2,4,7):
            P,l=transition((a,b)); sigs.append(signature(P,0,13))
        assert len(set(sigs))==1
        checks+=1
    print('VERIFY_OK',checks,'exact-rational checks')
if __name__=='__main__':check()

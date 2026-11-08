#!/usr/bin/env python3
"""Standalone finite-field checks for the retraction spectrum of bilinear-product algebras.
No external modules required. Tests are corroboration, not an infinite proof.
"""
import itertools
from math import prod

def gb(n,r,q):
    if r<0 or r>n:return 0
    return prod(q**(n-i)-1 for i in range(r))//prod(q**(r-i)-1 for i in range(r))

def gl(n,q):
    return prod(q**n-q**i for i in range(n))

def formula_isotropic(n,r,q,lam_class):
    if r>n or r<0:return 0
    if lam_class=='alternating':
        return prod(q**(2*(n-i))-1 for i in range(r))//prod(q**(r-i)-1 for i in range(r))
    if lam_class=='symmetric':
        return gb(n,r,q)*prod(q**(n-1-i)+1 for i in range(r))
    assert lam_class=='generic'
    acc=0
    for a in range(n+1):
        for b in range(n-a+1):
            t=a+b-r
            if 0<=t<=min(a,b):
                acc+=gb(n,a,q)*gb(n-a,b,q)*gb(a,t,q)*gb(b,t,q)*gl(t,q)
    return acc

def rref_subspaces(d,r,q):
    if r==0:
        yield ();return
    for pivots in itertools.combinations(range(d),r):
        pos=[(i,j) for i in range(r) for j in range(pivots[i]+1,d) if j not in pivots]
        for v in itertools.product(range(q),repeat=len(pos)):
            mat=[[0]*d for _ in range(r)]
            for i,p in enumerate(pivots):mat[i][p]=1
            for (i,j),x in zip(pos,v):mat[i][j]=x
            yield tuple(tuple(row) for row in mat)

def gf4mul(x,y):
    r=0
    for i in range(2):
        for j in range(2):
            if (x>>i)&1 and (y>>j)&1:
                deg=i+j
                if deg==2:r^=3 # t^2=t+1, in binary coordinates
                else:r^=(1<<deg)
    return r

def bil(u,v,n,lam,q):
    if q==4:
        s=0
        for i in range(n):s^=gf4mul(u[i],v[n+i])^gf4mul(lam,gf4mul(u[n+i],v[i]))
        return s
    return sum(u[i]*v[n+i]+lam*u[n+i]*v[i] for i in range(n))%q

def phase(q,lam):
    if q==4:
        if lam==1:return 'alternating'
        return 'generic'
    if (lam+1)%q==0:return 'alternating'
    if lam==1 and q%2:return 'symmetric'
    if lam==1 and q%2==0:return 'alternating'
    return 'generic'

def verify_subspaces(n,q,lam):
    actual=[]
    for r in range(2*n+1):
        num=sum(all(bil(a,b,n,lam,q)==0 for a in W for b in W) for W in rref_subspaces(2*n,r,q))
        actual.append(num)
    expected=[formula_isotropic(n,r,q,phase(q,lam)) for r in range(2*n+1)]
    assert actual==expected,(n,q,lam,actual,expected)
    return actual

def check_endomorphisms_n1(q,lam):
    # All maps must send z to alpha*z because z spans the square ideal.
    counts=[0]*4
    for a,b,c,d,t1,t2,alpha in itertools.product(range(q),repeat=7):
        basis=((1,0),(0,1)); ims=((a,c),(b,d))
        def B(v,w):return (v[0]*w[1]+lam*v[1]*w[0])%q
        if any(B(ims[i],ims[j])!=(alpha*B(basis[i],basis[j]))%q for i in range(2) for j in range(2)):continue
        if (alpha*alpha-alpha)%q:continue
        if (a*a+b*c-a)%q or (a*b+b*d-b)%q or (c*a+d*c-c)%q or (c*b+d*d-d)%q:continue
        if (t1*a+t2*c+alpha*t1-t1)%q or (t1*b+t2*d+alpha*t2-t2)%q:continue
        if alpha:
            assert (a*d-b*c)%q
            rank=3
        else:
            rank=0 if not any((a,b,c,d)) else (1 if (a*d-b*c)%q==0 else 2)
        counts[rank]+=1
    expected=[1, q*q*formula_isotropic(1,1,q,phase(q,lam)),0,1]
    assert counts==expected,(q,lam,counts,expected)
    return counts

def main():
    for q,lams in [(3,[1,2]),(5,[1,2,4]),(7,[1,2,3,6]),(4,[1,2,3])]:
        for lam in lams:
            for n in (1,2):
                print('SUBSPACE',q,lam,n,phase(q,lam),verify_subspaces(n,q,lam))
            if q!=4:print('ENDOMORPHISM',q,lam,check_endomorphisms_n1(q,lam))
    for n in (1,2,3,4):
        assert formula_isotropic(n,n,5,'generic')==sum(gb(n,a,5) for a in range(n+1))
        assert formula_isotropic(n,n,5,'alternating')==prod(5**i+1 for i in range(1,n+1))
    print('VERIFY_OK_BILINEAR_RETRACTIONS')

if __name__=='__main__':main()

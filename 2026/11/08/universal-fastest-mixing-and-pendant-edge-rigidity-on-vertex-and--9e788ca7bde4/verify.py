#!/usr/bin/env python3
"""Reproducible numerical and exact checks for the optimal symmetric mixing kernel on leaf coronas."""
import math, itertools, random
from fractions import Fraction as F
import numpy as np
import sympy as sp

def edges_cycle(n):
    return n,sorted({tuple(sorted((j,(j+1)%n))) for j in range(n)})
def edges_complete(n):
    return n,list(itertools.combinations(range(n),2))
def edges_cube(k):
    return 2**k,[(u,u^(1<<i)) for u in range(2**k) for i in range(k) if not(u&(1<<i))]
def edges_petersen():
    e=[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(i+5,((i+2)%5)+5) for i in range(5)]
    return 10,[tuple(sorted(x)) for x in e]

def L_base(n,es):
    z=np.zeros((n,n))
    for a,b in es:
        z[a,a]+=1;z[b,b]+=1;z[a,b]-=1;z[b,a]-=1
    return z

def P_matrix(n,es,r,p,q):
    N=n*(r+1)
    mat=np.eye(N)
    for a,b in es:
        mat[a,b]+=p;mat[b,a]+=p;mat[a,a]-=p;mat[b,b]-=p
    for a in range(n):
        for j in range(r):
            b=n+a*r+j
            mat[a,b]+=q;mat[b,a]+=q;mat[a,a]-=q;mat[b,b]-=q
    return mat

def all_edges(n,es,r):
    return es+[(a,n+a*r+j) for a in range(n) for j in range(r)]

def P_random(n,es,r,rng):
    e=all_edges(n,es,r);N=n*(r+1)
    weights=[rng.random()+0.01 for _ in e]
    sums=[0.0]*N
    for w,(u,v) in zip(weights,e):sums[u]+=w;sums[v]+=w
    scale=1/max(sums)*(0.1+0.9*rng.random())
    mat=np.eye(N)
    for w,(u,v) in zip(weights,e):
        w*=scale;mat[u,v]+=w;mat[v,u]+=w;mat[u,u]-=w;mat[v,v]-=w
    return mat

def mu(mat):
    eig=np.linalg.eigvalsh(mat)
    return max(abs(eig[0]),abs(eig[-2]))

def exact_C4(r):
    n,base=edges_cycle(4)
    D=1+4*r;q=F(2,D);p=F(1+2*r,2*D)
    N=n*(r+1)
    mat=sp.eye(N)
    for u,v in all_edges(n,base,r):
        w=sp.Rational(p.numerator,p.denominator) if u<n and v<n else sp.Rational(q.numerator,q.denominator)
        mat[u,u]-=w;mat[v,v]-=w;mat[u,v]+=w;mat[v,u]+=w
    ev=mat.eigenvals()
    arr=sorted([(k,v) for k,v in ev.items()],key=lambda x:float(x[0]))
    assert sum(v for k,v in arr)==N and arr[-1][0]==1
    assert sp.Rational(1,D)==1-arr[-2][0] or any(k==sp.Rational(1,D) for k,v in (sp.eye(N)-mat).eigenvals().items())
    assert max(abs(arr[0][0]),abs(arr[-2][0]))==sp.Rational(4*r,D)
    return len(arr)

def symbolic():
    t,r,d=sp.symbols('t r d', positive=True)
    D=1+r*(1+t)**2
    p=(1+r*(1+t))/(d*D)
    q=t*(1+t)/D
    l=t**2/D
    M=sp.Matrix([[p*d*t*t+r*q,-r*q],[-q,q]])
    z=sp.Matrix([1,1+t])
    assert all(sp.factor(k)==0 for k in M*z-l*z)
    assert sp.factor(d*p+r*q-1)==0
    assert sp.factor(q-l*(1+t)/t)==0
    # Rayleigh upper bound: testing vector (1,1+t) on the symmetric block.
    assert sp.factor((d*p*t*t + r*q*t*t) /D-l)==0
    return 'symbolic eigenvector, budget, Rayleigh identities'

def main():
    print('SYMBOLIC',symbolic())
    ec=0
    for r in range(1,5):ec+=exact_C4(r)
    print('EXACT_C4',ec,'distinct exact eigenvalues across four independent instances')
    families=[('C'+str(n),edges_cycle(n)) for n in range(3,13)]
    families += [('K'+str(n),edges_complete(n)) for n in range(3,9)]
    families += [('Q'+str(k),edges_cube(k)) for k in range(2,5)]
    families += [('Petersen',edges_petersen())]
    rng=random.Random(781029)
    cases=0;comp=0;finite=0
    for name,(n,es) in families:
        d=2*len(es)//n
        assert d*n==2*len(es)
        vals=np.linalg.eigvalsh(L_base(n,es))
        a=vals[1]/d;assert a>0 and a<=2+1e-12
        t=math.sqrt(a)
        for r in range(1,5):
            D=1+r*(1+t)**2
            p=(1+r*(1+t))/(d*D)
            q=t*(1+t)/D
            lam=a/D
            mat=P_matrix(n,es,r,p,q)
            ev=np.linalg.eigvalsh(mat)
            err=max(abs(1-ev[-2]-lam),abs(mu(mat)-(1-lam)))
            assert err<2e-10,(name,r,err)
            assert np.min(mat)>-2e-13
            assert max(abs(mat.sum(axis=0)-1))<2e-13
            assert abs(1-d*p-r*q)<2e-13
            cases+=1
            for z in range(12):
                cand=P_random(n,es,r,rng)
                assert mu(cand)>=(1-lam)-2e-10,(name,r,z)
                comp+=1
            # invariant competitors grid, including positivity and boundary
            for j in range(21):
                pc=j/(20*d)
                qc=(1-d*pc)/r
                cand=P_matrix(n,es,r,pc,qc)
                assert mu(cand)>=(1-lam)-2e-10,(name,r,j)
                finite+=1
    print('VERIFY_OK',cases,'network eigenvalue checks;',comp,'noninvariant random competitors;',finite,'orbit competitors; C4 exact rational spectra')
if __name__=='__main__':main()

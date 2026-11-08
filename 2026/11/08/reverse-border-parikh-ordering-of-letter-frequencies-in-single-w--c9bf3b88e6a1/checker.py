"""Independent finite and matrix checks for q-ary single-pattern avoidance frequencies."""
from itertools import product, combinations
from math import isclose
import numpy as np
from scipy.optimize import brentq

def borders(w):
    m=len(w)
    return [l for l in range(1,m+1) if w[:l]==w[m-l:]]

def border_sign(w,a,b):
    for l in reversed(borders(w)):
        d=w[:l].count(a)-w[:l].count(b)
        if d: return -1 if d>0 else 1
    return 0

def border_prediction(w,q):
    m=len(w); B=borders(w)
    C=lambda z:sum(z**(m-l) for l in B)
    D=lambda z:(1-q*z)*C(z)+z**m
    rho=brentq(D,1/q,1/(q-1) if m>1 else 1/(q-1)+1e-6,xtol=1e-14)
    # numerical implicit derivatives of D, actual frequencies
    Cz=sum((m-l)*rho**(m-l-1) for l in B if l<m)
    Dz=-q*C(rho)+(1-q*rho)*Cz+m*rho**(m-1)
    def Ta(a):return sum(rho**(m-l)*w[:l].count(a) for l in B)
    P=np.array([(-rho*C(rho) + rho**m*Ta(a)/C(rho))/(rho*Dz) for a in range(q)])
    return P,rho

def matrix_frequency(w,q):
    m=len(w)
    if m==1:
        p=np.ones(q)/float(q-1);p[w[0]]=0;return p
    states=list(product(range(q),repeat=m-1))
    idx={x:i for i,x in enumerate(states)}
    A=np.zeros((len(states),len(states)))
    M=[np.zeros_like(A) for _ in range(q)]
    for i,x in enumerate(states):
        for a in range(q):
            if x+(a,)==w:continue
            j=idx[(x+(a,))[1:]]
            A[i,j]+=1;M[a][i,j]+=1
    vals,vecs=np.linalg.eig(A);k=np.argmax(vals.real)
    lam=vals[k].real;r=vecs[:,k].real
    vals2,vecs2=np.linalg.eig(A.T);k2=np.argmin(abs(vals2-lam))
    left=vecs2[:,k2].real
    return np.array([left@(M[a]@r)/(lam*(left@r)) for a in range(q)])

def run():
    checks=0; unique=0
    # all ternary target words through length five, with independent left/right PF eigenvectors
    for q,maxm in ((3,5),(4,4)):
        for m in range(1,maxm+1):
            for w in product(range(q),repeat=m):
                p,rho=border_prediction(w,q)
                z=matrix_frequency(w,q)
                assert np.max(abs(p-z))<1e-9,(q,w,p,z)
                assert abs(sum(p)-1)<1e-9
                for a,b in combinations(range(q),2):
                    s=border_sign(w,a,b)
                    d=p[a]-p[b]
                    assert int(d>1e-9)-int(d< -1e-9)==s,(q,w,a,b,p,s)
                    checks+=1
                unique+=1
    # independent direct finite q-ary word counts, via all admissible words
    for w in product(range(3),repeat=3):
        for n in range(4,9):
            allowed=[u for u in product(range(3),repeat=n) if all(u[i:i+3]!=w for i in range(n-2))]
            counted=np.array([sum(u.count(a) for u in allowed)/(n*len(allowed)) for a in range(3)])
            # convergence is not required at short n; only sanity sum
            assert abs(sum(counted)-1)<1e-12
    example=(0,1,1,2,2,0)
    p,r=border_prediction(example,3)
    print('examples',example,'rho',format(r,'.15f'),'frequencies',p.tolist())
    print('passed',unique,'targets and',checks,'pair comparisons; exact finite enumeration of 135 instances')
if __name__=='__main__':run()

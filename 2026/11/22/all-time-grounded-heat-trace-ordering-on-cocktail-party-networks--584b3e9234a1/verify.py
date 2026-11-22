"""Finite reproducibility checks for the cocktail-party grounded heat-trace theorem.
The infinite-dimensional claims follow from the proof, not these samples.
Requires numpy, sympy (for symbolic characteristic-polynomial checks).
"""
import itertools
import math
import numpy as np
import sympy as sp

checks = dict(matrix_spectrum=0, all_orbits=0, all_subsets=0, heat=0, exact_charpoly=0)

def laplacian(m, mu=0.0):
    n=2*m
    adj=np.ones((n,n))-np.eye(n)
    for i in range(m):
        adj[2*i,2*i+1]=adj[2*i+1,2*i]=0
    return (n-2+mu)*np.eye(n)-adj

def expected_eigs(m,k,mu):
    h=2*m-k
    a=mu+2*m-1
    t=h//2
    if h==1:
        return np.array([a-1.])
    if not h%2:
        return np.array(sorted([a-1]*t+[a+1]*(t-1)+[a+1-h]),dtype=float)
    return np.array(sorted([a-1]*t+[a+1]*(t-1)+[a-t-math.sqrt(t*t+1),a-t+math.sqrt(t*t+1)]),dtype=float)

def optimal_count(m,k):
    r=k//2
    if k%2: return 2*(m-r)*math.comb(m,r)
    return math.comb(m,r)

def represent(m, k, r):
    s=k-2*r
    return list(range(2*r))+[2*(r+j) for j in range(s)]

for m in range(2,10):
    for k in range(1,2*m):
        for mu in (0.0,0.3,7.0):
            L=laplacian(m,mu)
            S=represent(m,k,k//2)
            U=[i for i in range(2*m) if i not in S]
            eig=np.linalg.eigvalsh(L[np.ix_(U,U)])
            assert np.allclose(eig,expected_eigs(m,k,mu),atol=1e-9,rtol=1e-9), (m,k,mu,eig)
            checks['matrix_spectrum']+=1
            scores=[]
            for r in range(max(0,k-m),k//2+1):
                if k-r>m: continue
                S=represent(m,k,r)
                U=[i for i in range(2*m) if i not in S]
                v=np.linalg.eigvalsh(L[np.ix_(U,U)])
                for p in (0.5,1.,2.,3.):
                    scores.append((r,p,float(sum(v**-p))))
            for p in (0.5,1.,2.,3.):
                vals=[(r,v) for r,q,v in scores if p==q]
                best=min(v for r,v in vals)
                winners=[r for r,v in vals if abs(v-best)<1e-8*max(1,best)]
                assert winners==[k//2], (m,k,mu,p,vals)
                checks['all_orbits']+=1
            for tm in (0.07,0.6,4.):
                scores=[]
                for r in range(max(0,k-m),k//2+1):
                    if k-r>m:continue
                    S=represent(m,k,r)
                    U=[i for i in range(2*m) if i not in S]
                    v=np.linalg.eigvalsh(L[np.ix_(U,U)])
                    scores.append((r,float(sum(np.exp(-tm*v)))))
                best=min(v for r,v in scores)
                winners=[r for r,v in scores if abs(v-best)<1e-9*max(1e-200,best)]
                assert winners==[k//2], (m,k,mu,tm,scores)
                checks['heat']+=1

for m in range(2,7):
    n=2*m
    L=laplacian(m)
    for k in range(1,n):
        correct=0
        for S in itertools.combinations(range(n),k):
            U=[i for i in range(n) if i not in S]
            eig=np.linalg.eigvalsh(L[np.ix_(U,U)])
            objective=sum(eig**(-1.0))
            ideal_eig=expected_eigs(m,k,0.0)
            bound=sum(ideal_eig**(-1.0))
            assert objective >= bound-1e-8, (m,k,S,objective,bound)
            if abs(objective-bound)<1e-8:
                correct+=1
                pairs=sum((2*i in S and 2*i+1 in S) for i in range(m))
                assert pairs==k//2, (m,k,S)
            checks['all_subsets']+=1
        assert correct==optimal_count(m,k), (m,k,correct,optimal_count(m,k))

z=sp.symbols('z')
for m in range(2,7):
  n=2*m
  for k in range(1,n):
    S=set(represent(m,k,k//2))
    U=[i for i in range(n) if i not in S]
    mat=sp.zeros(n,n)
    for i in range(n):
      mat[i,i]=n-2
      for j in range(n):
        if i!=j and i//2!=j//2:mat[i,j]=-1
    sub=mat.extract(U,U)
    a=n-1
    h=n-k
    t=h//2
    if h==1:
        cp=z-(a-1)
    elif h%2==0:
        cp=(z-(a-1))**t*(z-(a+1))**(t-1)*(z-(a+1-h))
    else:
        cp=(z-(a-1))**t*(z-(a+1))**(t-1)*((z-(a-t))**2-(t*t+1))
    assert sp.expand(sub.charpoly(z).as_expr()-cp)==0,(m,k)
    checks['exact_charpoly']+=1

print('Verification passed',checks,'total',sum(checks.values()))

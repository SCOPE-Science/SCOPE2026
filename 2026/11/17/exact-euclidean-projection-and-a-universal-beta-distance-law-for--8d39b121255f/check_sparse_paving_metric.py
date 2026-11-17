"""Exact small-instance checks and numerical corroboration of Euclidean projection and distance law."""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import random
import numpy as np
from scipy.optimize import minimize


def johnson_stable_sets(n,k):
    subsets=list(combinations(range(n),k))
    # A deterministic high-density greedy family, plus its truncations.
    forbidden=[]
    for h in sorted(subsets, key=lambda s: (sum((i+1)**2 for i in s) % (n+1),s)):
        if all(len(set(h)&set(j)) <= k-2 for j in forbidden):
            forbidden.append(h)
    return [forbidden[:j] for j in sorted(set([1, min(len(forbidden),2), min(len(forbidden),4),len(forbidden)]))]


def eulerian(m,j):
    vals=[1]
    for n in range(2,m+1):
        vals=[(k+1)*(vals[k] if k<len(vals) else 0)+(n-k)*(vals[k-1] if k>0 else 0) for k in range(n)]
    return vals[j]


def projection(x, nonbases, n,k):
    violated=[h for h in nonbases if sum((x[i] for i in h),F(0)) > k-1]
    assert len(violated)<=1
    if not violated: return x, F(0)
    h=violated[0]; hs=set(h)
    t=sum((x[i] for i in h),F(0))-k+1
    y=tuple(x[i]-t/k if i in hs else x[i]+t/(n-k) for i in range(n))
    return y,t


def verify_exact():
    rng=random.Random(1821)
    checks=0; full_checks=0; generated=0
    for n in range(4,10):
      for k in range(2,n-1):
        allbases=list(combinations(range(n),k))
        for nonbases in johnson_stable_sets(n,k):
          generated+=1
          pool=[]
          for _ in range(26):
             denom=rng.randint(7,31)
             picks=[rng.choice(allbases) for _ in range(denom)]
             x=tuple(F(sum(i in a for a in picks),denom) for i in range(n))
             pool.append(x)
          for h in nonbases:
             # Points strictly inside an excised corner for each forbidden vertex.
             p=tuple(F(int(i in h)) for i in range(n))
             u=tuple(F(k,n) for _ in range(n))
             pool.append(tuple(F(3,4)*p[i]+F(1,4)*u[i] for i in range(n)))
             pool.append(p)
          for x in pool:
            y,t=projection(x,nonbases,n,k)
            assert sum(x)==sum(y)==k
            assert all(F(0)<=v<=1 for v in y)
            assert all(sum((y[i] for i in h),F(0))<=k-1 for h in nonbases)
            d2=sum((a-b)**2 for a,b in zip(x,y))
            assert d2==t*t*F(n,k*(n-k)),(n,k,nonbases,x,y,d2,t)
            if t:
                h=next(h for h in nonbases if sum((x[i] for i in h),F(0))>k-1)
                normal=tuple(F(int(i in h),k)-F(int(i not in h),n-k) for i in range(n))
                assert all(x[i]-y[i]==t*normal[i] for i in range(n))
            checks+=1
          E=eulerian(n-1,k-1)
          assert len(nonbases)*comb(n-2,k-1) <= E
          full_checks+=1
    return checks,full_checks,generated


def verify_qp():
    rng=random.Random(1811); good=0; max_err=0.0
    for n in range(4,9):
      for k in range(2,n-1):
       families=johnson_stable_sets(n,k)
       for hs in families[:2]:
        allowed=[b for b in combinations(range(n),k) if b not in hs]
        H=np.array([[int(i in h) for i in range(n)] for h in hs],dtype=float)
        samples=[]
        for _ in range(3):
            picked=rng.choices(list(combinations(range(n),k)),k=10)
            samples.append(np.mean(np.array([[float(i in b) for i in range(n)] for b in picked]),axis=0))
        for h in hs:
            v=np.array([float(i in h) for i in range(n)])
            c=np.ones(n)*k/n
            samples.append(0.83*v+0.17*c)
            samples.append(v)
        for x in samples:
            yf,_=projection(tuple(F(float(t)).limit_denominator(1000000) for t in x),hs,n,k)
            y=np.array([float(t) for t in yf])
            cons=[{'type':'eq','fun':lambda z:sum(z)-k,'jac':lambda z: np.ones(n)}]
            if len(H): cons +=[{'type':'ineq','fun':lambda z,H=H:k-1-H@z,'jac':lambda z,H=H:-H}]
            res=minimize(lambda z:float(np.dot(z-x,z-x)), x0=np.ones(n)*k/n, jac=lambda z:2*(z-x),bounds=[(0,1)]*n,constraints=cons,method='SLSQP',options={'ftol':1e-12,'maxiter':1000})
            assert res.success,(n,k,hs,res.message)
            err=np.linalg.norm(res.x-y)
            assert err < 2e-5,(n,k,hs,err,x,y,res.x)
            max_err=max(max_err,err)
            good+=1
    return good,max_err

if __name__=='__main__':
 a,b,c=verify_exact();d,e=verify_qp()
 print(f'SPARSE_PAVING_METRIC_PASS exact_points={a} families={b} constructed_families={c} qp={d} max_qp_gap={e:.2e} n=4..9')

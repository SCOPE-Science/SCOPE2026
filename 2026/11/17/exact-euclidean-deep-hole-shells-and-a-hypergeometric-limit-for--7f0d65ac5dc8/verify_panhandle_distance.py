"""Exact and numerical checks of hypersimplex-to-panhandle distance formulas.
Requires Python >=3.10; optional SciPy/NumPy for independent optimization.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, isclose


def projected_vertex(n, s, r, subset):
    head = set(range(s)); tail = set(range(s,n))
    t = set(subset); a = t & head; b = t & tail
    j=len(b)
    if j<=1:
        return [F(int(i in t)) for i in range(n)]
    x=[F(0)]*n
    for i in a:x[i]=F(1)
    for i in head-a:x[i]=F(j-1,s-r+j)
    for i in b:x[i]=F(1,j)
    return x


def exact_checker():
    configs=0; vertices=0; missing=0; witnesses=0; shellcases=0
    for n in range(4,11):
      for s in range(3,n):
       for r in range(3,s+1):
        if n-s<2: continue
        bases=[frozenset(t) for t in combinations(range(n),r)
                 if len(set(t)&set(range(s,n)))<=1]
        byj={}; configs+=1
        for subset in map(frozenset,combinations(range(n),r)):
          j=len(subset & set(range(s,n)));vertices+=1
          if j<2:continue
          missing+=1
          p=projected_vertex(n,s,r,subset)
          v=[F(int(i in subset)) for i in range(n)]
          assert all(F(0)<=z<=F(1) for z in p)
          assert sum(p)==r and sum(p[s:])==1
          formula=F((j-1)**2,j)+F((j-1)**2,s-r+j)
          dist=sum((v[i]-p[i])**2 for i in range(n))
          assert dist==formula,(n,s,r,j,dist,formula)
          # Supporting normal: every feasible basis b satisfies <v-p, b-p> <=0.
          normal=[v[i]-p[i] for i in range(n)]
          cc=sum(normal[i]*p[i] for i in range(n))
          for basis in bases:
            assert sum(normal[i] for i in basis)<=cc, (n,s,r,j,basis)
            witnesses+=1
          byj[j]=byj.get(j,0)+1
        for j,count in byj.items():
          assert count==comb(n-s,j)*comb(s,r-j)
          shellcases+=1
        if byj:
          vals={j:F((j-1)**2,j)+F((j-1)**2,s-r+j) for j in byj}
          assert max(vals,key=vals.get)==min(r,n-s)
    return configs,vertices,missing,witnesses,shellcases


def numerical_checker():
    import numpy as np
    from scipy.optimize import minimize
    tests=0; gap=0.
    for n,s,r in [(6,4,3),(7,4,3),(8,5,4),
                   (9,6,4),(10,6,5),(11,7,4),(12,8,6)]:
        for subset in combinations(range(n),r):
            if sum(i>=s for i in subset)<2:continue
            v=np.array([float(i in subset) for i in range(n)])
            p=np.array([float(z) for z in projected_vertex(n,s,r,subset)])
            # Independently solve original QP with box bounds and both affine constraints.
            cons=[{'type':'eq','fun':lambda x,r=r: np.sum(x)-r,'jac':lambda x:np.ones_like(x)},
                  {'type':'ineq','fun':lambda x,s=s:1-np.sum(x[s:]),
                   'jac':lambda x,s=s: np.r_[np.zeros(s),-np.ones(len(x)-s)]}]
            x0=np.r_[np.full(s,(r-1)/s),np.full(n-s,1/(n-s))]
            sol=minimize(lambda x: np.sum((x-v)**2),x0,
                         jac=lambda x:2*(x-v),bounds=[(0,1)]*n,
                         constraints=cons,method='SLSQP',
                         options={'ftol':1.e-12,'maxiter':300})
            assert sol.success,(n,s,r,subset,sol.message)
            newgap=float(np.max(np.abs(sol.x-p)))
            gap=max(gap,newgap)
            assert newgap<2e-5,(n,s,r,subset,newgap)
            tests+=1
    return tests,gap

if __name__=='__main__':
    ex=exact_checker()
    num=numerical_checker()
    print('PANHANDLE_DISTANCE_PASS exact_configs=%d vertices=%d missing=%d supporting_inequalities=%d shell_counts=%d independent_QP=%d max_coordinate_gap=%.3g' % (*ex,*num))

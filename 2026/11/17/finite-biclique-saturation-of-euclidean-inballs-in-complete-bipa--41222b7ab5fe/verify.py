"""Independent finite checks for inscribed Euclidean balls in bipartite forest polytopes.

Standard Python 3, numpy and scipy. Analytical proof is in RESULT.md.
"""
import itertools
import math
import numpy as np
from scipy.optimize import linprog

count = 0

def g(a, b):
    return (a+b-1)/(a*b+math.sqrt(a*b))

def bstar(p):
    return (math.sqrt(p)*(p-1)+math.sqrt((p-1)*(p*p-p+1)))**2

def limit(p):
    return 2*(p-1)*(2*p*p-2*p+1)

def predicted(p,q):
    return min((g(p,b),b) for b in range(p,q+1))

def all_biclique_normals(p,q):
    for A in range(1,1<<p):
        a=A.bit_count()
        for B in range(1,1<<q):
            b=B.bit_count()
            normal=np.zeros(p*q)
            for i in range(p):
                for j in range(q):
                    if (A>>i)&1 and (B>>j)&1:
                        normal[q*i+j]=1.
            yield a,b,normal

for p in range(2,7):
    B=limit(p)
    b0=bstar(p)
    assert B-1<b0<B,(p,B,b0)
    count+=1
    for q in range(p,min(p+16,29)):
        oracle=min((g(a,b),a,b) for a in range(1,p+1) for b in range(1,q+1))
        fmin,bopt=predicted(p,q)
        assert abs(oracle[0]-fmin)<1e-13,(p,q,oracle,(fmin,bopt))
        assert abs(fmin-min(g(p,b) for b in range(p,min(q,B)+1)))<1e-13
        assert fmin>0
        count+=3
    if B<=1000:
        q=B+13
        v=min(g(p,b) for b in range(p,q+1))
        assert abs(v-min(g(p,B-1),g(p,B)))<1e-14
        count+=1

for p in range(2,5):
    for q in range(p,7):
        m=p*q
        fac=list(all_biclique_normals(p,q))
        A=[]; rhs=[]
        # x_e>=r => -x_e +r <=0
        for i in range(m):
            row=np.zeros(m+1); row[i]=-1.;row[-1]=1.
            A.append(row); rhs.append(0.)
        # x(E(U))+sqrt(ab)r <= a+b-1
        for a,b,v in fac:
            A.append(np.r_[v,math.sqrt(a*b)]);rhs.append(a+b-1.)
        c=np.zeros(m+1);c[-1]=-1.
        sol=linprog(c,A_ub=A,b_ub=rhs,bounds=[(None,None)]*m+[(0,None)],method='highs')
        assert sol.success,(p,q,sol.message)
        predicted_r,bopt=predicted(p,q)
        assert abs(sol.x[-1]-predicted_r)<3e-8,(p,q,sol.x[-1],predicted_r)
        assert np.max(np.abs(sol.x[:-1]-predicted_r))<3e-7,(p,q,sol.x)
        for a,b,v in fac:
            slack=(a+b-1-v@sol.x[:-1])/np.sqrt(a*b)
            assert slack+3e-7>=predicted_r
        count+=3+len(fac)

# Special exact two-row saturation comparison, independent of derivatives.
assert 2+20*math.sqrt(5)>33*math.sqrt(2)
for q in range(2,45):
    opt,b=predicted(2,q)
    assert b==min(q,10),(q,b)
    count+=1
print(f"PASS: {count} grouped mathematical checks; complete facet LP for 12 cases")

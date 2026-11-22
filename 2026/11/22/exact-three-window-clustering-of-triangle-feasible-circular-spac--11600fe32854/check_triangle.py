"""Independent exact moment and reproducible numerical checks for cyclic triangle-feasible spacings.
No external packages are required. Run: python check_triangle.py
"""
from fractions import Fraction as F
from math import comb
from random import Random

def wedge_integral(a,b):
    """Integral of exp(-a*x-b*y) for 0<y<x<infinity, a>0, a+b>0."""
    assert a>0 and a+b>0
    return F(1,a*(a+b))

# E[exp(-Y-Z)] for independent Exp(1) variables.
p = F(1) - 3*F(1,4)
# Shared-two overlap, condition on a,b; q=exp(-abs(a-b))-exp(-a-b).
joint1 = 2*(wedge_integral(3,-1)-2*wedge_integral(3,1)+wedge_integral(3,3))
# Shared-one overlap, condition on b; g(b)=b exp(-b).
joint2 = F(2,3**3)
assert (p,joint1,joint2) == (F(1,4),F(1,9),F(2,27))
v = p*(1-p)
c1 = joint1-p*p
c2 = joint2-p*p
assert (v,c1,c2)==(F(3,16), F(7,144), F(5,432))
assert c1/v == F(7,27) and c2/v == F(5,81)
sigma2 = v + 2*c1+2*c2
assert sigma2 == F(133,432)
assert sigma2/v == F(133,81)
assert 9*v == F(27,16)
assert 4*v+12*c1 == F(4,3)
for n in range(5,100):
    assert n*v + 2*n*c1 + 2*n*c2 == n*sigma2

# Replicable finite-sample simulation. This is a diagnostic, not the CLT proof.
rng = Random(407221)
for n, trials in [(3,50000),(4,50000),(5,50000),(7,50000),(20,50000)]:
    s1 = s2 = 0
    for _ in range(trials):
        x = [rng.expovariate(1.0) for j in range(n)]
        count = sum(int(2*max(x[i],x[(i+1)%n],x[(i+2)%n]) < x[i]+x[(i+1)%n]+x[(i+2)%n]) for i in range(n))
        s1 += count
        s2 += count*count
    mean = s1/trials
    var = s2/trials-mean**2
    target = F(27,16) if n==3 else F(4,3) if n==4 else n*sigma2
    assert abs(mean-n/4) < 0.065, (n,mean)
    assert abs(var-float(target)) < 0.25, (n,var,target)
    print('n=%d, simulated mean=%.5f, exact mean=%.5f, simulated var=%.5f, exact var=%.5f' %(n,mean,n/4,var,float(target)))
print('Exact rational overlap, covariance, boundary, and variance checks: PASS')

# Third joint moment of three successive (non-wrapping) triangle windows.
# Integrate over the independent central triple (B,C,D), conditional on
# its two independent outer neighbors. For each ordering of (B,C,D), the
# triangle domain is 0<u<v<w<u+v. Each expanded exponential term has
# an exact integral 1/[(beta+gamma)(alpha+beta+gamma)(alpha+beta+2gamma)].
from itertools import permutations
order_terms={}
for order in permutations(('b','c','d')):
    bases=({'b':1,'c':1,'d':1},{'b':1,'c':2,'d':2},
           {'b':2,'c':2,'d':1},{'b':2,'c':3,'d':2})
    vals=[]
    for k,coeffs in enumerate(bases):
        coeffs=coeffs.copy()
        for left,right,active in [('b','c',k in (0,1)),('c','d',k in (0,2))]:
            if active:
                high=max((left,right),key=lambda x:order.index(x))
                low=left if high==right else right
                coeffs[high]+=1
                coeffs[low]-=1
        alpha,beta,gamma=(coeffs[x] for x in order)
        vals.append(F(1,(beta+gamma)*(alpha+beta+gamma)*(alpha+beta+2*gamma)))
    order_terms[order]=vals[0]-vals[1]-vals[2]+vals[3]
assert order_terms[('b','c','d')]==order_terms[('d','c','b')]==F(16,1575)
assert order_terms[('b','d','c')]==order_terms[('d','b','c')]==F(38,4725)
assert order_terms[('c','b','d')]==order_terms[('c','d','b')]==F(2,315)
triple=sum(order_terms.values(),F(0))
assert triple==F(232,4725)
assert triple/joint1==F(232,525)

rng=Random(535)
count=0
for j in range(200000):
    x=[rng.expovariate(1) for k in range(5)]
    count+=all(2*max(x[i:i+3])<sum(x[i:i+3]) for i in range(3))
assert abs(count/200000-float(triple))<0.002
print('Exact six-cone third-order joint moment and independent Monte Carlo: PASS')

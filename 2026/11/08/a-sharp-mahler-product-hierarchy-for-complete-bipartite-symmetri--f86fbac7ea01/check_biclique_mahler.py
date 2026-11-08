# Exact rational and geometric checks for the complete-bipartite Mahler product.
# Requires Python 3, NumPy and SciPy.
from fractions import Fraction as F
from math import comb, factorial, sqrt
import math

def A(n):
    # Coefficients of the volume-slice polynomial in the ordinary power basis
    d=[F(0) for _ in range(n+1)]
    for i in range(n+1):
        for k in range(n-i+1):
            d[i+k]+=F(comb(n,i)**2*comb(n-i,k)*(-1)**k)
    return d

def integral_B(p,q):
    a=A(p-1); b=A(q-1)
    return F(p*q,2**(p+q-2))*sum((a[i]*b[j]/(i+j+1) for i in range(len(a)) for j in range(len(b))),F(0))

def hstar_R(p,q):
    return F(factorial(p)*factorial(q),factorial(p+q-1))*sum((F(comb(p-1,i)*comb(q-1,i)*comb(2*i,i),4**i) for i in range(min(p,q))),F(0))

for p in range(1,13):
 for q in range(1,13):
    a=integral_B(p,q); b=hstar_R(p,q)
    assert a==b,(p,q,a,b)
    if min(p,q)<=2: assert a==1
    if min(p,q)>=3: assert a>1
    if p>=2 and q>=3: assert integral_B(p+1,q)>a
print('exact_integral_hstar_and_monotonicity_144_pairs PASSED')

from scipy.spatial import ConvexHull
from scipy.linalg import null_space
import numpy as np
for p,q in [(1,2),(1,3),(2,2),(2,3),(3,2),(3,3),(2,4)]:
 n=p+q;H=null_space(np.ones((1,n)))
 points=[]
 for i in range(p):
  for j in range(p,n):
   u=np.eye(n)[i]-np.eye(n)[j]
   points.extend([u@H,-u@H])
 points=np.array(points)
 hull=ConvexHull(points)
 polar_vertices=np.array([-row[:-1]/row[-1] for row in hull.equations])
 polar=ConvexHull(polar_vertices)
 predicted_polar=2**(n-1)*factorial(p)*factorial(q)/(factorial(n-1)*sqrt(n))
 predicted_product=float(hstar_R(p,q))*4**(n-1)/factorial(n-1)
 assert math.isclose(polar.volume,predicted_polar,rel_tol=1e-8),(p,q,polar.volume,predicted_polar)
 assert math.isclose(polar.volume*hull.volume,predicted_product,rel_tol=1e-8),(p,q,polar.volume*hull.volume,predicted_product)
 print('hull',p,q,'P',hull.volume,'polar',polar.volume,'ratio',float(hstar_R(p,q)))
print('CONVEX_HULL_CHECKS_PASSED 7')

# Independently verify the central-term identity as a polynomial identity.
for n in range(0,16):
    right=[F(0) for _ in range(n+1)]
    for k in range(n//2+1):
        factor=comb(n,2*k)*comb(2*k,k)
        for j in range(k+1):
            right[k+j]+=F(factor*comb(k,j)*(-1)**j)
    assert right==A(n),(n,right,A(n))

# Exact mixture-of-order-statistics variance identity.
for p in range(1,31):
    n=p-1
    e2=sum((F(comb(n,i),2**n)*F((i+1)*(i+2),(p+1)*(p+2)) for i in range(p)),F(0))
    assert e2-F(1,4)==F(p,2*(p+1)*(p+2)),p
print('CONSTANT_TERM_AND_ORDER_STATISTIC_MOMENTS_PASSED 16 30')

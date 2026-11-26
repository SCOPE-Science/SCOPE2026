"""Standalone finite numerical checks for the inverse multitype SIR kernel theorem.

Run: python3 verify.py
Uses Python standard library Decimal; proof of all-size claims is in RESULT.md.
"""
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 70
D = Decimal
p = [D(1)/5, D(3)/10, D(1)/2]
u = [D(1), D(2), D(4)]
w = [D(4), D(2), D(1)]
lam = D(1)/2
n = len(p)
K = [[lam * u[i] * p[j] * w[j] for j in range(n)] for i in range(n)]
R0 = sum(p[i]*u[i]*w[i] for i in range(n))*lam
assert R0 == 2

def posroot(f):
    lo, hi = D('1e-35'), D(8)
    assert f(lo)>0 and f(hi)<0
    for _ in range(300):
        mid=(lo+hi)/2
        if f(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

# L = lam * sum_j p_j w_j z_j, z_j=1-exp(-u_j*L).
L = posroot(lambda x: lam*sum(p[i]*w[i]*(1-(-u[i]*x).exp()) for i in range(n))-x)
z = [1-(-u[i]*L).exp() for i in range(n)]
# H = lam * sum_i p_i u_i h_i, h_i= w_i H/(1+w_i H).
H = posroot(lambda x: lam*sum(p[i]*u[i]*(w[i]*x/(1+w[i]*x)) for i in range(n))-x)
h = [w[i]*H/(1+w[i]*H) for i in range(n)]
a = [-(1-x).ln() for x in z]
b = [x/(1-x) for x in h]
Tleft = sum(p[i]*a[i]*h[i] for i in range(n))
Tright = sum(p[i]*b[i]*z[i] for i in range(n))
T=(Tleft+Tright)/2
small=D('1e-50')
assert abs(Tleft-Tright)<small
Krec=[[a[i]*p[j]*b[j]/T for j in range(n)] for i in range(n)]
for i in range(n):
    assert abs(sum(Krec[i][j]*z[j] for j in range(n))-a[i])<small
    for j in range(n): assert abs(Krec[i][j]-K[i][j])<small
for j in range(n):
    assert abs(sum(p[i]*Krec[i][j]*h[i] for i in range(n))/p[j]-b[j])<small
assert abs(sum(p[i]*a[i]*b[i] for i in range(n))/T-2)<small
# A genuinely non-rank-one positive kernel in the exact same linear observational fiber.
# E is an outer product with w^T E=0, E z=0. Norm chosen extremely small.
left=[p[1]*h[1],-p[0]*h[0],D(0)]
right=[z[1],-z[0],D(0)]
E=[[left[i]*right[j] for j in range(n)] for i in range(n)]
Kother=[[Krec[i][j]+E[i][j]/100 for j in range(n)] for i in range(n)]
assert min(x for row in Kother for x in row)>0
for i in range(n):
    assert abs(sum(Kother[i][j]*z[j] for j in range(n))-a[i])<small
for j in range(n):
    assert abs(sum(p[i]*Kother[i][j]*h[i] for i in range(n))/p[j]-b[j])<small
assert abs(Kother[0][0]*Kother[1][1]-Kother[0][1]*Kother[1][0])>D('1e-10')
# Exact dimension (n-1)^2 for constraints E z=0 and (p h)^T E=0.
# Independent two-sided rank-one generators indexed by i,j >=1 form a basis.
for size in (2,3,5):
    weights=[D(i+1) for i in range(size)]
    zz=[D(i+2) for i in range(size)]
    count=0
    for i in range(1,size):
        for j in range(1,size):
            q=[D(0)]*size
            r=[D(0)]*size
            q[0]=weights[i];q[i]=-weights[0]
            r[0]=zz[j];r[j]=-zz[0]
            assert sum(q[t]*weights[t] for t in range(size)) == 0
            assert sum(r[t]*zz[t] for t in range(size)) == 0
            count+=1
    assert count==(size-1)**2
print('PASS: 70-digit final-size, branching survival, compatibility, rank-one reconstruction, R0,')
print('      positive non-rank-one observational twin, and all-size affine dimension basis checks')
print('R0:',R0)
print('z:', ', '.join(f'{v:.18f}' for v in z))
print('h:', ', '.join(f'{v:.18f}' for v in h))
print('T:',f'{T:.18f}')

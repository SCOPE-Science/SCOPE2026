from fractions import Fraction as F

def U(k,t):
    if k == -1:
        return F(0)
    if k == 0:
        return F(1)
    um1, u0 = F(0), F(1)
    for _ in range(k):
        um1, u0 = u0, 2*t*u0-um1
    return u0

def modal_errors(q,t,K):
    e0 = F(-1)
    e1 = q*q - 2*q*t
    out=[e0,e1]
    for _ in range(1,K):
        out.append(2*q*t*out[-1]-q*q*out[-2])
    return out[:K+1]

# Exact recurrence/Chebyshev identity checks.
for q in [F(1,5),F(1,3),F(1,2),F(3,5)]:
    for t in [F(-1),F(-1,2),F(0),F(1,2),F(1)]:
        E=modal_errors(q,t,10)
        for k,e in enumerate(E):
            rhs = -q**k*(U(k,t)-q*U(k-1,t))
            assert e == rhs

# The simple majorant used in the proof is <=1 for k>=2 at q=1/2.
for k in range(2,100):
    assert F(3*k+2, 2**(k+1)) <= 1

# Boundary kappa=9: mu=1, L=9, q=1/2, alpha=1/4, beta=1/4.
mu,L = F(1),F(9)
q=F(1,2); alpha=F(1,4); beta=F(1,4)
x0=F(0); xm1=F(0); b=F(1)
x1=x0-alpha*(L*x0-b)+beta*(x0-xm1)
x2=x1-alpha*(L*x1-b)+beta*(x1-x0)
assert x1 == F(1,4)
assert x2 == 0
assert (1+q)**2*(1-2*q) == 0

# Strict failure kappa=16: mu=1, L=16, q=3/5.
L=F(16); q=F(3,5); alpha=F(4,25); beta=F(9,25)
x0=F(0); xm1=F(0)
x1=x0-alpha*(L*x0-b)+beta*(x0-xm1)
x2=x1-alpha*(L*x1-b)+beta*(x1-x0)
xstar=F(1,16)
assert x1 == F(4,25)
assert x2 == F(-4,125)
assert x2/xstar == F(-64,125)
assert (1+q)**2*(1-2*q) == F(-64,125)

print("VERIFY_OK")

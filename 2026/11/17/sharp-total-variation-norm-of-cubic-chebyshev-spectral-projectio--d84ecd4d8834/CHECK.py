"""Exact certificate for the cubic Chebyshev projection variation norm.
Standard-library Python 3 only. Run: python CHECK.py
"""
from fractions import Fraction as F
from math import isqrt, pi, sqrt

# Polynomials in increasing degree, over exact rationals.
def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]: a.pop()
    return a

def add(a,b):
    return trim([ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                  for i in range(max(len(a),len(b)))])

def neg(a): return [-x for x in a]
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)

def power(a,n):
    r=[F(1)]
    for _ in range(n): r=mul(r,a)
    return r

def der(a):return trim([i*a[i] for i in range(1,len(a))] or [0])

def evaluate(a,x):
    s=F(0)
    for v in reversed(a): s=s*x+v
    return s

def rem(a,b):
    a=trim(a);b=trim(b)
    assert b[-1]
    while len(a)>=len(b) and any(a):
        v=a[-1]/b[-1]; j=len(a)-len(b)
        for i in range(len(b)):a[j+i]-=v*b[i]
        a=trim(a)
    return a

def sturm_variations(a,x):
    chain=[trim(a),der(a)]
    while any(chain[-1]):
        r=neg(rem(chain[-2],chain[-1]))
        if not any(r):break
        chain.append(r)
    signs=[]
    for q in chain:
        value=evaluate(q,x)
        if value: signs.append(1 if value>0 else -1)
    return sum(x!=y for x,y in zip(signs,signs[1:])),signs

# Radical derivative stationarity, after squaring:
# ((1-2u)(4u-1)^3)^2 - (16u^2-11u+2)(64u^3-80u^2+24u-1)^2 = -P(u).
u1=[F(1),F(-2)]
t=[F(-1),F(4)]
J=[F(2),F(-11),F(16)]
R=[F(-1),F(24),F(-80),F(64)]
P=[F(1),F(-79),F(1676),F(-14464),F(64448),F(-161536),F(228352),F(-167936),F(49152)]
assert add(power(mul(u1,power(t,3)),2),neg(mul(J,power(R,2))))==neg(P)
lo,hi=sturm_variations(P,F(4,9)),sturm_variations(P,F(1))
assert lo[0]==3 and hi[0]==2
assert sturm_variations(P,F(692,1000))[0] == 3
assert sturm_variations(P,F(693,1000))[0] == 2
# Unsquared stationary expression is positive at u=1/2 and negative at u=1:
# (1-2u)(4u-1)^3 - sqrt(J(u))*R(u); its values are 1/sqrt(2), -27-7sqrt(7).
assert evaluate(R,F(1,2))==-1 and evaluate(J,F(1,2))==F(1,2)
assert evaluate(R,F(1))==7 and evaluate(J,F(1))==7
print('EXACT_STURM_UNIQUENESS_AND_ROOT_ISOLATION_PASS',lo[0],hi[0])

# On c in [0,2/3], H(c)=sqrt(1-c^2)*int_{-1}^1 |Q_c(x)| dx.
# Midpoint integration for a quadratic with up to two real roots has error <=24/M^2.
# |H'(c)| < 80. A c-grid of spacing 1/N requires a 40/N allowance.
# sqrt upper endpoints are certified by integer square roots, not floats.
N=12000; M=128; SCALE=10**8
max_h=F(0);where=None
NN=N*N
for k in range(0,8001):
    kk=k*k
    A=16*kk-4*NN
    B=4*k*N
    C=2*NN-4*kk
    qsum=0
    for j in range(M):
        x=2*j+1-M
        qsum+=abs(A*x*x + B*x*M + C*M*M)
    s_upper=isqrt(((NN-kk)*SCALE*SCALE)//NN)+1
    value=(F(s_upper,SCALE)*(F(2*qsum,NN*M**3)+F(24,M*M)) + F(40,N))
    if value>max_h: max_h,where=value,k
assert max_h < F(49,20), (max_h,where)
print('EXACT_MIDPOINT_GRID_CERTIFICATE_PASS',float(max_h),where)

# At c=5/6, H(c)=sqrt(11)*(673sqrt(673)+44032)/82944.
# Provable lower rational square-root bounds are sqrt(11)>3.316,
# sqrt(673)>25.94, each by squaring.
assert F(3316,1000)**2 < 11
assert F(2594,100)**2 < 673
lower=F(3316,1000)*(673*F(2594,100)+44032)/82944
assert lower>F(49,20)
print('EXACT_GLOBAL_GAP_CERTIFICATE_PASS',float(lower))

# Numerical reporting only; no part of the exact certificate depends on these floats.
from decimal import Decimal, localcontext
with localcontext() as ctx:
    ctx.prec=65
    def Pval(z):
        v=Decimal(0)
        for coef in reversed(P):v=v*z+Decimal(coef.numerator)
        return v
    a,b=Decimal('0.692'),Decimal('0.693')
    for _ in range(220):
        m=(a+b)/2
        if Pval(a)*Pval(m)<=0:b=m
        else:a=m
    u=(a+b)/2
    j=16*u*u-11*u+2
    H=Decimal(4)/3*(1-u).sqrt()*(1+2*u+j*j.sqrt()/(4*u-1)**2)
    K=2*float(H)/pi
    assert 1.56534<K<1.56535
    print('NUMERICAL_ROOT',str(u)[:44])
    print('NUMERICAL_SHARP_BV_COEFFICIENT',format(K,'.15f'))
print('ALL_CERTIFICATES_PASS')

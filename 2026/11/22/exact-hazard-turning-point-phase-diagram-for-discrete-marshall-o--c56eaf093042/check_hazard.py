"""Standalone exact-rational enclosure and numerical consistency checks.
Run: python3 check_hazard.py. No nonstandard dependencies.
"""
from fractions import Fraction as F
from math import factorial, exp, log, sqrt, isclose

def sum_exp_neg_half(N):
    return sum((F(-1, 2) ** k) / factorial(k) for k in range(N+1))

# Alternating Taylor series: lower (odd order), upper (even order).
QLOW, QHIGH = sum_exp_neg_half(25), sum_exp_neg_half(24)
assert 0 < QLOW < QHIGH < 1

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def neg(a): return (-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    v=[x*y for x in a for y in b]
    return (min(v),max(v))
def div(a,b):
    assert b[0]*b[1]>0
    inv=(1/b[1],1/b[0])
    return mul(a,inv)
def exact(x):return (F(x),F(x))
def power(a,n):
    assert n>=0
    y=exact(1)
    for _ in range(n):y=mul(y,a)
    return y
q=(QLOW,QHIGH);t=F(1,2);c=F(1,2)

def U(n):return mul(power(q,n),exact(1+n*t))
def E_D(n):
    a,b,d=U(n),U(n+1),U(n+2)
    D=sub(mul(b,b),mul(a,d))
    E=mul(b,sub(mul(b,add(a,d)),mul(exact(2),mul(a,d))))
    return E,D
signs=[]
for n in range(6):
    E,D=E_D(n)
    assert E[0]>0 and D[0]>0
    Delta=sub(mul(exact(c),E),D)
    assert Delta[0]>0 or Delta[1]<0,(n,Delta)
    signs.append('decrease' if Delta[0]>0 else 'increase')
assert signs==['increase','increase','increase','decrease','decrease','increase'],signs

# Independently compare consecutive conventional hazard values for the same case.
def direct_h(n,t,gamma):
    u=lambda m:(1+m*t)*exp(-m*t)
    S=lambda m:gamma*u(m)/(1-(1-gamma)*u(m))
    return 1-S(n+1)/S(n)
for n,sgn in enumerate(signs):
    a,b=direct_h(n,.5,.5),direct_h(n+1,.5,.5)
    assert (b<a)==(sgn=='decrease')

# Algebraic identity for the explicit threshold and numerical sign agreement.
for t1 in (.01,.05,.1,.25,.5,1.,2.,3.,5.):
    q1=exp(-t1)
    for n in range(0,30):
        a=q1**n*(1+n*t1);b=q1**(n+1)*(1+(n+1)*t1);d=q1**(n+2)*(1+(n+2)*t1)
        D=b*b-a*d;E=b*(b*(a+d)-2*a*d)
        # floating cancellation; this assertion is not used in place of proof
        if D<=0 or E<=0:continue
        z=n*t1;v=1+z; w=v+t1; y=v+2*t1
        P=w*(w*(v/q1+q1*y)-2*v*y)
        assert isclose(D/E,exp(z+t1)*t1*t1/P,rel_tol=1e-7,abs_tol=1e-9)

# Dense random-free grid: at most one discrete decreasing-hazard block.
for t1 in (.03,.1,.25,.5,.7,1.,2.,3.,5.):
    for gamma in (.01,.05,.1,.2,.3,.45,.5,.6,.8,1.,2.):
        # evaluate via r_n explicit formula, avoiding survival underflow
        cc=1-gamma
        if cc<=0:continue
        n_max=min(1200,int(10/t1)+30)
        active=[]
        for n in range(n_max):
            z=n*t1;v=1+z;w=v+t1;y=v+2*t1
            P=w*(w*(exp(t1)*v+exp(-t1)*y)-2*v*y)
            if P<=0:continue
            # compare with logarithms to avoid e^z overflow
            active.append((log(cc)+log(P)-(z+t1)-2*log(t1))>0)
        k=[i for i,x in enumerate(active) if x]
        assert not k or len(k)==k[-1]-k[0]+1,(t1,gamma,k)

# Universal high-resolution critical constant.
z=1+sqrt(2)
gcrit=1-exp(z)/((1+z)*(1+z*z))
assert .5204<gcrit<.5205
print('PASS exact q interval width:',float(QHIGH-QLOW))
print('PASS six exact-rational signs:',', '.join(signs))
print('PASS consistency checks and consecutive-block diagnostics')
print('universal high-resolution gamma limit:',format(gcrit,'.16f'))

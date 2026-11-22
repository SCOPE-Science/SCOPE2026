#!/usr/bin/env python3
"""Reproduce exact exponential-polynomial identities and numerical thresholds.
Only Python's standard library is used. Run: python3 check.py
"""
from decimal import Decimal, localcontext

# Exact polynomials: dictionary exponent -> integer coefficient.
def add(a, b):
    z = a.copy()
    for k,v in b.items():
        z[k] = z.get(k,0)+v
    return {k:v for k,v in z.items() if v}
def neg(a): return {k:-v for k,v in a.items()}
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    z={}
    for i,u in a.items():
        for j,v in b.items():z[i+j]=z.get(i+j,0)+u*v
    return {k:v for k,v in z.items() if v}
def derivative(a):return {k-1:k*v for k,v in a.items() if k>0 and v}
def sc(a,k):return {p:k*v for p,v in a.items() if k*v}
# Exponential polynomials: power of exp(z) -> polynomial in z.
def ea(a,b):
    t=a.copy()
    for k,v in b.items():t[k]=add(t.get(k,{}),v)
    return {k:v for k,v in t.items() if v}
def en(a):return {k:neg(v) for k,v in a.items()}
def es(a,k):return {i:sc(v,k) for i,v in a.items() if sc(v,k)}
def em(a,b):
    z={}
    for i,u in a.items():
        for j,v in b.items():z[i+j]=add(z.get(i+j,{}),mul(u,v))
    return {k:v for k,v in z.items() if v}
def ed(a):return {k:add(derivative(v),sc(v,k)) for k,v in a.items() if add(derivative(v),sc(v,k))}

# Derivatives of A(s)=(exp(sqrt(s))-1)/s, at s=z*z.
B0={1:{0:-2,1:1},0:{0:2}}
H={1:{0:8,1:-5,2:1},0:{0:-8}}
Z={0:{1:1}}
assert ea(em(Z,ed(B0)),en(es(B0,4))) == H, 'chain-rule A second derivative'
# B(z)=-2 A'(z*z)/A''(z*z) = N(z)/H(z).
N=em({0:{2:-4}},B0)
G={2:{3:1,2:-10,1:34,0:-32},1:{3:-2,2:2,1:-34,0:64},0:{0:-32}}
lhs=ea(em(ed(N),H),en(em(N,ed(H))))
rhs=em({0:{1:-4}},G)
assert lhs==rhs, 'numerator of B derivative'
assert ea(N,en(em({0:{2:1}},H))) == {1:{3:1,4:-1}}, 'B-z^2 sign identity'

# G has a unique positive zero: g_2<0, g_3=0, all g_n>0 for n>=4.
def gn(n):
    p=n**3-23*n*n+158*n-256
    q=-16*n**3+64*n*n-320*n+512
    a=2**n*p+q
    assert a%8==0
    return a//8 - (32 if n==0 else 0)
assert [gn(n) for n in range(4)] == [0,0,-12,0]
assert [gn(n) for n in range(4,11)] == [48,150,320,546,768,942,1536]
# The infinite case n>=11 is proved in RESULT.md via P'(n)>0 and 30*2^n>16*n^3+320*n.
for n in range(11,501):
    assert n**3-23*n*n+158*n-256 >= 30
    assert 30*2**n > 16*n**3+320*n
    assert gn(n)>0

with localcontext() as ctx:
    ctx.prec=72
    one=Decimal(1); two=Decimal(2); four=Decimal(4)
    def E(z): return z.exp()
    def h(z):return (z*z-5*z+8)*E(z)-8
    def Gv(z):return (z**3-10*z*z+34*z-32)*E(z)**2 +(-2*z**3+2*z*z-34*z+64)*E(z)-32
    def B(z):return -four*z*z*((z-2)*E(z)+2)/h(z)
    def bracket_root(f,a,b,iterations=270):
        assert f(a)*f(b)<0, (a,b,f(a),f(b))
        left,right=a,b
        sl=f(left)>0
        for _ in range(iterations):
            mid=(left+right)/2
            if mid==left or mid==right: break
            if (f(mid)>0)==sl:left=mid
            else:right=mid
        return (left+right)/2
    zc=bracket_root(Gv,Decimal('1.1'),Decimal('1.3'))
    zs=bracket_root(lambda z:(z-2)*E(z)+2,Decimal('1.5'),Decimal('1.8'))
    C=B(zc)
    rho_star=zc*zc-C
    assert 1<zc<zs<2
    assert 1<C<zc*zc
    assert abs(zc-Decimal('1.179266071363136013470355227284380135'))<Decimal('1e-32')
    assert abs(C-Decimal('1.106428220936437384832986182994696536'))<Decimal('1e-32')
    assert abs(rho_star-Decimal('0.284240246131807615986459348992371400'))<Decimal('1e-32')

    mu=Decimal('1.05')
    zl=bracket_root(lambda z:B(z)-mu,mu.sqrt(),zc)
    zu=bracket_root(lambda z:B(z)-mu,zc,zs)
    rl=zl*zl-mu
    ru=zu*zu-mu
    assert abs(rl-Decimal('0.0587451332319848276'))<Decimal('1e-18')
    assert abs(ru-Decimal('0.61152196303662872'))<Decimal('1e-17')
    def variance_and_mean(mu,r):
        z=(mu+r).sqrt()
        ee=E(z)
        aa=(ee-1)/(z*z)
        ap=((z-2)*ee+2)/(2*z**4)
        app=h(z)/(4*z**6)
        mean=(aa+mu*ap)/(1+mu*aa)
        var=mean*mean-(2*ap+mu*app)/(1+mu*aa)
        mean_original=(r*(ee-1)+mu*z*ee/2)/((mu+r)*(mu*ee+r))
        var_original=(ee*ee*((mu+r)**2+(z-4)*(mu/2)**2)-r*r -r*ee*(r*z+(z*z+3*z+8)*mu/4))/((mu+r)**2*(mu*ee+r)**2)
        assert abs(mean-mean_original)<Decimal('1e-58')
        assert abs(var-var_original)<Decimal('1e-58')
        return mean,var
    for mu_test,r_test in [
        ('0.1','0'),('0.8','0.5'),('1','0'),('1.01','0.1'),
        ('1.05','0'),('1.05','0.1'),('1.05','0.3'),('1.05','0.9'),
        ('1.1','0.2'),('1.12','0.3'),('2','3'),('10','8')]:
        mu1=Decimal(mu_test);r1=Decimal(r_test)
        m,v=variance_and_mean(mu1,r1)
        assert m>0 and v>0
        z=(mu1+r1).sqrt()
        sg1=(v-m*m)>0
        sg2=(B(z)-mu1)>0
        assert sg1==sg2
    for r,sgn in [('0',-1),('0.1',1),('0.3',1),('0.9',-1)]:
        m,v=variance_and_mean(mu,Decimal(r))
        assert ((v-m*m)>0)==(sgn==1)
    print('PASS: exact identities, infinite sign proof hypotheses, and independent original moment formulas')
    print('z_critical=',zc)
    print('mortality_threshold=',C)
    print('tangent_reset_rate=',rho_star)
    print('example_mortality=1.05 crossings=',rl,ru)

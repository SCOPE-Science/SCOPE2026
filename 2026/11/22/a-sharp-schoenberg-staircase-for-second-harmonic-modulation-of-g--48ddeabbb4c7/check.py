"""Independent finite and symbolic cross-checks for a spherical kernel criterion.
Run: python check.py   (requires sympy and mpmath).
The all-degree proof is analytic in RESULT.md; sampled tests are corroboration only.
"""
import math
import sympy as s
import mpmath as mp

n,z=s.symbols('n z', positive=True)
u=(n+1)*(n+2)/((2*n+1)*(2*n+3))
v=(n+1)**2/((2*n+1)*(2*n+3))+n**2/((2*n+1)*(2*n-1))
w=n*(n-1)/((2*n+1)*(2*n-1))
up=(n*n+z)/((n+3)**2+z)
down=((n+1)**2+z)/((n-2)**2+z)
R=s.factor(2*(u*up+v+w*down)-1)
expected=(n**4+2*n**3+2*n*n*z+7*n*n+2*n*z+6*n+z*z+z-12)/((n*n-4*n+z+4)*(n*n+6*n+z+9))
assert s.cancel(R-expected)==0
assert s.cancel(R-1-6*(3*n*n+3*n-2*z-8)/((n*n-4*n+z+4)*(n*n+6*n+z+9)))==0
P=-3*n**4-12*n**3+(4*z+1)*n*n+(8*z+26)*n+7*z*z+35*z+28
expr=s.factor(R.subs(n,n+1)-R)
den=(n*n-4*n+z+4)*(n*n-2*n+z+1)*(n*n+6*n+z+9)*(n*n+8*n+z+16)
assert s.factor(expr-12*(n+1)*P/den)==0
assert s.factor(R.subs(n,0)-(z-3)/(z+9))==0
assert s.factor(R.subs(n,1)-(z+4)/(z+16))==0
assert s.factor(R.subs(n,1)-R.subs(n,0))==84/((z+9)*(z+16))
assert s.factor(R.subs({n:3,z:1})-s.Rational(115,37))==0
for k in range(2,21):
    B=4*k*k+8*k+35
    C=-3*k**4-12*k**3+k*k+26*k+28
    zk=(-B+math.sqrt(B*B-28*C))/14
    assert zk>0
    for q in (.995,1.005):
        a2=zk*q
        rr=lambda j:float(R.subs({n:j,z:a2}))
        assert (rr(k+1)>rr(k)) == (q>1)
mp.mp.dps=40
for a in (mp.mpf('0.2'),mp.mpf('1'),mp.mpf('1.8'),mp.mpf('3.7')):
    vals=[]
    for k in range(0,10):
        values=mp.quad(lambda t:mp.exp(-a*t)*mp.legendre(k,mp.cos(t))*mp.sin(t),[0,mp.pi])
        vals.append(values)
    for k in range(0,8):
        predicted=vals[k]*(a*a+k*k)/(a*a+(k+3)**2)
        assert abs(vals[k+2]-predicted)<mp.mpf('1e-30')
    for k in range(0,8):
        direct=mp.quad(lambda t:mp.exp(-a*t)*mp.cos(2*t)*mp.legendre(k,mp.cos(t))*mp.sin(t),[0,mp.pi])
        predicted=mp.mpf(str(float(R.subs({n:k,z:float(a*a)}))))*vals[k]
        assert abs(direct-predicted)<mp.mpf('2e-14')
print('PASS: symbolic identities, sharp staircase comparisons, and 4 x 10 independent moments.')

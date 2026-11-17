"""Standalone numerical and symbolic checks for geometric escape thresholds."""
import math
import mpmath as mp
import sympy as sp

xvar, y, p, q = sp.symbols('x y p q', real=True)
X = y * (1 + q)/(1 - q)
Q = y + p*y**3
P = X - X**2*y + p*X*y**2 + y**3
qprime = -2*y*q/(1 + p*y**2)
residual = sp.factor((sp.diff(X,y) + sp.diff(X,q)*qprime)*Q - P)
assert residual == 0, residual

mp.mp.dps = 65
b = mp.mpf('0.7'); a=mp.mpf('2.3'); q0=(a-b)/(a+b)

def q_of_y(p,Y):
    return q0*((1+p*b*b)/(1+p*Y*Y))**(1/p)

def signed_gap(p,Y):
    qq=q_of_y(p,Y)
    return 2*Y*qq/(1-qq)

def signed_area(p,Y):
    hmax=mp.log((1+p*Y*Y)/(1+p*b*b))/p
    return (1+p*b*b)*q0*mp.quad(lambda h: mp.exp((p-1)*h)/(1-q0*mp.exp(-h)),[0,hmax/2,hmax])

# Exact global finite-area integral and a separate direct physical-coordinate quadrature.
for p0 in [mp.mpf('0.3'),mp.mpf('0.5'),mp.mpf('0.75')]:
    A=(1+p0*b*b)*q0/(1-p0)*mp.hyp2f1(1,1-p0,2-p0,q0)
    B=(1+p0*b*b)*q0*mp.quad(lambda h: mp.exp((p0-1)*h)/(1-q0*mp.exp(-h)),[0,10,mp.inf])
    assert abs(A/B-1) < mp.mpf('1e-35'), (p0,A,B)

# Compare the finite critical formulas with the exact flow for a very large height.
Y=mp.mpf('1e80'); L=mp.log(Y)
for lam in [-2,-1,0,1,2]:
    p2=2+mp.mpf(lam)/L
    c=q0*mp.sqrt(2*(1+2*b*b))
    target=c*mp.exp(mp.mpf(lam)/2)
    actual=signed_gap(p2,Y)
    assert abs(actual/target-1) < mp.mpf('0.02'), (lam,'affine',actual,target)
    p1=1+mp.mpf(lam)/(2*L)
    target1=mp.expm1(lam)/lam if lam else mp.mpf(1)
    actual1=signed_area(p1,Y)/(2*q0*(1+b*b)*L)
    assert abs(actual1/target1-1) < mp.mpf('0.02'), (lam,'area',actual1,target1)

# Large-height phase diagram, with rationally normalized cases.
for p0 in [mp.mpf('0.5'),mp.mpf('1.5'),mp.mpf('2'),mp.mpf('3')]:
    A=((1+p0*b*b)/p0)**(1/p0)
    limit=2*q0*A
    Y=mp.mpf('1e15')
    actual=signed_gap(p0,Y)/Y**(1-2/p0)
    assert abs(actual/limit-1) < mp.mpf('1e-8'), (p0,actual,limit)

# Exact logarithmic critical area and second asymptotic offset at p=2.
C1=q0*(1+b*b)
Y=mp.mpf('1e12')
D1_exact=C1*mp.log((1+Y*Y-C1)/(1+b*b-C1))
assert abs(signed_area(mp.mpf(1),Y)/D1_exact-1) < mp.mpf('1e-50')
c=q0*mp.sqrt(2*(1+2*b*b))
assert abs((signed_gap(mp.mpf(2),Y)-c)*Y/(c*c/2)-1) < mp.mpf('1e-9')

# The original-time scalar clock and the shape law coincide at a test time.
p0=mp.mpf(2); delta=mp.mpf('0.003')
tb=mp.log(1+1/(p0*b*b))/2
ysq=1/(p0*mp.expm1(2*delta))
y0=mp.sqrt(ysq)
q1=q0*((1+p0*b*b)/(1+p0*y0*y0))**(1/p0)
q2=q0*((1+p0*b*b)*(1-mp.exp(-2*delta)))**(1/p0)
assert abs(q1-q2) < mp.mpf('1e-40')
print('DARBOUX_TWO_GEOMETRIC_THRESHOLDS_CHECK_OK')

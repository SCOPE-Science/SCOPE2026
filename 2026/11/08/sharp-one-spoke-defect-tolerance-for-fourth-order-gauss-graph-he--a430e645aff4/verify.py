"""Exact symbolic and rational checks for an anomalous-spoke weighted star.

Run: python gauss_star_checker.py. Requires Python 3 and SymPy.
This is finite diagnostic evidence supplementing the algebraic theorem, not
an alternative proof of its all-degree and all-timestep quantifiers.
"""
import sympy as sp

k, t, h = sp.symbols('k t h', positive=True)
Q = sp.Matrix([[k+t, -k, -t], [-1, 1, 0], [-t, 0, t]])
z = h*Q
A = z*z + 6*z + 12*sp.eye(3)
N = z*z - 6*z + 12*sp.eye(3)
Delta = sp.factor(A.det())
num = N*A.adjugate()
r = h*h - 6*h + 12
s = h*h + 6*h + 12
B = (h**3*t*((k+4)*t-1) + h**2*(6*k*t+12*t*t+12*t)
     + h*(12*k+48*t+24)+72)
expected = {
 (0,1): 144*h*k*(t*(2*t-1)*h*h+6*t*h+12),
 (0,2): 144*h*t*((k+1-k*t)*h*h+6*h+12),
 (1,2): 144*h*h*t*(h*(k+2*t+1)+6),
 (2,1): 144*h*h*k*t*(h*(k+2*t+1)+6),
}
checks=0
for (i,j), expr in expected.items():
    assert sp.cancel(num[i,j]-expr)==0
    checks+=1
assert sp.cancel(num[1,1]*s-Delta*r-144*h*h*k*B)==0
checks+=1
# The equitable quotient is 3x3: its spectrum is zero and the two quadratic roots.
x = sp.symbols('x')
assert sp.cancel(Q.charpoly(x).as_expr()-x*(x*x-(k+1+2*t)*x+(k+2)*t))==0
checks+=1

def exact_step(m, weight, step):
    W=[sp.S(1)]*(m-1)+[weight]
    L=sp.zeros(m+1)
    for i,w in enumerate(W,1):
        L[0,0]+=w; L[i,i]+=w; L[0,i]-=w; L[i,0]-=w
    z=step*L
    U=(z*z+6*z+12*sp.eye(m+1)).inv()*(z*z-6*z+12*sp.eye(m+1))
    return U

for m in range(4,9):
    upper=sp.Rational(m,m-1)
    for tt in [sp.Rational(1,2),sp.Rational(3,4),sp.S(1),upper]:
        for hh in [sp.Rational(1,5),sp.S(1),sp.S(5),sp.S(40)]:
            T=exact_step(m,tt,hh)
            assert T==T.T
            assert all(sum(T[i,j] for j in range(m+1))==1 for i in range(m+1))
            assert all(T[i,j]>0 for i in range(m+1) for j in range(m+1))
            checks+=1
    # Necessity at a sufficiently late timestep, for each side of the interval.
    low=sp.Rational(1,4);high=upper+sp.Rational(1,2)
    for tt, j in [(low,1),(high,m)]:
        T=exact_step(m,tt,sp.S(10000))
        assert T[0,j]<0
        checks+=1
print('VERIFY_OK',checks)

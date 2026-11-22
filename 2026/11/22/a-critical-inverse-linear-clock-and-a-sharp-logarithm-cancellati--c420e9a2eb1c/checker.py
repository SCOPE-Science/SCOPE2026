"""Exact symbolic checks and finite diagnostics for the critical five-lag map.

Requires Python 3 and SymPy. Finite diagnostics do not establish the infinite-time
asymptotics; these follow from the proof in RESULT.md.
"""
import math
import sympy as sp

b, t = sp.symbols('b t', real=True, positive=True)
d = b + 5
c = b + 1
q = 1 / d
alpha = sp.Matrix([(j*d - 10) / d**2 for j in range(5)])
e = sp.ones(5, 1)
pi = sp.Matrix([[c/d, 1/d, 1/d, 1/d, 1/d]])
M = sp.zeros(5)
M[0, 0], M[0, 4] = b/c, 1/c
for j in range(1, 5):
    M[j, j-1] = 1
assert sp.simplify(pi*M-pi) == sp.zeros(1, 5)
assert sp.simplify(M*e-e) == sp.zeros(5, 1)
assert sp.simplify(pi*alpha) == sp.zeros(1, 1)

x = sp.symbols('x0:5', nonnegative=True)
xp = (b*x[0] + x[4])/(c+x[1])
W = c*x[0] + sum(x[1:])
Wp = c*xp + sum(x[:4])
assert sp.simplify(W-Wp-x[1]*xp) == 0

h = t*e + t**2*alpha
h_first = (b*h[0]+h[4])/(c+h[1])
Th = sp.Matrix([h_first,h[0],h[1],h[2],h[3]])
t_new = sp.cancel((pi*Th)[0])
for power, coeff in [(0,0),(1,1),(2,-q),(3,20/d**3)]:
    assert sp.simplify(sp.series(t_new,t,0,4).removeO().expand().coeff(t,power)-coeff) == 0
for j in range(5):
    residual = Th[j] - (t_new + alpha[j]*t_new**2)
    assert sp.simplify(sp.series(residual,t,0,3).removeO()) == 0
assert sp.simplify(q**2-20/d**3-(b-15)/d**3)==0
assert sp.simplify((q**2-20/d**3)/q-(b-15)/d**2)==0


def sample(beta, steps=200000):
    values = [0.4]*5
    last = None
    for n in range(1, steps+1):
        nxt = (beta*values[0]+values[4])/(beta+1+values[1])
        values = [nxt] + values[:4]
        if n in (steps//2, steps):
            gamma=(beta-15)/(beta+5)**2
            residual=1/values[0]-n/(beta+5)-gamma*math.log(n)
            last=(n,n*values[0],residual)
            assert abs(n*values[0]-(beta+5))<0.05*(beta+5)
    return last

if __name__ == '__main__':
    print('Exact symbolic identities: PASS')
    for beta in (1.,5.,15.,25.):
        print('b',beta,'(n, n*x_n, renormalized residual)',sample(beta))
    print('Finite diagnostics: PASS')

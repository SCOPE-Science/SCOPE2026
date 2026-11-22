"""Reproduce finite exact identities and transfer witnesses for a bidiagonal solve.

Requires Python 3.10+, sympy and numpy. Finite tests complement the proof.
"""
from fractions import Fraction
from math import sqrt
import numpy as np
import sympy as sp

checks = 0

def check(test, label):
    global checks
    if not bool(test):
        raise AssertionError(label)
    checks += 1

q = sp.symbols('q', positive=True, real=True)
for n in range(2, 9):
    S = sp.zeros(n)
    for i in range(1, n):
        S[i, i-1] = 1
    T = sp.eye(n) - q*S
    H = (T.inv() + T.inv().T)/2
    expected = sp.Matrix(n, n, lambda i,j: 1 if i == j else q**abs(i-j)/2)
    check(H == expected, f'KMS exact identity at n={n}')

H2 = sp.Matrix([[1,q/2],[q/2,1]])
check(sp.factor(H2.charpoly().as_expr()) == sp.factor((sp.Symbol('lambda')-1)**2-q*q/4) or H2.eigenvals() == {1+q/2:1, 1-q/2:1}, 'H2 spectrum')
H3 = sp.Matrix([[1,q/2,q**2/2],[q/2,1,q/2],[q**2/2,q/2,1]])
lm = 1+q*q/4-q*sp.sqrt(q*q+8)/4
lp = 1+q*q/4+q*sp.sqrt(q*q+8)/4
la = 1-q*q/2
for eig in (lm,lp,la):
    check(sp.simplify((H3-eig*sp.eye(3)).det())==0, f'H3 exact eigenvalue {eig}')
check(sp.expand((4+q*q)**2 - 9*q*q*(q*q+8)) == -8*(q**4+8*q*q-2),'sharp quartic threshold')
check(sp.simplify((3*sp.sqrt(2)-4)**2+8*(3*sp.sqrt(2)-4)-2)==0, 'three-site threshold')

# Exact rational cross-vector witness in dimension two beyond the sharp finite-size boundary.
t=sp.Rational(3,4)
T2=sp.Matrix([[1,0],[-t,1]])
ymax=sp.Matrix([1,1]); ymin=sp.Matrix([1,-1])
b=T2.inv()*ymax; c=T2.inv()*ymin
alpha=sp.factor((b.T*T2*b)[0]/(T2*b).dot(T2*b))
res=c-alpha*T2*c
check(alpha==sp.Rational(11,8), 'training GMRES coefficient')
check(c==sp.Matrix([1,-sp.Rational(1,4)]), 'test vector')
check(sp.factor(res.dot(res)/c.dot(c))==sp.Rational(45,34), 'amplification 45/34 in squared Euclidean norm')
train_res=b-alpha*T2*b
check(sp.factor(train_res.dot(train_res)/b.dot(b)) < 1,'training fit improves its own residual')

# Random spot checks of the Rayleigh-quotient range and cross-residual identity.
rng=np.random.default_rng(20261120)
for n in (2,3,4,7,12,25):
    for t in (0.01,0.14,0.3,1/3,0.38,0.45,0.5,0.7,0.95):
        T=np.eye(n)-t*np.diag(np.ones(n-1),-1)
        Tinv=np.linalg.inv(T)
        H=(Tinv+Tinv.T)/2
        vals,vs=np.linalg.eigh(H)
        M,m=vals[-1],vals[0]
        check(abs(np.trace(H)-n)<1e-8,'trace')
        check(M>=1-1e-8 and m<=1+1e-8,'bounds on eigenvalues')
        for k in range(7):
            b=rng.standard_normal(n); c=rng.standard_normal(n)
            alpha=np.dot(b,T@b)/np.dot(T@b,T@b)
            beta=np.dot(c,T@c)/np.dot(T@c,T@c)
            check(m-1e-10<=alpha<=M+1e-10, 'alpha spectral range')
            direct=np.linalg.norm(c-alpha*T@c)**2-np.dot(c,c)
            formula=alpha*(alpha-2*beta)*np.dot(T@c,T@c)
            check(abs(direct-formula)<3e-9*max(1,abs(direct)), 'cross-residual identity')
        by=Tinv@vs[:,-1]; cy=Tinv@vs[:,0]
        a=np.dot(by,T@by)/np.dot(T@by,T@by)
        new=np.linalg.norm(cy-a*T@cy)**2-np.linalg.norm(cy)**2
        check((new>1e-9)==(M>2*m+1e-9) or abs(M-2*m)<1e-9, 'sharp eigendirection witness')
        if t<=1/3:
            check(M < 2*m+1e-10,'safe regime')

# Explicit failure at subunit t, where every training residual is still strictly improved.
n=25;t=0.4
T=np.eye(n)-t*np.diag(np.ones(n-1),-1)
H=(np.linalg.inv(T)+np.linalg.inv(T).T)/2
vals,vs=np.linalg.eigh(H)
check(vals[-1]>2*vals[0], 'out-of-sample reversal occurs for n=25, t=0.4')
check(np.linalg.eigvalsh((T+T.T)/2)[0]>0, 'training step strictly improves for any nonzero b')

print(f'PASS: {checks} symbolic / exact-rational / numerical assertions')
print('n=2 rational witness: alpha=11/8, test residual squared-norm ratio=45/34')
print(f'n=25, t=0.4: max/min sym-inverse = {vals[-1]:.9f}/{vals[0]:.9f}; 2m-M={2*vals[0]-vals[-1]:.9f}')
print('n=3 t_3 =',sqrt(3*sqrt(2)-4))

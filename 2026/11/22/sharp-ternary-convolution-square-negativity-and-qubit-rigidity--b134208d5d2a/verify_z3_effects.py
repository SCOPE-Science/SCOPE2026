"""Exact and numerical ancillary checks for the sharp ternary matrix-convolution bound.
Run: python verify_z3_effects.py
"""
import sympy as sp
import numpy as np

q=sp.Rational
h=sp.sqrt(30)/12
A=sp.Matrix([[q(1,2),h],[h,q(5,12)]])
B=sp.Matrix([[q(1,2),-h],[-h,q(5,12)]])
C=sp.diag(0,q(1,6))
I=sp.eye(2)
assert A+B+C==I
assert A.det()==B.det()==0
assert list(A.eigenvals())==[0,q(11,12)] or set(A.eigenvals())=={0,q(11,12)}
assert set(B.eigenvals())=={0,q(11,12)}
assert C.eigenvals()=={0:1,q(1,6):1}
S=A+B; X=A-B
assert S==sp.diag(1,q(5,6))
assert sp.simplify(X*X)==q(5,6)*I
H=sp.simplify(A*B+B*A+C*C)
assert H==sp.diag(q(1,12),-q(1,24)), H
assert H + I/24==sp.diag(q(1,8),0)
assert sp.simplify((S*S-X*X)/2+C*C)==H
assert (A*B-B*A)!=sp.zeros(2)
print('Exact witness matrices, sharp eigenvalue, noncommutativity: OK')

# independent deterministic finite-dimensional stress tests, not an infinite proof
rng=np.random.default_rng(28117)
minval=0.0
samples=0
for n in (1,2,3,4,6,9):
    eye=np.eye(n)
    for trial in range(500):
        R=[]
        for j in range(3):
            X0=rng.standard_normal((n,n))+1j*rng.standard_normal((n,n))
            R.append(X0.conj().T@X0)
        total=sum(R)
        evals,U=np.linalg.eigh(total)
        Z=(U/np.sqrt(evals))@U.conj().T
        a,b,c=[Z@x@Z for x in R]
        s=a+b; x=a-b
        assert np.linalg.norm(a+b+c-eye)<3e-10
        assert np.linalg.eigvalsh(s-x@x).min()>=-3e-10
        for h in (a@b+b@a+c@c,a@c+c@a+b@b,b@c+c@b+a@a):
            v=np.linalg.eigvalsh(h).min()
            minval=min(minval,v)
            assert v >= -1/24-3e-10,(n,trial,v)
            samples+=1
print('Random PSD-effect triples: '+str(samples)+' convolution coefficient eigenvalue checks passed; min='+str(minval))
# Extremal rank-one two-parameter slice has an exact global minimum at t=5/6.
t=sp.symbols('t',real=True)
phi=sp.factor((t*t-t)/2+(1-t)**2)
assert sp.simplify(phi+q(1,24)-sp.Rational(3,2)*(t-q(5,6))**2)==0
assert sp.solve(sp.Eq(phi,0),t)==[q(2,3),1]
for j in range(1,1000):
    tt=j/1000
    aa=np.array([[0.5,np.sqrt(tt)/2],[np.sqrt(tt)/2,tt/2]])
    bb=np.array([[0.5,-np.sqrt(tt)/2],[-np.sqrt(tt)/2,tt/2]])
    cc=np.diag([0.,1-tt])
    out=aa@bb+bb@aa+cc@cc
    assert np.linalg.eigvalsh(aa).min()>-1e-12
    assert np.linalg.eigvalsh(bb).min()>-1e-12
    assert np.linalg.eigvalsh(out).min()>=-1/24-1e-12
print('Exact contact polynomial and 999 rank-one family tests: OK')

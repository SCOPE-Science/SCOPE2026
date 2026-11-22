"""Exact-rational identities for a three-row Kaczmarz delivery-order comparison.

Execute: python verify.py (requires SymPy).  Supplementary finite-mask
checks are separate from the algebraic proof in RESULT.md.
"""
import itertools
import sympy as s

p,t=s.symbols('p t', real=True)
I=s.eye(2)
A=[s.Matrix([1,-3])/s.sqrt(10),s.Matrix([1,0]),s.Matrix([1,3])/s.sqrt(10)]
P=[s.simplify(I-u*u.T) for u in A]
classes=[(0,1,2),(0,2,1),(1,0,2)]

def propagated(order,rate):
    M=I
    for j in reversed(order):
        M=s.simplify((1-rate)*M+rate*P[j]*M*P[j])
    return M

def exact_mask(order,rate):
    M=s.zeros(2)
    for bits in itertools.product((0,1),repeat=3):
        X=I; prob=s.Integer(1)
        for j,b in zip(order,bits):
            prob*=rate if b else 1-rate
            X=(P[j] if b else I)*X
        M+=prob*X.T*X
    return s.simplify(M)

Ms=[propagated(o,p) for o in classes]
for o,M in zip(classes,Ms):
    assert all(s.simplify(a)==0 for a in (M-M.T))
    assert s.simplify(M-exact_mask(o,p))==s.zeros(2)
for order in itertools.permutations(range(3)):
    M=propagated(order,p)
    assert any(s.simplify(s.trace(M)-s.trace(N))==0 and s.simplify(M.det()-N.det())==0 for N in Ms)

T=[s.factor(s.trace(M)) for M in Ms]
D=[s.factor(M.det()) for M in Ms]
assert s.factor(T[1]-T[2])==0
assert s.factor(D[1]-D[2])==s.factor(54*p**3*(p-2)*(p-1)*(36*p-100)/100000)
assert s.factor(T[0]-T[2])==s.factor(-54*p**3/1000)
x=s.factor((D[2]-D[0])/(T[2]-T[0]))
assert s.simplify(x-(p-1)*(67*p*p+600*p-1000)/500)==0
Q=12231*p**5-38171*p**4-48500*p**3+423000*p**2-600000*p+250000
assert s.factor(x*x-T[0]*x+D[0])==s.factor(-(p-1)*Q/250000)
assert s.simplify(s.expand((1+t)**5*Q.subs(p,t/(1+t))) - (-1440*t**5-16171*t**4+120500*t**3+523000*t**2+650000*t+250000))==0
assert Q.subs(p,s.Rational(7,8))>0 and Q.subs(p,s.Rational(9,10))<0
# The equal eigenvalue is the maximum eigenvalue on the isolating interval.
for Y in T:
    a=s.factor(x-Y/2)
    assert a.subs(p,s.Rational(9,10))>0
    assert s.diff(a,p).subs(p,s.Rational(7,8))<0
    assert s.diff(a,p).subs(p,s.Rational(9,10))<0
    assert s.discriminant(s.together(s.diff(a,p)).as_numer_denom()[0],p)>=0

# Exact spectral comparisons to orient the two sides of the unique crossover.
def maxeig(M,z):
    MM=M.subs(p,z)
    return s.simplify((s.trace(MM)+s.sqrt(s.trace(MM)**2-4*MM.det()))/2)
assert s.simplify(maxeig(Ms[0],s.Rational(1,2))-(117+s.sqrt(565))/320)==0
assert s.simplify(maxeig(Ms[2],s.Rational(1,2))-(369+s.sqrt(3385))/1000)==0
assert maxeig(Ms[0],s.Integer(1))==s.Rational(1,100)
assert maxeig(Ms[2],s.Integer(1))==s.Rational(8,125)
assert maxeig(Ms[1],s.Integer(1))==s.Rational(8,125)
for z in [s.Rational(1,10),s.Rational(1,4),s.Rational(1,2),s.Rational(3,4),s.Rational(9,10),s.Rational(99,100),s.Integer(1)]:
    for order in itertools.permutations(range(3)):
        assert propagated(order,z)==exact_mask(order,z)
    # Every matrix is a convex combination of X^T X and hence PSD.
    for M in Ms:
        MM=M.subs(p,z)
        assert MM[0,0]>=0 and MM[1,1]>=0 and MM.det()>=0

root=float([v for v in s.nroots(Q,maxsteps=500) if abs(s.im(v))<1e-12 and 0<float(s.re(v))<1][0])
print('PASS: algebraic identities, all six permutations, exact mask checks, boundary and root certificates')
print('unique crossover p_star ≈ %.13f'%root)
print('equation:',Q)

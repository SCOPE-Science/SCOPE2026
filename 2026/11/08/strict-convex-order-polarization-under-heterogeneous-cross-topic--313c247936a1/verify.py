"""Exact checks for a weighted convex-order relation in heterogeneous cross-topic opinion averaging.

Run with: python verify.py
Requires sympy. Analytic statements in RESULT.md are proved separately;
finite checks here test formulas and illustrative boundary cases.
"""
from fractions import Fraction
from random import Random
from sympy import Matrix, Rational, eye, ones

rng=Random(27019)
count=0

def make_S(n):
    # Positive rational row-stochastic, generally directed and nonreversible.
    rows=[]
    for _ in range(n):
        a=[rng.randint(1,8) for _ in range(n)]
        sm=sum(a)
        rows.append([Rational(v,sm) for v in a])
    return Matrix(rows)

def left_stationary(S):
    n=S.rows
    A=S.T-eye(n)
    A[n-1,:]=Matrix([[1]*n])
    b=Matrix([0]*(n-1)+[1])
    p=A.inv()*b
    assert all(z>0 for z in p)
    assert (p.T*S)==p.T
    return p

def filt(S,e):
    return e*(eye(S.rows)-(1-e)*S).inv()

for n in (2,3,4,5):
    for trial in range(12):
        S=make_S(n)
        pi=left_stationary(S)
        w=Matrix([Rational(rng.randint(0,10),10) for _ in range(n)])
        if len(set(w))==1:
            w[0]=Rational(1,7)
        a=Rational(rng.randint(1,4),10)
        b=Rational(rng.randint(6,9),10)
        Fa,Fb=filt(S,a),filt(S,b)
        K=(a/b)*(eye(n)+(b-a)*S*(eye(n)-(1-a)*S).inv())
        assert Fa==K*Fb
        assert all(z>=0 for z in K)
        assert K*ones(n,1)==ones(n,1)
        assert (pi.T*K)==pi.T
        ha,hb=Fa*w,Fb*w
        assert ha==K*hb
        assert (pi.T*ha)==(pi.T*hb)==(pi.T*w)
        mu=(pi.T*w)[0]
        Va=sum(pi[i]*(ha[i]-mu)**2 for i in range(n))
        Vb=sum(pi[i]*(hb[i]-mu)**2 for i in range(n))
        assert 0<Va<Vb
        for t in (Rational(1,5),Rational(1,2),Rational(4,5)):
            ca=sum(pi[i]*abs(ha[i]-t) for i in range(n))
            cb=sum(pi[i]*abs(hb[i]-t) for i in range(n))
            assert ca<=cb
        count+=1

# Two-source, two-agent model: source consensus values 1 and 0.
S=Matrix([[Rational(1,2)]*2]*2)
w=Matrix([Rational(1,4),Rational(3,4)])
e=Rational(1,2)
h=filt(S,e)*w
assert h==Matrix([Rational(3,8),Rational(5,8)])
assert filt(S,Rational(1,100))*w==Matrix([Rational(199,400),Rational(201,400)])
print(f'PASS: {count} directed positive-matrix instances, 3 convex hinge tests each, exact kernel, strict variance, stationary averages and the two-agent boundary.')

# In directed networks the stationary weighting is essential:
# ordinary equal-node empirical variance can *decrease* as the cross-topic
# influence rate increases, although stationary-weighted convex order holds.
d=Rational(1,100)
T=Matrix([[d,1-2*d,d],[d,1-d,0],[d,0,1-d]])
z=Matrix([Rational(1,2),1,0])
p=left_stationary(T)
assert p==Matrix([Rational(1,100),Rational(98,100),Rational(1,100)])
h_low=filt(T,Rational(1,5))*z
h_high=filt(T,Rational(4,5))*z
def uniform_var(z):
    av=sum(z)/len(z)
    return sum((v-av)**2 for v in z)/len(z)
def stationary_var(z,p):
    av=(p.T*z)[0]
    return sum(p[i]*(z[i]-av)**2 for i in range(len(z)))
assert uniform_var(h_low)==Rational(14071,76050)
assert uniform_var(h_high)==Rational(6075272,36180225)
assert uniform_var(h_low)>uniform_var(h_high)
assert 0<stationary_var(h_low,p)<stationary_var(h_high,p)
print('PASS: exact directed three-agent counterexample for unweighted variance, with increasing stationary-weighted variance.')

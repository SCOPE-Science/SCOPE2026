"""Exact symbolic and rational checks for the two-person aspiration circulation theorem.
Run: python verify_aspiration_cycle.py
Requires SymPy; no external inputs or network requests.
"""
from fractions import Fraction
import math
import sympy as sp

x, y, t = sp.symbols('x y t')
forward_den = (1+x*t)*(1+y**2*t)*(1+y*x**2*t)
reverse_den = (1+x*y**2*t)*(1+x**2*t)*(1+y*t)
assert sp.factor(forward_den-reverse_den) == -t*(x-1)*(x-y)*(y-1)*(t*x*y-1)

states = ((0,0),(1,0),(1,1),(0,1))
def exact_chain(A):
    P=sp.zeros(4)
    for k, state in enumerate(states):
        S=2*state[0]+state[1]
        for i in (0,1):
            dest=tuple(1-state[j] if j==i else state[j] for j in (0,1))
            j=states.index(dest)
            payoff=2*S-(2 if i==0 and state[i] else 1 if i==1 and state[i] else 0)
            P[k,j]=sp.Rational(1,2)/(1+sp.Rational(2)**(payoff-A))
        P[k,k]=1-sum(P[k,j] for j in range(4) if j!=k)
    Q=P.T-sp.eye(4)
    Q[3,:]=sp.ones(1,4)
    pi=Q.inv()*sp.Matrix([0,0,0,1])
    assert all(z>0 for z in pi)
    assert (P.T*pi-pi)==sp.zeros(4,1)
    J=sp.factor(pi[0]*P[0,1]-pi[1]*P[1,0])
    assert all(sp.factor(pi[k]*P[k,(k+1)%4]-pi[(k+1)%4]*P[(k+1)%4,k]-J)==0 for k in range(4))
    ratio=sp.factor(sp.prod(P[k,(k+1)%4] for k in range(4)) / sp.prod(P[k,(k-1)%4] for k in range(4)))
    return pi,J,ratio

assert exact_chain(2)[1:] == (sp.Rational(-6,14419),sp.Rational(24,25))
assert exact_chain(3)[1:] == (0,1)
assert exact_chain(4)[1:] == (sp.Rational(24,29255),sp.Rational(25,24))
assert list(exact_chain(3)[0])==[sp.Rational(9,51),sp.Rational(12,51),sp.Rational(20,51),sp.Rational(10,51)]

for B in (sp.Rational(2,5),sp.Rational(4,5),sp.Rational(6,5),sp.Rational(3,2),sp.Rational(2),sp.Rational(3)):
    for a,b in ((sp.Rational(3,2),sp.Rational(1,3)),(sp.Rational(4),sp.Rational(1)),(sp.Rational(3),sp.Rational(2))):
        aa,bb=float(a),float(b)
        vv,uu=float(B),float(B-1)
        ca,cb=math.exp(uu*aa),math.exp(uu*bb)
        ha,hb=math.exp(vv*aa),math.exp(vv*bb)
        p=(ha-1)*(cb-1)-(hb-1)*(ca-1)
        q=ca*cb*ha*hb*((1-1/ha)*(1-1/cb)-(1-1/hb)*(1-1/ca))
        assert (p>0) == (B>1)
        assert (q<0) == (B>1)
        tt=-p/q
        assert tt>0
        # Directly verify the log-cycle product ratio at the root.
        f=(1+ca*tt)*(1+hb*tt)*(1+cb*ha*tt)
        r=(1+ca*hb*tt)*(1+ha*tt)*(1+cb*tt)
        assert abs(f/r-1)<2e-11
print('PASS: factorization, general-sign grid, exact stationary laws, three exact circulation witnesses')

# Independent exact-rational social-dilemma witness: multiplier r=3/2
# with a=2, b=1 and beta=4 log(2).
def exact_dilemma_chain(A):
    P=sp.zeros(4)
    for k, state in enumerate(states):
        for i in (0,1):
            dest=tuple(1-state[j] if j==i else state[j] for j in (0,1))
            j=states.index(dest)
            payoff=sp.Rational(3,4)*(2*state[0]+state[1])-(2 if i==0 else 1)*state[i]
            P[k,j]=sp.Rational(1,2)/(1+sp.Rational(2)**(4*(payoff-A)))
        P[k,k]=1-sum(P[k,j] for j in range(4) if j!=k)
    Q=P.T-sp.eye(4)
    Q[3,:]=sp.ones(1,4)
    pi=Q.inv()*sp.Matrix([0,0,0,1])
    assert P.T*pi==pi
    J=sp.factor(pi[0]*P[0,1]-pi[1]*P[1,0])
    ratio=sp.factor(sp.prod(P[k,(k+1)%4] for k in range(4)) / sp.prod(P[k,(k-1)%4] for k in range(4)))
    return J,ratio,pi
assert exact_dilemma_chain(sp.Rational(0))[0:2] == (sp.Rational(1,2904),sp.Rational(33,26))
assert exact_dilemma_chain(sp.Rational(1,2))[0:2] == (0,1)
assert list(exact_dilemma_chain(sp.Rational(1,2))[2])==[sp.Rational(5,16),sp.Rational(17,64),sp.Rational(9,64),sp.Rational(9,32)]
assert exact_dilemma_chain(sp.Rational(1))[0:2] == (sp.Rational(-8,2055),sp.Rational(26,33))
# At B=1/2 (multiplication factor 1), the reversible level is A=0.
xx,yy=sp.symbols('xx yy', positive=True)
cca,ccb,hha,hhb=1/xx,1/yy,xx,yy
P_half=sp.factor((hha-1)*(ccb-1)-(hhb-1)*(cca-1))
Q_half=sp.factor(cca*ccb*hha*hhb*((1-1/hha)*(1-1/ccb)-(1-1/hhb)*(1-1/cca)))
assert sp.simplify(P_half+Q_half)==0
print('PASS: positive-aspiration social-dilemma reversal, critical multiplier identity')

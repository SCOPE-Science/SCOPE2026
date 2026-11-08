"""Exact symbolic and numerical checks of the Lorenz Cantor-string gap law.
Run with Python 3 and dependencies specified in requirements.txt.
The infinite-dimensional conclusions are proved in RESULT.md, not inferred from finite tests.
"""
import sympy as S
from mpmath import mp

r = S.sqrt(6)
beta = 2*S.sqrt(6)/3
b1, b2, b3 = S.Rational(6,5), beta, 5/(2*r)
a1 = S.Rational(2,245)*(132-25*r)
a2 = S.Rational(2,49)*(32-3*r)
p = S.simplify((a2-a1)/(b1-b2))
q = S.simplify((1-a2)/(b2-b3))
assert -1 < float(p) < float(q) < 0

# Breakpoints for the conjugate map f(x)=(g(2x-1)+1)/2.
breaks = [S.Integer(0), S.simplify((p+1)/2),S.simplify((q+1)/2),
          S.Rational(1,2),S.simplify((1-q)/2),S.simplify((1-p)/2),S.Integer(1)]
slopes = [b1,beta,b3,b3,beta,b1]
shifts = [a1,a2,S.Integer(1),S.Integer(-1),-a2,-a1]

def F(x):
    for j in range(6):
        if float(breaks[j])-1e-11<=float(x)<=float(breaks[j+1])+1e-11:
            return S.simplify((slopes[j]*(2*x-1)+shifts[j]+1)/2)
    raise ValueError('not within unit interval')

p1=(43-10*r)/98
p2=(73-10*r)/98
p3=(73+10*r)/98
p4=(25+22*r)/98
q1=(55+10*r)/98
q2=(25+10*r)/98
q3=(25-10*r)/98
q4=(73-22*r)/98
intervals = [(q3,p1),(q4,p2),(q2,p4),(q1,p3)]
assert all(float(intervals[i][1])<float(intervals[i+1][0]) for i in range(3))
for idx, (lo,hi) in enumerate(intervals):
    lo_im, hi_im=F(lo),F(hi)
    expected=[(q4,p2),(q2,p3),(q3,p2),(q2,p4)][idx]
    assert S.simplify(lo_im-expected[0])==0
    assert S.simplify(hi_im-expected[1])==0
    assert S.simplify((hi_im-lo_im)-beta*(hi-lo))==0
print('EXACT_LORENZ_BRANCHES_OK six_piece=6 core_intervals=4')

delta=S.simplify(q4-p1)
kappa=S.simplify(q2-p2)
assert delta>0 and kappa>0
assert S.simplify(q1-p4-delta)==0
assert S.simplify(kappa+2*delta/(1-1/beta-1/beta**2)-(p3-q3))==0
A=S.Matrix([[0,1,0,0],[0,0,1,1],[1,1,0,0],[0,0,1,0]])
v=S.Matrix([0,1,1,0])
z=S.symbols('z')
# Two exterior gaps of length delta, and one unit gap for each visit to I1 or I2.
counts=[2]
for m in range(1,16):
    counts.append(int((S.ones(1,4)*(A**(m-1))*v)[0]))
fib=[0,1]
for n in range(30):fib.append(fib[-1]+fib[-2])
assert all(counts[m]==2*fib[m+1] for m in range(16))
G=S.simplify(2+z*(S.ones(1,4)*(S.eye(4)-z*A).inv()*v)[0])
assert S.simplify(G-2/(1-z-z**2))==0
print('EXACT_FIBONACCI_GAPS_OK generations=16 total_length_matches_convex_hull')

mp.dps=70
B=mp.sqrt(mp.mpf(8)/3); R=mp.sqrt(6)
phi=(1+mp.sqrt(5))/2
psi=(1-mp.sqrt(5))/2
d=(15-6*R)/49
k=(10*R-24)/49
D=mp.log(phi)/mp.log(B)
assert D>0 and D<1

def profile(theta):
    return 2*d**D/mp.sqrt(5)*(phi**(3-theta)+phi**2/(B-phi)*B**((1-D)*theta))

def tube(eps):
    K=int(mp.floor(mp.log(d/(2*eps))/mp.log(B)))
    assert K>=0
    first=4*eps*((phi**(K+3)-psi**(K+3))/mp.sqrt(5)-1)
    tail=2*d/mp.sqrt(5)*(phi*(phi/B)**(K+1)/(1-phi/B)
                          -psi*(psi/B)**(K+1)/(1-psi/B))
    return first+tail+min(k,2*eps)

assert abs(profile(0)-profile(1))<mp.mpf('1e-65')
assert profile(0)-profile(mp.mpf('0.5'))>mp.mpf('0.0005')
for theta in [mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('0.85')]:
    eps=d*B**(-100-theta)/2
    assert abs(tube(eps)/(2*eps)**(1-D)-profile(theta))<mp.mpf('1e-20')
print('TUBE_ASYMPTOTIC_SPOTCHECK_OK theta=0.1,0.5,0.85 k=100')
print('D=',mp.nstr(D,18),'delta=',mp.nstr(d,18),'kappa=',mp.nstr(k,18))
print('nonconstant_profile P0=',mp.nstr(profile(0),18),'P_half=',mp.nstr(profile(mp.mpf('.5')),18))

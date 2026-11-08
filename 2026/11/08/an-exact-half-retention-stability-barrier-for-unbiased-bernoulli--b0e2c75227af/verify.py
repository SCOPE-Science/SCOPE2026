"""Exact reproducibility checks for scalar Bernoulli-unbiased compression with error feedback.

Requires Python 3 and SymPy. The analytical result is proved in RESULT.md;
these checks validate identities and finite-prefix calculations only.
"""
from fractions import Fraction
from itertools import product
import sympy as S

checks = 0

def verify(condition, detail=''):
    global checks
    checks += 1
    if not bool(condition):
        raise AssertionError(detail or f'assertion {checks} failed')

p, h, m, c, v = S.symbols('p h m c v', real=True)
zero = S.Matrix([[1, 0], [h, 1]])
one = S.Matrix([[1-h/p, -1/p], [h*(1-1/p), 1-1/p]])
W = S.Matrix([[m, c], [c, v]])
Wnext = (1-p)*zero*W*zero.T + p*one*W*one.T
Wnext = Wnext.applyfunc(S.factor)
verify(S.factor(Wnext[0,1]-Wnext[1,1]) == 0, 'E[xe]=E[e^2] after a step')
red = Wnext.subs({c: v})
N = S.Matrix([
    [S.diff(red[0,0],m), S.diff(red[0,0],v)],
    [S.diff(red[1,1],m), S.diff(red[1,1],v)],
]).applyfunc(S.factor)
Nexpected = S.Matrix([
    [1-2*h+h*h/p, (1+2*h)/p-2],
    [(1-p)*h*h/p, (1-p)*(1+2*h)/p],
])
for i,j in product(range(2),repeat=2):
    verify(S.factor(N[i,j]-Nexpected[i,j])==0, 'N matrix')
T = S.trace(N)
D = N.det()
verify(S.factor(T - (1+h*h+2*h-4*h*p)/p)==0)
verify(S.factor(D - (1-p)*(1-2*h*h)/p)==0)
verify(S.factor(1-T+D -h*(4*p-2-(3-2*p)*h)/p)==0)
verify(S.factor(1+T+D -(2-(2*p-1)*h*(2-h))/p)==0)
verify(S.factor(1-D -(2*p-1+2*(1-p)*h*h)/p)==0)
verify(S.factor(((4*p-2)/(3-2*p))-2*p).subs(p,S.Rational(3,4))<0)
verify(S.factor(2*p-((4*p-2)/(3-2*p)) - (2*(2*p+1)*(1-p)/(3-2*p)))==0)

# Direct enumeration of the 2^k compression histories exactly matches the closed moment law.
for prob in [Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(9,10)]:
    for step in [Fraction(1,10),Fraction(1,2),Fraction(1),Fraction(3,2)]:
        # All expectations represented as exact Fractions
        outcomes = {(Fraction(1),Fraction(0)):Fraction(1)}
        mprev = Fraction(1); vprev=Fraction(0)
        pr=prob; al=step
        for k in range(1,8):
            nxt={}
            for (x,e),mass in outcomes.items():
                u=al*x+e
                for flag,pm in [(0,1-pr),(1,pr)]:
                    d=Fraction(flag,1)*u/pr
                    state=(x-d,u-d)
                    nxt[state]=nxt.get(state,Fraction(0))+mass*pm
            outcomes=nxt
            exx=sum(w*x*x for (x,e),w in outcomes.items())
            exe=sum(w*x*e for (x,e),w in outcomes.items())
            eee=sum(w*e*e for (x,e),w in outcomes.items())
            verify(exe==eee,'exact orthogonality after one step')
            if k==1:
                verify(exx==1-2*al+al*al/pr)
                verify(eee==(1-pr)*al*al/pr)
            else:
                A=1-2*al+al*al/pr
                B=(1+2*al)/pr-2
                C=(1-pr)*al*al/pr
                E=(1-pr)*(1+2*al)/pr
                verify(exx==A*mprev+B*vprev,'moment transition m')
                verify(eee==C*mprev+E*vprev,'moment transition v')
            mprev,vprev=exx,eee
        # For p>1/2, evaluate sign of characteristic polynomial at 1 exactly.
        threshold=(4*pr-2)/(3-2*pr)
        numerator=step*(4*pr-2-(3-2*pr)*step)/pr
        verify((numerator>0)==(pr>Fraction(1,2) and step<threshold))

# Independent p=1 case reduces exactly to usual gradient descent.
verify(S.simplify(N.subs(p,1)-S.Matrix([[(1-h)**2,2*h-1],[0,0]]))==S.zeros(2))
print(f'PASS {checks} symbolic and exact rational assertions')
print('Formula: mean-square EF stable iff p>1/2 and 0<h<(4p-2)/(3-2p).')
print('Baseline memoryless unbiased compression stable iff 0<h<2p.')

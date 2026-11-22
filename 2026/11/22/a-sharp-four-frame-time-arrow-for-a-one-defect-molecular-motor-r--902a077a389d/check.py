"""Exact verification of the four-state binary observation theorem.

Requires Python 3.10+ and SymPy (tested with SymPy 1.13).
No random simulation is used to certify the analytic identities.
"""
from fractions import Fraction
from itertools import product
from random import Random
import sympy as S

p,q,s=S.symbols('p q s',positive=True)
c=[s,1,1,1]
P=S.zeros(4)
for i in range(4):
    P[i,i]=1-c[i]*(p+q)
    P[i,(i+1)%4]=c[i]*p
    P[i,(i-1)%4]=c[i]*q
pi=S.Matrix([[1,s,s,s]])/(1+3*s)
E=(S.diag(1,1,0,0),S.diag(0,0,1,1))
ones=S.ones(4,1)

def prob(word):
    v=pi
    for i,bit in enumerate(word):
        v=v*E[bit]
        if i<len(word)-1:
            v=v*P
    return S.cancel((v*ones)[0])

assert all(S.factor(v)==0 for v in (pi*P-pi))
assert S.factor(pi[0,0]*P[0,1]-pi[0,1]*P[1,0])==s*(p-q)/(1+3*s)
delta=p*q*s*(p-q)*(1-s)/(1+3*s)
expected={'0001':0, '0010':1,'0011':-1,'0101':1,'0111':0,'1011':1}
count=0
for w in product((0,1),repeat=4):
    rev=w[::-1]
    if w>=rev: continue
    key=''.join(map(str,w))
    assert key in expected
    assert S.factor(prob(w)-prob(rev)-expected[key]*delta)==0, key
    count+=1
assert count==6
# Classify the optimization, with activity u=p+q and bias magnitude d=|p-q|.
u,d=S.symbols('u d',positive=True)
F=s*(1-s)/(1+3*s)
assert S.simplify(S.diff(F,s)-(1-2*s-3*s**2)/(1+3*s)**2)==0
assert S.simplify(F.subs(s,S.Rational(1,3)))==S.Rational(1,9)
assert S.factor(S.diff((u*u-d*d)*d,d))==u*u-3*d*d
assert S.simplify((4*F*(u*u-d*d)*d/4).subs({s:S.Rational(1,3),d:u/S.sqrt(3)})-2*u**3/(27*S.sqrt(3)))==0
# Independent rational 4-state path enumerator (not matrix multiplication).
def frac_test(a,b,t):
    C=[t,Fraction(1),Fraction(1),Fraction(1)]
    M=[[Fraction(0) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        M[i][i]=1-C[i]*(a+b)
        M[i][(i+1)%4]=C[i]*a
        M[i][(i-1)%4]=C[i]*b
    stationary=[Fraction(1),t,t,t]
    stationary=[x/(1+3*t) for x in stationary]
    assert all(sum(stationary[i]*M[i][j] for i in range(4))==stationary[j] for j in range(4))
    def enumerate_word(word):
        total=Fraction(0)
        for path in product(range(4),repeat=4):
            if any(int(state>=2)!=word[k] for k,state in enumerate(path)): continue
            weight=stationary[path[0]]
            for k in range(3): weight*=M[path[k]][path[k+1]]
            total+=weight
        return total
    values={w:enumerate_word(w) for w in product((0,1),repeat=4)}
    assert sum(values.values())==1
    z=a*b*t*(a-b)*(1-t)/(1+3*t)
    assert values[(0,1,0,1)]-values[(1,0,1,0)]==z
    tv=sum(abs(values[w]-values[w[::-1]]) for w in values)/2
    assert tv==4*abs(z)
    return tv
assert frac_test(Fraction(3,8),Fraction(1,8),Fraction(1,3))==Fraction(1,192)
rng=Random(4102026)
for _ in range(45):
    A=rng.randint(1,6);B=rng.randint(1,6)
    denom=A+B+rng.randint(1,7)
    T=Fraction(rng.randint(1,9),10)
    frac_test(Fraction(A,denom),Fraction(B,denom),T)
print('PASS: six exact reversal-pair identities, stationary flux, sharp joint optimizer, 46 independent rational-path enumerations')

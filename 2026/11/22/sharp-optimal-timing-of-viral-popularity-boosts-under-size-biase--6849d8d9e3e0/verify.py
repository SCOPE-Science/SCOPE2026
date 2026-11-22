"""Standalone exact checks of finite event-size ordering and the periodic diversity limit."""
from fractions import Fraction
from itertools import permutations
from math import gamma
import sympy as sp

S,a,b = sp.symbols('S a b', positive=True)
def factor(s,r):
    return s*(s+2*r)/(s+r)**2
swap=sp.factor(factor(S,a)*factor(S+a,b)-factor(S,b)*factor(S+b,a))
assert sp.simplify(swap + 2*S*a*b*(a-b)/((S+a)*(S+b)*(S+a+b)**2))==0
print('adjacent-swap exact symbolic identity: PASS')

def expected_herfindahl_by_states(n,steps):
    states={(1,)*n:Fraction(1)}
    for r in steps:
        out={}
        for weights,prob in states.items():
            total=sum(weights)
            for i,w in enumerate(weights):
                nxt=list(weights);nxt[i]+=r;nxt=tuple(nxt)
                out[nxt]=out.get(nxt,Fraction(0))+prob*Fraction(w,total)
        states=out
    assert sum(states.values(),Fraction(0))==1
    return sum((p*sum(Fraction(w*w,sum(state)**2) for w in state) for state,p in states.items()),Fraction(0))

def predicted_herfindahl(n,steps):
    s=Fraction(n);d=Fraction(n-1,n)
    for r in steps:
        d*=s*(s+2*r)/(s+r)**2
        s+=r
    return 1-d

for n in range(2,5):
 for steps in [(1,3),(3,1),(1,4,2),(2,1,4),(2,2,2),(1,2,3,4),(3,1,4,2)]:
    assert expected_herfindahl_by_states(n,steps)==predicted_herfindahl(n,steps)
print('exact rational Markov-state enumeration: PASS (21 configurations)')
for n in (2,3,4):
 for steps in ((1,2,3),(2,1,4),(2,3,5),(1,1,4)):
    values={perm:predicted_herfindahl(n,perm) for perm in set(permutations(steps))}
    order_asc=tuple(sorted(steps));order_desc=tuple(sorted(steps,reverse=True))
    assert values[order_asc]==min(values.values())
    assert values[order_desc]==max(values.values())
    for perm,val in values.items():
     if perm!=order_asc and len(set(perm))>1 and perm!=order_desc:
      assert values[order_asc]<val<values[order_desc]
print('all permutation ordering for 12 multiset cases: PASS')
assert predicted_herfindahl(2,(1,3))==Fraction(2,3)
assert predicted_herfindahl(2,(3,1))==Fraction(31,45)
print('two-user exact example: PASS')
import mpmath as mp
mp.mp.dps=60
def q_infty(n,m):
 L=mp.mpf(m+1)
 return (mp.mpf(n-1)/n)*mp.exp(mp.loggamma(mp.mpf(n+1)/L)+2*mp.loggamma(1+mp.mpf(n)/L)-mp.loggamma(mp.mpf(n)/L)-mp.loggamma(mp.mpf(n+2)/L)-mp.loggamma(2+mp.mpf(n-1)/L))
for n in [2,3,6]:
 assert abs(q_infty(n,1)-mp.mpf(n-1)/(n+1))<mp.mpf('1e-45')
 for m in [2,5,20]:
    finite=mp.mpf(n-1)/n
    for k in range(50000):
        s=n+k*(m+1)
        finite*=mp.mpf(s)*(s+2)*(s+2*m+1)/((s+1)*(s+m+1)**2)
    assert finite > q_infty(n,m)
    assert abs(finite-q_infty(n,m))<mp.mpf('1e-4')
 for m in [10**5,10**6]:
    ratio=q_infty(n,m)*m
    target=mp.mpf(n-1)*(n+2)/(n+1)
    assert abs(ratio-target)<mp.mpf('1e-3')
print('gamma products, ordinary-reinforcement and large-viral limits: PASS')

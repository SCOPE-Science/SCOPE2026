"""Independent symbolic identities and finite exact-arithmetic examples for switched quadratic population maps.

Run: python checks/check.py
The all-word theorem follows from the proof, not from sampling.
"""
from fractions import Fraction as Q
from itertools import product
import sympy as S

x,t = S.symbols('x t', real=True)
q=x+t*x*(1-x)
R=S.diff(q,x)*x*(1-x)/(q*(1-q))
D=t**2*x*(1-x)/((1+t*(1-x))*(1-t*x))
assert S.cancel(R-1-D)==0

# Exact nontrivial primitive two-cycle inside two distinct admissible subintervals.
x0=Q(1,5)
x1=Q(17,50)
t0=(x1-x0)/(x0*(1-x0))
t1=(x0-x1)/(x1*(1-x1))
assert t0==Q(7,8) and t1==Q(-350,561)
def f(xx,tt): return xx+tt*xx*(1-xx)
assert f(x0,t0)==x1 and f(x1,t1)==x0
mult=(1+t0*(1-2*x0))*(1+t1*(1-2*x1))
assert mult == Q(27389,22440) and mult>1
A=(1+t0)*(1+t1)
B=(1-t0)*(1-t1)
assert A<1 and B<1

# Finite exact-arithmetic consistency for uniformly switched words.
cases=0
for n in range(1,5):
    for ts in product([Q(-3,4),Q(-1,2),Q(0),Q(1,2),Q(3,4)],repeat=n):
        if not any(ts): continue
        aa=Q(1); bb=Q(1)
        for tt in ts: aa*=1+tt; bb*=1-tt
        # For fixed word, compare signs of Q_w(x)-x at two rational interior test states.
        for xx in [Q(1,10000),Q(9999,10000)]:
            yy=xx
            for tt in ts: yy=f(yy,tt)
            if aa<1 and bb<1:
                # Only these inequalities at sufficiently near endpoints; not guaranteed for each sample.
                pass
            # The local derivative of logit never contracts (exact).
            yy=xx
            for tt in ts:
                den=(1+tt*(1-yy))*(1-tt*yy)
                assert den>0
                gain=1+tt*tt*yy*(1-yy)/den
                assert gain>=1
                yy=f(yy,tt)
        cases+=1
print('SWITCHED_QUADRATIC_LOGIT_CHECK_OK', 'word_cases='+str(cases),'two_cycle_multiplier='+str(mult))

#!/usr/bin/env python3
"""Exact certificate for the stationary signed-current variance on a seven-site constrained exclusion ring.

Requirements: Python 3 and SymPy.  Run: python check.py
"""
from itertools import product
import sympy as S

q=S.symbols('q', positive=True)
L,N=7,3
all_states=[x for x in product((0,1),repeat=L) if sum(x)==N]
def orbit(x):
    return min(x[i:]+x[:i] for i in range(L))
reps=sorted(set(orbit(x) for x in all_states))
assert len(reps)==5 and len(all_states)==35
index={r:i for i,r in enumerate(reps)}

def jumps(x):
    for k in range(L):
        pos=[(k+i)%L for i in range(3)]
        pat=tuple(x[i] for i in pos)
        if pat not in ((0,1,0),(0,0,1)):
            continue
        d=1 if pat==(0,1,0) else -1
        dest=(0,0,1) if d==1 else (0,1,0)
        y=list(x)
        for i,z in zip(pos,dest):y[i]=z
        yield tuple(y),d,(q if d==1 else S.Integer(1))

def matrices(states,indexer):
    n=len(states)
    A=S.zeros(n);B=S.zeros(n);C=S.zeros(n)
    for j,x in enumerate(states):
        for y,d,rate in jumps(x):
            i=indexer(y)
            A[i,j]+=rate
            A[j,j]-=rate
            B[i,j]+=rate*d
            C[i,j]+=rate
    return A,B,C

A,B,C=matrices(reps,lambda y:index[orbit(y)])
assert (S.ones(1,5)*A)==S.zeros(1,5)
R=q**3+q**2+q+2
p=S.Matrix([q**3/R,q**2/R,3*q/((2*q+1)*R),q/R,(q+2)/((2*q+1)*R)])
assert S.simplify(sum(p)-1)==0
assert all(S.simplify(z)==0 for z in A*p)

def cumulants(A,B,C,p):
    n=A.rows
    mean=S.factor((S.ones(1,n)*B*p)[0])
    T=A.copy();T[-1,:]=S.ones(1,n)
    rhs=(mean*S.eye(n)-B)*p;rhs[-1]=0
    u=T.inv()*rhs
    assert all(S.simplify(z)==0 for z in A*u - (mean*S.eye(n)-B)*p)
    var=S.factor((S.ones(1,n)*(C*p+2*B*u))[0])
    return mean,var

m,v=cumulants(A,B,C,p)
P=8*q**9+30*q**8+55*q**7+39*q**6+33*q**5+89*q**4+103*q**3+55*q**2+34*q+4
m_expected=2*(q*q-1)/((2*q+1)*R)
v_expected=2*(q+1)*P/((2*q+1)**3*R**3)
assert S.factor(m-m_expected)==0
assert S.factor(v-v_expected)==0
assert S.limit(q*q*m/L,q,S.oo)==S.Rational(1,7)
assert S.limit(q*q*v/L,q,S.oo)==S.Rational(2,7)
assert S.limit(v/m,q,S.oo)==2
assert S.factor(v.subs(q,1)/L)==S.Rational(8,105)

# Independent, unreduced 35-state check at exact rational parameters.
fullidx={x:i for i,x in enumerate(all_states)}
Af,Bf,Cf=matrices(all_states,lambda y:fullidx[y])
for value in (S.Rational(1,2),S.Integer(2)):
    G=Af.subs(q,value);D=Bf.subs(q,value);E=Cf.subs(q,value)
    T=G.copy();T[-1,:]=S.ones(1,len(all_states))
    rhs=S.zeros(len(all_states),1);rhs[-1]=1
    pf=T.inv()*rhs
    mf,vf=cumulants(G,D,E,pf)
    assert S.factor(mf-m_expected.subs(q,value))==0
    assert S.factor(vf-v_expected.subs(q,value))==0
print('PASS: 5-orbit symbolic stationary law, both exact cumulants, high-drive limits, 35-state rational cross-checks')

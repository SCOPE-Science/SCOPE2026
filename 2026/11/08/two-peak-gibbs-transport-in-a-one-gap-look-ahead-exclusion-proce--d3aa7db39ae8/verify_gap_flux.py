"""Exact finite-state and polynomial checks for a preferred-gap exclusion flux.
Run: python3 verify_gap_flux.py. Uses Python standard library only.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(a,b):
    c=[0]*max(len(a),len(b))
    for j,x in enumerate(a):c[j]+=x
    for j,x in enumerate(b):c[j]+=x
    return trim(c)

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def neg(a):return [-x for x in a]
def sub(a,b):return add(a,neg(b))
def deriv(a):return [j*a[j] for j in range(1,len(a))] or [0]
def powpoly(a,k):
    r=[1]
    for _ in range(k):r=mul(r,a)
    return r

def evaluate(a,x):
    v=0
    for c in a[::-1]:v=v*x+c
    return v

# I=2, k=7, weight w_7=100; rational current J=2 U/V.
z=[0,1]; one_minus_z=[1,-1]
U=mul(powpoly(z,2),mul(one_minus_z, add([1],mul([99],mul(powpoly(z,7),one_minus_z)))))
V=add([1],mul([792],mul(powpoly(z,7),powpoly(one_minus_z,2))))
E=sub(mul(deriv(U),V),mul(U,deriv(V)))
assert E[0]==0
P=E[1:]
expected={0:2,1:-3,7:-3069,8:10692,9:-12375,10:4752,14:156816,15:-627264,16:940896,17:-627264,18:156816}
assert len(P)==19 and all(c==expected.get(j,0) for j,c in enumerate(P))
# Mobius change z=x/(1+x) maps x>0 onto 0<z<1.
q=[sum(P[j]*comb(18-j,k-j) for j in range(k+1)) for k in range(19)]
signs=[1 if v>0 else -1 for v in q if v]
changes=sum(s!=t for s,t in zip(signs,signs[1:]))
assert changes==3
assert all(c>0 for c in q[0:9]); assert all(c<0 for c in q[9:14]);assert all(c>0 for c in q[14:16]);assert all(c<0 for c in q[16:19])
points=[F(2,5),F(1,2),F(3,4),F(19,20)]
assert [(evaluate(P,x)>0) for x in points]==[True,False,True,False]
print('CERTIFICATE: derivative identity, Mobius-Descartes 3-root upper bound, and 3 disjoint rational sign-change brackets OK')

def compositions(total,parts):
    if parts==1:
        yield (total,)
    else:
        for n in range(total+1):
            for c in compositions(total-n,parts-1):yield(n,)+c

def w(n):return 100 if n==7 else 1
def u(n):return F(w(n-2),w(n)) if n>=2 else F(0)
# Exact canonical stationarity in the gap representation on labelled rings.
# Both directions can be checked separately; their positive superpositions also satisfy balance.
case_count=0
for N in [3,4]:
  for G in [7,8,9,10,11,12]:
    states=list(compositions(G,N));weights={s:__import__('math').prod(w(x) for x in s) for s in states}
    for forward in [True,False]:
      inflow={s:F(0) for s in states};outflow={s:F(0) for s in states}
      for state in states:
        for i in range(N):
          donor=i if forward else (i-1)%N
          receiver=(i-1)%N if forward else i
          if state[donor]<2:continue
          dest=list(state);dest[donor]-=2;dest[receiver]+=2;dest=tuple(dest)
          rate=u(state[donor])
          mass=weights[state]*rate
          outflow[state]+=mass;inflow[dest]+=mass
      assert inflow==outflow,(N,G,forward)
      case_count+=1
print('CERTIFICATE: exact canonical Gibbs balance for',case_count,'directed-ring tests OK')
# Independent physical current formula identity: Z+z Z' has positive coeffs, positive for 0<z<1.
# The analytic proof of E_nu[u(n)]=z^2 uses termwise reindexing, not finite tests.
print('ALL_CHECKS_PASSED')

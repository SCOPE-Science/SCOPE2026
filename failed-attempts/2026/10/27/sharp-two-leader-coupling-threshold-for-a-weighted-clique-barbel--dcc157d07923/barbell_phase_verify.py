"""Exact symbolic and rational checks of weighted clique-barbell leader costs.

Requires SymPy. Run: python barbell_phase_verify.py
The general proof is in RESULT.md; finite tests supplement it.
"""
from itertools import combinations
import sympy as sp

q,t=sp.symbols('q t',positive=True)
CASES={'GG':('a','b'),'GN':('a','v'),'NG':('u','b'),
       'NN':('u','v'),'AA':('a','u'),'BV':('b','v'),
       'VW':('v','w')}
EXPECTED={
 'GG':(3*q-2)/q,
 'GN':(3*q**2+5*q*t-2*q-6*t)/(q*(q+2*t)),
 'NG':(2*q*t+3*q-2*t-2)/(q*(t+1)),
 'NN':(2*q**2*t+3*q**2+3*q*t-2*q-6*t)/(q*(q*t+q+2*t)),
 'AA':(q**2+2*q*t-2*t)/(q*t),
 'BV':(5*q*t+4*q-6*t)/(2*q*t),
 'VW':(5*t+4)/(2*t),
}

def reduced_trace(case):
 leaders=CASES[case]
 aa='a' not in leaders
 uu='u' not in leaders
 bb='b' not in leaders
 # remaining right-clique non-gateway vertices
 k=q-1-sum(v in leaders for v in ('v','w'))
 labels=[x for x,active in [('a',aa),('u',uu),('b',bb),('W',True)] if active]
 ix={x:i for i,x in enumerate(labels)}
 M=sp.zeros(len(labels))
 def put(x,y,value):
  if x in ix and y in ix: M[ix[x],ix[y]]=value
 if aa: put('a','a',1+t)
 if uu: put('u','u',1)
 put('a','u',-1);put('u','a',-1)
 if bb: put('b','b',q-1+t)
 put('W','W',q-k)
 if bb:put('b','W',-sp.sqrt(k));put('W','b',-sp.sqrt(k))
 put('a','b',-t);put('b','a',-t)
 return sp.factor(sp.trace(M.inv())+(k-1)/q)

for name in CASES:
 assert sp.cancel(reduced_trace(name)-EXPECTED[name])==0,name

NN=EXPECTED['NN'];NG=EXPECTED['NG']
COMPARISONS={
 'GG-NN': t*(q*q+q+2)/(q*(q*t+q+2*t)),
 'GN-NN': t*(q*q+(q-2)*t)/((q+2*t)*(q*t+q+2*t)),
 'AA-NG': ((q-1)*t+q)/(t*(t+1)),
 'BV-NG': ((q-2)*t*t+(3*q-2)*t+4*q)/(2*q*t*(t+1)),
 'VW-NG': ((q+4)*t*t+(3*q+4)*t+4*q)/(2*q*t*(t+1)),
 'NG-NN': -t*((q-2)*t-(q+2))/(q*(t+1)*(q*t+q+2*t)),
}
for key,rhs in COMPARISONS.items():
 a,b=key.split('-')
 assert sp.cancel(EXPECTED[a]-EXPECTED[b]-rhs)==0,key

def full_trace(Q,T,leader_pair):
 N=Q+2
 L=sp.zeros(N)
 def edge(i,j,w):
  L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
 edge(0,1,sp.Integer(1))
 for i,j in combinations(range(2,N),2):edge(i,j,sp.Integer(1))
 edge(0,2,T)
 keep=[i for i in range(N) if i not in leader_pair]
 return sp.trace(L.extract(keep,keep).inv())

orbits={'GG':(0,2),'GN':(0,3),'NG':(1,2),
        'NN':(1,3),'AA':(0,1),'BV':(2,3),'VW':(3,4)}
checks=0
for Q in range(3,11):
 for T in (sp.Rational(1,7),sp.Rational(3,2),sp.Rational(Q+2,Q-2),sp.Rational(13,2)):
  for name, leaders in orbits.items():
   actual=full_trace(Q,T,leaders)
   assert sp.cancel(actual-EXPECTED[name].subs({q:Q,t:T}))==0,(Q,T,name)
   checks+=1
  best=min(full_trace(Q,T,v) for v in orbits.values())
  target=min(NN.subs({q:Q,t:T}),NG.subs({q:Q,t:T}))
  assert best==target,(Q,T)
print('VERIFIED: 7 symbolic orbit formulas, 6 symbolic exact differences,',checks,'direct rational inverse checks, 32 exhaustive orbit minima.')

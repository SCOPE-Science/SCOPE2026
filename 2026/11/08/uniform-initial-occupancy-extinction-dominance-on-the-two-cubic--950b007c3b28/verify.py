#!/usr/bin/env python3
"""Reproduce the exact six-patch extinction-time comparison."""
from itertools import permutations
import sympy as sp

C=sp.symbols('c')
VERTICES=tuple(range(6))
K33=tuple((i,j) for i in (0,1,2) for j in (3,4,5))
PRISM=((0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5))

# Expected values, independently compared with generated Markov equations.
TK= (1620*C**8+5832*C**7+10548*C**6+13008*C**5+12657*C**4+10952*C**3+6671*C**2+2223*C+294)/(4*(298*C**3+402*C**2+189*C+30))
TP= (45360*C**11+254880*C**10+696960*C**9+1245708*C**8+1659000*C**7+1797048*C**6+1627274*C**5+1182129*C**4+639161*C**3+235641*C**2+52362*C+5292)/(12*(2912*C**6+9848*C**5+14579*C**4+12038*C**3+5813*C**2+1554*C+180))
P=635040*C**11+4620672*C**10+16572996*C**9+37914840*C**8+60557352*C**7+69947220*C**6+58940833*C**5+35930580*C**4+15447328*C**3+4448622*C**2+771816*C+61176
EXPECTED_DIFF=C**3*P/(12*(298*C**3+402*C**2+189*C+30)*(2912*C**6+9848*C**5+14579*C**4+12038*C**3+5813*C**2+1554*C+180))

def all_autos(edges):
 E={frozenset(e) for e in edges}
 return [pm for pm in permutations(VERTICES) if {frozenset((pm[u],pm[v])) for u,v in edges}==E]

def canon(s,perms):
 return min(sum(1<<p[i] for i in VERTICES if s>>i&1) for p in perms)

def quotient(edges):
 autos=all_autos(edges)
 reps={s:canon(s,autos) for s in range(1,64)}
 orbits=sorted(set(reps.values()),key=lambda x:(x.bit_count(),x))
 j={s:i for i,s in enumerate(orbits)}
 mat=sp.zeros(len(orbits))
 for s in orbits:
  r=j[s]
  for u in VERTICES:
   if s>>u&1:
    mat[r,r]+=1
    t=s^(1<<u)
    if t:mat[r,j[reps[t]]]-=1
   else:
    k=sum(1 for x,y in edges if (x==u and s>>y&1) or (y==u and s>>x&1))
    if k:
     mat[r,r]+=k*C
     mat[r,j[reps[s|(1<<u)]]]-=k*C
 return mat,j[reps[63]],len(autos)

# For random initial occupancy uniform among all k-subsets, k=1,...,6.
P1=317520*C**11+2204496*C**10+7498746*C**9+16237422*C**8+24545199*C**7+26873516*C**6+21522422*C**5+12508979*C**4+5142426*C**3+1419420*C**2+236400*C+18000
P2=1587600*C**11+11551680*C**10+41203170*C**9+93417564*C**8+147529767*C**7+168217453*C**6+139767745*C**5+83943616*C**4+35531716*C**3+10067784*C**2+1717224*C+133680
P3=3175200*C**11+23103360*C**10+82864980*C**9+189508680*C**8+302451624*C**7+348919470*C**6+293503963*C**5+178514691*C**4+76531438*C**3+21965682*C**2+3795798*C+299460
EXPECTED_GAPS={1:C**3*P1/(6*(298*C**3+402*C**2+189*C+30)*(2912*C**6+9848*C**5+14579*C**4+12038*C**3+5813*C**2+1554*C+180)),
               2:C**3*P2/(30*(298*C**3+402*C**2+189*C+30)*(2912*C**6+9848*C**5+14579*C**4+12038*C**3+5813*C**2+1554*C+180)),
               3:C**3*P3/(60*(298*C**3+402*C**2+189*C+30)*(2912*C**6+9848*C**5+14579*C**4+12038*C**3+5813*C**2+1554*C+180)),
               4:EXPECTED_DIFF,5:EXPECTED_DIFF,6:EXPECTED_DIFF}

def vector_symbolic(edges):
 M,_,_ = quotient(edges)
 t=M.inv()*sp.ones(M.rows,1)
 perms=all_autos(edges)
 rep={s:canon(s,perms) for s in range(1,64)}
 orbits=sorted(set(rep.values()),key=lambda x:(x.bit_count(),x))
 ids={s:i for i,s in enumerate(orbits)}
 return [sp.cancel(sum(t[ids[rep[s]]] for s in range(1,64) if s.bit_count()==k)/sp.binomial(6,k)) for k in range(1,7)]

def full_numeric(edges,rate):
 M=sp.zeros(63)
 for s in range(1,64):
  r=s-1
  for u in VERTICES:
   if s>>u&1:
    M[r,r]+=1
    t=s^(1<<u)
    if t:M[r,t-1]-=1
   else:
    k=sum(1 for x,y in edges if (x==u and s>>y&1) or (y==u and s>>x&1))
    if k:
     M[r,r]+=rate*k
     M[r,(s|(1<<u))-1]-=rate*k
 v=M.inv()*sp.ones(63,1)
 return [sum(v[s-1] for s in range(1,64) if s.bit_count()==k)/sp.binomial(6,k) for k in range(1,7)]

def main():
 assert len(K33)==len(PRISM)==9
 assert all(sum(u in e for e in edges)==3 for edges in (K33,PRISM) for u in VERTICES)
 for edges, expr, expected_autos, expected_orbits in ((K33,TK,72,9),(PRISM,TP,12,12)):
  M,i,n=quotient(edges)
  assert n==expected_autos and M.rows==expected_orbits
  t=M.inv().row(i).dot(sp.ones(M.rows,1))
  assert sp.cancel(t-expr)==0
  print(f'{expected_orbits}-orbit symbolic full-occupancy solution checked')
 assert sp.cancel(TK-TP-EXPECTED_DIFF)==0
 assert all(x>0 for q in (P,P1,P2,P3) for x in sp.Poly(q,C).all_coeffs())
 assert all(x>0 for x in sp.Poly(sp.denom(TK),C).all_coeffs())
 assert all(x>0 for x in sp.Poly(sp.denom(TP),C).all_coeffs())
 u=vector_symbolic(K33);v=vector_symbolic(PRISM)
 for k in range(1,7):
  assert sp.cancel(u[k-1]-v[k-1]-EXPECTED_GAPS[k])==0, k
  assert sp.cancel((u[k-1]-v[k-1]).subs(C,0))==0
 for edges,expected in ((K33,u),(PRISM,v)):
  for rate in (sp.Rational(1,3),sp.Integer(1),sp.Integer(3)):
   whole=full_numeric(edges,rate)
   assert all(whole[k-1]==sp.cancel(expected[k-1].subs(C,rate)) for k in range(1,7))
 print('24 symbolic k-by-graph identities, six exact 63-state systems and all positivity certificates passed')

if __name__=='__main__':main()

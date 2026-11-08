#!/usr/bin/env python3
"""Independent geometric smoothness tests for each generator orbit representative."""
import runpy
from pathlib import Path
import sympy as sp
f=Path(__file__).with_name('enumerate_tf_pencils.py')
d=runpy.run_path(str(f))
TF=d['TF'];orbits=d['orbits'];pencils=d['pencils'];E=d['E'];V=d['V'];EXPS=d['EXPS'];trans=d['trans'];transform=d['transform']
assert set(TF)=={c for p in pencils for c in p}
X,Y,Z=sp.symbols('X Y Z');v=(X,Y,Z)
def groebner_smooth(code):
 F=sum(TF[code][i]*sp.prod(v[j]**e[j] for j in range(3)) for i,e in enumerate(EXPS))
 for index in range(3):
  subs={v[index]:1}; vars2=[w for j,w in enumerate(v) if j!=index]
  eqs=[sp.expand(p.subs(subs)) for p in [F,sp.diff(F,X),sp.diff(F,Y),sp.diff(F,Z)]]
  b=sp.groebner(eqs,*vars2,modulus=3)
  if tuple(b.polys)==():return False
  if not any(p.as_expr()==1 for p in b.polys):
   print('singular',code,index,[p.as_expr() for p in b.polys]); return False
 return True
cases=sorted({c for p,n in orbits for c in p})
assert all(groebner_smooth(c) for c in cases)
print('SMOOTH_REPRESENTATIVES_PASS',len(cases))
# Every curve belongs to orbit of one representative (verify by generators)
covered=set();groups=[]
for c in cases:
 if c in covered:continue
 orbit={c};frontier=[c]
 while frontier:
  q=frontier.pop()
  for T in trans:
   n=transform(q,T)
   if n not in orbit:orbit.add(n);frontier.append(n)
 covered|=orbit;groups.append((min(orbit),len(orbit)))
assert covered==set(TF)
print('ALL_SMOOTH_PASS',sorted(groups),len(covered))
for p,n in orbits:
 pointprofile=tuple(sorted(d['classify'](TF[c])[1] for c in p))
 bases=[i for i in range(13) if all(sum(a*b for a,b in zip(TF[c],E[i]))%3==0 for c in p)]
 print('PENCIL_REP',p,'profile',pointprofile,'base_count',len(bases),'base_indices',bases)

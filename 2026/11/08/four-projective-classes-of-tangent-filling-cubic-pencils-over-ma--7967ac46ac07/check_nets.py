#!/usr/bin/env python3
"""Exact maximal dimension check for tangent-filling linear systems of ternary cubics."""
import runpy
from pathlib import Path
D=runpy.run_path(str(Path(__file__).with_name('enumerate_tf_pencils.py')))
TF=D['TF'];norm=D['norm'];reps=D['orbits'];
for p,n in reps:
 a,b=TF[p[0]],TF[p[1]]
 U={norm([(i*x+j*y)%3 for x,y in zip(a,b)]) for i in range(3) for j in range(3) if (i,j)!=(0,0)}
 assert U==set(p)
 candidates=0
 for k,c in TF.items():
  if k in U:continue
  candidates+=1
  if all(norm([(v+i*x+j*y)%3 for v,x,y in zip(c,a,b)]) in TF for i in range(3) for j in range(3)):
   raise AssertionError(('unexpected net',p,k))
 print('NO_NET_EXTENSION',p,candidates)
print('NO_TANGENT_FILLING_NETS_PASS')

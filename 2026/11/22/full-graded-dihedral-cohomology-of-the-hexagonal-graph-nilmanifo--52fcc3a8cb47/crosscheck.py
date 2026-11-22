#!/usr/bin/env python3
"""Cross-check the exact character through independently computed invariant subcomplexes."""
import json
from pathlib import Path
P=Path(__file__).parent
main=json.loads((P/'character_output.json').read_text())
identity=json.loads((P/'identity_output.json').read_text())
full=json.loads((P/'invariant_output.json').read_text())
subgroups={tuple(o['subgroup']):o['D_quotient_betti'] for o in json.loads((P/'subgroup_outputs.json').read_text())}
b=main['betti']; q=main['D_quotient_betti']
assert identity['D_quotient_betti']==b
assert full['D_quotient_betti']==q
r6=subgroups[(0,1,2,3,4,5)]
r3=subgroups[(0,2,4)]
r2=subgroups[(0,3)]
re=subgroups[(0,6)]
ro=subgroups[(0,7)]
chars=main['characters']
for k in range(13):
 tr3=(3*r3[k]-b[k])//2
 tr2=2*r2[k]-b[k]
 tr6=(6*r6[k]-b[k]-2*tr3-tr2)//2
 trre=2*re[k]-b[k]
 trro=2*ro[k]-b[k]
 assert 3*r3[k]-b[k]==2*tr3
 assert 6*r6[k]-b[k]-2*tr3-tr2==2*tr6
 for g,t in [((0,1),b[k]),((1,1),tr6),((2,1),tr3),((3,1),tr2),((0,-1),trre),((1,-1),trro)]:
  assert chars[str(g)][k]==t,(g,k,chars[str(g)][k],t)
 assert 12*q[k]==b[k]+2*tr6+2*tr3+tr2+3*trre+3*trro
assert sum(b)==1172 and sum(q)==100
assert b==b[::-1]
assert sum((-1)**k*b[k] for k in range(13))==0
assert all(chars[str((0,-1))][k]==(-1)*chars[str((0,-1))][12-k] for k in range(13))
assert all(chars[str((1,-1))][k]==(-1)*chars[str((1,-1))][12-k] for k in range(13))
print('PASS: all 13 degrees, six conjugacy classes, exact subgroup invariant ranks, character averages, duality')

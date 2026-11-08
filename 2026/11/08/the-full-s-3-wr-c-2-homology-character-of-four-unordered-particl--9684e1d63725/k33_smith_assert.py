"""Exact integer elementary-divisor cross-check using unimodular unit cancellations."""
from integer_pivot_k33 import cancel_unit
from try_k33_4 import differential,bases

expected={1:(494,0),2:(1481,1),3:(1199,0),4:(240,0)}
for k in (1,2,3,4):
 p,remaining,rows=cancel_unit(differential(k),120,verbose=False)
 assert p==expected[k][0],(k,p)
 if k!=2:
  assert not remaining,(k,len(remaining))
  print(f'INTEGER_BOUNDARY_{k}_SNF',f'1^{p}',flush=True)
  continue
 assert len(remaining)==82,(k,len(remaining))
 vectors=list(remaining.values())
 v0=vectors[0]
 assert len(v0)==4 and set(map(abs,v0.values()))=={2},v0
 for v in vectors:
  assert v==v0 or v=={r:-a for r,a in v0.items()},v
 print('INTEGER_BOUNDARY_2_SNF','1^1481, 2^1', 'residual rank 1',flush=True)
print('COMPLETE_INTEGRAL_SMITH_CERTIFICATE_PASS')

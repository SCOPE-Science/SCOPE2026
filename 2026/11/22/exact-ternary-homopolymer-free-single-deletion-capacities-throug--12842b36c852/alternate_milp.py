"""Independent integer-programming cross-check (requires SciPy >=1.9 and NumPy)."""
from itertools import product
import numpy as np
from scipy.sparse import coo_matrix
from scipy.optimize import milp, Bounds, LinearConstraint

expected={2:1,3:3,4:4,5:8,6:12,7:22}
for n,answer in expected.items():
 vocabulary=[''.join(z) for z in product('012',repeat=n)
             if all(z[i]!=z[i+1] for i in range(n-1))]
 incidence={}
 for j,w in enumerate(vocabulary):
  for k in range(n):
   z=w[:k]+w[k+1:]
   incidence.setdefault(z,set()).add(j)
 rs=[];cs=[]
 for r,(v,parents) in enumerate(sorted(incidence.items())):
  for col in parents:rs.append(r);cs.append(col)
 H=coo_matrix((np.ones(len(rs)),(rs,cs)),shape=(len(incidence),len(vocabulary))).tocsr()
 opt=milp(c=-np.ones(len(vocabulary)),integrality=np.ones(len(vocabulary)),
          bounds=Bounds(0,1),constraints=LinearConstraint(H,0,1),
          options={'time_limit':45,'mip_rel_gap':0.0})
 assert opt.status==0 and opt.fun is not None, f'n={n}: MILP not proven optimal: {opt.message}'
 assert abs(opt.fun+answer)<1e-7
 selected=[vocabulary[i] for i,x in enumerate(opt.x) if x>0.5]
 assert len(selected)==answer
 deletions=[{s[:i]+s[i+1:] for i in range(n)} for s in selected]
 assert len(set().union(*deletions))==sum(map(len,deletions))
 print('MILP',n,answer, 'OPTIMAL')
print('ALTERNATE_OK')

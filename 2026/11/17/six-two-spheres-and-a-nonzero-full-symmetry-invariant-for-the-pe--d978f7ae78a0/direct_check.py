"""Independent mod-prime chain rank check of a perfect-matching complex."""
import verify as v
from collections import defaultdict
cells={d:sorted(x for x in v.NONEMPTY if x.bit_count()==d+1) for d in range(5)}
def rank_mod_p(cols,p):
 pivots={}
 for col in cols:
  vec={r:c%p for r,c in col.items() if c%p}
  while vec:
   piv=min(vec)
   if piv not in pivots:
    a=pow(vec[piv],-1,p)
    pivots[piv]={r:(a*c)%p for r,c in vec.items()}
    break
   coeff=vec[piv]
   for r,c in pivots[piv].items():
    new=(vec.get(r,0)-coeff*c)%p
    if new:vec[r]=new
    elif r in vec:del vec[r]
 return len(pivots)
for p in (2,3,5):
 ranks=[0]
 for d in range(1,5):
  prev={f:i for i,f in enumerate(cells[d-1])}
  cols=[{prev[sm]:c for sm,c in v.simplicial_boundary(x).items()} for x in cells[d]]
  ranks.append(rank_mod_p(cols,p))
 betti=[len(cells[d])-(ranks[d] if d else 0)-(ranks[d+1] if d<4 else 0) for d in range(5)]
 print('prime',p,'boundary ranks',ranks,'unreduced betti',betti)
 assert betti==[1,0,6,0,0]

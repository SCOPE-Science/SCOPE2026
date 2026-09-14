import sys; sys.path.insert(0,'output/artifacts')
from qscat import *
import sympy as sp
for (n,p1,p2,N,label) in [
  (2,{0:1},{0:1},5,"1,1 n=2"),
  (2,{1:1,-1:1},{1:1,-1:1},4,"[2],[2] n=2"),
  (1,{1:1,-1:1},{1:1,-1:1},4,"[2],[2] n=1"),
  (2,{0:1},{1:1,-1:1},4,"1,[2] n=2"),
]:
    print("====",label)
    Q,E,bad=solve(n,p1,p2,N)
    for v in sorted(Q):
        q=Q[v]
        print(v,sp.expand(q),"bar:",is_barinv(q),"Lef:",lefschetz_decomp(q))
    print("residual:",{k:str(v) for k,v in bad.items()})

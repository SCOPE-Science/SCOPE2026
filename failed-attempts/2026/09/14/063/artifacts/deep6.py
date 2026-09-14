import sys; sys.path.insert(0,'output/artifacts')
from qscat import *
import sympy as sp
cases=[
 (3,{1:1,-1:1},{1:1,-1:1},5,"[2],[2] n=3"),
 (2,{2:1,0:1,-2:1},{2:1,0:1,-2:1},4,"[3],[3] n=2"),
 (2,{3:1,1:1,-1:1,-3:1},{3:1,1:1,-1:1,-3:1},4,"[4],[4] n=2"),
 (4,{1:1,-1:1},{1:1,-1:1},4,"[2],[2] n=4"),
]
for (n,p1,p2,N,label) in cases:
    print("====",label,flush=True)
    try:
        Q,E,bad=solve(n,p1,p2,N)
    except Exception as e:
        print("SOLVER-FAIL:",type(e).__name__,str(e)[:300]); continue
    for v in sorted(Q):
        q=Q[v]
        print(v,sp.expand(sp.cancel(sp.together(q))),"Lef:",lefschetz_decomp(q),flush=True)
    print("residual:",{k:str(v) for k,v in bad.items()},flush=True)

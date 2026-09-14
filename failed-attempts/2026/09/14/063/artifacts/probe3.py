import sys; sys.path.insert(0,'output/artifacts')
from qscat import *
import sympy as sp
# [3]=t^2+1+t^-2 ; mixed and n=3 attempts with robust laurent conversion
def Qshow(n,p1,p2,N,label):
    print("====",label,flush=True)
    try:
        Q,E,bad=solve(n,p1,p2,N)
    except Exception as e:
        print("SOLVER-FAIL:",type(e).__name__,str(e)[:300]); return
    for v in sorted(Q):
        q=Q[v]
        print(v,sp.expand(q),"bar:",is_barinv(q),"Lef:",lefschetz_decomp(q),flush=True)
    print("residual:",{k:str(v) for k,v in bad.items()},flush=True)
Qshow(2,{2:1,0:1,-2:1},{2:1,0:1,-2:1},3,"[3],[3] n=2")
Qshow(3,{0:1},{0:1},4,"1,1 n=3")
Qshow(3,{1:1,-1:1},{1:1,-1:1},3,"[2],[2] n=3")

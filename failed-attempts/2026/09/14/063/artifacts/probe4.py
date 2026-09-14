import sys; sys.path.insert(0,'output/artifacts')
from qscat import *
import sympy as sp
def Qshow(n,p1,p2,N,label):
    print("====",label,flush=True)
    try:
        Q,E,bad=solve(n,p1,p2,N)
    except Exception as e:
        print("SOLVER-FAIL:",type(e).__name__,str(e)[:400]); return
    for v in sorted(Q):
        q=Q[v]
        print(v,sp.expand(sp.cancel(sp.together(q))),"bar:",is_barinv(q),"Lef:",lefschetz_decomp(q),flush=True)
    print("residual:",{k:str(v) for k,v in bad.items()},flush=True)
# [4]=t^3+t+t^-1+t^-3 ; [5]=t^4+t^2+1+t^-2+t^-4
Qshow(2,{3:1,1:1,-1:1,-3:1},{3:1,1:1,-1:1,-3:1},3,"[4],[4] n=2")
Qshow(3,{3:1,1:1,-1:1,-3:1},{3:1,1:1,-1:1,-3:1},3,"[4],[4] n=3")
Qshow(4,{0:1},{0:1},4,"1,1 n=4")
Qshow(4,{1:1,-1:1},{1:1,-1:1},3,"[2],[2] n=4")

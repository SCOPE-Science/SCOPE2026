# Restricted cobar: exclude \bar x (deg1, dual of Sq^1) factors.
# b'_d = b_d minus [d==1]. Then C'^s dims; bidegree census (s,stem).
from collections import defaultdict
b={0:0,1:1,2:1,3:2,4:2,5:2,6:3,7:4,8:3,9:4,10:5,11:4,12:4,13:5,14:4,15:3,16:4,17:3,18:2,19:2,20:2,21:1,22:1,23:1}
bp=dict(b); bp[1]=0
def conv(a,c):
    r=[0]*(len(a)+len(c)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(c):
            r[i+j]+=x*y
    return r
N=24
P=[bp.get(d,0) for d in range(N)]
print("restricted b'_d:", {d:bp.get(d,0) for d in range(12)})
Pw=[1]
import math
for s in range(1,8):
    Pw=conv(Pw,P)
    print(f"--- s={s}")
    for stem in [52,53,54,55,56]:
        t=stem+s
        dim=Pw[t] if t < len(Pw) else 0
        print(f"  stem {stem} (t={t}): dim C'^s_t = {dim}")
# Column A: total restricted cells per stem
from collections import defaultdict
tot=defaultdict(int)
Pw2=[1]
Pws=[[1]]
for s in range(1,8):
    Pw2=conv(Pw2,P); Pws.append(list(Pw2))
for stem in [52,53,54,55,56]:
    tot=sum(Pws[s][stem+s] if stem+s < len(Pws[s]) else 0 for s in range(1,8))
    print("stem",stem,"total restricted cells s=1..7:",tot)
# Column B crude: h0-families via h0-free quotient dims rho(t-s,s)
# rho = coefficient of (1-u)^-1 * P ~ cumulative; report pairing count bound

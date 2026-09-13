import numpy as np, sys, time
sys.path.insert(0,'output/artifacts')
from delta import Delta
t0=time.time()
def maxratio(x, menu, N=14):
    best=0.0
    for (a,b) in menu:
        best=max(best, abs(Delta(x,a,b,N=N))/abs(a*b))
    return best
# candidate menu: 4 signs at scale 0.03
menu4=[(0.03,0.03),(0.03,-0.03),(-0.03,0.03),(-0.03,-0.03)]
menu8=menu4+[(0.015,0.015),(0.015,-0.015),(-0.015,0.015),(-0.015,-0.015)]
for name,menu in [("menu4",menu4),("menu8",menu8)]:
    n=100; xs=np.linspace(0,1,n,endpoint=False)
    mn=1e9; arg=None
    for i in range(n):
        for j in range(n):
            v=maxratio(np.array([xs[i],xs[j]]),menu)
            if v<mn: mn=v; arg=(xs[i],xs[j])
    print(name,"gridmin",mn,"at",arg,"time",time.time()-t0)

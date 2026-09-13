import numpy as np, sys
sys.path.insert(0,'output/artifacts')
from delta import Delta
def Kof(x, h=0.003, N=14):
    x=np.asarray(x)%1.0
    return (Delta(x,h,h,N=N)-Delta(x,h,-h,N=N)-Delta(x,-h,h,N=N)+Delta(x,-h,-h,N=N))/(4*h*h)
# simple coordinate descent
x=np.array([1/6,0.5667]); print("K0",Kof(x))
step=0.01
for it in range(60):
    improved=False
    for d in [np.array([1.,0.]),np.array([0.,1.])]:
        for s in [step,-step]:
            v=Kof(x+s*d)
            if v**2 < Kof(x)**2:
                x=x+s*d; improved=True
    if not improved: step*=0.5
    if step<1e-7: break
print("xmin",x,"K",Kof(x),"K(h=0.002)",Kof(x,h=0.002),"K(h=0.0015)",Kof(x,h=0.0015))
for s in np.linspace(-0.02,0.02,9):
    print(round(float(s),4), Kof(x+s*np.array([1.,0.3])))

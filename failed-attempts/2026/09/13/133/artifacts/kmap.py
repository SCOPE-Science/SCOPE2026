import numpy as np, sys
sys.path.insert(0,'output/artifacts')
from delta import Delta
# robust K via Richardson: K_h = (D(h,h)-D(h,-h)-D(-h,h)+D(-h,-h))/4h^2
n=60; xs=np.linspace(0,1,n,endpoint=False)
def Kof(x):
    h=0.003
    return (Delta(x,h,h,N=14)-Delta(x,h,-h,N=14)-Delta(x,-h,h,N=14)+Delta(x,-h,-h,N=14))/(4*h*h)
K=np.zeros((n,n))
for i in range(n):
  for j in range(n):
    K[i,j]=Kof(np.array([xs[i],xs[j]]))
print("min|K|",np.abs(K).min(),"at",np.unravel_index(np.argmin(np.abs(K)),K.shape))
print("pct",np.percentile(np.abs(K),[0,1,5,25,50,75,100]))
# refine around minimizer
i0,j0=np.unravel_index(np.argmin(np.abs(K)),K.shape)
for di in range(-2,3):
  for dj in range(-2,3):
    x=np.array([xs[(i0+di)%n],xs[(j0+dj)%n]])
    print(round(x[0],4),round(x[1],4),Kof(x))
np.save('output/artifacts/K60.npy',K)

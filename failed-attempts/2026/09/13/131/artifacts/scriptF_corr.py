"""Script F: correlation decay by orbit averaging (INDICATIVE): time averages along long
orbits + ensemble; observables with genuine projection onto unstable directions."""
import numpy as np, math
Amat=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
a,b=0.03,0.02
def f(x):
    z=np.stack([x[...,0]+a*np.sin(2*np.pi*x[...,1]),x[...,1]+b*np.sin(2*np.pi*x[...,2]),x[...,2]],axis=-1)%1
    return (z@Amat.T)%1
rng=np.random.default_rng(11)
X=rng.random((200000,3))
N=12
PH=np.zeros((N+1,200000)); PS=np.zeros((N+1,200000))
PH[0]=np.sin(2*np.pi*(X[:,0]+2*X[:,1]))+np.cos(2*np.pi*(X[:,1]-X[:,2]))
PS[0]=np.cos(2*np.pi*(2*X[:,0]+X[:,1]))+np.sin(2*np.pi*(X[:,1]+X[:,2]))
Xn=X.copy()
for n in range(1,N+1):
    Xn=f(Xn)
    PH[n]=np.sin(2*np.pi*(Xn[:,0]+2*Xn[:,1]))+np.cos(2*np.pi*(Xn[:,1]-Xn[:,2]))
    PS[n]=np.cos(2*np.pi*(2*Xn[:,0]+Xn[:,1]))+np.sin(2*np.pi*(Xn[:,1]+Xn[:,2]))
print("means:",PH.mean(),PS.mean())
for lag in range(9):
    c=np.mean(PH[0]*PS[lag])-np.mean(PH[0])*np.mean(PS[lag])
    print(f"lag {lag}: C={c:+.5f}")

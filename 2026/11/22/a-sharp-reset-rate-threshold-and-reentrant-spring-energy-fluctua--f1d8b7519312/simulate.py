"""Independent exact-interreset Gaussian simulator for a reset Brownian spring pair."""
import numpy as np

def simulate(r,g,num=5000,burn=2000,take=100,seed=314159):
    rng=np.random.default_rng(seed)
    P=np.array([[1,g],[1,g]])/(g+1)
    J=np.eye(2)-P
    rootD=np.diag([1,1/np.sqrt(g)])
    PD=P@rootD; JD=J@rootD
    lam=1+1/g
    y=np.zeros(num)
    w=[]
    for h in range(burn+take):
        tt=rng.exponential(1/r,num)
        z=np.exp(-lam*tt)
        source=np.vstack([np.zeros(num),y])
        deterministic=P@source+z*(J@source)
        rand0=rng.normal(size=(2,num));rand1=rng.normal(size=(2,num))
        out=deterministic+np.sqrt(2*tt)*(PD@rand0)+np.sqrt(-np.expm1(-2*lam*tt)/lam)*(JD@rand1)
        if h>=burn:
            x=out[0]
            w.append((x*out[1]-x*x/2))
        y=out[1]
    w=np.concatenate(w)
    return w.mean(),w.var()/w.mean()**2

if __name__=='__main__':
    for g in (.1,.5,1,10):
        mu,c=simulate(.5,g,burn=500)
        print('r=.5, g=',g,'sample work mean',round(mu,5),'CV^2',round(c,5))

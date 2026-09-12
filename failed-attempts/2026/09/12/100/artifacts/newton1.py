"""Newton search for period-1 Poincare fixed point at H0=-10."""
import numpy as np
g=9.81
def f(state):
    th1,th2,w1,w2 = state
    D = 3.0 - np.cos(2*(th1-th2)); d = th1-th2
    a1 = (-g*3*np.sin(th1) - g*np.sin(th1-2*th2) - 2*np.sin(d)*(w2*w2 + w1*w1*np.cos(d)))/D
    a2 = (2*np.sin(d)*(2*w1*w1 + 2*g*np.cos(th1) + w2*w2*np.cos(d)))/D
    return np.array([w1,w2,a1,a2])
def rk4_step(s, dt):
    k1=f(s); k2=f(s+0.5*dt*k1); k3=f(s+0.5*dt*k2); k4=f(s+dt*k3)
    return s+dt/6*(k1+2*k2+2*k3+k4)
H0=-10.0
def w2branch(th2,w1,branch=+1):
    V=-19.62*np.cos(0.0)-9.81*np.cos(th2); c=np.cos(-th2)
    a=0.5;b=w1*c;cc=w1*w1+V-H0
    disc=b*b-4*a*cc
    if disc<0: return None
    return (-b+branch*np.sqrt(disc))/(2*a)
def full(th2,w1,branch=+1):
    w2=w2branch(th2,w1,branch)
    return np.array([0.0,th2,w1,w2]) if w2 is not None else None
def pmap(x,branch=+1,dt=0.0005,maxT=60):
    s0=full(x[0],x[1],branch)
    if s0 is None: return None
    s=s0.copy(); prev=s.copy(); t=0; n=int(maxT/dt)
    for i in range(n):
        s=rk4_step(s,dt); t+=dt
        if prev[0]<0 and s[0]>=0 and s[2]>0 and t>0.5:
            a=-prev[0]/(s[0]-prev[0]); sc=prev+a*(s-prev)
            # project to energy: adjust w2? just return section coords
            return np.array([sc[1],sc[2]]),t
        prev=s.copy()
    return None

def residual(x,branch=+1):
    r=pmap(x,branch)
    if r is None: return None,None
    y,t=r; return y-x,t

# coarse scan of |P(x)-x| to find basin
best=[]
for th2 in np.linspace(-1.2,1.2,25):
    for w1 in np.linspace(1.0,4.5,29):
        x=np.array([th2,w1])
        r=pmap(x)
        if r is None: continue
        y,t=r
        # wrap th2 diff
        d=np.array([((y[0]-x[0]+np.pi)%(2*np.pi))-np.pi, y[1]-x[1]])
        n=np.linalg.norm(d)
        best.append((n,th2,w1,t))
best.sort()
for b in best[:15]: print("%.4f th2=%.3f w1=%.3f T=%.3f"%b)

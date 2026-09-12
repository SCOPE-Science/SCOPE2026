"""Section maps + search for periodic orbit at H0=-10."""
import numpy as np
g=9.81
def f(state):
    th1,th2,w1,w2 = state
    D = 3.0 - np.cos(2*(th1-th2))
    d = th1-th2
    a1 = (-g*3*np.sin(th1) - g*np.sin(th1-2*th2) - 2*np.sin(d)*(w2*w2 + w1*w1*np.cos(d)))/D
    a2 = (2*np.sin(d)*(2*w1*w1 + 2*g*np.cos(th1) + w2*w2*np.cos(d)))/D
    return np.array([w1,w2,a1,a2])
def rk4_step(s, dt):
    k1=f(s); k2=f(s+0.5*dt*k1); k3=f(s+0.5*dt*k2); k4=f(s+dt*k3)
    return s+dt/6*(k1+2*k2+2*k3+k4)
def energy_of(s):
    th1,th2,w1,w2=s
    return w1*w1+0.5*w2*w2+w1*w2*np.cos(th1-th2)-19.62*np.cos(th1)-9.81*np.cos(th2)

def section_returns(s0, nret=12, dt=0.0005, maxT=200, section='th1'):
    s=np.array(s0,float); prev=s.copy(); out=[]; t=0
    n=int(maxT/dt)
    for i in range(n):
        s=rk4_step(s,dt); t+=dt
        if section=='th1':
            if prev[0]<0 and s[0]>=0 and s[2]>0:
                a=-prev[0]/(s[0]-prev[0]); sc=prev+a*(s-prev)
                out.append((t,sc.copy()))
                if len(out)>=nret: break
        prev=s.copy()
    return out

H0=-10.0
def w2e(th1,th2,w1):
    V=-19.62*np.cos(th1)-9.81*np.cos(th2); c=np.cos(th1-th2)
    a=0.5;b=w1*c;cc=w1*w1+V-H0
    disc=b*b-4*a*cc
    return (-b+np.sqrt(max(disc,0)))/(2*a) if disc>=0 else None

for w1 in [3.0,3.2,3.4,3.6,3.8,4.0]:
    for th2 in [0.0,0.3,0.6]:
        w2=w2e(0.0,th2,w1)
        if w2 is None: continue
        s0=np.array([0.0,th2,w1,w2])
        rets=section_returns(s0,nret=6,maxT=60)
        if len(rets)>=3:
            print(f"th2={th2} w1={w1} w2={w2:.4f} nret={len(rets)}")
            for t,sc in rets[:4]:
                print(f"   t={t:.4f} th2={sc[1]:.4f} w1={sc[2]:.4f} w2={sc[3]:.4f} E={energy_of(sc):.6f} wrap2={((sc[1]+np.pi)%(2*np.pi))-np.pi:.4f}")

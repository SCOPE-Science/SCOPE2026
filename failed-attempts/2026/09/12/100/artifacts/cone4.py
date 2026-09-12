"""Tighten: measure ACTUAL DP variation on small boxes (not global L*r) + use r=1e-4 box."""
import numpy as np
import sys
g=9.81
def f(s):
    th1,th2,w1,w2=s
    Dd=3.0-np.cos(2*(th1-th2)); d=th1-th2
    a1=(-g*3*np.sin(th1)-g*np.sin(th1-2*th2)-2*np.sin(d)*(w2*w2+w1*w1*np.cos(d)))/Dd
    a2=(2*np.sin(d)*(2*w1*w1+2*g*np.cos(th1)+w2*w2*np.cos(d)))/Dd
    return np.array([w1,w2,a1,a2])
def rk4(s,dt):
    k1=f(s);k2=f(s+0.5*dt*k1);k3=f(s+0.5*dt*k2);k4=f(s+dt*k3)
    return s+dt/6*(k1+2*k2+2*k3+k4)
H0=-10.0
def w2b(th2,w1):
    V=-19.62-9.81*np.cos(th2);c=np.cos(th2)
    disc=(w1*c)**2-2*(w1*w1+V-H0)
    return (-w1*c+np.sqrt(disc)) if disc>=0 else None
def Pmap(x,dt=0.000125):
    s0=np.array([0.0,x[0],x[1],w2b(x[0],x[1])]);s=s0.copy();prev=s.copy();t=0
    n=int(60/dt)
    for i in range(n):
        s=rk4(s,dt);t+=dt
        if prev[0]<0 and s[0]>=0 and s[2]>0 and t>0.5:
            a=-prev[0]/(s[0]-prev[0]);sc=prev+a*(s-prev)
            return np.array([sc[1],sc[2]]),t
        prev=s.copy()
    return None
def DP_fd(x,dt=0.000125,r=2e-5):
    DPm=np.zeros((2,2))
    for j in range(2):
        e=np.zeros(2);e[j]=r
        yp,_=Pmap(x+e,dt);ym,_=Pmap(x-e,dt)
        DPm[:,j]=np.array([((yp[0]-ym[0]+np.pi)%(2*np.pi))-np.pi,yp[1]-ym[1]])/(2*r)
    return DPm
DPstar=np.load('output/artifacts/DPstar.npy');xstar=np.load('output/artifacts/xstar.npy')
ev,V=np.linalg.eig(DPstar)
iu=np.argmax(np.abs(ev));is_=1-iu
eu=np.real(V[:,iu]);eu/=np.linalg.norm(eu);es=np.real(V[:,is_]);es/=np.linalg.norm(es)
S=np.column_stack([eu,es]);Si=np.linalg.inv(S)
lamu=abs(float(np.real(ev[iu])));lams=abs(float(np.real(ev[is_])))
D0=np.real(Si@DPstar@S)
print("D0=",D0,"lamu",lamu,"lams",lams)
# actual max deviation in eigenbasis coords over box r
for r in [1e-4,2e-4,5e-4]:
    mx=0;mxinv=None
    worst=None
    for a in np.linspace(-1,1,9):
        for b in np.linspace(-1,1,9):
            x=xstar+r*np.array([a,b])
            D2=DP_fd(x)
            E=np.real(Si@(D2-DPstar)@S)
            n=np.linalg.norm(E,2)
            if n>mx: mx=n; worst=x
    print(f"r={r}: max|E|_2 over 81-pt grid = {mx:.5f}")
    e=mx*1.5  # safety factor for grid->sup
    print(f"   with x1.5 safety e={e:.5f}")
    # forward cone
    for gmm in [0.1,0.2]:
        num=lams*gmm+e*(1+gmm);den=lamu-e*(1+gmm)
        print(f"   fwd g={gmm}: slope={num/den:.4f} mu={lamu-e*(1+gmm):.3f}")
    # backward: dInv bound
    s0=lams
    if e<s0:
        Ni=1/(s0-e);dInv=Ni*e*(1/lams)
        print(f"   dInv={dInv:.4f}")
        for gmm in [0.2,0.3,0.4]:
            num=(1/lamu)*gmm+dInv*(1+gmm);den=(1/lams)-dInv*(1+gmm)
            print(f"   back g={gmm}: slope={num/den if den>0 else np.inf:.4f} mu={1/lams-dInv*(1+gmm):.3f}")
    else: print("   e>=s0, shrink box")

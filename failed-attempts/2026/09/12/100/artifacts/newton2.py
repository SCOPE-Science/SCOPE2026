"""Newton polish on Poincare fixed points; variational matrix -> multipliers."""
import numpy as np
g=9.81
def f(state):
    th1,th2,w1,w2 = state
    D = 3.0 - np.cos(2*(th1-th2)); d = th1-th2
    a1 = (-g*3*np.sin(th1) - g*np.sin(th1-2*th2) - 2*np.sin(d)*(w2*w2 + w1*w1*np.cos(d)))/D
    a2 = (2*np.sin(d)*(2*w1*w1 + 2*g*np.cos(th1) + w2*w2*np.cos(d)))/D
    return np.array([w1,w2,a1,a2])
def Df(state):
    h=1e-7; n=4; J=np.zeros((4,4)); f0=f(state)
    for j in range(n):
        e=np.zeros(n); e[j]=h; J[:,j]=(f(state+e)-f(state-e))/(2*h)
    return J
def rk4_step_aug(s,Phi,dt):
    k1=f(s); J1=Df(s)
    s2=s+0.5*dt*k1; J2=Df(s2)
    s3=s+0.5*dt*(f(s2)); J3=Df(s3)
    s4=s+dt*f(s3); J4=Df(s4)
    k2=f(s2); k3=f(s3); k4=f(s4)
    snew=s+dt/6*(k1+2*k2+2*k3+k4)
    # propagate Phi with RK4 on time-varying linear system (freeze approx via Simpson of J*Phi)
    A1=J1@Phi; A2=J2@(Phi+0.5*dt*A1); A3=J3@(Phi+0.5*dt*A2); A4=J4@(Phi+dt*A3)
    Phinew=Phi+dt/6*(A1+2*A2+2*A3+A4)
    return snew,Phinew
H0=-10.0
def w2branch(th2,w1,branch=+1):
    V=-19.62-9.81*np.cos(th2); c=np.cos(th2)
    a=0.5;b=w1*c;cc=w1*w1+V-H0
    disc=b*b-4*a*cc
    if disc<0: return None
    return (-b+branch*np.sqrt(disc))/(2*a)
def full(x,branch=+1):
    w2=w2branch(x[0],x[1],branch)
    return np.array([0.0,x[0],x[1],w2]) if w2 is not None else None
def pmap_aug(x,dt=0.00025,maxT=60):
    s0=full(x)
    if s0 is None: return None
    s=s0.copy(); Phi=np.eye(4); prev=s.copy(); PhiP=Phi.copy(); t=0
    n=int(maxT/dt)
    for i in range(n):
        s,Phi=rk4_step_aug(s,Phi,dt); t+=dt
        if prev[0]<0 and s[0]>=0 and s[2]>0 and t>0.5:
            # linear interpolation factor
            a=-prev[0]/(s[0]-prev[0])
            # need prev Phi: store each step
            sc=prev+a*(s-prev)
            # approximate Phi at crossing
            # recompute: linear interp between PhiP and Phi
            Phic=PhiP+a*(Phi-PhiP)
            v=f(sc)
            # section correction: D P = Pi (I - v e1^T / v1) Phi restricted; section coords (th2,w1)
            v1=v[0]
            M=(np.eye(4)-np.outer(v,[1,0,0,0])/v1)@Phic
            # rows for (th2(idx1), w1(idx2))
            DP=np.array([[M[1,1],M[1,2]],[M[2,1],M[2,2]]])
            y=np.array([sc[1],sc[2]])
            return y,t,DP,sc
        prev=s.copy(); PhiP=Phi.copy()
    return None
def newton(x0,nit=12,eps=1e-6):
    x=np.array(x0,float)
    for it in range(nit):
        r=pmap_aug(x)
        if r is None: print("lost"); return x
        y,t,DP,sc=r
        d=np.array([((y[0]-x[0]+np.pi)%(2*np.pi))-np.pi, y[1]-x[1]])
        print(f"it{it} x=({x[0]:.6f},{x[1]:.6f}) res=({d[0]:.3e},{d[1]:.3e}) T={t:.5f} Edev={(sc[2]**2+0.5*sc[3]**2+sc[2]*sc[3]*np.cos(sc[0]-sc[1])-19.62*np.cos(sc[0])-9.81*np.cos(sc[1]))-H0:.2e}")
        if np.linalg.norm(d)<1e-10: return x
        J=DP-np.eye(2)
        try: dx=np.linalg.solve(J,-d)
        except: print("sing"); return x
        # wrap th2 update
        x=x+dx; x[0]=((x[0]+np.pi)%(2*np.pi))-np.pi
        if np.linalg.norm(dx)<1e-12: return x
    return x

for guess in [(-0.8,3.375),(0.0,1.125),(0.9,3.125)]:
    print("=== guess",guess)
    x=newton(guess)
    print("final",x)
    r=pmap_aug(x)
    if r is not None:
        y,t,DP,sc=r
        ev=np.linalg.eigvals(DP)
        print("DP=",DP,"eig=",ev,"|eig|=",np.abs(ev),"T=",t)

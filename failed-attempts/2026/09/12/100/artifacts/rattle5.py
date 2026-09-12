"""Unit test RATTLE impl on 1-pendulum (1 constraint) vs exact; then 2-pendulum with standard formulas."""
import numpy as np
g=9.81
# --- single pendulum length 1 mass 1: q=(x,y), g=|q|^2-1 ---
def rattle1(q,p,h):
    pn=p-0.5*h*np.array([0,g])
    # position: q1 = q+h pn + (h^2/2)(2q)lam = q+h pn + h^2 q lam; |q1|^2=1
    a=h*h*np.dot(q,q);b=2*np.dot(q,q+h*pn);c=np.dot(q+h*pn,q+h*pn)-1
    lam=(-b+np.sqrt(b*b-4*a*c))/(2*a)
    q1=q+h*pn+h*h*q*lam
    p1h=pn+0.5*h*(2*q*lam)
    G1=2*q1
    mu=np.dot(G1,p1h)/np.dot(G1,G1)
    p1=p1h-G1*mu
    return q1,p1
# exact single pendulum
def exact1(q0,p0,T):
    import math
    th=np.arctan2(q0[0],-q0[1]);w=p0[0]*np.cos(th)+p0[1]*np.sin(th)
    s=np.array([th,w]);dt=1e-5;n=int(T/dt)
    for i in range(n):
        def F(s): return np.array([s[1],-g*np.sin(s[0])])
        k1=F(s);k2=F(s+0.5*dt*k1);k3=F(s+0.5*dt*k2);k4=F(s+dt*k3)
        s=s+dt/6*(k1+2*k2+2*k3+k4)
    q=np.array([np.sin(s[0]),-np.cos(s[0])]);p=np.array([np.cos(s[0]),np.sin(s[0])])*s[1]
    return q,p
q0=np.array([0.0,-1.0]);p0=np.array([3.0,0.0])
for h in [0.005,0.002,0.001]:
    q1,p1=rattle1(q0,p0,h)
    qr,pr=exact1(q0,p0,h)
    print(f"h={h}: 1-pend local err={np.linalg.norm(np.concatenate([q1-qr,p1-pr])):.4e} ~h^3? {np.linalg.norm(np.concatenate([q1-qr,p1-pr]))/h**3:.2f}")
# --- now double pendulum: write RATTLE per Hairer Lubich Wanner: solve position constraint by Newton on FULL q1 with G(q)^T lam, check lambda scaling
exec(open('output/artifacts/rattle1.py').read().split("def rattle_step")[0].split("g=9.81",1)[1])

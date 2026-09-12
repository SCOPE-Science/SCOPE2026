"""Cone field certification: eigenbasis boxes; Lipschitz of DP; rigorous-ish enclosure via sampling bounds."""
import numpy as np
DP=np.load('output/artifacts/DPstar.npy')
xstar=np.load('output/artifacts/xstar.npy')
print("x*=",xstar,"\nDP=",DP)
ev,V=np.linalg.eig(DP)
print("eig:",ev)
iu=np.argmax(np.abs(ev));is_=1-iu
lamu=ev[iu];lams=ev[is_]
print("lamu",lamu,"lams",lams)
vu=np.real(V[:,iu]);vs=np.real(V[:,is_])
print("vu",vu,"vs",vs)
# normalize
eu=vu/np.linalg.norm(vu);es=vs/np.linalg.norm(vs)
print("eu",eu,"es",es)
# cone: |eta|<=gamma|xi| in (xi,eta) coords along (eu,es). Compute image cone slope bound.
# write DP in eigenbasis: D = [[a,b],[c,d]] with x=xi eu+eta es
S=np.column_stack([eu,es]);Si=np.linalg.inv(S)
D=np.real(Si@DP@S)
print("D in eigenbasis (should be ~diag):",D)
# Lipschitz constant of DP: need bound on second derivatives. Estimate via FD Hessian sampling.
import sys
sys.path.insert(0,'output/artifacts')
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
# sample DP over box radius r; bound Lipschitz L = max |DP(x)-DP(x*)|/r
for r in [1e-4,3e-4,1e-3,3e-3]:
    mx=0
    for a in np.linspace(-1,1,5):
        for b in np.linspace(-1,1,5):
            x=xstar+r*np.array([a,b])
            D2=DP_fd(x)
            mx=max(mx,np.linalg.norm(D2-DP,2))
    print(f"r={r} max|DP-DP*|_2={mx:.4e} L~{mx/r:.4e}")

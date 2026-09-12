"""Polish fixed point A with central-difference DP (trajectory only), small dt."""
import numpy as np
g=9.81
def f(s):
    th1,th2,w1,w2=s
    D=3.0-np.cos(2*(th1-th2)); d=th1-th2
    a1=(-g*3*np.sin(th1)-g*np.sin(th1-2*th2)-2*np.sin(d)*(w2*w2+w1*w1*np.cos(d)))/D
    a2=(2*np.sin(d)*(2*w1*w1+2*g*np.cos(th1)+w2*w2*np.cos(d)))/D
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
            return np.array([sc[1],sc[2]]),t,sc
        prev=s.copy()
    return None
def DP_fd(x,dt=0.000125,r=2e-5):
    y0,_,_=Pmap(x,dt)
    DP=np.zeros((2,2))
    for j in range(2):
        e=np.zeros(2);e[j]=r
        yp,_,_=Pmap(x+e,dt);ym,_,_=Pmap(x-e,dt)
        # wrap angle comp for diffs
        d1=((yp[0]-ym[0]+np.pi)%(2*np.pi))-np.pi
        DP[:,j]=np.array([d1,yp[1]-ym[1]])/(2*r)
    return DP,y0
x=np.array([-0.86787701,3.29962211])
for it in range(8):
    DP,y0=DP_fd(x)
    d=np.array([((y0[0]-x[0]+np.pi)%(2*np.pi))-np.pi,y0[1]-x[1]])
    print(f"it{it} x=({x[0]:.9f},{x[1]:.9f}) |d|={np.linalg.norm(d):.3e}")
    if np.linalg.norm(d)<3e-12: break
    x=x+np.linalg.solve(DP-np.eye(2),-d);x[0]=((x[0]+np.pi)%(2*np.pi))-np.pi
print("x*=",x)
DP,y0=DP_fd(x)
print("resid:",y0-x,"DP=",DP)
ev,EV=np.linalg.eig(DP)
print("eig:",ev,"abs:",np.abs(ev))
# dt sensitivity
for dt in [0.00025,0.000125,0.0000625]:
    DP2,y2=DP_fd(x,dt=dt)
    print(f"dt={dt} resid={np.linalg.norm(y2-x):.3e} eigabs={np.abs(np.linalg.eigvals(DP2))}")
np.save('output/artifacts/xstar.npy',x);np.save('output/artifacts/DPstar.npy',DP)

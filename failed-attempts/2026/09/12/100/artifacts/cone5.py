"""FAST bounded test: DP variation on r=2e-4 box (dt=5e-4, 5x5 grid) + flow L and log-norm on tube."""
import numpy as np, time
t0=time.time()
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
DT=0.0005
def Pmap(x):
    s0=np.array([0.0,x[0],x[1],w2b(x[0],x[1])]);s=s0.copy();prev=s.copy();t=0
    n=int(60/DT)
    for i in range(n):
        s=rk4(s,DT);t+=DT
        if prev[0]<0 and s[0]>=0 and s[2]>0 and t>0.5:
            a=-prev[0]/(s[0]-prev[0]);sc=prev+a*(s-prev)
            return np.array([sc[1],sc[2]]),t,sc
        prev=s.copy()
    return None
def DP_fd(x,r=2e-5):
    DPm=np.zeros((2,2))
    for j in range(2):
        e=np.zeros(2);e[j]=r
        yp,_,_=Pmap(x+e);ym,_,_=Pmap(x-e)
        DPm[:,j]=np.array([((yp[0]-ym[0]+np.pi)%(2*np.pi))-np.pi,yp[1]-ym[1]])/(2*r)
    return DPm
DPstar=np.load('output/artifacts/DPstar.npy');xstar=np.load('output/artifacts/xstar.npy')
ev,V=np.linalg.eig(DPstar)
iu=np.argmax(np.abs(ev));is_=1-iu
eu=np.real(V[:,iu]);eu/=np.linalg.norm(eu);es=np.real(V[:,is_]);es/=np.linalg.norm(es)
S=np.column_stack([eu,es]);Si=np.linalg.inv(S)
lamu=abs(float(np.real(ev[iu])));lams=abs(float(np.real(ev[is_])))
print("lamu=%.5f lams=%.5f residual_P=%.2e"%(lamu,lams,np.linalg.norm(Pmap(xstar)[0]-xstar)),flush=True)
for r in [2e-4,5e-4]:
    mx=0
    for a in np.linspace(-1,1,5):
        for b in np.linspace(-1,1,5):
            x=xstar+r*np.array([a,b])
            E=np.real(Si@(DP_fd(x)-DPstar)@S)
            mx=max(mx,np.linalg.norm(E,2))
    e=mx*2.0
    print(f"BOX r={r}: gridmax|E|={mx:.5f} e(safe x2)={e:.5f}",flush=True)
    for gmm in [0.2,0.3]:
        num=lams*gmm+e*(1+gmm);den=lamu-e*(1+gmm)
        print(f"  fwd g={gmm}: slope={num/den:.4f}<=?{gmm} mu={lamu-e*(1+gmm):.3f}",flush=True)
    s0=lams
    if e<s0:
        Ni=1/(s0-e);dInv=Ni*e*(1/lams)
        for gmm in [0.3,0.4]:
            num=(1/lamu)*gmm+dInv*(1+gmm);den=(1/lams)-dInv*(1+gmm)
            print(f"  back g={gmm}: slope={num/den:.4f}<=?{gmm} mu={1/lams-dInv*(1+gmm):.3f}",flush=True)
    print("  elapsed %.0fs"%(time.time()-t0),flush=True)
# flow Lipschitz + log norm on tube around orbit
def Df_fd(s,h=1e-7):
    J=np.zeros((4,4))
    for j in range(4):
        e=np.zeros(4);e[j]=h
        J[:,j]=(f(s+e)-f(s-e))/(2*h)
    return J
sA=np.array([0.0,xstar[0],xstar[1],w2b(xstar[0],xstar[1])])
s=sA.copy();Lmax=0;mumax=-1e9;n=int(2.87125/0.002)
for i in range(n):
    for pert in [np.zeros(4)]:
        J=Df_fd(s+pert)
        Lmax=max(Lmax,np.linalg.norm(J,2))
        mumax=max(mumax,np.linalg.eigvalsh((J+J.T)/2).max())
    s=rk4(s,0.002)
print("tube: operator L<=%.3f lognorm mu<=%.3f elapsed %.0fs"%(Lmax,mumax,time.time()-t0),flush=True)

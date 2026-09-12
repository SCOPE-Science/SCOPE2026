"""Measure: sup_t ||D Phi_t|| over period, sup|f|, transversality, Hessian bound on tube."""
import numpy as np, time
t0=time.time()
g=9.81
def f(s):
    th1,th2,w1,w2=s
    Dd=3.0-np.cos(2*(th1-th2)); d=th1-th2
    a1=(-g*3*np.sin(th1)-g*np.sin(th1-2*th2)-2*np.sin(d)*(w2*w2+w1*w1*np.cos(d)))/Dd
    a2=(2*np.sin(d)*(2*w1*w1+2*g*np.cos(th1)+w2*w2*np.cos(d)))/Dd
    return np.array([w1,w2,a1,a2])
def Df_fd(s,h=1e-8):
    J=np.zeros((4,4))
    for j in range(4):
        e=np.zeros(4);e[j]=h
        J[:,j]=(f(s+e)-f(s-e))/(2*h)
    return J
def rk4(s,Phi,DT):
    J1=Df_fd(s);k1=f(s)
    s2=s+0.5*DT*k1;J2=Df_fd(s2);k2=f(s2)
    s3=s+0.5*DT*k2;J3=Df_fd(s3);k3=f(s3)
    s4=s+DT*k3;J4=Df_fd(s4);k4=f(s4)
    sn=s+DT/6*(k1+2*k2+2*k3+k4)
    A1=J1@Phi;A2=J2@(Phi+0.5*DT*A1);A3=J3@(Phi+0.5*DT*A2);A4=J4@(Phi+DT*A3)
    return sn,Phi+DT/6*(A1+2*A2+2*A3+A4)
H0=-10.0
xstar=np.load('output/artifacts/xstar.npy')
def w2b(th2,w1):
    V=-19.62-9.81*np.cos(th2);c=np.cos(th2)
    disc=(w1*c)**2-2*(w1*w1+V-H0)
    return (-w1*c+np.sqrt(disc))
s=np.array([0.0,xstar[0],xstar[1],w2b(xstar[0],xstar[1])])
Phi=np.eye(4);DT=0.0005;T=2.87125
Mmax=0;fmax=0;Hs=0;w1min=1e9
n=int(T/DT)
for i in range(n):
    s,Phi=rk4(s,Phi,DT)
    Mmax=max(Mmax,np.linalg.svd(Phi,compute_uv=False)[0])
    fmax=max(fmax,np.linalg.norm(f(s)))
    if abs(s[0])<0.05: w1min=min(w1min,abs(s[2]))
    if i%200==0:
        # Hessian (2nd deriv) Frobenius-ish via FD of Df
        h=1e-6;H=0
        J0=Df_fd(s)
        for j in range(4):
            e=np.zeros(4);e[j]=h
            H=max(H,np.linalg.norm((Df_fd(s+e)-Df_fd(s-e))/(2*h),2))
        Hs=max(Hs,H)
print("Mmax=sup||DPhi_t|| %.4f  fmax=%.4f  min|w1|near section=%.4f  2ndderiv<=%.3f  T=%.5f elapsed %.0fs"%(Mmax,fmax,w1min,Hs,T,time.time()-t0),flush=True)
print("DP section norm:",np.linalg.svd(np.load('output/artifacts/DPstar.npy'),compute_uv=False),flush=True)
# angle ranges (libration evidence)
s=np.array([0.0,xstar[0],xstar[1],w2b(xstar[0],xstar[1])]);mx1=mx2=0;E0=None;Ed=0
for i in range(n):
    k1=f(s);k2=f(s+0.5*DT*k1);k3=f(s+0.5*DT*k2);k4=f(s+DT*k3)
    s=s+DT/6*(k1+2*k2+2*k3+k4)
    mx1=max(mx1,abs(((s[0]+np.pi)%(2*np.pi))-np.pi));mx2=max(mx2,abs(((s[1]+np.pi)%(2*np.pi))-np.pi))
    E=s[2]**2+0.5*s[3]**2+s[2]*s[3]*np.cos(s[0]-s[1])-19.62*np.cos(s[0])-9.81*np.cos(s[1])
    if E0 is None:E0=E
    Ed=max(Ed,abs(E-E0))
print("max|th1|=%.4f max|th2|=%.4f Edrift=%.2e E0=%.6f"%(mx1,mx2,Ed,E0),flush=True)

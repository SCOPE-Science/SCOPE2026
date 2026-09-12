"""Refine orbit A/B: verify same orbit, libration, convergence in dt, analytic Jacobian."""
import numpy as np
g=9.81
def f(s):
    th1,th2,w1,w2=s
    D=3.0-np.cos(2*(th1-th2)); d=th1-th2
    a1=(-g*3*np.sin(th1)-g*np.sin(th1-2*th2)-2*np.sin(d)*(w2*w2+w1*w1*np.cos(d)))/D
    a2=(2*np.sin(d)*(2*w1*w1+2*g*np.cos(th1)+w2*w2*np.cos(d)))/D
    return np.array([w1,w2,a1,a2])
def J_analytic(s):
    th1,th2,w1,w2=s; h=1e-8
    J=np.zeros((4,4)); f0=f(s)
    for j in range(4):
        e=np.zeros(4); e[j]=h
        J[:,j]=(f(s+e)-f(s-e))/(2*h)
    return J
def rk4(s,Phi,dt,Df):
    k1=f(s);J1=Df(s)
    s2=s+0.5*dt*k1;J2=Df(s2);k2=f(s2)
    s3=s+0.5*dt*k2;J3=Df(s3);k3=f(s3)
    s4=s+dt*k3;J4=Df(s4);k4=f(s4)
    sn=s+dt/6*(k1+2*k2+2*k3+k4)
    A1=J1@Phi;A2=J2@(Phi+0.5*dt*A1);A3=J3@(Phi+0.5*dt*A2);A4=J4@(Phi+dt*A3)
    return sn,Phi+dt/6*(A1+2*A2+2*A3+A4)
H0=-10.0
def w2b(th2,w1):
    V=-19.62-9.81*np.cos(th2);c=np.cos(th2)
    disc=(w1*c)**2-2*(w1*w1+V-H0)
    return (-w1*c+np.sqrt(disc)) if disc>=0 else None
def pmap(x,dt=0.00025,Df=J_analytic):
    s0=np.array([0.0,x[0],x[1],w2b(x[0],x[1])]);s=s0.copy();Phi=np.eye(4)
    prev=s.copy();Pp=Phi.copy();t=0;n=int(60/dt)
    for i in range(n):
        s,Phi=rk4(s,Phi,dt,Df);t+=dt
        if prev[0]<0 and s[0]>=0 and s[2]>0 and t>0.5:
            a=-prev[0]/(s[0]-prev[0]);sc=prev+a*(s-prev);Pc=Pp+a*(Phi-Pp)
            v=f(sc);M=(np.eye(4)-np.outer(v,[1,0,0,0])/v[0])@Pc
            DP=np.array([[M[1,1],M[1,2]],[M[2,1],M[2,2]]])
            return np.array([sc[1],sc[2]]),t,DP,sc
        prev=s.copy();Pp=Phi.copy()
    return None
A=np.array([-0.86788293,3.29968203]);B=np.array([0.86781168,3.29895488])
for dt in [0.0005,0.00025,0.000125]:
    print("dt=",dt)
    for nm,x in [("A",A),("B",B)]:
        y,t,DP,sc=pmap(x,dt=dt)
        ev=np.linalg.eigvals(DP)
        print(f"  {nm} y=({y[0]:.6f},{y[1]:.6f}) T={t:.6f} eig={np.abs(ev)} det={np.linalg.det(DP):.6f}")
# check B maps to A (same orbit, period-2 on section? then T_A should equal full period)
yA,TA,DP_A,scA=pmap(A,dt=0.000125); yB,TB,DP_B,scB=pmap(B,dt=0.000125)
print("A->",yA," B->",yB)
# integrate from A full state through crossings: record two successive section hits
sA=np.array([0.0,A[0],A[1],w2b(A[0],A[1])])
print("sA E=",(sA[2]**2+0.5*sA[3]**2+sA[2]*sA[3]*np.cos(sA[0]-sA[1])-19.62*np.cos(sA[0])-9.81*np.cos(sA[1])))
# libration: integrate over one period and check max angles
s=sA.copy();dt=0.00025;mx1=mx2=0
for i in range(int(2.87125/dt)):
    s,_=rk4(s,np.eye(4),dt,J_analytic)
    mx1=max(mx1,abs(((s[0]+np.pi)%(2*np.pi))-np.pi));mx2=max(mx2,abs(((s[1]+np.pi)%(2*np.pi))-np.pi))
print("max|th1|,max|th2| over T:",mx1,mx2," (librational iff < pi)")
print("DP_A=",DP_A,"DP_B=",DP_B)

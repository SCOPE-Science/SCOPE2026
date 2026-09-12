"""Standalone: correct angle->Cartesian map derived from scratch + RATTLE order test."""
import numpy as np
g=9.81
# q1=(sin t1,-cos t1), q2=q1+(sin t2,-cos t2). dq/du = J with columns d/dt1, d/dt2:
# d q1/dt1=(cos t1, sin t1); d q2/dt1=(cos t1,sin t1); d q2/dt2=(cos t2,sin t2).
def angle_to_cart(t1,t2,u1,u2):
    q=np.array([np.sin(t1),-np.cos(t1),np.sin(t1)+np.sin(t2),-np.cos(t1)-np.cos(t2)])
    J=np.array([[np.cos(t1),0],[np.sin(t1),0],[np.cos(t1),np.cos(t2)],[np.sin(t1),np.sin(t2)]])
    return q,J@np.array([u1,u2])
def G(q):
    x1,y1,x2,y2=q
    return np.array([[2*x1,2*y1,0,0],[-2*(x2-x1),-2*(y2-y1),2*(x2-x1),2*(y2-y1)]])
def gradV(q): return np.array([0,g,0,g])
def rattle_step(q,p,h):
    pn=p-0.5*h*gradV(q)
    lam=np.zeros(2);Gq=G(q)
    q1=q+h*pn.copy()
    for _ in range(30):
        q1=q+h*pn+0.5*h*h*(Gq.T@lam)
        gv=np.array([q1[0]**2+q1[1]**2-1,(q1[2]-q1[0])**2+(q1[3]-q1[1])**2-1])
        if np.linalg.norm(gv)<1e-15: break
        Jm=(0.5*h*h)*(G(q1)@Gq.T)
        lam-=np.linalg.solve(Jm,gv)
    p1h=pn-0.5*h*gradV(q1)+0.5*h*(Gq.T@lam)
    G1=G(q1)
    mu=np.linalg.solve(G1@G1.T,(2.0/h)*(G1@p1h))
    return q1,p1h-0.5*h*(G1.T@mu)
def energy(q,p): return 0.5*np.dot(p,p)+g*(q[1]+q[3])
H0=-10.0
xstar=np.load('output/artifacts/xstar.npy')
def w2b(th2,w1):
    V=-19.62-9.81*np.cos(th2);c=np.cos(th2)
    disc=(w1*c)**2-2*(w1*w1+V-H0)
    return (-w1*c+np.sqrt(disc))
th2,w1=xstar;w2=w2b(th2,w1)
q,p=angle_to_cart(0.0,th2,w1,w2)
print("Gp:",G(q)@p,"E:",energy(q,p),"H0:",H0)
gA=9.81
def fA(s):
    t1,t2,u1,u2=s;Dd=3.0-np.cos(2*(t1-t2));d=t1-t2
    a1=(-gA*3*np.sin(t1)-gA*np.sin(t1-2*t2)-2*np.sin(d)*(u2*u2+u1*u1*np.cos(d)))/Dd
    a2=(2*np.sin(d)*(2*u1*u1+2*gA*np.cos(t1)+u2*u2*np.cos(d)))/Dd
    return np.array([u1,u2,a1,a2])
def exact(h,dt=1e-5):
    s=np.array([0.0,th2,w1,w2]);n=int(round(h/dt))
    for i in range(n):
        k1=fA(s);k2=fA(s+0.5*dt*k1);k3=fA(s+0.5*dt*k2);k4=fA(s+dt*k3)
        s=s+dt/6*(k1+2*k2+2*k3+k4)
    return angle_to_cart(s[0],s[1],s[2],s[3])
for h in [0.002,0.001,0.0005,0.00025]:
    q1,p1=rattle_step(q,p,h)
    qr,pr=exact(h)
    e=np.linalg.norm(np.concatenate([q1-qr,p1-pr]))
    print(f"h={h}: local err={e:.4e} e/h^2={e/h**2:.2f} e/h^3={e/h**3:.2f} Edev={energy(q1,p1)-energy(q,p):.2e}")
np.save('output/artifacts/q0.npy',q);np.save('output/artifacts/p0.npy',p)

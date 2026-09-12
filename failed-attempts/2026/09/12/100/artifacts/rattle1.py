"""RATTLE Cartesian double pendulum: defect scaling + constraint residuals vs step h."""
import numpy as np
g=9.81
# Cartesian: q=(x1,y1,x2,y2), constraints g1=|q1|^2-1, g2=|q2-q1|^2-1; M=I(4). V=g(y1+y2).
def G(q):
    x1,y1,x2,y2=q
    return np.array([[2*x1,2*y1,0,0],[ -2*(x2-x1),-2*(y2-y1),2*(x2-x1),2*(y2-y1) ]])
def gradV(q):
    return np.array([0,g,0,g])
def rattle_step(q,p,h):
    # standard RATTLE with Lagrange multipliers solved 2x2 via Newton
    pn_half=p-0.5*h*gradV(q)
    # position projection: q1=q+h pn_half + h^2/2 G(q)^T lam ; solve g(q1)=0
    lam=np.zeros(2)
    q1=q+h*pn_half.copy()
    Gq=G(q)
    for _ in range(20):
        q1=q+h*pn_half+0.5*h*h*(Gq.T@lam)
        gv=np.array([q1[0]**2+q1[1]**2-1,(q1[2]-q1[0])**2+(q1[3]-q1[1])**2-1])
        if np.linalg.norm(gv)<1e-14: break
        J=(0.5*h*h)*(G(q1)@Gq.T)
        lam-=np.linalg.solve(J,gv)
    p1h=pn_half+0.5*h*(Gq.T@lam)
    # momentum projection: p1 = p1h - G1^T mu, (G1 G1^T)mu = G1 p1h
    G1=G(q1)
    mu=np.linalg.solve(G1@G1.T,G1@p1h)
    p1=p1h-G1.T@mu
    return q1,p1
def energy(q,p):
    return 0.5*np.dot(p,p)+g*(q[1]+q[3])
def angle_to_cart(th1,th2,w1,w2):
    q=np.array([np.sin(th1),-np.cos(th1),np.sin(th1)+np.sin(th2),-np.cos(th1)-np.cos(th2)])
    J=np.array([[np.cos(th1),0], [np.sin(th1),0],[np.cos(th1),np.cos(th2)],[np.sin(th1),np.sin(th2)]])
    p=J@np.array([w1,w2])
    return q,p
H0=-10.0
xstar=np.load('output/artifacts/xstar.npy')
def w2b(th2,w1):
    V=-19.62-9.81*np.cos(th2);c=np.cos(th2)
    disc=(w1*c)**2-2*(w1*w1+V-H0)
    return (-w1*c+np.sqrt(disc))
th2,w1=xstar;w2=w2b(th2,w1)
q,p=angle_to_cart(0.0,th2,w1,w2)
print("E0:",energy(q,p),"g:",np.array([q[0]**2+q[1]**2-1,(q[2]-q[0])**2+(q[3]-q[1])**2-1]),"Gp:",G(q)@p)
for h in [0.005,0.002,0.001,0.0005]:
    qq,pp=q.copy(),p.copy()
    # one RATTLE step vs fine RK4 reference in cartesian coords
    q1,p1=rattle_step(qq,pp,h)
    # reference: integrate angle model with tiny dt then convert
    import sys
    gA=9.81
    def fA(s):
        t1,t2,u1,u2=s;Dd=3.0-np.cos(2*(t1-t2));d=t1-t2
        a1=(-gA*3*np.sin(t1)-gA*np.sin(t1-2*t2)-2*np.sin(d)*(u2*u2+u1*u1*np.cos(d)))/Dd
        a2=(2*np.sin(d)*(2*u1*u1+2*gA*np.cos(t1)+u2*u2*np.cos(d)))/Dd
        return np.array([u1,u2,a1,a2])
    s=np.array([0.0,th2,w1,w2]);dt=2e-5;n=int(h/dt)
    for i in range(n):
        k1=fA(s);k2=fA(s+0.5*dt*k1);k3=fA(s+0.5*dt*k2);k4=fA(s+dt*k3)
        s=s+dt/6*(k1+2*k2+2*k3+k4)
    qr,pr=angle_to_cart(s[0],s[1],s[2],s[3])
    otp=np.linalg.norm(np.concatenate([q1-qr,p1-pr]))/h
    gv=np.array([q1[0]**2+q1[1]**2-1,(q1[2]-q1[0])**2+(q1[3]-q1[1])**2-1])
    print(f"h={h}: |g|={np.linalg.norm(gv):.2e} |Gp|={np.linalg.norm(G(q1)@p1):.2e} h^-1*onestep err={otp:.4e} Edev={energy(q1,p1)-energy(q,p):.2e}")

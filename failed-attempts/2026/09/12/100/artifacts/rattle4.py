"""Cross-check RATTLE vs exact angle-flow over SHORT time: global err at t=0.05,0.1 for h=5e-3..5e-4."""
import numpy as np
exec(open('output/artifacts/rattle1.py').read().split("H0=-10.0")[0])
H0=-10.0
xstar=np.load('output/artifacts/xstar.npy')
def w2b(th2,w1):
    V=-19.62-9.81*np.cos(th2);c=np.cos(th2)
    disc=(w1*c)**2-2*(w1*w1+V-H0)
    return (-w1*c+np.sqrt(disc))
th2,w1=xstar;w2=w2b(th2,w1)
q0,p0=angle_to_cart(0.0,th2,w1,w2)
gA=9.81
def fA(s):
    t1,t2,u1,u2=s;Dd=3.0-np.cos(2*(t1-t2));d=t1-t2
    a1=(-gA*3*np.sin(t1)-gA*np.sin(t1-2*t2)-2*np.sin(d)*(u2*u2+u1*u1*np.cos(d)))/Dd
    a2=(2*np.sin(d)*(2*u1*u1+2*gA*np.cos(t1)+u2*u2*np.cos(d)))/Dd
    return np.array([u1,u2,a1,a2])
def exact(h):
    s=np.array([0.0,th2,w1,w2]);dt=1e-5;n=int(h/dt)
    for i in range(n):
        k1=fA(s);k2=fA(s+0.5*dt*k1);k3=fA(s+0.5*dt*k2);k4=fA(s+dt*k3)
        s=s+dt/6*(k1+2*k2+2*k3+k4)
    return angle_to_cart(s[0],s[1],s[2],s[3])
for T in [0.05,0.1]:
    print("T=",T)
    for h in [0.005,0.002,0.001,0.0005]:
        qq,pp=q0.copy(),p0.copy();n=int(T/h)
        for i in range(n): qq,pp=rattle_step(qq,pp,h)
        qr,pr=exact(n*h)
        print(f"  h={h}: globerr={np.linalg.norm(np.concatenate([qq-qr,pp-pr])):.4e} Edev={energy(qq,pp)-energy(q0,p0):.4e}")

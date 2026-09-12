"""Verify angle<->Cartesian velocity map via FD; test RATTLE vs exact with CORRECT p0."""
import numpy as np
g=9.81
src=open('output/artifacts/rattle1.py').read()
ns={}
exec(src.split("H0=-10.0")[0].split('def rattle_step')[0],ns)
G=ns['G'];angle_to_cart=ns['angle_to_cart'];energy=ns['energy']
gsrc=src.split("def rattle_step")[1].split("def energy")[0]
ns2=dict(G=G,gradV=ns['gradV'],np=np)
exec("def rattle_step"+gsrc.split("def rattle_step",1)[-1] if False else "pass")
import re
m=re.search(r"(def rattle_step.*?return q1,p1)",src,re.S)
exec(m.group(1),ns2)
rattle_step=ns2['rattle_step']
H0=-10.0
xstar=np.load('output/artifacts/xstar.npy')
def w2b(th2,w1):
    V=-19.62-9.81*np.cos(th2);c=np.cos(th2)
    disc=(w1*c)**2-2*(w1*w1+V-H0)
    return (-w1*c+np.sqrt(disc))
th2,w1=xstar;w2=w2b(th2,w1)
# FD check of J
th1=0.0;h=1e-7
def Q(t1,t2): return np.array([np.sin(t1),-np.cos(t1),np.sin(t1)+np.sin(t2),-np.cos(t1)-np.cos(t2)])
Jfd=np.column_stack([(Q(th1+h,th2)-Q(th1-h,th2))/(2*h),(Q(th1,th2+h)-Q(th1,th2-h))/(2*h)])
J=np.array([[np.cos(th1),0],[np.sin(th1),0],[np.cos(th1),np.cos(th2)],[np.sin(th1),np.sin(th2)]])
print("J exact:\n",J,"\nJ fd:\n",Jfd)
q,p=angle_to_cart(th1,th2,w1,w2)
print("Gp:",G(q)@p,"E:",energy(q,p))
# exact short flow from file's fA? use rattle1's reference with dt=1e-5 and SECOND-order check via h-scaling of ONE step error at smaller h
gA=9.81
def fA(s):
    t1,t2,u1,u2=s;Dd=3.0-np.cos(2*(t1-t2));d=t1-t2
    a1=(-gA*3*np.sin(t1)-gA*np.sin(t1-2*t2)-2*np.sin(d)*(u2*u2+u1*u1*np.cos(d)))/Dd
    a2=(2*np.sin(d)*(2*u1*u1+2*gA*np.cos(t1)+u2*u2*np.cos(d)))/Dd
    return np.array([u1,u2,a1,a2])
def exact(h,dt=1e-5):
    s=np.array([th1,th2,w1,w2]);n=int(h/dt)
    for i in range(n):
        k1=fA(s);k2=fA(s+0.5*dt*k1);k3=fA(s+0.5*dt*k2);k4=fA(s+dt*k3)
        s=s+dt/6*(k1+2*k2+2*k3+k4)
    return angle_to_cart(s[0],s[1],s[2],s[3])
for h in [0.002,0.001,0.0005,0.00025]:
    q1,p1=rattle_step(q,p,h)
    qr,pr=exact(h)
    e=np.linalg.norm(np.concatenate([q1-qr,p1-pr]))
    print(f"h={h}: local err={e:.4e} e/h^2={e/h**2:.2f} e/h^3={e/h**3:.2f}")

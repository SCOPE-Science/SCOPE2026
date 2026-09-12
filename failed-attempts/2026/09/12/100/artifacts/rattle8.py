"""Isolate: single RATTLE step from REST state + compare two angle conventions; print q1 vs exact."""
import numpy as np
exec(open('output/artifacts/rattle7.py').read().split("H0=-10.0")[0])
# rest: th1=th2=0.2, w=0
q,p=angle_to_cart(0.2,0.2,0.0,0.0)
print("E0:",energy(q,p))
h=0.001
q1,p1=rattle_step(q,p,h)
# exact: Taylor q(h)=q + h v + h^2/2 a_proj; just compare with tiny-dt full constrained... use angle flow
gA=9.81
def fA(s):
    t1,t2,u1,u2=s;Dd=3.0-np.cos(2*(t1-t2));d=t1-t2
    a1=(-gA*3*np.sin(t1)-gA*np.sin(t1-2*t2)-2*np.sin(d)*(u2*u2+u1*u1*np.cos(d)))/Dd
    a2=(2*np.sin(d)*(2*u1*u1+2*gA*np.cos(t1)+u2*u2*np.cos(d)))/Dd
    return np.array([u1,u2,a1,a2])
s=np.array([0.2,0.2,0.0,0.0]);dt=1e-6;n=int(h/dt)
for i in range(n):
    k1=fA(s);k2=fA(s+0.5*dt*k1);k3=fA(s+0.5*dt*k2);k4=fA(s+dt*k3)
    s=s+dt/6*(k1+2*k2+2*k3+k4)
qr,pr=angle_to_cart(s[0],s[1],s[2],s[3])
print("rest local err:",np.linalg.norm(np.concatenate([q1-qr,p1-pr])))
print("q1:",q1,"\nqr:",qr)
print("p1:",p1,"\npr:",pr)
# unconstrained Taylor check: q+h p - h^2/2 gradV projected?
print("q+h p-h^2/2 gradV:",q+h*p-0.5*h*h*gradV(q))

"""Diagnose RATTLE energy blowup: track E(t) over first steps; compare velocity-Verlet unconstrained core."""
import numpy as np
exec(open('output/artifacts/rattle1.py').read().split("H0=-10.0")[0])
H0=-10.0
xstar=np.load('output/artifacts/xstar.npy')
def w2b(th2,w1):
    V=-19.62-9.81*np.cos(th2);c=np.cos(th2)
    disc=(w1*c)**2-2*(w1*w1+V-H0)
    return (-w1*c+np.sqrt(disc))
th2,w1=xstar;w2=w2b(th2,w1)
q,p=angle_to_cart(0.0,th2,w1,w2)
print("E0",energy(q,p),"|p|",np.linalg.norm(p))
h=0.005
qq,pp=q.copy(),p.copy()
for i in range(6):
    qq,pp=rattle_step(qq,pp,h)
    print(i,"E",energy(qq,pp),"|g|",np.linalg.norm([qq[0]**2+qq[1]**2-1,(qq[2]-qq[0])**2+(qq[3]-qq[1])**2-1]),"q",qq,"p",pp)

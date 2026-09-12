"""Check RATTLE local order properly: compare against exact h-flow AND h/2+h/2 Richardson."""
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
for h in [0.005,0.002,0.001]:
    q1,p1=rattle_step(q,p,h)
    # two half steps
    qh,ph=rattle_step(q,p,h/2);q2,p2=rattle_step(qh,ph,h/2)
    d=np.linalg.norm(np.concatenate([q1-q2,p1-p2]))
    print(f"h={h}: |R(h)-R(h/2)^2|={d:.4e}  ratio-est order={(d):.4e} (expect ~C h^3: {d/h**3:.3f})")
# global error over fixed time
for h in [0.005,0.0025]:
    qq,pp=q.copy(),p.copy();n=int(0.5/h)
    for i in range(n): qq,pp=rattle_step(qq,pp,h)
    print(f"h={h} global@0.5: Edev={energy(qq,pp)-energy(q,p):.4e}")

"""Script C2: correct stable-cone check. Stable cone K_s(kappa) = {|w|+|u| <= kappa|s|}
(rescale: sample s=+-1, (w,u) inside disc radius kappa; check image under Df^{-1}
stays inside with stable-component expansion). Worst case over boundary ||(w,u)||=kappa."""
import math
import numpy as np
A = np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
w,P = np.linalg.eigh(A)
alp,bet = 2*math.pi*0.03, 2*math.pi*0.02
def Df(c2,c3):
    return np.array([[2.,1+2*alp*c2,bet*c3],[1.,2+alp*c2,1+2*bet*c3],[0.,1.,1+bet*c3]])
def Mb(c2,c3): return P.T@Df(c2,c3)@P
rng = np.random.default_rng(3)
def stable_check(kappa,trials=150000):
    wr,we=0.0,1e9
    for _ in range(trials):
        M=np.linalg.inv(Mb(rng.uniform(-1,1),rng.uniform(-1,1)))
        th=rng.uniform(0,2*math.pi); sgn=1 if rng.random()<0.5 else -1
        v=np.array([sgn, kappa*math.cos(th), kappa*math.sin(th)])
        z=M@v
        r=math.hypot(z[1],z[2])/abs(z[0])
        e=abs(z[0])/1.0
        wr=max(wr,r); we=min(we,e)
    return wr,we
for k in [0.3,0.5,0.8,1.0]:
    r,e=stable_check(k); print(f"stable cone kappa={k}: worst_ratio={r:.3f} (<{k}? {r<k}) worst_stable_exp={e:.3f} (>1? {e>1})")

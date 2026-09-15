"""MF root finder CORRECTED: Eq.(17) is q-th root, not square root for general q.
q * (1 - J/rho0)^{1/q} = J, J = alpha(1-rho0). Also compare with target's transcription
(1-J/rho0)^{1/q} = J/q -- identical. Check q=2 bisect vs earlier bm_root (same eq).
The previous mfroot.py wrongly used sqrt for general q display only for q=2 so same;
recheck: for q=2, q-th root = sqrt, so bisect should equal bm_root. Diagnose mismatch."""
import numpy as np, math

def mf_rho0(alpha, q):
    def g(r):
        J=alpha*(1-r)
        if J>=r or J<0: return -1.0
        return q*((1-J/r)**(1.0/q)) - J
    lo,hi=1e-12,1-1e-12
    for _ in range(400):
        m=(lo+hi)/2
        if g(m)>0: hi=m
        else: lo=m
    return (lo+hi)/2

def explicit18(alpha):
    th_denom = 36-18*alpha-alpha**2
    th_num = 6*math.sqrt(6*alpha**4+18*alpha**3+20*alpha**2+24*alpha+8)
    theta = math.atan2(th_num, alpha*th_denom)
    return (2/3)*(1 - math.sqrt(alpha**2+12*alpha+12)/(2*alpha)*math.cos((math.pi+theta)/3))

for a in [0.2,0.4,0.5,0.7,1.0]:
    r=mf_rho0(a,2); J=a*(1-r)
    re=explicit18(a); Je=a*(1-re)
    print(f"a={a}: qth-root rho0={r:.6f} J={J:.6f} | explicit(18) rho0={re:.6f} J={Je:.6f}")
    # verify eq residual for bisect root
    print(f"   resid bisect: q*(1-J/r)^(1/q)-J = {2*((1-J/r)**0.5)-J:.3e}; explicit resid = {2*((1-Je/re)**0.5)-Je:.3e}")

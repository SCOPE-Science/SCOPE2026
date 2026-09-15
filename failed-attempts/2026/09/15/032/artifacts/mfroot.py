"""MF root finder for Eq.(17) and Monte-Carlo re-check of Fig.2 point.
Uses output/artifacts/gillespie.py simulate imported inline? Recompute MF root via bisection for q=2.
Eq17: q*sqrt(1 - J/rho0) = J, J=alpha(1-rho0). Solve for rho0 in (0,1).
Also compute BM explicit formula (18)-(19) algebraically to verify agreement.
"""
import numpy as np

def mf_rho0(alpha, q):
    def g(r):
        if r<=0 or r>=1: return np.nan
        J=alpha*(1-r)
        return q*(max(0.0,1-J/r))**0.5 - J if J<=r else -J  # q*sqrt - J
    # g(0+): q*sqrt(1-alpha*(1-r)/r)... at r->0, J/r->inf => root of max(0,..)=0 => g->-J<0
    # g(1-): q*1 - 0 = q >0. unique root.
    lo,hi=1e-12,1-1e-12
    glo=g(lo)
    for _ in range(300):
        m=(lo+hi)/2
        if g(m)>0: hi=m
        else: lo=m
    return (lo+hi)/2

def explicit18(alpha):
    import math
    th_denom = 36-18*alpha-alpha**2
    th_num = 6*math.sqrt(6*alpha**4+18*alpha**3+20*alpha**2+24*alpha+8)
    theta = math.atan2(th_num, alpha*th_denom)
    return (2/3)*(1 - math.sqrt(alpha**2+12*alpha+12)/(2*alpha)*math.cos((math.pi+theta)/3))

for a in [0.2,0.4,0.5,0.7,1.0]:
    r=mf_rho0(a,2); J=a*(1-r)
    re=explicit18(a); Je=a*(1-re)
    print(f"a={a}: bisect rho0={r:.6f} J={J:.6f} | explicit rho0={re:.6f} J={Je:.6f}")

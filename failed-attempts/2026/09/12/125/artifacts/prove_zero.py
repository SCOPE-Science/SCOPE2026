import numpy as np
from fractions import Fraction
# Exact structure: claim det M(y,th) == 0 identically? det ~1e-20 uniformly, lo~1e-8 uniformly -> suggests det is EXACTLY 0 for all (y,th)!
# Why? Look for exact linear dependence among the 11 rows/columns valid for all y,th.
# M[s,sp] = b^{-1} sum_{k: s-sp-12k = 11 q} G_k(y+s d) e^{2pi i q th}.
# Try: dependence over s from partition-of-unity / Strang-Fix of B3? B3 shifts reproduce polynomials; Janssen ties: sum_k c_k G_k(y) = const?
# Janssen's tie: for B-splines, sum over dual-lattice phase gives zero function when b> something? Here b=11/6 ~1.833, support 4: Janssen tie condition sum_m g(x - m/a?) ...
# Numerically compute null vector at a few (y,th) and see pattern (e.g. alternating? theta-dependent?).
def B3f(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; b=11/6; beta=6/11; delta=1/22; binv=6/11
KS=list(range(-7,8)); NS=list(range(-16,17))
def Gk(k,x):
    x=np.asarray(x,float); tot=np.zeros_like(x)
    for n in NS: tot+=B3f(x-n*a)*B3f(x-n*a-k*beta)
    return tot
def Mmat(y,th):
    M=np.zeros((11,11),complex)
    for s_ in range(11):
        for sp in range(11):
            tot=0j
            for k in KS:
                if (s_-12*k)%11 != sp: continue
                q=(s_-12*k-sp)//11
                tot+=Gk(k,np.array([y+s_*delta]))[0]*np.exp(2j*np.pi*q*th)
            M[s_,sp]=binv*tot
    return M
for (y,th) in [(0.0,0.0),(0.01,0.3),(0.02,0.7),(delta*0.5,0.123)]:
    M=Mmat(y,th); e,v=np.linalg.eigh(M)
    print(f"y={y:.5f} th={th}: eig[0:3]={e[:3]}")
    print("  nullvec phases:",np.round(np.angle(v[:,0]),3))
    print("  nullvec abs:",np.round(np.abs(v[:,0]),3))
# test rank: how many eigs ~0?
M=Mmat(0.01,0.3); e=np.linalg.eigvalsh(M)
print("full eig:",e)
print("svd:",np.linalg.svd(M,compute_uv=False))

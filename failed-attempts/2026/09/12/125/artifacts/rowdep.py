import numpy as np
from fractions import Fraction
# Hypothesis: rows of M sum to zero exactly? i.e. vector 1=(1,...,1) in kernel: sum_sp M[s,sp] = 0?
# sum_sp M[s,sp] = b^{-1} sum_k G_k(y+s d) S_k(th), S_k = sum over sp compatible... For fixed s, as sp runs 0..10, each k with |k|<=7 appears exactly once (map k -> sp=(s-12k) mod 11 is injective since 12 invertible mod 11 and |k|<=7<11 distinct). So rowsum R_s = b^{-1} sum_{|k|<=7} G_k(y+s d) e^{2pi i q(k,s) th}.
# At th=0: R_s = b^{-1} sum_k G_k = b^{-1} sum_k sum_n g(y+s d-na)g(y+s d-na-k/b).
# Inner sum over k at fixed n: sum_k g(z-k/b) where z=y+sd-na. Since 1/b=6/11 and g=B3 compact support, sum over k covers shifts by 6/11... partition of unity of B3 is over INTEGER shifts: sum_j B3(z-j)=1. Shifts by 6/11: sum_k B3(z-6k/11) is 6/11-periodic, NOT constant... but weighted?
# Numerically test row sums:
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
M=Mmat(0.0,0.0)
rs=np.sum(M,axis=1)
print("rowsums th=0:",rs)
M=Mmat(0.01,0.3)
print("rowsums th=.3:",np.round(rs,6))
# alt: column sums? nullvec at th=0 looked like symmetric bump (not const) -> kernel is not 1-vector except maybe at special th.
# At general th nullvec abs ~flat 0.30=1/sqrt(11) with linear phases -> looks like Fourier vector! c_s = 11^{-1/2} e^{2pi i j s/11} for some j?
# phases at (0.01,0.3): [pi, -1.827, -0.514, 0.8, 2.114, -2.856, ...]: differences ~1.314 = 2pi*? 2pi*?=1.314 -> ?=0.209? hmm 12*0.3/11? Let's fit: phase[s+1]-phase[s] const?
for (y,th) in [(0.01,0.3),(0.02,0.7),(0.0227,0.123)]:
    M=Mmat(y,th); e,v=np.linalg.eigh(M); c=v[:,0]
    d=np.angle(c[1:]*np.conj(c[:-1]))
    print(f"y={y} th={th} mean phase-step={np.mean(d):.5f} std={np.std(d):.2e} | pred 2pi*? ...")

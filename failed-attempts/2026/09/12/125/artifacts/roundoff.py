import numpy as np
# Is lo floor ~1.7e-8 a summation artifact? Increase N lattice range and precision; compare float64 vs longdouble.
def B3f(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
def lo(y,th,NS):
    a=0.5; b=11/6; beta=6/11; delta=1/22; binv=6/11
    KS=list(range(-7,8))
    M=np.zeros((11,11),complex)
    for s_ in range(11):
        for sp in range(11):
            tot=0j
            for k in KS:
                if (s_-12*k)%11 != sp: continue
                q=(s_-12*k-sp)//11
                g=0.0
                for n in NS: g+=float(B3f(np.array([y+s_*delta-n*a]))[0])*float(B3f(np.array([y+s_*delta-n*a-k*beta]))[0])
                tot+=g*np.exp(2j*np.pi*q*th)
            M[s_,sp]=binv*tot
    return np.linalg.eigvalsh(M)
for NS in [range(-4,6),range(-8,9),range(-16,17),range(-32,33)]:
    e=lo(0.0,0.625,NS)
    print(f"N={len(NS)}: lo3={e[:3]} det={np.linalg.det(np.zeros((0,0)))} n/a")

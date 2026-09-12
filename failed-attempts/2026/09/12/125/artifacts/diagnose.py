import numpy as np
def B3(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; beta=6/11; delta=1/22; binv=6/11
def Gk(k,x):
    x=np.asarray(x,float); tot=np.zeros_like(x)
    for n in range(-12,13):
        tot+=B3(x-n*a)*B3(x-n*a-k*beta)
    return tot
# zero-BC L=8 spectrum: number below 0.5 = 256 of 352. Fiber said spectrum in [~0,2]. But density?
# Frame bound A would be essinf fiber ~0 -> consistent with NO lower bound. But then ZZ toy scan disagrees -> toy scan used wrong covering.
# Let's directly test Janssen tie: Phi(s,theta)=ZZ vector. Find explicit zero of ZZ matrix: search singular values of Z(u,nu) 11x12.
def Za(x,nu):
    tot=0j
    for k in range(-8,9):
        tot+=B3(np.array([x-a*k]))[0]*np.exp(2j*np.pi*k*nu)
    return tot
# Convention A (Zibulski-Zeevi): with p=11,q=12? a*b=11/12=p/q with p=11,q=12 coprime.
# phi[j](x,nu) with j=0..q-1: Z_{1/b} g(x + j/b? ...). Take lattice consistent: step 1/b for rows? Let's define
# Zr[s](x,nu) = Za(x + s/(q b)?...). Try both and scan min singular value.
def smin_Z(x,nu,mode):
    p=11;q=12
    Z=np.zeros((p,q),complex)
    for r in range(p):
        for s in range(q):
            if mode=='A':
                Z[r,s]=Za(x + r/(p*b)+s/(q*b), nu)  # guess
            elif mode=='B':
                # standard: Phi_r,s = Z_a g(x + r/b - s q? ...)
                Z[r,s]=Za(x + s*a/q - r/b, nu)
            elif mode=='C':
                Z[r,s]=Za(x + r*a/p + s/(b*q), nu)
    return np.linalg.svd(Z,compute_uv=False)[-1]
for mode in ['A','B','C']:
    mn=1e9;arg=None
    for x in np.linspace(0,0.5,25,endpoint=False):
        for nu in np.linspace(0,1,25,endpoint=False):
            v=smin_Z(x,nu,mode)
            if v<mn: mn=v;arg=(x,nu)
    print(mode,"min-svd",mn,"at",arg)

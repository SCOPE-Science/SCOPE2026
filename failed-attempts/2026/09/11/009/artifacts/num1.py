import mpmath
mpmath.mp.dps = 30
m0 = mpmath.mpf('0.5')
K = mpmath.ellipk(m0)
L = 2*K
k0 = 2*mpmath.pi/L
print("L=", float(L), "k0=", float(k0))
# sample u* on uniform grid and FFT using numpy
import numpy as np
M = 4096
xs = np.linspace(0, float(L), M, endpoint=False)
us = np.zeros(M); u0s=np.zeros(M)
for i,x in enumerate(xs):
    s = float(mpmath.ellipfun('sn', mpmath.mpf(str(x)), m0))
    c = float(mpmath.ellipfun('cn', mpmath.mpf(str(x)), m0))
    us[i]=2*s*s+0.1*c**4
    u0s[i]=2*s*s
Uh = np.fft.rfft(us)/M
U0h = np.fft.rfft(u0s)/M
print("mean u*=", Uh[0].real)
for n in range(12):
    print(f"n={n} c_n(u*)={Uh[n].real:.12f}  c_n(u0)={U0h[n].real:.12f}")

def hill_eigs(cd, N):
    dim=2*N+1
    H=np.zeros((dim,dim))
    kk=float(k0)
    for i in range(dim):
        n=i-N
        H[i,i]=(n*kk)**2+cd[0]
        for j in range(dim):
            mm=j-N
            d=n-mm
            if d!=0 and abs(d) in cd:
                H[i,j]+=cd[abs(d)]
    return np.sort(np.linalg.eigvalsh(H))

cd={n: float(Uh[n].real) for n in range(60)}
cd0={n: float(U0h[n].real) for n in range(60)}
for N in [5,8,12,16,20,25]:
    e=hill_eigs(cd,N); e0=hill_eigs(cd0,N)
    print(f"N={N} u*:", np.round(e[:8],6))
    print(f"N={N} u0:", np.round(e0[:8],6))

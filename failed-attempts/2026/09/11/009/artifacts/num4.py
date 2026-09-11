import mpmath
mpmath.mp.dps = 40
m0 = mpmath.mpf('0.5')
K = mpmath.ellipk(m0); L=2*K; k0=2*mpmath.pi/L
import numpy as np
M=8192
xs = np.linspace(0, float(L), M, endpoint=False)
us=np.zeros(M); u0s=np.zeros(M); vs=np.zeros(M)
for i,x in enumerate(xs):
    s=float(mpmath.ellipfun('sn', mpmath.mpf(repr(x)), m0))
    c=float(mpmath.ellipfun('cn', mpmath.mpf(repr(x)), m0))
    us[i]=2*s*s+0.1*c**4; u0s[i]=2*s*s; vs[i]=1.0*s*s
Uh=np.fft.rfft(us)/M; U0h=np.fft.rfft(u0s)/M; Vh=np.fft.rfft(vs)/M
def spec(cd,N,half=False):
    dim=2*N+1; H=np.zeros((dim,dim)); kk=float(k0)
    for i in range(dim):
        n=i-N
        q=(n+0.5)*kk if half else n*kk
        H[i,i]=q*q+cd[0]
        for j in range(dim):
            d=n-(j-N)
            if d!=0 and abs(d) in cd: H[i,j]+=cd[abs(d)]
    return np.sort(np.linalg.eigvalsh(H))
for name,cd in [("v(true Lame m=1)",{n:float(Vh[n].real) for n in range(80)}),
                ("u0=2sn^2",{n:float(U0h[n].real) for n in range(80)}),
                ("u*",{n:float(Uh[n].real) for n in range(80)})]:
    N=24
    p=spec(cd,N); a=spec(cd,N,half=True)
    print(f"== {name}")
    print("  per :", np.round(p[:10],9))
    print("  anti:", np.round(a[:10],9))
    print("  per gaps:", np.round(np.diff(p[:10]),9))
    print("  anti gaps:", np.round(np.diff(a[:10]),9))

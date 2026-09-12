import numpy as np

def B3(x):
    x = np.asarray(x, dtype=float)
    ax = np.abs(x)
    out = np.zeros_like(x)
    m1 = ax < 1.0
    out[m1] = (4.0 - 6.0*x[m1]**2 + 3.0*ax[m1]**3)/6.0
    m2 = (ax >= 1.0) & (ax <= 2.0)
    out[m2] = (2.0 - ax[m2])**3/6.0
    return out

a = 0.5; b = 11.0/6.0; beta = 1.0/b; delta = 1.0/22.0
binv = 1.0/b
print("a,beta,delta,binv:", a, beta, delta, binv)

def gamma(k, x, s):
    # G_k(x + s*delta)
    y = x + s*delta
    tot = 0.0j
    for n in range(-6, 7):
        tot += B3(np.array([y - n*a]))[0] * B3(np.array([y - n*a - k*beta]))[0]
    return tot  # real

def Mmat(x, th):
    M = np.zeros((11,11), dtype=complex)
    for s in range(11):
        for k in range(-7, 8):
            sp = (s - k) % 11
            m = (s - 12*k - sp)//11
            assert m*11 == (s - 12*k - sp)
            M[s, sp] += binv * gamma(k, x, s) * np.exp(2j*np.pi*m*th)
    return M

# hermitian test
for (x,th) in [(0.01,0.3),(0.0,0.0),(0.04,0.9)]:
    M = Mmat(x,th)
    print(x, th, "herm err", np.max(np.abs(M-M.conj().T)))

# scan
for N in [12, 24, 48]:
    xs = np.linspace(0, delta, N, endpoint=False)
    ths = np.linspace(0, 1, N, endpoint=False)
    mn = 1e9; arg=None; mx=-1e9
    for x in xs:
        for th in ths:
            e = np.linalg.eigvalsh(Mmat(x,th))
            if e[0] < mn: mn=e[0]; arg=(x,th)
            if e[-1] > mx: mx=e[-1]
    print(f"N={N} min={mn:.6f} at x={arg[0]:.6f},th={arg[1]:.6f}  maxeig={mx:.6f}")

# compare ratio with earlier Gmat at corresponding point
import importlib.util
spec = importlib.util.spec_from_file_location("zz", "output/artifacts/zz_scan.py")

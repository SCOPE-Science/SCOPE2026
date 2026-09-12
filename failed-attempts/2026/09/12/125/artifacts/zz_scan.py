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

# check integral ~1
xs = np.linspace(-2,2,20001)
print("integral B3 ~", np.trapz(B3(xs), xs))
print("B3(0)=", B3(np.array([0.0])), "B3(1)=", B3(np.array([1.0])), "B3(0.5)=", B3(np.array([0.5])))

def Gmat(u, xi):
    B = 11
    q = 12
    r = np.arange(B)  # 0..10
    tau = (u + r)/B  # shape (B,)
    b_a = B3(2*tau)       # B3(2tau)
    b_b = B3(2*tau-2)     # equals B3(2-2tau)
    s = np.arange(q)  # 0..11
    # A[r,s] = b_a[r] + b_b[r]*exp(2pi i (xi - 11 s/12))
    ph = np.exp(2j*np.pi*(xi - 11.0*s[None,:]/12.0))  # shape (1,q)? need per s
    # Actually ph depends only on s, broadcast
    A = b_a[:,None] + b_b[:,None]*ph  # (B,q) -- ph broadcasts (q,) ok
    # phase E[r,s] = exp(2pi i s (r)/12)? careful: W includes exp(2pi i 11 s tau/12); G includes E* A conj(A)
    # W_r(s) = sqrt2 * exp(2pi i 11 s tau_r/12) * A_r(s)
    # G[r,r'] = 2 sum_s exp(2pi i 11 s (tau_r - tau_r')/12) A_r conj(A_r')
    # = 2 sum_s exp(2pi i s (r-r')/12) A_r conj(A_r')
    E = np.exp(2j*np.pi*np.outer(r, s)/12.0)  # (B,q): exp(2pi i r s/12)
    WE = E * A  # (B,q) = exp part times A
    G = 2.0 * (WE @ WE.conj().T)
    return G

# quick test hermitian
G = Gmat(0.3, 0.7)
print("Hermitian err:", np.max(np.abs(G-G.conj().T)))
print("eig:", np.linalg.eigvalsh(G))

# coarse scan
for N in [24, 48, 96]:
    us = np.linspace(0,1,N,endpoint=False)
    xis = np.linspace(0,1,N,endpoint=False)
    mn = 1e9; arg=None
    for u in us:
        for xi in xis:
            e = np.linalg.eigvalsh(Gmat(u,xi))[0]
            if e < mn:
                mn=e; arg=(u,xi)
    print(f"N={N} min eig ~ {mn:.6e} at {arg}")

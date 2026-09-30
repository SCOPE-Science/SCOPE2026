import numpy as np

# 2D model of the audited configuration: transverse x (concentration), axial y (fast phase)
# W(x,y) = r^{-1} psi(x/r) e^{i lam y}; source g = sin(y) d_x W  [model of (v0.nabla)W]
# R via Fourier multiplier m(xi)=i xi/|xi|^2 (gradient antidivergence; same order/freq-gain as symmetric R)
# Checks: (i) ||W||_{B^{1/3}_{3,inf}} ~ lam^{(1+al)/3}; (ii) ||R g||_1 / ||g||_1 ~ lam^{-1}
rng = np.random.default_rng(0)
def run(lam, al):
    r = lam**(-al)
    N = int(2**np.ceil(np.log2(16/r)))  # resolve tube
    N = min(max(N, 256), 4096)
    x = np.linspace(0, 2*np.pi, N, endpoint=False); dx = x[1]-x[0]
    X, Y = np.meshgrid(x, x, indexing='ij')
    psi = np.exp(-((X-np.pi)/r)**2)  # bump centered pi, width r (periodization error ~ e^{-(pi/r)^2}, negligible)
    dpsi = (-2*(X-np.pi)/r**2)*psi
    W = (1/r)*psi*np.exp(1j*lam*Y)
    g = np.sin(Y)*((1/r)*dpsi*np.exp(1j*lam*Y))
    g1 = np.sum(np.abs(g))*dx**2
    # Besov B^{1/3}_{3,inf} of W via dyadic LP blocks in Fourier
    F = np.fft.fft2(W)*dx**2/(2*np.pi)  # approx Fourier coeffs (unitary-ish); use consistent norm below
    # simpler: work with fft values and Parseval-free direct block L3 via ifft
    F = np.fft.fft2(W)
    kx = np.fft.fftfreq(N, d=dx)*2*np.pi
    KX, KY = np.meshgrid(kx, kx, indexing='ij')
    K = np.sqrt(KX**2+KY**2)
    bmax = 0.0
    j = 0
    while 2**j <= N:
        lo, hi = (2**(j-1) if j>=1 else 0), 2**j
        mask = (K>=lo)&(K<hi) if j>=1 else (K<1)
        blk = np.fft.ifft2(F*mask)
        b3 = (np.sum(np.abs(blk)**3)*dx**2)**(1/3)
        bmax = max(bmax, (2**j)**(1/3)*b3)
        j += 1
    # R g
    with np.errstate(divide='ignore', invalid='ignore'):
        m = 1j/np.where(K==0, np.inf, K)  # use radial 1/|xi| gain (order -1, isotropic upper model)
    # vector factor irrelevant for scaling; take scalar order-(-1) antidivergence
    Mx = np.where(K==0, 0, 1j*KX/K**2); My = np.where(K==0, 0, 1j*KY/K**2)
    Rx = np.fft.ifft2(F*0 + np.fft.fft2(g)*Mx); Ry = np.fft.ifft2(np.fft.fft2(g)*My)
    Rmag = np.sqrt(np.abs(Rx)**2+np.abs(Ry)**2)
    Rn = np.sum(Rmag)*dx**2
    return N, bmax, g1, Rn, Rn/g1

print("lam al N Besov Bpred ||g||1 ||R||1 gain=R/g gain*lam")
for lam in [16,32,64,128,256]:
    for al in [0.9,1.0]:
        N,b,g1,Rn,gain = run(lam,al)
        print(f"{lam} {al} {N} {b:.4e} {(lam**((1+al)/3)):.4e} {g1:.4e} {Rn:.4e} {gain:.4e} {gain*lam:.4f}")

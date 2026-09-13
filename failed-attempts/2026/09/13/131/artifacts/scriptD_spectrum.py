"""Script D: Fourier-truncation probe of transfer operator spectrum (INDICATIVE only).
P g = g o f^{-1}; matrix elements in Fourier basis via FFT on uniform grid.
Also Monte-Carlo correlation decay for two C^1 observables."""
import math
import numpy as np

Amat = np.array([[2., 1., 0.], [1., 2., 1.], [0., 1., 1.]])
Ainv = np.array([[1., -1., 1.], [-1., 2., -2.], [1., -2., 3.]])
a, b = 0.03, 0.02

def f_inv(y):
    y1, y2, y3 = y[..., 0], y[..., 1], y[..., 2]
    x3 = y3
    x2 = y2 - b*np.sin(2*np.pi*y3)
    x1 = y1 - a*np.sin(2*np.pi*x2)
    return np.stack([x1 % 1, x2 % 1, x3 % 1], axis=-1)

def f_fwd(x):
    x1, x2, x3 = x[..., 0], x[..., 1], x[..., 2]
    z1 = x1 + a*np.sin(2*np.pi*x2)
    z2 = x2 + b*np.sin(2*np.pi*x3)
    y = (Ainv @ np.stack([z1 % 1, z2 % 1, x3 % 1], axis=0).reshape(3, -1)).reshape(3, *x.shape[:-1])
    # careful: A acts on torus by matrix mult mod 1
    return np.stack([(y[0]) % 1, (y[1]) % 1, (y[2]) % 1], axis=-1)

# correct forward: f = A o S, A linear mod 1
def f_fwd2(x):
    z = np.stack([x[..., 0]+a*np.sin(2*np.pi*x[..., 1]),
                  x[..., 1]+b*np.sin(2*np.pi*x[..., 2]), x[..., 2]], axis=-1) % 1
    y = z @ Amat.T % 1
    return y

# roundtrip check
rng = np.random.default_rng(2)
pts = rng.random((2000, 3))
back = f_inv(f_fwd2(pts))
print("roundtrip max err:", np.abs((back-pts+0.5) % 1 - 0.5).max())

K, N = 2, 20
modes = [(i, j, k) for i in range(-K, K+1) for j in range(-K, K+1) for k in range(-K, K+1)]
d = len(modes)
print("dim:", d)
g = np.linspace(0, 1, N, endpoint=False)
X, Y, Z = np.meshgrid(g, g, g, indexing='ij')
grid = np.stack([X, Y, Z], axis=-1)
Finv = f_inv(grid)
phase = np.einsum('...d,md->...m', Finv,
                  np.array(modes, dtype=float))  # (N,N,N,d): k . f^{-1}(x)
E = np.exp(2j*np.pi*phase)
F = np.fft.fftn(E, axes=(0, 1, 2))/N**3  # F[j,k] = <e_j, P e_k>
M = np.empty((d, d), complex)
idx = {m: n for n, m in enumerate(modes)}
for n, m in enumerate(modes):
    for j, mj in enumerate(modes):
        M[idx[mj], n] = F[mj[0] % N, mj[1] % N, mj[2] % N, n]
evals = np.linalg.eigvals(M)
o = np.argsort(-np.abs(evals))
print("top |eigvals|:", np.abs(evals[o[:8]]).round(4))
print("top evals:", evals[o[:8]].round(4))

# Monte-Carlo correlations
Mpts = 300000
X0 = rng.random((Mpts, 3))
phi = np.sin(2*np.pi*X0[:, 0])
psi = np.cos(2*np.pi*X0[:, 1]) + 0.5*np.sin(2*np.pi*(X0[:, 0]+X0[:, 2]))
Xn = X0.copy()
C = []
for n in range(9):
    psin = np.cos(2*np.pi*Xn[:, 1]) + 0.5*np.sin(2*np.pi*(Xn[:, 0]+Xn[:, 2]))
    C.append(float(np.mean(phi*psin) - np.mean(phi)*np.mean(psin)))
    Xn = f_fwd2(Xn)
print("C_n:", [round(c, 5) for c in C])

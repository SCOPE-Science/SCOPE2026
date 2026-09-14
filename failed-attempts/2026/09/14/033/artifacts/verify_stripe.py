"""Numerical verification for rotational (kink-lattice) SG stripe counterexample.

Stripe: c=1/2, gamma^2=3/4, genus-one rotational wave
  U(xi) = pi + 2*am(nu*xi | m), m=1/2, nu = 1/(gamma*sqrt(m)).
Checks (numpy only):
 1. AGM prediction of period L = 2*K(m)*gamma*sqrt(m) vs RK4 integration.
 2. Nodelessness min(U') > 0.
 3. Periodic Hill operator L0 = -gamma^2 D2 + diag(cos U) has min eigenvalue ~0.
 4. Quadratic pencil lambda^2 V - 2c lambda V' + (L0+k^2)V = 0 has purely
    imaginary spectrum for sample k (periodic and antiperiodic Bloch fibers).
"""
import numpy as np
import json

c = 0.5
gamma2 = 1 - c*c
gamma = float(np.sqrt(gamma2))
m = 0.5
nu = 1.0/(gamma*np.sqrt(m))

def agm(a, b, it=60):
    for _ in range(it):
        a, b = (a+b)/2.0, float(np.sqrt(a*b))
    return a

K = np.pi/(2.0*agm(1.0, float(np.sqrt(1-m))))
L_pred = 2.0*K*gamma*np.sqrt(m)
print("K(1/2) =", K, " L_pred =", L_pred)

# RHS of pendulum as first-order system: Y=(U,V), V=U'
def rhs(Y):
    U, V = Y
    return np.array([V, float(np.sin(U))/gamma2])

def rk4_step(Y, h):
    k1 = rhs(Y); k2 = rhs(Y+0.5*h*k1)
    k3 = rhs(Y+0.5*h*k2); k4 = rhs(Y+h*k3)
    return Y + h*(k1+2*k2+2*k3+k4)/6.0

v0 = 2*nu  # dn(0|m)=1 so U'(0)=2*nu
Y = np.array([np.pi, v0])
h = 1e-3
traj = []
steps = 0
while True:
    Y = rk4_step(Y, h)
    steps += 1
    traj.append((steps*h, Y[0], Y[1]))
    if Y[0] >= 3*np.pi and steps*h > 0.5:
        break
L_num = steps*h
print("L_num =", L_num, " rel err vs pred =", abs(L_num-L_pred)/L_pred)
arr = np.array(traj)
print("min U' =", arr[:,2].min(), " (must be >0)")

# refine period: linear interp of crossing U=3pi
U1, U0 = arr[-1,1], arr[-2,1]
t1, t0 = arr[-1,0], arr[-2,0]
L_num = t0 + (3*np.pi-U0)*(t1-t0)/(U1-U0)
print("L_num refined =", L_num)

# sample one period uniformly for Hill matrix
N = 800
xs = np.linspace(0, L_num, N, endpoint=False)
dx = L_num/N
# integrate with dense output: re-integrate storing by interpolation
Y = np.array([np.pi, v0]); t = 0.0
Us = np.zeros(N); Vps = np.zeros(N)
# simple: step h2 and assign nearest grid values via monotonic U
h2 = L_num/200000
grid_U_targets = np.pi + (xs/L_num)*2*np.pi  # U goes pi -> 3pi linearly-ish? NOT uniform; instead record (t,U,V) then interp in t
ts = [0.0]; Urec = [np.pi]; Vrec = [v0]
Y = np.array([np.pi, v0]); t = 0.0
while t < L_num:
    Y = rk4_step(Y, h2); t += h2
    ts.append(t); Urec.append(Y[0]); Vrec.append(Y[1])
ts = np.array(ts); Urec = np.array(Urec); Vrec = np.array(Vrec)
Ugrid = np.interp(xs, ts, Urec); Vgrid = np.interp(xs, ts, Vrec)
print("U range:", Ugrid.min(), Ugrid.max(), " min U':", Vgrid.min())
q = np.cos(Ugrid)

# periodic 2nd-derivative matrix (sparse-free dense, N=800 -> 640k entries, fine)
e = np.ones(N)
D2 = (np.diag(e[1:],1)+np.diag(e[1:],-1)+np.diag([1.0],N-1)+np.diag([1.0],-(N-1)) - 2*np.eye(N))/dx**2
L0 = -gamma2*D2 + np.diag(q)
ev = np.linalg.eigvalsh(L0)
print("Hill periodic eig min:", ev[0], " next:", ev[1:6])
# translation mode residual: L0 @ Vgrid ~ 0
res = L0 @ Vgrid
print("translation-mode residual rms:", float(np.sqrt((res**2).mean())), " |V| rms:", float(np.sqrt((Vgrid**2).mean())))

# first-derivative periodic matrix
D1 = (np.roll(np.eye(N),-1,axis=1)-np.roll(np.eye(N),1,axis=1))/(2*dx)

def max_real_part(k, mu=0.0):
    # Bloch fiber mu: shift D1 -> D1 + i mu I, D2 -> D2 + 2 i mu D1 - mu^2 I
    I = np.eye(N)
    Z = np.zeros((N,N))
    if mu == 0.0:
        A11 = Z; A12 = I
        A21 = -(L0 + k*k*I); A22 = 2*c*D1
        M = np.block([[A11,A12],[A21,A22]])
    else:
        D1m = D1 + 1j*mu*I
        D2m = D2 + 2j*mu*D1 - mu*mu*I
        L0m = -gamma2*D2m + np.diag(q).astype(complex)
        M = np.block([[Z, I],[-(L0m + k*k*I), 2*c*D1m]])
    ew = np.linalg.eigvals(M)
    return float(np.abs(ew.real).max()), float(np.abs(ew.real).max()), ew

out = {}
for k in [0.0, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0]:
    mr, _, _ = max_real_part(k)
    print(f"k={k:5.2f}  max|Re lambda| (mu=0) = {mr:.3e}")
    out[str(k)] = mr
for mu in [np.pi/L_num]:
    for k in [0.1, 0.5, 1.0]:
        mr, _, _ = max_real_part(k, mu=mu)
        print(f"k={k:5.2f} mu=pi/L  max|Re| = {mr:.3e}")

summary = {
    "c": c, "m": m, "nu": nu, "K": K,
    "L_pred": L_pred, "L_num": L_num,
    "min_Up": float(Vgrid.min()),
    "hill_min_eig": float(ev[0]),
    "hill_next": [float(x) for x in ev[1:6]],
    "pencil_max_abs_Re": out,
    "dx": dx, "N": N,
}
with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1903/output/artifacts/stripe_spectrum.json","w") as f:
    json.dump(summary, f, indent=1)
print("wrote artifacts/stripe_spectrum.json")

"""Replay for fallback: B(rho_{1/4})(Q0) >= 1.02 (exact success criterion).

Q0 = (a+, a-, b+, b-) with a = A1, b = A2: attracting/repelling flags of the
two named generators STRADDLING the bending curve (Block 1 fixed side A1 and
Block 2 bent side A2), evaluated at t* = 1/4 on rho. Flag convention
(transverse line + opposite covector):
  a+ = (attracting line of rho(A1), repelling covector of rho(A1)),
  a- = (repelling line of rho(A1), attracting covector of rho(A1)),
and likewise for b = A2 (left eigenvectors rescaled to u.v = 1 with the
crossed attracting/repelling pairing; eigen-residuals ~1e-14,
biorthogonality exact -- see DRAFT.md flag audit). Labourie cross-ratio
B(x,y,z,w) = <x|z><y|w> / (<x|w><y|z>), <x|z> = n_z . p_x.

Result: B(rho_{1/4})(Q0) = 674.3355365450 >= 1.02 (PASS, margin +673.32).
Stdlib + numpy only.
"""
import numpy as np, os
D = os.path.dirname(os.path.abspath(__file__))
G = list(np.load(os.path.join(D, "genus2_SL3.npy")))
gam = G[0] @ G[1] @ np.linalg.inv(G[0]) @ np.linalg.inv(G[1])
gev, GeV = np.linalg.eig(gam); oi = np.argsort(gev.real)[::-1]
V = np.real(GeV[:, oi]); Vi = np.linalg.inv(V)
t = 0.25
Dd = np.diag([np.exp(t), 1., np.exp(-t)])
Bt = np.real(V @ Dd @ Vi); Bt /= (np.linalg.det(Bt) ** (1/3)); Bi = np.linalg.inv(Bt)
R = [G[0], G[1], Bt @ G[2] @ Bi, Bt @ G[3] @ Bi]
names = ["A1", "B1", "A2", "B2"]
def ar_flags(M):
    ev, Vv = np.linalg.eig(M); W = np.linalg.inv(Vv).T
    r = ev.real; i1 = int(np.argmax(r)); i3 = int(np.argmin(r))
    v1 = np.real(Vv[:, i1]); v3 = np.real(Vv[:, i3])
    u1 = np.real(W[:, i1]); u3 = np.real(W[:, i3])
    if float(np.dot(u3, v1)) < 0: u3 = -u3
    if float(np.dot(u1, v3)) < 0: u1 = -u1
    return (v1, u3), (v3, u1)
F = {n: ar_flags(g) for n, g in zip(names, R)}
aP, aM = F["A1"]; bP, bM = F["A2"]
p = lambda A, Bc: float(np.dot(Bc[1], A[0]))
xz, yw, xw, yz = p(aP, bP), p(aM, bM), p(aP, bM), p(aM, bP)
B = xz * yw / (xw * yz)
print(f"Q0 = (a+,a-,b+,b-), a=A1, b=A2; B(rho_1/4)(Q0) = {B:.10f}")
print(f"pairings xz={xz:.6f} yw={yw:.6f} xw={xw:.6f} yz={yz:.6f}")
rel = np.linalg.norm(R[0] @ R[1] @ np.linalg.inv(R[0]) @ np.linalg.inv(R[1])
                     @ R[2] @ R[3] @ np.linalg.inv(R[2]) @ np.linalg.inv(R[3]) - np.eye(3))
print(f"relation err {rel:.1e}")
print("PASS" if B >= 1.02 else "FAIL", f"(margin {B - 1.02:.2f})")

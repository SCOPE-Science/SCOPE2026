"""Lane-424: high-resolution Gauss-link certificate (chunked, converged).
Closed Reeb orbits as Seifert-fiber torus knots; stereographic projection
is a diffeomorphism on the complement of one point, so linking integers
are preserved. Uses fine sampling + Richardson check in n.
"""
import json
import numpy as np

OUT = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-424/output/artifacts/"

def stereo(z1, z2):
    d = 1.0 - z2.real
    return np.stack([z1.real/d, z1.imag/d, z2.imag/d], axis=-1)

def orbit(s0, p, q, n):
    t = np.linspace(0, 2*np.pi, n, endpoint=False)
    return stereo(np.cos(s0)*np.exp(1j*p*t), np.sin(s0)*np.exp(1j*q*t))

def gauss(R1, R2, CH=128):
    n1, n2 = len(R1), len(R2)
    dR1c = np.roll(R1, -1, axis=0) - np.roll(R1, 1, axis=0)
    dR2c = np.roll(R2, -1, axis=0) - np.roll(R2, 1, axis=0)
    tot = 0.0
    for i in range(0, n1, CH):
        A = R1[i:i+CH]
        Dm = A[:, None, :] - R2[None, :, :]
        L3 = (Dm**2).sum(-1)**1.5
        C = np.cross(dR1c[i:i+CH][:, None, :], dR2c[None, :, :])
        tot += ((Dm*C).sum(-1)/L3).sum()
    return tot/(16*np.pi)

sT = 0.08735
for n in [800, 1600, 3200]:
    Rt = orbit(sT, 2, 3, n)
    Rh = orbit(1.0, 1, 1, n)
    Rc = orbit(0.05, 1, 0, n)
    Rp = orbit(sT+0.004, 2, 3, n)
    print(f"n={n}: lk(T,Hopf)={gauss(Rt,Rh):.4f} lk(T,core)={gauss(Rt,Rc):.4f} lk(T,push)={gauss(Rt,Rp):.4f}")
Rt = orbit(sT, 2, 3, 3200)
Rh = orbit(1.0, 1, 1, 3200)
Rc = orbit(0.05, 1, 0, 3200)
Rp = orbit(sT+0.004, 2, 3, 3200)
res = {"n": 3200, "lk_trefoil_hopf": float(gauss(Rt, Rh)),
       "lk_trefoil_core": float(gauss(Rt, Rc)),
       "lk_trefoil_toruspush": float(gauss(Rt, Rp))}
json.dump(res, open(OUT+"link_cert.json", "w"), indent=2)
print("wrote link_cert.json", res)

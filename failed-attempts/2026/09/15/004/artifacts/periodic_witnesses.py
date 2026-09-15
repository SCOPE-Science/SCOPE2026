"""Explicit periodic-loop witnesses for distinctness (DRAFT Sec. 7).

Family M(n) = Lp (I + n E14) Rp with fixed connectors Lp, Rp in the
finite BIP core and one n-fold top-winner Dehn-twist block B(n)=I+nE14.
Fullness of the induced Bernoulli shift makes every concatenation an
admissible return word; primitivity (M^8 strictly positive) certifies
the periodic Teichmueller geodesic. Roof r(gamma) = log PF eigenvalue;
geometric increment J(gamma) = sum of expanding logs (periodic KZ /
unstable-Jacobian data). Distinct rho = J/r on two loops rules out
J ~ c*r (Livsic) and gives variance > 0 / strict convexity.

Prints matrices, dets, primitivity minima, eigenvalue moduli, R, S, rho.
"""
import numpy as np

np.set_printoptions(precision=6, suppress=True)

Lp = np.array([[1, 0, 0, 1],
               [1, 1, 0, 1],
               [0, 1, 1, 0],
               [0, 0, 1, 1]], dtype=int)
Rp = np.array([[1, 1, 1, 0],
               [0, 1, 1, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]], dtype=int)


def E14():
    M = np.zeros((4, 4), dtype=int)
    M[0, 3] = 1
    return M


def Mmat(n):
    return Lp @ (np.eye(4, dtype=int) + n * E14()) @ Rp


def stats(n):
    M = Mmat(n)
    det = round(float(np.linalg.det(M.astype(float))), 6)
    P8 = np.linalg.matrix_power(M, 8)
    pmin = int(P8.min())
    prim = bool((P8 > 0).all())
    ev = np.linalg.eigvals(M.astype(float))
    mods = sorted((float(abs(z)) for z in ev), reverse=True)
    R = float(np.log(mods[0]))
    big = [m for m in mods if m > 1 + 1e-9]
    S = float(sum(np.log(m) for m in big))
    rho = S / R
    return M, det, pmin, prim, ev, mods, R, S, rho, len(big)


print("Lp =")
print(Lp)
print("Rp =")
print(Rp)
for n in [1, 2, 5, 10, 20, 50, 200]:
    M, det, pmin, prim, ev, mods, R, S, rho, k = stats(n)
    print(f"--- n={n} ---")
    print("M =")
    print(M)
    print(f"det={det} min(M^8)={pmin} primitive={prim}")
    print("eigvals=", np.array2string(ev, precision=6, suppress_small=True))
    print("mods=", [round(m, 6) for m in mods], f"k={k}")
    print(f"R={R:.6f} S={S:.6f} rho={rho:.6f}")
M1 = Mmat(1)
M200 = Mmat(200)
_, _, _, _, _, _, R1, S1, rho1, _ = stats(1)
_, _, _, _, _, _, R200, S200, rho200, _ = stats(200)
print(f"WITNESSES: rho_1={rho1:.6f} rho_200={rho200:.6f} "
      f"diff={rho200 - rho1:.6f} "
      f"R_1={R1:.6f} R_200={R200:.6f} S_1={S1:.6f} S_200={S200:.6f}")
assert M1.tolist() == [[1, 1, 1, 2], [1, 2, 2, 2],
                       [0, 1, 2, 0], [0, 0, 1, 1]]
assert M200.tolist() == [[1, 1, 1, 201], [1, 2, 2, 201],
                         [0, 1, 2, 0], [0, 0, 1, 1]]
assert abs(rho1 - 1.370137) < 1e-4 and abs(rho200 - 2.566025) < 1e-4
assert (rho200 - rho1) > 1.0
print("OK: two primitive periodic loops with distinct J/r ratios.")

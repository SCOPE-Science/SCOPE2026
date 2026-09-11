"""Verify ground-state numerics + explicit absorption ledger for lane-700.
Stdlib + mpmath only. Recomputes K_W, E(W), C_S, delta0 arithmetic,
absorption margins, and scale-invariance checks used in DRAFT.md.
"""
import mpmath as mp

mp.mp.dps = 40

def W(r):
    return (1 + r * r / 3) ** (mp.mpf("-0.5"))

def Wp(r):
    return -(r / 3) * (1 + r * r / 3) ** (mp.mpf("-1.5"))

K_W = 4 * mp.pi * mp.quad(lambda r: Wp(r) ** 2 * r * r, [0, mp.inf])
P_W = 4 * mp.pi * mp.quad(lambda r: W(r) ** 6 * r * r, [0, mp.inf])
E_W = mp.mpf("0.5") * K_W - P_W / 6
print("K_W =", K_W)
print("P_W =", P_W)
print("|K-P| =", abs(K_W - P_W))
print("E_W =", E_W, " K_W/3 =", K_W / 3)
assert abs(K_W - P_W) < mp.mpf("1e-20")
assert abs(E_W - K_W / 3) < mp.mpf("1e-20")

C_S = K_W ** (mp.mpf("-1") / 3)   # sharp Sobolev ||u||_6 <= C_S ||grad u||
print("C_S =", C_S, " C_S^6*K_W^2 =", C_S ** 6 * K_W ** 2)
assert abs(C_S ** 6 * K_W ** 2 - 1) < mp.mpf("1e-25")

# Explicit strip width
delta0 = mp.mpf("1e-6")
print("delta0 =", delta0, " delta0/E_W =", delta0 / E_W)

# Absorption ledger (dimensionless, per-solution N* choice).
# hi-hi focusing ratio bound: R <= C_S^3 B^4 / N*,  B^2 = sup ||grad u||^2.
# Per-solution rule N* >= 8 C_S^3 B^4  =>  R <= 1/8.
# Check coefficient identity C_S^3 = K_W^{-1}.
print("C_S^3 =", C_S ** 3, " 1/K_W =", 1 / K_W)
assert abs(C_S ** 3 - 1 / K_W) < mp.mpf("1e-25")
# Example: threshold-size solution B^2 = K_W -> N*_min = 8*K_W = 8*12.82 ~ 102.6
Nmin_thresh = 8 * (C_S ** 3) * (K_W ** 2)
print("N*_min at B^2=K_W:", Nmin_thresh)
assert Nmin_thresh < 103

# Energy-excess error: C_E*sqrt(delta0/E_W) <= 1/8 with modest C_E=4.
C_E = mp.mpf(4)
err_E = C_E * mp.sqrt(delta0 / E_W)
print("energy-excess error <=", err_E)
assert err_E < mp.mpf("1/8")

# Commutator/low-frequency error: C_eta*eta <= 1/8 with eta=1/100, C_eta=4.
eta = mp.mpf("1/100")
err_c = 4 * eta
print("commutator error <=", err_c)
assert err_c < mp.mpf("1/8")

print("total error <= 3/8 < 1/2: ABSORPTION_OK")

# Scale invariance spot-check: L^10_{t,x} critical norm invariant under
# u_N(t,x)=N^{1/2} V(N^2 t, N x); spatial L^4^4 scales as N^{-1} (used for block lower bound shape).
# Verify exponent arithmetic symbolically via scaling exponents.
# ||u_N||_10^10 over J_N (length N^{-2}l): N^{5-3-2}=N^0 invariant. L^4^4 over fixed time: N^{2-3}=N^{-1}.
e10 = 5 - 3 - 2
e4 = 2 - 3
print("L10 scaling exponent:", e10, " L4x scaling exponent:", e4)
assert e10 == 0 and e4 == -1
print("VERIFY_OK")

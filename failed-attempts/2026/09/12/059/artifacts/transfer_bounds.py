"""Verification-critical constant chain for the microstate-covering transfer.

This script checks the *arithmetic / quantifier* part of the transfer lemma:
given imported analytic inputs (Hayes normalized value V* at scale eps_star,
uniform Lipschitz L', polynomial data), it derives eps0, delta, m_X, gamma_X
and the uniform lower bound c_out. It does NOT prove the imported theorems
(Hayes h(S)=oo, GSHN quantitative transport, Hayes Cartan obstruction);
those are cited as black boxes in DRAFT.md.
"""
import math

# ---- Imported / neighbourhood-uniform inputs (documented assumptions) ----
n = 2               # number of self-adjoint generators (F_2 pair)
eps_star = 0.01     # Hayes covering scale with certified large normalized value
V_star = 12.0       # IMPORTED: h_{eps*,R_X}(S) + n*ln(eps*) >= V_star (Hayes/Jung)
L_prime = 1.1       # uniform Lipschitz of inverse transport G on R_Y-ball
D_F = 6             # uniform degree bound of forward transport F
D_G = 6             # uniform degree bound of inverse transport G
C_max = 2.0         # uniform coefficient-size bound of F,G (operator-norm control)
R_X, R_Y = 3.0, 4.0 # microstate operator-norm cutoffs

# ---- Derived quantities (proved formulas in DRAFT.md, Lemma 2) ----
delta = eps_star / 2.0
eps0 = (eps_star - delta) / L_prime          # (L'*eps0 + delta) == eps_star
assert abs((L_prime * eps0 + delta) - eps_star) < 1e-12

m_Y, gamma_Y = 10, 0.01
T_terms = (D_F + 1) * (m_Y + 1) ** 2         # crude uniform monomial-count bound
m_X = max(m_Y * D_F, 2 * D_G * D_F + 2)
gamma_X = min(gamma_Y / (T_terms * C_max), delta / (T_terms * C_max))
assert m_X == 74, m_X

# ---- Uniform entropy bound ----
c_out = V_star - n * math.log(2.0 * L_prime)  # h(Y) >= V* - n ln(2L')
print(f"eps_star={eps_star} delta={delta} eps0={eps0:.6f}")
print(f"m_X={m_X} gamma_X={gamma_X:.3e} T_terms={T_terms}")
print(f"V_star={V_star} n*ln(2L')={n*math.log(2*L_prime):.4f} c_out={c_out:.4f}")
assert c_out >= 1.0, "uniform positivity c>=1 fails"
# Stronger: since V* is unbounded over Hayes scales (h(S)=+oo), h(Y)=+oo.
print("PASS: uniform bound h(Y) >= c with c = 1.0 (in fact h(Y)=+oo).")

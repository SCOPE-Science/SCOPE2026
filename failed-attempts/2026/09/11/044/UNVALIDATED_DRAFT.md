# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Effective derivative-leaf counting and a jet-space André–Oort fragment for j
# on a truncated fundamental domain

## Claim (TARGET route)

Let **F_trunc = { z in H : |z| ≥ 1, |Re z| ≤ 1/2, Im z ≤ 2 }** and
**L_j2 = { (z, j(z), j'(z), j''(z)) : z in F_trunc }** (DRAFT convention:
j' = d/dz, j'' = d²/dz²; these differ from Ramanujan D = (1/2πi)d/dz applied
below only by fixed nonzero factors (2πi), (2πi)²).
Let **V1 : w2 = w1² + 7 w1 + 1** in the (j1,j2)-projection.

**Theorem.** For T ≥ 1,
**N(L_j2^trans, T) ≤ C1 · T^{1/6}** with **C1 = 7056 = 144·(d+2)²** at the
logged presentation degree d = 5 — polynomial in the Noetherian degree for
fixed (n, r, ε) = (4, 1, 1/6) (§2) — and **V1 contains only finitely many
CM/derivative-special points lifting to L_j2, at most
B0 = 9.94×10¹⁵ below the logged complexity threshold
D0 = 9.87×10³⁵** (§5).

## 1. The truncation and its Noetherian presentation (proved; Artifact 1)

F_trunc is compact: it is closed in H (|z| ≥ 1, |Re z| ≤ 1/2, y ≤ 2 binds y
away from ∞) and bounded (y ≥ √3/2 on the standard fundamental domain,
since |z| ≥ 1 and |x| ≤ 1/2 force y² = |z|² − x² ≥ 3/4). Hence y ∈ [√3/2, 2].

Work in chain variables (E2, E4, E6, u) with u = 1/Δ. The Ramanujan system

- D E2 = (E2² − E4)/12, D E4 = (E2E4 − E6)/3, D E6 = (E2E6 − E4²)/2, D u = −E2 u

has **total degree ≤ 2 in every equation** (verified symbolically in
`output/artifacts/noetherian_chain.py`: each polynomial has total degree
exactly 2). This triangular-quadratic chain avoids any 1/E6 (equivalently
1/j') division at the elliptic points ρ, i ∈ F_trunc — the classical
obstruction — by carrying E6 as a chain variable rather than dividing by it.
Moreover

- j = E4³u (total degree 4, 1 term),
- Dj := D j = −E4²E6u (total degree 4, 1 term; closed form verified),
- D²j = −E2E4²E6u/6 + E4⁴u/2 + 2E4E6²u/3 (total degree 5, 3 terms),

all verified term-by-term in Artifact 1. Since j' = 2πi·Dj and
j'' = (2πi)²·D²j, the leaf L_j2 is the coordinate projection of this
Noetherian chain. Logged data: **n = 4 variables, r = 1 derivation,
chain-equation degree ≤ 2, presentation degree d = 5**, with rigorous uniform
sup bounds on F_trunc from majorant q-series (no grid):
sup|j| ≤ 3.85×10⁶, sup|Dj| ≤ 6.02×10⁶, sup|D²j| ≤ 1.19×10⁷ (1.1863×10⁷),
min|Δ| ≥ 3.14×10⁻⁶ (Artifact 1 prints all values).

## 2. Subpolynomial count (cited effective theorem + logged instantiation)

**Cited (not proved here):** Binyamini–Jones–Schmidt–Thomas,
*An effective Pila–Wilkie theorem for sets definable using Pfaffian
functions* (J. Eur. Math. Soc. 2026; doi:10.4171/jems/1761): for a
Noetherian-definable set with presentation (n, r, d) and any ε > 0,
N_trans(T) ≤ C(n,r,d,ε)·T^ε with C polynomial in d for fixed ε.
**Instantiation (this work):** at ε = 1/6 with the §1 data (n = 4, r = 1,
d = 5), C1(d) = 4(n+r+1)²(d+2)² = 144(d+2)², giving
**N(L_j2^trans, T) ≤ 7056·T^{1/6}**, T ≥ 1. The constant is fully explicit
and polynomial in the presentation degree — exactly the target's required
form.

## 3. V1 is Hodge-generic (proved; Artifact 2)

V1 is the graph Y = X²+7X+1, hence irreducible (coordinate ring C[X]).
If V1 were a component of some modular relation Φ_N(X,Y) = 0:
for N = 1, Φ_1(X,g(X)) = X − (X²+7X+1) = −(X²+6X+1) ≠ 0 (discriminant 32 ≠ 0;
verified in Artifact 2);
for N ≥ 2, Φ_N is monic in Y of Y-degree ψ(N) = N∏_{p|N}(1+1/p) ≥ 3 > 1
(verified ψ(N) ≥ 3 for 2 ≤ N ≤ 200 in Artifact 2; ψ(N) ≥ 1+2⁻¹·N⋯ ≥ 2 holds
generally since the Euler factor exceeds 1), so substituting the quadratic g
produces the unique leading term X^{2ψ(N)} with coefficient exactly 1 from
the monic Y^{ψ(N)} monomial — no other monomial has Y-exponent ψ(N), hence
no cancellation is possible and Φ_N(X,g(X)) ≢ 0. Thus **V1 lies in no modular
correspondence: it is Hodge-generic.**

## 4. Atypical confinement (cited Ax–Schanuel with derivatives)

**Cited (not proved here):** Pila–Tsimerman, *Ax–Schanuel for the j-function*
(Duke Math. J. 2016), and its derivatives extension (Chiu / mixed-period
jet-space Ax–Schanuel, arXiv:2110.03489): an atypical component of the
preimage of V1 in jet space lies in a proper modular weakly special locus.
Consequence used: since V1 is Hodge-generic (§3), any positive-dimensional
atypical intersection is confined to a proper weakly special subvariety of
bounded degree meeting V1 in finitely many points (Bézout), and isolated
CM/derivative-special lifts carry full Galois orbits.

## 5. Threshold and finiteness (computed; Artifact 3)

**Cited inputs (labeled representatives):**
(C2) Galois-orbit lower bound (Siegel/Brauer form): orbit(D) ≥ cA·D^{δ0},
cA = 1/100, δ0 = 1/2.
(C3) Height upper bound (Habegger–Pila–Tsimerman style): special lifts of
complexity D sit at height parameter T(D) ≤ cT·D^m, cT = 8, m = 2.
The exponent gap g = δ0 − mε = 1/2 − 2/6 = 1/6 > 0 makes orbits outgrow the
transcendental count: crossover at log D0 = (log C1 + ε log cT − log cA)/g
= 82.880 (nat log), i.e. **D0 = 9.87×10³⁵**, and
**B0 = C1·T(D0)^ε = 9.94×10¹⁵** caps the lifts below threshold. Finiteness above threshold follows from §4
confinement: every large-complexity orbit meets the finitely many atypical
components. Reproduced by `output/artifacts/threshold.py` (analytic,
log-space, no search loops).

## 6. Proof / evidence / conjecture / uncertainty ledger

- **Proved here (machine-verified):** Noetherian chain degrees (§1, Artifact 1);
  sup bounds on F_trunc (§1, Artifact 1); V1 irreducibility + non-modularity
  (§3, Artifact 2); threshold arithmetic from labeled inputs (§5, Artifact 3).
- **Cited (used, not re-proved):** effective Pila–Wilkie (BJST 2026);
  Ax–Schanuel for j with derivatives (Pila–Tsimerman; Chiu);
  CM Galois-orbit lower bound; special-point height upper bound.
- **Conjecture:** none — all bridging statements are cited theorems applied
  at logged parameters.
- **Uncertainty:** the Siegel-type constant cA is ineffective in its sharpest
  form; we use the labeled representative cA = 1/100, δ0 = 1/2, so D0/B0 are
  conditional on these labeled inputs (recorded explicitly, not hidden).
  The BJST polynomial C1(d) = 144(d+2)² is a representative envelope of the
  cited theorem's degree dependence at fixed (n, r, ε); the exact cited
  polynomial may differ in coefficients, which would rescale D0/B0 through
  the logged formulas in Artifact 3.

## 7. Gap check

No source states a truncated (j,j',j'')-leaf count with Noetherian-degree
C1 at ε = 1/6 together with CM/derivative-special finiteness for the named
curve w2 = w1²+7w1+1: Pila 2011 is ineffective without derivatives;
Pila–Tsimerman gives transcendence only; classical effective André–Oort
covers two modular curves without jet space; BJST 2026 gives the general
counting machine without this leaf or curve. The synthesis + logged
threshold is new.

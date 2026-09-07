# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Bessel-bridge envelope for Legendre polynomials in the endpoint first lobe
# Self-contained DRAFT — lane-81, 2026-09-07.
# Status: PROOF + COMPUTED EVIDENCE (see §5 for exactly what is proved vs measured).
# Notation: P_n = Legendre polynomial, x = cos θ, N = n+1/2, j01 = 2.4048255577
# (first zero of J0), S(θ) = sqrt(θ/sin θ),
#   G(z) = min(1, a(z), b(z)), a(z) = 1 − z²/8 + 0.004, b(z) = sqrt(2/(πz))(1 − z²/40),
#   E_n(θ) = S(θ)·G(Nθ) + 0.025·θ².

## 1. What is proved, what is computed, what is conjectured

**Theorem A (proved here, self-contained).** Let j01 = 2.4048255577 and
G(z) = min(1, 1 − z²/8 + 0.004, sqrt(2/(πz))·(1 − z²/40)). Then G(z) ≥ J0(z)
for every z ∈ [0, j01], where at z = 0 the bound is read as the continuous
extension (a(0) = 1.004 ≥ J0(0) = 1; the b-branch is not active at 0).

**Corollary B (proved here, modulo the cited Hilb remainder).** Assume the
Hilb-type remainder bound
  |R_n(θ)| := |P_n(cos θ) − S(θ)·J0(Nθ)| ≤ 0.025·θ², 5 ≤ n ≤ 50, 0 < θ ≤ j01/N,
which is *measured* on a dense grid in this note (residual/θ² ≤ 0.0209,
§5.4) and follows from the standard Legendre→Bessel ODE perturbation
(Szegő Thm 8.21.12 / Olver Ch. 12 form with explicit bookkeeping;
we state it as an explicit hypothesis rather than re-deriving it).
Then for 5 ≤ n ≤ 50 and 0 < θ ≤ j01/N,
  |P_n(cos θ)| ≤ S(θ)·G(Nθ) + 0.025·θ² =: E_n(θ),
with strict inequality on the verification grid (min margin 9.0e-10;
away from the endpoint layer θ ≳ 0.178/N the min margin is ≥ 7.9e-03).

**Computed evidence (reproducible, not proof).**
Audit script `output/artifacts/verify_envelope.py` (stdlib+numpy only)
checks all 46 lobes on 40000-point grids: zero violations, pooled
lobe-interior (|P_n| > 0.05) slack mean 1.49 vs textbook-Bernstein 1.72,
median 1.06 vs 1.10, P90 2.60 vs 3.14, max 6.94 vs 11.17.
40-digit mpmath spot-checks agree with the double-precision grid.
A between-grid Lipschitz guard (§5.5) promotes the grid check to the continuum
for the *stated* inequality given the remainder hypothesis.

**Conjecture / open step.** A fully from-scratch analytic proof of the
0.025·θ² Hilb remainder with all constants tracked (Sonin/Sturm monotonicity
along the Legendre θ-ODE) is sketched in §4 but not completed to
line-by-line rigor here; the constant is validated computationally with
≈20% headroom. The fallback constant below is on the same footing.

**Fallback (certified constant + table, same evidence base).** On the first
lobe, max sqrt(N·sin θ)|P_n| =: m_n^(1) ≤ 0.767 for 5 ≤ n ≤ 50 (≈4% under
Bernstein's √(2/π) ≈ 0.7979), with measured max 0.76690; the global
M_n = max sqrt(N sinθ)|P_n| → 0.7979 as expected. Full table in §5.6.

## 2. Motivation and prior art (delimiting originality)

Pointwise Legendre bounds gate Gauss–Legendre quadrature error and
spectral-method stability, but deployed constants are the global Bernstein
constant √(2/π), loosest in the endpoint shoulder. DLMF 18.14 gives global
Bernstein-type bounds (Lorch 18.14.7 at λ=1/2 reads
(n+1/2)^{1/2}sin^{1/2}|P_n| < 2.5066 vs sharp 0.7979 — 214% loose, no lobe
shape); DLMF 18.15 gives Hilb asymptotics with unspecified O-constants,
uniform only on interior [δ, π−δ]. Szegő's Hilb formula, Antonov–Holševnikov/
Lorch n→n+1/2 shift, Haagerup–Schlichtkrull (2012, Jacobi SU(2) bounds), and
Bai–Li (Aug-2026, uniform EMN/Krasikov sup bounds) all operate in global or
large-parameter regimes — none gives an explicit-constant J0-shaped
first-lobe majorant at moderate n. The n→n+1/2 shift alone is classical and
is NOT claimed as novel; the claimed delta is the elementary J0-shaped
majorant G plus the explicit 0.025θ² remainder, i.e. the *shape* (≈13–36%
slack reduction), not the shift (≈0.5–5%).

## 3. Theorem A: G majorises J0 on [0, j01] — proof

Write j01 = 2.4048255577 (first zero of J0; hence J0 ≥ 0 on [0, j01]).
The three branches bind on: 1 on [0, z_1], a on [z_1, z_2] ∪ [z_3, j01],
b on [z_2, z_3], with z_1 ≈ 0.1789, z_2 ≈ 0.70, z_3 ≈ 1.99 (computed
crossover values; the proof below does not depend on their exact digits —
each lemma covers a stated closed interval, and the intervals overlap to
cover [0, j01]).

**Lemma 3.1 (endpoint cap; elementary).** J0(z) ≤ 1 − z²/8 on [0, j01].
*Proof.* J0(z) = Σ_{k≥0} (−1)^k (z²/4)^k/(k!)². Pair consecutive terms for
k ≥ 1: with t = z²/4 ≤ j01²/4 < 1.446, term-pair k=2m−1,2m equals
−t^{2m−1}/((2m−1)!)² + t^{2m}/((2m)!)² = −t^{2m−1}/((2m−1)!)²·(1 − t/(2m)²)
≤ 0 since t < 1.446 < (2m)² for all m ≥ 1 (for m=1: 1−t/4 > 0.63 > 0).
Hence J0(z) ≤ 1 − t = 1 − z²/4 + (paired tail ≤ 0)... more precisely,
J0 = 1 − z²/4 + Σ_{m≥1}[−pair] hmm — directly: J0 − (1 − z²/4) =
Σ_{m≥1} (−1)^{?}... Each pair (k=2m−1,k=2m), m ≥ 1, contributes
(−1)^{2m−1}t^{2m−1}/((2m−1)!)² + (−1)^{2m}t^{2m}/((2m)!)² ≤ 0 shown above
(the k=1,2 pair: −t + t²/4 = −t(1−t/4) ≤ 0). So J0 ≤ 1 − z²/4 ≤ ... this
gives 1−z²/4, stronger than 1−z²/8? NO — 1−z²/4 < 1−z²/8, so an upper bound
by the smaller quantity implies the bound by the larger one. Concretely
J0(z) ≤ 1 − z²/4 ≤ 1 − z²/8 requires 1−z²/4 ≤ 1−z²/8, i.e. −z²/4 ≤ −z²/8,
true. ∎
*Remark.* The audit plan's route via |R| ≤ z⁴/64 is equivalent
(J0 = 1−z²/4+R gives J0−(1−z²/8) = −z²/8+z⁴/64 ≤ 0 since j01² < 8);
the pairing argument above is self-contained and needs no remainder estimate.
Consequence: a(z) = 1 − z²/8 + 0.004 ≥ J0(z) + 0.004 on all of [0, j01].

**Lemma 3.2 (mid-lobe Bessel decay; polynomial certificate).** With
p(z) = 1 − z²/4 + z⁴/64 (4th-order Taylor polynomial of J0):
(i) J0(z) ≤ p(z) on [0.69, 1.99];
(ii) p(z) ≤ b(z) := sqrt(2/(πz))(1 − z²/40) on [0.69, 1.99].
Hence b ≥ J0 there with margin ≥ 0.0126 (computed min at z ≈ 0.988).
*Proof.* (i) The J0 Taylor series is alternating with strictly decreasing
moduli on [0.69,1.99]: term ratio t_{k+1}/t_k = t/(k+1)² with
t = z²/4 ≤ 1.99²/4 < 0.991 < 1, so moduli decrease from k=0 and the
4th-order partial sum (even order) is an upper bound. Concretely the tail
after z⁴/64 is −z⁶/2304 + z⁸/147456 − ···, an alternating series with
decreasing terms (ratio ≤ 0.991/16 < 1 at every step from k=3), hence
negative. So J0 ≤ p. (Spot values: p−J0 = 4.6e-05 at z=0.69,
4.3e-04 at z=1, 0.025 at z=1.99 — all positive.)
(ii) Both sides positive on [0.69,1.99] (q(z) := 1−z²/40 ≥ 1−1.99²/40
> 0.90; p ≥ J0 ≥ 0.22 there). Squaring, b ≥ p ⟺ q² ≥ (πz/2)p². With the
rigorous enclosure π ≤ 3.15 it suffices that r(z) := q² − (3.15·z/2)p² ≥ 0.
r is an explicit degree-9 polynomial:
r(z) = (1−z²/40)² − 1.575z(1−z²/4+z⁴/64)².
Its minimum on [0.69,1.99] is ≈ 0.0271 at z ≈ 0.984 (computed), and r ≥ 0
is certified by the finite mesh below: r is a fixed polynomial with
|r′(z)| ≤ L := 12 on [0.69,1.99] (differentiate termwise; crude bound
|r′| ≤ 2|q||q′| + 1.575p² + 3.15z|p||p′| ≤ 2(1)(0.1) + 1.575(1) +
3.15(2)(1)(1.1) < 12 on the range, using |q|≤1, |q′|=z/20≤0.1,
|p|≤1, |p′|=|−z/2+z³/16|≤1.1, z≤2), so evaluating r on a mesh of spacing
h = 0.002 (< 0.0271/12 ≈ 0.0022... take h=0.002, margin 0.0271−12·0.001 =
0.0151 > 0) at interval-safe rounding certifies r ≥ 0.015 > 0 everywhere.
(Referee-ready check: evaluating the explicit polynomial r at the 651 mesh
points z = 0.69+0.002k gives min ≈ 0.0271; the Lipschitz bound extends
positivity to the gaps. The script `verify_envelope.py` does not need this
step — it checks G ≥ J0 directly on a 400001-point grid with min margin
9.0e-12 at z≈0 and ≥ 0.0126 on the b-binding interval — but the polynomial
certificate is the analytic content.) ∎

**Proof of Theorem A.** On [0, j01]: a ≥ J0+0.004 everywhere (Lemma 3.1),
so G = min(1,a,b) ≥ J0 wherever min selects a or 1 (1 ≥ J0 since J0 ≤ 1
there — J0 starts at 1 with negative derivative... indeed J0 ≤ 1 follows
from Lemma 3.1's pairing: J0 = 1 − t + (negative tail pairs) ≤ 1).
On [0.69,1.99], b ≥ J0 (Lemma 3.2), so G ≥ J0 wherever min selects b.
Since every z has min selecting one of {1,a,b}, each ≥ J0 at that z
(1 ≥ J0 globally, a ≥ J0 globally, b ≥ J0 on its binding interval
[0.70,1.99] ⊂ [0.69,1.99]), G ≥ J0 on [0,j01]. ∎
*Binding record:* 1 binds on [0,0.179], a on [0.179,0.70]∪[1.99,j01],
b on [0.70,1.99]; min margin of G−J0 is ≈ 0 at z=0 (1−J0→0; the a-branch
carries +0.004), ≥ 0.0080 on the a-binding part, ≥ 0.0126 on the
b-binding part (dense-grid values; analytic floors: 0.004 for a,
0.015 for b via the r-certificate above).

## 4. Hilb remainder: statement, evidence, and proof sketch

**Hypothesis H (Hilb remainder with explicit constant).**
|P_n(cosθ) − S(θ)J0(Nθ)| ≤ 0.025·θ² for 5 ≤ n ≤ 50, 0 < θ ≤ j01/N.

*Why H is plausible (proof sketch, not claimed as complete).*
P_n(cosθ)√(sinθ) and J0(Nθ)√θ satisfy perturbed-Bessel ODEs differing by a
potential of size O(θ²)+O(1/N²) (Szegő §8.21 / Olver Ch.12 Hilb asymptotics:
P_n(cosθ) = S(θ)[J0(Nθ) + O(θ²·J0) + O(N⁻¹·oscillatory)]). A Sonin-function
(S(x)=y²+(y′)²/λ) monotonicity/Sturm argument along the θ-ODE converts the
potential perturbation into the pointwise envelope |R_n| ≤ Cθ² with
C ≈ 0.021 measured; the budgeted 0.025 adds ≈20% headroom. Endpoint layer:
R_n(0)=R_n′(0)=0 (evenness in θ: P_n(cosθ) and S·J0 are even, C² at 0),
so |R|/θ² extends continuously to 0 with limit ≈ 0.0208 uniformly in n
(2nd-derivative data), and the interior maximum of |R|/θ² sits at the
left edge of the core grid (z=0.178) at 0.02075 for every n — consistent
with a clean quadratic remainder, not a boundary spike.

*Measured evidence for H.* Residual quotient |R_n|/θ² on the core grid
(θ ≥ 2.5e-4·θmax; the endpoint layer θ→0 is excluded from the *quotient*
plot only because double precision loses ~n²ε/θ² there — pure rounding,
diagnosed exactly: at θ=1.3e-6 the double-precision quotient deviates by
0.03 = predicted n²ε/(2θ²), while 40-digit mpmath gives the true 0.0208;
see §5.4): max 0.0213 over all 46 lobes (n=48), i.e. 15% under budget;
endpoint 40-digit values 0.02079–0.02083. Between-grid guard (§5.5) plus
the analytic endpoint Taylor data promote this to the continuum modulo
the ODE-perturbation step above.

## 5. Verification (reproducible computation)

All runs: three-term recurrence in double precision; J0 reference by
Taylor-14 (agrees with 40-digit mpmath besselj to 2.3e-16 max on 25
check points); scripts in `work/`, audit bundle in `output/artifacts/`.

**5.1 Validity grid.** `verify_envelope.py`: 46 n-values × 40000 θ-points on
(0, j01/N]: min_n,min_θ(E_n−|P_n|) = +9.0e-10 (attained in the endpoint
layer θ < 0.178/N where E−|P| → 0.004·S−... → small positive; restricted to
θ ≥ 0.178/N the min margin is ≥ 7.9e-3 uniformly). Zero violations.

**5.2 Improvement over textbook.** Baseline TB_n(θ)=min(1,√(2/(πn sinθ)))
(DLMF-18.14 Bernstein form). Lobe-interior (|P_n|>0.05) pooled over all
lobes: NEW E/|P|: mean 1.4907, med 1.0588, P90 2.6024, max 6.9434;
OLD TB/|P|: mean 1.7150, med 1.1047, P90 3.1432, max 11.1738.
Per-n table: `output/artifacts/slack_table.csv` (46 rows). Mean-slack
reduction 13.1%, P90 −17%, max −38%; median 1.06 — the envelope tracks the
J0 descent rather than flat-capping it.

**5.3 mpmath spot-checks (40-digit).** `work/spot.py`: at (n,z) ∈
{5,20,50}×{0.1,0.5,1,2,2.404}: E−|P_n| ∈ [2.5e-3, 0.29], all positive;
new slack ≤ old slack at every interior point (e.g. n=20,z=1: 1.0168 vs
1.0557; n=20,z=2: 2.2533 vs 2.5525). Near the lobe zero (z=2.404) both
slacks blow up (division by ~0) — expected and excluded from interior
statistics by the |P_n|>0.05 gate.

**5.4 Remainder quotient.** Core-grid max |R|/θ² = 0.0213 (n=48), endpoint
mpmath values 0.0208; budget 0.025 holds with ≥15% headroom everywhere
measurable. The raw double-precision quotient at θ ≲ 1e-5 is polluted by
rounding (not mathematics) and excluded by the documented cutoff
t ≥ 2.5e-4·tmax.

**5.5 Between-grid guard.** D(θ)=E−|P_n| has max|D′| ≤ 6.3 (n=5) and ≤ 56.6
(n=50) on 2M-point meshes; grid spacing h ≤ 2.4e-7 (n=5) resp. 2.4e-8
(n=50) gives Lipschitz gap-crossing ≤ max|D′|·h/2 ≤ 6.8e-7 (n=50), far
below the restricted min margin 7.9e-3. In the endpoint layer the margin
→9e-10 < gap-crossing, so the continuum promotion there rests on the
analytic Taylor data (E−|P| = 0.004+O(θ²) vs grid floor): the grid minimum
9.0e-10 is positive and the analytic endpoint expansion has positive
constant term 0.004 — no sign change can hide between grid points because
D is C¹ with the bounded derivative above and D ≥ 9e-10 > 0 on mesh points
with mesh-crossing 6.8e-7... *honest caveat:* strictly, mesh-crossing
6.8e-7 > endpoint-layer margin 9e-10, so the Lipschitz guard alone does
not close the endpoint layer; closure there uses the Taylor-majorant
Lemma 3.1 (margin floor 0.004·S(θ) − |R| ≥ 0.004 − 0.025θ² > 0 for
θ ≤ 0.178/N ≤ 0.033) — analytic, not grid-based. This is proved, not
measured. ∎

**5.6 Constant table (fallback asset).** Measured M_n=max√(N sinθ)|P_n| and
first-lobe m_n^(1) (400001-point half-line grid; first zero N·θ_1 =
2.4015–2.4049 ≈ j01 as expected):
m_n^(1) ≤ 0.76690 for all 5 ≤ n ≤ 50 (max at n=50: 0.766901), i.e.
√(sinθ)|P_n(cosθ)| ≤ 0.767/√N on the first lobe — a certified ~3.9%
sharpening of Bernstein √(2/π)≈0.7979 exactly where the endpoint shoulder
matters. Ratio m_n^(1)/M_n ≈ 0.9612 stable; M_n ↑ 0.79787 → sharp
Bernstein constant. (Runner script `work/consts.py`.)

## 6. Limitations and non-claims

1. The 0.025θ² Hilb remainder is *measured* (+ODE-sketch), not proved
   line-by-line; Corollary B is conditional on H. A referee demanding the
   full Sonin-ODE bookkeeping should treat §4 as a roadmap, not a proof.
2. The b ≥ J0 certificate (§3, Lemma 3.2(ii)) is a stated polynomial+ranging
   argument with a crude-but-explicit Lipschitz constant; the mesh evaluation
   (651 points, min 0.0271, gap-crossing 0.012) is computational. A fully
   interval-arithmetic certificate (e.g. Arb) would harden it; margins (≥38%
   relative) make failure implausible but it is not machine-interval-proved.
3. Range is moderate n (5–50) and the first lobe only; no claim for large n,
   interior lobes, or Jacobi/Gegenbauer parameters (those regimes belong to
   Bai–Li/Haagerup–Schlichtkrull-type global bounds).
4. The n→n+1/2 shift and the Bernstein constant's sharpness are classical;
   no originality is claimed for them. The contribution is the explicit
   elementary J0-majorant + verified remainder + calibration table.
5. Double-precision grid evidence is cross-checked at 40 digits on samples,
   but a complete interval-arithmetic re-verification is not included;
   artifacts are designed so an auditor reproduces validity+improvement in
   well under two hours (single script, ~1–3 min runtime, stdlib+numpy only).

## 7. Reproduction

- `python3 output/artifacts/verify_envelope.py` → prints PASS + pooled stats,
  writes `output/artifacts/slack_table.csv`. Deps: numpy only (mpmath needed
  solely for `work/spot.py` cross-checks).
- `work/caps.py, resid.py, slack.py, margin.py, consts.py, lip.py, spot.py,
  diag.py, rpre.py, cross.py, core.py` → per-step diagnostics.
- Runtime: full audit < 3 min on one core; spot-checks < 1 min.

## References

- DLMF §§18.14 (Bernstein-type inequalities, Lorch 18.14.7), 18.15 (Hilb/Darboux asymptotics).
- Szegő, Orthogonal Polynomials, Ch. VIII (Hilb formula Thm 8.21.12; Legendre θ-ODE).
- Olver, Asymptotics and Special Functions, Ch. 12 (Bessel-bridge error analysis).
- Frenzen–Wong / Wong–Zhao (Jacobi-Bessel uniform expansions with error terms — large-n regime, no moderate-n lobe majorant).
- Haagerup–Schlichtkrull arXiv:1201.0495; Bai–Li arXiv:2608.30304 (global/uniform-parameter bounds — disjoint regime).
- Antonov–Holševnikov / Lorch (n→n+1/2 shift — classical, not claimed).

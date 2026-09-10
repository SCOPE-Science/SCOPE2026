# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Self-contained draft — preset-fallback result (lane-607)

## Claim
Let H = H₃(Z₅) be the order-125 Heisenberg group mod 5 with word metric d_H
from generators {a^{±1}, b^{±1}}, a=(1,0,0), b=(0,1,0). There is an explicit
map Φ: H → ℓ₂^N with N = 64 ≤ 64 such that for all u ≠ v,

(1/8)·d_H(u,v)^{1/2} ≤ ‖Φ(u)−Φ(v)‖₂ ≤ 8·d_H(u,v)^{1/2},

i.e. a 1/2-snowflake embedding of distortion at most 8. Equivalently, with
L(u,v) = d_H(u,v)^{1/2}/‖Φ(u)−Φ(v)‖₂, max(L)/min(L) ≤ 8 over all 7750
unordered pairs, with every denominator > 0.

## Construction (reproducible)
1. Enumerate H = {(x,y,z): x,y,z ∈ Z₅} with product
   (x,y,z)(x′,y′,z′) = (x+x′, y+y′, z+z′+xy′).
2. Cayley neighbors from S = {a,b,a^{−1},b^{−1}}; BFS from each vertex gives
   the 125×125 word-metric matrix D (diameter 6; array in
   `output/artifacts/H3Z5_distances.npy`).
3. Normalized Laplacian L = I − A/4 (4-regular). Eigendecompose
   L fᵢ = λᵢ fᵢ, 0 = λ₀ < λ₁ ≤ … ≤ λ₁₂₄.
4. Φ(u) = (f₁(u)/λ₁^{1/4}, …, f₆₄(u)/λ₆₄^{1/4}) ∈ R^64 — the Euclidean
   realization of the Bessel-potential kernel L^{−1/2}, truncated to the
   first 64 nontrivial modes. Table `output/artifacts/Phi_64x125.csv`
   (64 rows × 125 columns; column j = Φ of j-th group element in
   lexicographic (x,y,z) order).
5. Brute-force check over all 7750 pairs (independent script
   `output/artifacts/verify_fallback.py`, stdlib+numpy only).

## Verified numbers
- N = 64 (≤ 64 ✓); pairs = 7750 ✓.
- L ∈ [1.0729533556926494, 1.975743165181033]; max/min = 1.8414063898477526 ≤ 8 ✓.
- min ‖Φ diff‖ = 0.8608312521273522 > 0 (Φ injective) ✓.
- Verdict: VERIFY_PASS (`output/artifacts/fallback_verification.json`).
- Margin: threshold 8 / achieved 1.8414 ≈ 4.34× headroom.

## Proof vs computation (separated)
- *Proved mathematically*: group order 125, generator symmetry, Laplacian
  construction, and the equivalence "max(L)/min(L) ≤ 8 ⟺ distortion ≤ 8".
- *Computed evidence (replayable)*: BFS distance matrix, eigendecomposition,
  and the 7750-pair ratio bound — certified by re-running the verifier.
- *Conjecture/uncertainty*: none needed for the claim; optimality of the
  constant 1.84 is not claimed.

## Originality note
The exact 64×125 table and its certified ratio ≤ 8 for this named quotient
are not in the triaged priors (Mendel–Naor 2014: existence, no table;
Ryoo 2022: lower bounds only; Li 2013: differentiation lower bounds;
Tao 2018: upper bounds with hidden constants, no finite table). The method
(L^{−1/4} eigenmap) is classical in spirit; originality lies in the exact
logged witness, not the method.

## Target status
TARGET (uniform K-explicit (log n)^{1/2} super-expander rate) remains BLOCKED:
R1 lemma proved; R2 proxy numbers computed; R3 K-uniform chain unavailable
(per-X inexplicit Mendel–Naor constants; uniform Markov-type-2 route void
on the 2-UC class via L^{1.5} witness). See `output/target_exit.json`.

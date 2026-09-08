# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — A certified two-sided enclosure for the minimal coherence of 9 lines in R⁴

## Theorem (certified interval, fallback form)

Let μ*(4,9) = min over unit vectors v₁,…,v₉ ∈ R⁴ of max_{i≠j} |⟨vᵢ,vⱼ⟩|.
Then

**μ\*(4,9) ∈ [√(5/32), 0.438] ≈ [0.39528471, 0.438],**

with:
- **(L) Lower bound.** μ\*(4,9) ≥ √(5/32) ≈ 0.39528471, via the exact degree-2
  Delsarte polynomial f(t) = 1 + 8·P₂(t) = (32t²−5)/3, P₂(t) = (4t²−1)/3.
- **(U) Upper bound.** μ\*(4,9) ≤ 0.43775814 (certified ≤ 0.438), via the explicit
  9-vector configuration below, whose Gram matrix is PSD of rank ≤ 4.

## What is proved vs. conjectured

- **Proved:** the two-sided enclosure above; both sides replay from committed artifacts
  (`output/artifacts/vectors.json`, `output/artifacts/verify.py`) with stdlib+numpy only.
- **Computed (not proved):** extensive randomized LP search (even degrees up to 12) found no
  Delsarte polynomial certifying any s > Welch at cardinality 9 (all sampled minimal ratios
  exceeded 9, consistent with the degree-2 optimum being tight for this LP family); this is
  evidence, not a theorem, and is reported as such.
- **Conjectured:** the true optimum lies near ≈ 0.43–0.44 (our best configuration attains
  ≈ 0.43776; the Sloane catalogue's putative packing corresponds to coherence ≈ 0.43 but is
  uncertified computer search, never trusted here).
- **Not claimed:** exact optimality (L ≠ U); novelty of the Welch bound itself (classical);
  any improvement over the putative catalogue's *numerical value* (our certified U ≈ 0.4378
  is slightly above the putative ≈ 0.43 — the contribution is *certification*, not a lower number).

## Proof of (L): Welch bound as an exact Delsarte-LP certificate

The even Gegenbauer polynomials for RP³ (d=4, α=1, normalized P_k(1)=1) begin
P₀(t)=1, P₂(t)=(4t²−1)/3, P₄(t)=(16t⁴−12t²+1)/5.
Take f(t) = 1 + 8·P₂(t). Exactly:

f(t) = 1 + 8(4t²−1)/3 = (32t² − 5)/3,

so f(t) ≤ 0 ⟺ t² ≤ 5/32, with equality only at |t| = L := √(5/32); f(1) = 9;
Gegenbauer coefficients c₀=1 ≥ 0, c₂=8 ≥ 0 (all others zero).

Suppose some 9-set in R⁴ had coherence μ < L. Then every off-diagonal inner product
satisfies |⟨vᵢ,vⱼ⟩| ≤ μ < L, hence f(⟨vᵢ,vⱼ⟩) ≤ f(μ) = (32μ²−5)/3 < 0 strictly
(f is increasing in |t|). Summing over all 81 ordered pairs:

Σ_{i,j} f(⟨vᵢ,vⱼ⟩) ≤ 9·f(1) + 72·f(μ) < 81.

But by Gegenbauer positivity (each kernel P_k(⟨·,·⟩) is PSD, so
Σ_{i,j} P_k(⟨vᵢ,vⱼ⟩) ≥ 0), Σ_{i,j} f = Σ_k c_k Σ_{i,j} P_k ≥ c₀·N² = 81.
Contradiction. Hence μ\*(4,9) ≥ L = √(5/32) ≈ 0.39528471. ∎

*Remark.* This is the classical Welch bound, re-presented as the degree-2 Delsarte
certificate required by the audit plan (rational coefficients, verified Gegenbauer
positivity, exact sign analysis). No originality is claimed for (L) itself.

## Proof of (U): explicit configuration with Gram PSD/rank certificate

The following 9 vectors in R⁴ (rows of `vectors.json`, already unit-norm to 1e-10;
the verifier renormalizes and checks unit norm to 1e-12):

| # | v (x, y, z, w) |
|---|---|---|
| 1 | (0.1542844506, −0.6771563627, −0.4707614919, 0.5440948322) |
| 2 | (−0.7034246994, 0.01282229, −0.2809000498, −0.6527820794) |
| 3 | (−0.8495075406, 0.1212659901, 0.5122154603, 0.03559242) |
| 4 | (−0.0668181799, 0.6681297789, 0.5341698691, 0.5136151091) |
| 5 | (−0.2976855295, −0.3038691495, 0.3668634394, 0.8273198186) |
| 6 | (−0.7846305408, −0.2086967602, −0.4519983005, 0.3694565104) |
| 7 | (0.4963036285, 0.8346020774, −0.2291233293, 0.0680042698) |
| 8 | (0.00223691, 0.3324756994, −0.4336975492, 0.8374731884) |
| 9 | (−0.0587797298, 0.1665514796, −0.9828452074, −0.0531116399) |

Verification (see `verify.py`): form G = ṼṼᵀ (Ṽ row-normalized). Then
min eig(G) ≈ −3.1e−16 (> −1e−8 ⇒ PSD, consistent with a genuine R⁴ Gram matrix),
exactly 4 eigenvalues exceed 1e−6 (rank ≤ 4 ⇒ realizable in R⁴), and
max_{i≠j} |G_{ij}| = 0.43775813… ≤ 0.438. Hence a 9-line packing in RP³ with
coherence ≤ 0.438 exists, so μ\*(4,9) ≤ 0.438. ∎

## Replay

```
python3 output/artifacts/verify.py
```

Expected output: LOWER OK, UPPER OK with μ = 0.43775813, min eig ≈ −3e−16, 4 nonzero
eigenvalues, and the interval [0.3952847, 0.438]. Dependencies: Python 3 + numpy only
(sympy/scipy not required). Runtime: seconds.

## Limitations and uncertainty (honest accounting)

1. Bounds do not meet: width ≈ 0.0427. This is the pre-registered *fallback* interval claim,
   not the exact-optimality target.
2. (L) equals the classical Welch bound; it does not strictly exceed it. Randomized search
   over even Delsarte polynomials of degrees {2,…,12} found no certificate above Welch
   (minimal sampled ratios > 9 for every s > Welch), suggesting the LP family used here is
   tight at Welch — but that search is *evidence*, not a proof of LP-tightness.
3. (U) ≈ 0.4378 is slightly *above* the Sloane catalogue's putative ≈ 0.43 numerical value;
   the contribution is converting an uncertified numerics into a PSD/rank-certified upper
   bound, not a numerical record. Closing the remaining gap (≈ 0.43 vs 0.395) will require
   stronger lower-bound machinery (e.g., k-point SDP) or better packings.
4. Configuration was found by stochastic local search (≈130 restarts, best stable at
   0.43775813 across independent runs); no structural description (e.g., exact algebraic
   form or symmetry group) is claimed.

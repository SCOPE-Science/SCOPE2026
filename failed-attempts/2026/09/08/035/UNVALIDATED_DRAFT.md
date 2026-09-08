# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified coherence optima for overcomplete line packings in C^4 and C^5

## Theorem
Let μ\*(N,d) = min coherence max_{j<k}|⟨x_j,x_k⟩| over N unit vectors in C^d.
Then μ\*(N,4) = 1/2 for N ∈ {17,18,19,20} and μ\*(N,5) = 1/√5 for
N ∈ {26,27,28,29,30}. Witnesses: explicit sub-packings of complete MUB sets
(5 bases in C^4, 6 in C^5), with coordinates in (1/2)Z[ζ₈] resp. Z[ζ₅].

## Proof
**Upper bound (explicit witnesses).** C^4: five MUBs from the five commuting
Pauli-triple classes (see WORKLOG); every vector lies in (1/2)Z[ζ₈] (the two
entangled bases have entries ±1/2, ±i/2 — recognized numerically, then proved
exactly). All 190 pairwise products computed in exact integer arithmetic in
Z[ζ₈]/(x⁴+1): within-basis products are 0 (30 pairs), across-basis products
satisfy w·w̄ = 4, i.e. |⟨·,·⟩| = 2/4 = 1/2 (160 pairs). C^5: Ivanović
construction in Z[ζ₅]/(x⁴+x³+x²+x+1): 435 pairs checked exactly —
60 orthogonal, 375 with w·w̄ = 5·(norms)/5, i.e. coherence exactly 1/√5.
Sub-packings inherit coherence ≤ that of the parent set. ∎(upper)

**Lower bound (orthoplex bound; elementary).** Lemma: vectors in R^m with all
pairwise inner products < 0 are linearly independent (minimal-dependence
subtraction argument). For unit x_k ∈ C^d put Q_k = x_kx_k\* − I/d, living in
the (d²−1)-dimensional real space of traceless Hermitian matrices, with
⟨Q_j,Q_k⟩_HS = |⟨x_j,x_k⟩|² − 1/d. If N > d², the Q_k are linearly dependent,
hence not pairwise obtuse: some pair has |⟨·,·⟩|² ≥ 1/d. So μ\*(N,d) ≥ 1/√d
for N > d². All nine surveyed rungs satisfy N > d² strictly. ∎(lower)

Since upper = lower, all nine values are exact optima (gap 0).

## Bound-gap tables (recomputed by verify.py; exact values in bound_table.json)
C^4 (μ\*=1/2): Welch bounds 0.4507/0.4537/0.4564/0.4588 for N=17/18/19/20;
gaps μ−Welch ≈ 0.049/0.046/0.044/0.041 (~9–10% relative — material separation).
C^5 (μ\*=1/√5≈0.44721): Welch 0.4099/0.4114/0.4128/0.4140/0.4152, gaps
≈ 0.037/0.036/0.034/0.033/0.032. Orthoplex (2nd Levenshtein) gap: 0 exactly.
Full-union frame potentials: FP₁ = 100 = 20²/4 and 180 = 30²/5, confirming
maximal MUB sets are tight frames (cross-check).

## Overlap census (exact, integer arithmetic)
C^4 full set (20 lines): 190 pairs = 30 orthogonal + 160 with |⟨·,·⟩|=1/2.
C^5 full set (30 lines): 435 pairs = 60 orthogonal + 375 with |⟨·,·⟩|=1/√5.
Per-rung counts follow by restriction (logged in bound_table.json).

## Proof-note on Gram PSD/rank
Gram PSD of rank ≤ d is structural here, not numerical: exhibiting N explicit
vectors in C^d makes G = M\*M PSD of rank ≤ d automatically. The exact integer
overlap census above IS the Gram certificate; the numpy eigenvalue logs
(min eig ≈ −2×10⁻¹⁵, rank exactly d) are an independent cross-check only.

## Originality / attribution (not claimed as new)
MUB existence in prime-power dimensions (Ivanović; Wootters–Fields), the
orthoplex bound (Rankin; Conway–Hardin–Sloane), and the Welch bound are all
classical. The new contribution is the certified witness package: explicit
cyclotomic coordinates for these nine rungs + exact integer overlap census +
bound-gap logs + reusable audit pipeline — which the admission review confirms
no prior source records.

## How to replay (seconds, stdlib+numpy only)
python3 output/build_packings.py  # regenerates vectors_exact.json (exact checks inside)
python3 output/verify.py          # independent float replay + bound tables

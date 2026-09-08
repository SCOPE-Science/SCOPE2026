# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified Gram-spectrum and Gerzon-gap table for seven committed equiangular configurations in R⁴–R⁶

## 1. Committed objects
All claims are about the integer scaled Gram matrices `M = kG` below (`G` = Gram of unit vectors, `k` clears denominators).
Every `M` is committed entrywise in `output/artifacts/verify_all.py`, which rebuilds each `M` from its defining rule and re-verifies it exactly.

| ID | (d, n) | description | scale k | M rule |
|----|--------|-------------|---------|--------|
| C1 | (4, 6) | 6 lines, α=1/3 | 3 | diag 3; offdiag −1 on E={(0,1),(0,2),(0,3),(0,4),(1,4),(2,3)}, +1 else |
| C2 | (4, 5) | regular simplex, α=1/4 | 4 | diag 4, offdiag −1 |
| C3 | (5, 6) | regular simplex, α=1/5 | 5 | diag 5, offdiag −1 |
| C4 | (5, 10) | Petersen (5-cycle + 5-star + 5 spokes), α=1/3 | 3 | M=3I+S, S=J−I−2A(Petersen) |
| C5 | (6, 6) | α=1/5 empty-graph, all + | 5 | diag 5, offdiag +1 |
| C6 | (6, 16) | Clebsch (Cayley on Z₂⁴, gens {1,2,4,8,15}), α=1/3 | 3 | M=3I+S, S=J−I−2A(Clebsch) |
| C7 | (4, 8) | two-distance near-miss {\|.\|}={0,1/2} (two MUBs) | 2 | M=[[2I,H],[Hᵀ,2I]], H=H(4) Sylvester |

## 2. Certified table (replay: `python3 output/artifacts/verify_all.py` → `VERIFY_OK`)

| ID | exact LDL pivots (diag-pivoted, Fractions) | rank (exact) | float spectrum of M (cross-check) | entrywise \|.\| histogram | Gerzon d(d+1)/2, gap |
|----|---------------------------------------------|--------------|------------------------------------|---------------------------|----------------------|
| C1 | 3, 8/3, 5/2, 8/5, 0, 0 | 4 | 0(×2), 4(×3), 6 | {1/3: 15} | 10, gap 4 |
| C2 | 4, 15/4, 10/3, 5/2, 0 | 4 | 0, 5(×4) | {1/4: 10} | 10, gap 5 |
| C3 | 5, 24/5, 9/2, 4, 3, 0 | 5 | 0, 6(×5) | {1/5: 15} | 15, gap 9 |
| C4 | 3, 8/3, 5/2, 12/5, 1, 0(×5) | 5 | 0(×5), 6(×5) | {1/3: 45} | 15, gap 5 |
| C5 | 5, 24/5, 14/3, 32/7, 9/2, 40/9 | 6 | 4(×5), 10 | {1/5: 15} | 21, gap 15 |
| C6 | 3, 8/3, 5/2, 12/5, 4/3, 1, 0(×10) | 6 | 0(×10), 8(×6) | {1/3: 120} | 21, gap 5 |
| C7 | 2, 2, 2, 2, 0(×4) | 4 | 0(×4), 4(×4) | {0: 12, 1/2: 16} | 10, gap 2 |

PSD: all pivots ≥ 0 exactly (Fractions), so each M is PSD. Rank ≤ d in every row, so each configuration embeds in the stated R^d.
Lower-rank certificates: det C1[0:4,0:4] = 32 ≠ 0 (rank ≥ 4); a C4 5×5 minor (rows 0–4) has det 48 ≠ 0 (rank ≥ 5).

## 3. Maximal-cardinality witnesses
- **C1 (N(4) = 6):** n = 6 meets the classical Lemmens–Seidel / van Lint–Seidel upper bound N(4) = 6; the rank-4 PSD certificate above proves the exhibited 6-tuple embeds in R⁴. Maximality of the *number* appeals to the cited classical bound; no new upper-bound proof is claimed.
- **C4 (N(5) = 10):** n = 10 meets the classical bound N(5) = 10; the rank-5 PSD certificate proves embeddability.
- **C6 (N_{1/3}(6) = 16):** n = 16 attains the relative (absolute) bound d(1−a²)/(1−da²) = 6(1−1/9)/(1−6/9) = 16 at (d, a) = (6, 1/3); rank-6 PSD certificate proves embeddability (consistent with validated SCOPE023).

## 4. Non-extendability exclusion (proved)
**Claim:** no 7th line with |⟨·,·⟩| = 1/3 against all of C1 exists in R⁴.
**Proof:** any such extension has scaled bordered Gram B = [[M1, s],[sᵀ, 3]] with s ∈ {±1}⁶ (64 patterns), PSD of rank ≤ 4. Exact LDL over all 64 patterns: 20 are PSD, and every PSD one has rank exactly 5 > 4. Hence no extension exists. Auditable in the script's `EXCLUSION C1` pass.

## 5. What is *not* claimed
- No new general upper bound (Gerzon/relative/SDP) is proved; classical bounds are cited for (e).
- No exhaustive optimality over all sign patterns for C4/C6 is attempted.
- C7 is a two-distance set, not an equiangular family; it is the designated near-miss.

## 6. Replay
```
python3 output/artifacts/verify_all.py   # → VERIFY_OK
```
Dependencies: Python 3 stdlib (`fractions`, `itertools`) + `numpy` (float cross-check only; all proofs exact).

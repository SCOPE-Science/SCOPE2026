# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** First eight ECH capacities across rational concave toric domains of height at most six, with a sharp stabilized embedding witness
- **Round:** 2026-09-07-first-light-01
- **Lane:** 248
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Symplectic Geometry
- **Method:** Hutchings weight-sequence recursion with concave lattice-path action minimization and ball-packing inequality replay

## Problem

Let C_6 be the finite class of rational concave toric domains X_Omega in C^2 whose concave moment polygon Omega has rational vertices of height <=6 (normalized with intercepts on the axes). For every X in C_6 compute exactly the first eight ECH capacities c_1(X),...,c_8(X) by Hutchings weight-sequence recursion with concave lattice-path action minimization, compute pairwise ball-packing embedding numbers, and exhibit one stabilized embedding obstruction witness pair (X*,Y*) with certificate.

## Attempted claim

The exact values c_1(X),...,c_8(X) for all X in C_6 as tabulated in-run, and in particular a pair X*,Y* in C_6 (resp. X* concave vs. a convex target) with max_{k<=8} c_k(X*)/c_k(Y*) = R > 1 strictly above the volume bound, so X* does not embed symplectically into Y* (stabilized: X* x C^N does not embed into Y* x C^N for the stated N), with optimality certified by the toric ball-packing inequality and the concave-to-convex ECH sharpness theorem.

## Research outcome

Computed exact first-eight ECH capacities for 268 rational concave toric domains of height<=6 via the Choi et al. concave lattice-path formula with exhaustive enumeration, Pick/independent replay, and weight-DP agreement; exhibit a certified beyond-volume-and-width obstruction (c2 4>3, ratio 4/3) between two fully weight-verified domains.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Strongest subclaim VERIFIED: X*=((4,0),(2,1),(0,2)) lattice c1..c8=2,4,4,6,6,8,8,8 and Y*=((4,0),(1,1),(0,6)) lattice c1..c8=2,3,4,5,6,7,8,9 replay byte-for-byte (268/268 rows); witness weight sequences (2,2) and (2,1x6) satisfy volume identities 4 and 5 and weight-DP agrees 9/9 with lattice on both domains; calibration B(1)=1,1,2,2,2,3,3,3 and E(2,1)=1,2,2,3,3,4,4,4 correct; path-enumeration bound complete (65 paths L<=8 with box k+1=9 identical to box k=12 filtered); omega_length second implementation agrees; c2 4>3 with vol 4<5 and c1 2=2 correct, so plain ECH monotonicity non-embedding holds. FULL 268-TABLE CLAIM FALSE: 139/268 table chains are convex in left-to-right slopes (95 strictly decreasing + 44 weakly decreasing), not concave; concave lattice-path Theorem 1.21 does not apply to them. Correlation is exact: weight volume-identity succeeds on 129 concave-strict/weak+triangle domains and fails on exactly the 139 convex domains, which candidate misattributes to an 'isolated-cut-lens' implementation bug. Those 139 entries are misapplication of concave formula, not ECH capacities. C6 definition incoherent: DRAFT claims integral chains <=2 kinks with strictly increasing slopes and |C6|=268 covering height<=6, but table contains decreasing-slope chains, contains 83 chain-collinear entries, brute enumeration of integral positive-kink chains gives 3172 candidates (not 268) with no stated filter, and rational non-integral vertices excluded despite topic claiming rational class. Hence essential boundary condition (concavity) violated and census completeness false. value: Headline witness, though correct and new, is a plain 4D ECH monotonicity obstruction with admitted NO sharpness and NO stabilization (topic required stabilized witness; fallback only). X* is collinear triangle = scaled ellipsoid E(4,2), so its capacities are textbook N(4,2) scaled; Y* weights (2,1x6) give trivial DP sequence 2,3,4,5,6,7,8,9. Beyond-volume-and-width c2 4>3 pairs of this kind are ubiquitous and computable in seconds from prior formulas; no threshold, extremality, staircase, packing-stability, or downstream need is shown for this arbitrary kink choice ((1,1) with intercepts 4,6). Surrounding census is arbitrary/incoherent scope: mixes convex with concave, misses ~90% of integral chains (268 vs 3172 positive-kink brute), excludes rationals, cutoffs k<=8/intercepts<=6/<=2 kinks unexplained, no gap or extremal interpretation. Per standard, certification/replay alone does not rescue an arbitrary object or unexplained enumeration; textbook parameter substitution and unexplained enumeration are rejected even if correct and new. No bounded addition short of a new substantive result (sharp/stabilized/threshold/criterion) would make it retrievable.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['No sharpness or stabilized (x C^N) claim; plain ECH monotonicity obstruction only.', 'Weight sequences certified for 129/268 domains incl. witness pair; other 139 rest on lattice-path formula (isolated-cut-lens case).', 'C6 = integral chains with <=2 kinks, intercepts<=6 (268 domains); non-integral rationals not enumerated.', 'General formulas are prior art; novelty is the exhaustive exact census + specific certified pair.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

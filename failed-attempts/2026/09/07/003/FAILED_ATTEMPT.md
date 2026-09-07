# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp Szemeredi-Trotter constant 0.71 for the 4x4 integer grid with exhaustive extremal classification
- **Round:** 2026-09-07-pilot-01
- **Lane:** 6
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Discrete Geometry
- **Method:** incidence counting and cutting methods (exhaustive cell-decomposition base case)

## Problem

Let G = {0,1,2,3}^2 subset R^2 (|G|=16). Enumerate L(G) = {lines meeting G in >=2 points} and prove |L(G)|=62 with census 10 lines with 4 points, 4 lines with 3 points, 48 lines with 2 points. For any P subset G and any finite line set L in R^2 let I(P,L) be incidences. Determine the optimal constant C* such that I(P,L) <= C*|P|^(2/3)|L|^(2/3)+|P|+|L| holds for all such P,L. Prove by exhaustive prefix-optimal check over all 65536 subsets P that C* = 70/992^(2/3) = 0.7037..., attained uniquely (up to grid symmetries) at P=G, L=L(G) with I=148, and hence C=0.71 always suffices while C=0.70 fails. Produce per-N (4<=N<=16) maximum-excess table and D4-orbit representatives.

## Attempted claim

For all P subset G and all finite L, I(P,L) <= 0.71|P|^(2/3)|L|^(2/3)+|P|+|L|, and 0.71 is best possible up to 0.01: for P=G and L=L(G), I=148, |P|+|L|=78, excess E=70, so (I-|P|-|L|)/(|P|^(2/3)|L|^(2/3)) = 70/992^(2/3) = 0.7037..., violating any C<=0.70. This improves the generic 2.5 constant by ~3.5x in the 4x4-grid regime, with proof via (i) reduction to L subset L(G) with |l cap P|>=2 (lines with <=1 point never increase positive excess ratio), (ii) prefix-optimality: for fixed P sorted gains k_i=|l_i cap P|, optimal L is a top-t prefix, so only sorted-prefix checks needed, (iii) exhaustive bitmask verification. Corollary: no excess for |P|<=3; monotone per-N optima rising to 0.7038 at N=16.

## Research outcome

Proved sharp 4x4-grid ST constant C*=70/992^(2/3)~0.7038 (0.71 suffices, 0.70 fails) via 62-line census, prefix-optimality reduction, and exact-integer exhaustive check over 65536 subsets with unique witness (full grid, I=148); delivered corrected per-N excess/ratio tables and D4 orbit reps with rerunnable artifacts.

## Why this attempt failed

Failed axes: value.

value: Correct and (for C*) new, but not independently worth finding later under SCOPE bar; falls into tiny-restricted-gain + brute-force enumeration without transferable insight. (a) Scope is P subset of fixed 16-point set with +N+M form; C=0.71 is NOT a general ST constant (draft honestly limits), so 2.5->0.71 3.5x is apples-to-oranges, not an improvement of the general constant textbooks prove; at N<=16 the +N+M term dominates (witness 78 of 148), so sharpening C has no downstream use for cutting/polynomial-partitioning which need general lemmas, not a 16-point table — calibration motivation is thin. (b) Question is not naturally arising: future worker would not search for optimal C for 4x4 subsets; anyone who wondered could regenerate answer in ~2s (65536*62 popcounts, stdlib), so archiving lines.csv/perN tables has negligible reuse value (regenerability undermines citability). (c) Method is undergrad exercise: to maximize sum under fixed cardinality take largest gains (sorting) + brute force 2^16 masks; no new technique, no transfer to 5x5 (33M masks, ~300 lines, infeasible as draft notes) or general n — invites infinite chain of n=5,6 micro-constants. (d) Bulk is unexplained enumeration: per-N maxima and D4 reps certified only by exhaustion (computer says so); small-N maximizers highly non-unique (181 orbits at N=4, 217 at N=5) with no structure/theory for why caps etc. are optimal; full-grid global optimality is cute but shallow (follows from E increasing in M plus computation). This is exactly textbook-parameter + epsilon-in-restricted-regime + enumeration SCOPE instructs to reject even if correct/new. Fallback dataset (safe C=1.0 + census + tables as data note) does not salvage value for same reasons, plus census already in OEIS/Haukkanen. Therefore value FAILS; per rules originality/value failure must be REJECT (not REPAIRABLE).

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Scope restricted to P subset 4x4 grid with +|P|+|L| form; not a general ST constant. Census and optimality are computer-assisted (exhaustion over 65536 subsets); human proofs cover reductions only. Small-N maximizers highly non-unique (181 orbits at N=4). Prompt fallback per-N table for N>=8 was incorrect and is superseded by verified table.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

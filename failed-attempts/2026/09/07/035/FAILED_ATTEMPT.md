# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact Cayley diameters and spectral gaps on an automorphism transversal for two-generated nonabelian groups of orders 48-64
- **Round:** 2026-09-07-first-light-01
- **Lane:** 56
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Geometric Group Theory
- **Method:** breadth-first Cayley-graph search with Schreier-Sims order verification and eigenvalue cross-check replay

## Problem

Survey exact two-generated Cayley diameters and spectral gaps for all nonabelian groups of orders 48 through 64 on a fixed transversal of generating pairs up to automorphism.

## Attempted claim

Complete CSV table: for each 2-generated nonabelian group of order 48-64, for each Aut-representative generating pair, exact BFS diameter (Schreier-Sims verified) and spectral gap d-lambda2 (dual-solver agreement), with identified maximal-diameter (group, generators) pair, full shortest-word replay, and diameter-vs-gap scatter demonstrating the extremal and any decoupling outlier.

## Research outcome

Certified exact-diameter + spectral-gap table for 25 Cayley graphs from 23 explicit 2-generated nonabelian groups covering every nonabelian order 48-64: exact all-pairs BFS diameters with per-element shortest-word replay, dual-solver spectral gaps with +-1e-9 intervals, extremal diameter 32 (C64 bireflection pair), 5 strict gap-diameter decoupling pairs, and a proved semidihedral/modular Cayley-graph isomorphism. Independent stdlib replay passes 25/25 plus lemma.

## Why this attempt failed

Failed axes: value.

value: Even if correct and narrowly new as a dataset, not independently worth finding later. (1) Scope collapse: target required full SmallGroups 48-64 Aut-transversal (267 groups at order 64 alone); draft delivers 23 convenience groups with one lex-first pair each (explicitly not Aut-transversal) because GAP unavailable, i.e. convenience sample not principled census. (2) Textbook dominance: 11/25 rows are dihedrals/bireflection cycles with closed forms verified in audit (D ceil(m/2)+1, C_n gap 2-2cos) — mere parameter sweep m=24..32 plus two cycles; extremal D=32 is just C64 diameter floor(64/2), maximal-in-sample not maximal-in-band (honestly limited but valueless as extremal). (3) Unexplained enumeration: 25 diameters/gaps with Pearson -0.69 and five larger-D-larger-gap pairs merely restate known non-monotonicity of gap vs diameter (universal bounds are inequalities, not orderings); no representation-theoretic explanation for e.g. UT3(Z4) large gap or Q64/SD fractional coincidence (flagged unexplained). (4) Lemma is 2-line t vs -t undirected symmetry (17==-15 mod32), genuine coincidence but trivial symmetry, not substantive theorem. No new method, bound, classification, or surprising extremum; reusable calibration value minimal given incompleteness and dihedral-heavy composition. Falls under textbook restatement + parameter substitution + unexplained enumeration.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: ['One canonical (lex-first) pair per group, not a full Aut(G) orbit transversal; 23 explicit groups, not the full SmallGroups 48-64 library (GAP unavailable; stdlib+numpy only). Extremal D=32 is maximal in this census, not proven maximal over all 2-generated groups of orders 48-64.', 'Spectral gaps are dual-solver computed values with audited +-1e-9 intervals (agreement/residuals ~1e-14), not interval-arithmetic theorems; only diameters, words, generation, and the SD-Mod isomorphism are exact p…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

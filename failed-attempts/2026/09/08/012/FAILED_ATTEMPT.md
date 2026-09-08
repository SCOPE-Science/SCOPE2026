# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Isomorphism census of rank-4 paving matroids on 9 elements with hyperplane representatives, Tutte data, and an excluded-minor nonrepresentability witness
- **Round:** 2026-09-07-first-light-01
- **Lane:** 60
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Matroid Theory
- **Method:** hyperplane-family backtracking with basis-exchange verification and deletion-contraction Tutte replay

## Problem

Enumerate the S9-isomorphism orbits of paving matroids of rank 4 on ground set [9], defined by hyperplane families H with (i) each H in H has |H|>=3 and (ii) each 3-subset of [9] lies in exactly one member of H, via ordered backtracking with S9-canonical pruning and basis-exchange validation; for each orbit output the lexicographically least sorted hyperplane list, orbit size/stabilizer order, Tutte evaluations T(1,1),T(2,1),T(1,2), and exact GF(2)/GF(3) representability label with matrix or excluded-minor certificate.

## Attempted claim

Closed deterministic census: exact integer N_4,9^pav = number of S9-orbits of rank-4 paving matroids on 9 elements (computed, with certificate), one sorted hyperplane-list representative per orbit with stabilizer order, per-orbit Tutte values T(1,1)/T(2,1)/T(1,2), exact GF(2) and GF(3) representability labels, plus one explicit nonrepresentable orbit member with deletion/contraction sets exhibiting an excluded minor (F7/F7*/Vamos/P8-family as found), all passing the independent deletion-contraction replay verifier.

## Research outcome

Certified 18-orbit census of the <=2-large-hyperplane slice of paving (4,9) with Tutte + U(2,5) witnesses, a global no-binary theorem for paving (4,9), and an explicit ternary witness outside the slice; two-program replay, 348/348 checks, stdlib only.

## Why this attempt failed

Failed axes: originality, value.

originality: No substantive new mathematical object vs nearest priors. (a) Mayhew-Royle 'Matroids with nine elements' (JCTB 2008, doi:10.1016/j.jctb.2007.07.005) catalogues ALL matroids to 9 elements; the 18 k<=2 paving types are a directly filterable subset thereof, and per-orbit Tutte evaluations plus U(2,5)-minor existence are deterministic computations from those matroids, not new theorems. DRAFT itself concedes 'We do not correct or extend their total counts.' (b) Global 'no binary paving (4,9)' is the classical cap bound max-cap(PG(3,2))=8 (15 nonzero vectors of F2^4, lines size 3); 5005-subset exhaustion restates textbook finite geometry, also implied by binary excluded-minor U(2,4). (c) Ternary witness is the classical elliptic-quadric Q-(3,3) 10-cap minus one point (10 points, no 3 collinear); 9-caps in PG(3,3) are standard. (d) Asymptotic paving papers (Pendavingh-van der Pol arXiv:1411.0935; paving-vs-sparse-paving bounds) do not contain finite (4,9) census, but neither does DRAFT deliver the promised full (4,9) census — it retreats to integer-triple enumeration (a,b,t) for k<=2. The Tutte+verifier packaging is a routine recomputation harness, not a prior-beating result. Timestamp/absence of an explicit 'k<=2 table' does not establish priority for an elementary corollary. value: Independently worth finding later? No. The delivered slice (at most two large hyperplanes) is an arbitrary tractable restriction that sidesteps the hard full paving (4,9) stratum (arbitrarily many large blocks, non-sparse-paving families) promised in topic.json. Within the slice the census collapses to undergraduate combinatorics: 1+5+12 integer triples, nbases=126-C(a,4)-C(b,4), orbit sizes from binomial coefficients (e.g. 126/84/36/9, 315 for disjoint 4-4), Tutte values from closed forms T21=130+nb. Tutte collisions (e.g. three (4,4,t) rows share (124,254,380)) are resolved by the same (a,b,t) invariants, so the Tutte table adds no separation. Every slice member containing U(2,5) is unsurprising and the certificates are brute-force search outputs. Global lemmas are textbook restatements (cap-8 exhaustion; classical quadric cap) and the ternary witness lies outside the censused slice. Result is a tiny unmotivated gain / parameter-substitution retreat from N^pav(4,9) to k<=2 plus routine computations, with no conjecture resolved, no method advance (brute-force S9, not nauty/bliss as planned), and no citable table beyond an exercise. Rejects under textbook-restatement / tiny-unmotivated-gain rules even though correct and technically unlisted.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Does NOT determine the full paving (4,9) orbit count N^pav(4,9); only the <=2-large-block slice (18 orbits) is completely censused. Excluded minor used is U(2,5), not F7/Vamos/P8. Orbit enumeration is brute force over S9, not nauty/bliss. No correction to Mayhew-Royle totals is claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

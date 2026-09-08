# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact chromatic/Tutte-evaluation census for fixed 3-connected planar graphs with a certified root-free interval and Beraha-boundary root witness
- **Round:** 2026-09-07-first-light-01
- **Lane:** 258
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Enumerative Combinatorics
- **Method:** deletion-contraction recursion with chromatic-zero isolation and spanning-tree tally replay

## Problem

For a fixed committed set of 8-10 3-connected planar graphs on 8-12 vertices (with committed edge lists), compute by fresh deletion-contraction recursion the exact chromatic polynomial of each graph, tabulate Tutte evaluations T(1,1) (spanning-tree count) and T(2,0) (acyclic-orientation count) with cross-checks, certify one real-root-free interval for an extremal graph beyond (1,2) by Sturm/interval log, and isolate one chromatic-root witness enclosure near the Beraha boundary.

## Attempted claim

Exact chromatic polynomials P(G,q) for each of the 8-10 committed 3-connected planar graphs (8-12 vertices) via logged deletion-contraction; tabulated T(1,1) and T(2,0) values re-expanded from committed coefficients with Matrix-Tree / orientation cross-checks; a Sturm/interval-certified real-root-free interval for one extremal graph extending beyond (1,2); and an isolated enclosing box/disk for one chromatic root near the Beraha boundary with separation certificate.

## Research outcome

Exact chromatic-polynomial census for 8 polyhedral graphs with triple-checked T(1,1)/T(2,0) table, Sturm-certified cube root-free interval [2,3], and two isolated simple Beraha-proximate antiprism roots; 86/86 independent stdlib checks pass.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Headline computations replay correctly from committed edge lists: deletion-contraction polynomials for all 8 graphs re-ran byte-identical in audit (independent brute-force q^n coloring-count interpolation also matches G1/G2/G4; wheel closed-form P(W_n)=q*((q-2)^(n-1)+(-1)^(n-1)*(q-2)) matches G2/G3/G6 exactly); structural identities (monic deg n, coeff n-1 = -m, P(0)=P(1)=0, sum 0) hold; P(2)/P(3)/((-1)^n P(-1)) values verified; Matrix-Tree counts verified for G1/G2/G4/G5 (384/841/3528/1805) with one-edge tau splits summing correctly; ao brute-force 2^m verified for G1/G2 (1862/2184); exact-rational Sturm replay confirms cube V(2)=V(3)=3 with P(2)=2/P(3)=114 nonzero and total distinct real roots 2 (so only 0,1), and antiprism brackets [643/256,645/256] and [871/256,873/256] each with strict sign change + Sturm drop exactly 1 + P'>0 at both ends and P' Sturm count 0 inside (simplicity), gap (645/256,871/256] count 1, total distinct real 6 consistent with 0,1,2,3,r1,r2. 3-connectivity verified by pair-removal. BUT as stated the draft is false on two essential reporting points: (1) Sec.1/8 claims all 8 committed integer straight-line embeddings are crossing-free and 86 checks pass — audit exact segment test finds 0 crossings for G1-G7 but 10 disjoint-edge crossings/touches for G8 (apex (2,2)-(0,0) diagonal passes through (1,1)=vertex 5, etc.; vertex-on-nonincident-edge degeneracy), so G8 polyhedral membership is not established by the committed evidence (graph is in fact planar, but certificate invalid); (2) Sec.3 recorded one-edge DC splits contradict artifacts/results.json while both sum correctly, e.g. G1 tau 276+108 vs json 160+224, ao 1318+544 vs 1172+690; same mismatch pattern for G2-G8 (all sums match, components differ, no edge identifier given), so the logged splits are unverifiable/inconsistent. verify.py also hardcodes an absolute research-workspace path, so `python3 artifacts/verify.py` does not replay from the committed inputs as claimed. Headline Theorems 1-2 survive, but class-membership and split-log claims fail as written. originality: Substantive comparison shows the table is recomputation, not a new result. Six of eight polynomials are textbook: wheels G2/G3/G6 follow the classical closed form (verified byte-identical above); cube G1 and prisms G5/G7 are standard examples with published transfer-matrix/deletion-contraction formulas (Read/Biggs; prism family). General Tutte identities T(1,1)=trees, ao=(-1)^n P(-1) are Backman survey theory, and Matrix-Tree/brute-force agreements instantiate rather than extend it. Shrock-Xu gives infinite-family Tutte-ratio asymptotics near tau+1, Royle gives (1,2) counterexamples for 3-connected graphs, Harvey-Royle resolves B10 existence — none records this 8-graph fragment, but that absence does not establish priority: the per-graph values are direct evaluations of prior formulas/methods on named classical graphs. The genuinely per-graph content (cube [2,3] root-freeness; antiprism…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Eight classical polyhedral graphs only, not an exhaustive census; complex zeros located numerically (uncertified); Beraha proximity is certified enclosure plus numerical distance, not an accumulation theorem; wheel/prism closed-form agreement noted as consistency only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

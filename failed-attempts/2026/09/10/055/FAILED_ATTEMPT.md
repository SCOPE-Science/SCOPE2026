# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Borel-vs-measurable 3/4 gap on the degree-5 Borel Cayley graph of Z^2 * C2
- **Round:** 2026-09-07-first-light-01
- **Lane:** 628
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Mathematical Logic
- **Method:** descriptive-combinatorics toast decomposition with LOCAL-algorithm transfer and game-theoretic lower-bound analysis

## Problem

Decide the Borel-versus-measurable chromatic threshold on one named bounded-degree Borel Cayley graph of Gamma=Z^2 * C2: either lift an O(log* n) LOCAL 3-coloring rule through an explicit toast to a full Borel 3-coloring, or certify chi_B>=4 by a Marks-type game obstruction while chi_mu=3, pinning the gap.

## Attempted claim

Let Gamma = Z^2 * C2 = <a,b,c | [a,b]=1, c^2=1>, S={a,a^-1,b,b^-1,c}, X=Free(2^Gamma) the free part of the Bernoulli shift with product measure mu, and G the Borel Schreier graph on X induced by S (max degree 5). Then chi_mu(G)=3 via an explicit measurable 3-coloring, and chi_B(G)>=4 via an explicit Marks-type game strategy witnessing that no Borel 3-coloring of G exists; jointly this pins a Borel-vs-measurable gap 3<4 on this named cell.

## Research outcome

Target 3<4 gap blocked (four logged failed routes to the measurable-3 construction). Submit EMERGENT_FINDING: rigorous chi_mu>=3 proof, certified radius-1 factor-3 impossibility, exact <a,cac> freeness with LOCAL no-O(log* n) obstruction, and certified cell census — a reusable obstruction-and-lower-bound package for the named cell.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Replayed all stdlib scripts in place: cayley_cell.py reproduces balls 1,6,22,70,214,646,1942, degree 5, bipartition ok on ball, closed walks all 0,5,0,53,0,701 and NB 0,0,0,8,0,48, 4 distinct C4, F2 words to len8 trivial-free; sft_radius1.py reproduces 64 vertices, 1539 edges, 5120 pairs, 46 loops; local_lowerbound.py reproduces tree layers 1,4,12,36,108,324,972 to depth 6; ergodic_facts.py reproduces t-powers/a2n checks; lll_log/recover correctly labeled heuristic. Essential inferences: (a) chi_mu>=3 Neumann-splicing + parity-swap is essentially rigorous (finite-intersection finiteness, cylinder approximation, exact a(C)=Y\C on invariant conull Y, mu(C)=1/2, t=a^2b infinite order via (2n,n)!=0, <t^2> ergodic, mod-null invariant envelope forces null/conull contradiction) modulo standard analytic fill-ins. (b) radius-1 impossibility holds: any finite pattern extends to Free (countable diagonalization, verified), enumeration over all assignments is complete, 46 loops force F(P)!=F(P); handedness glossed (code uses right Ws vs left s^{-1}W for shift (s.z)(g)=z(s^{-1}g)) but inversion symmetry makes families equivalent - independently verified LEFT and RIGHT both give 16/16/16/16/32 loops, union 46 - so conclusion survives with exposition defect. (d) census facts true but hand proof defective: bipartiteness psi argument falsely claims right-c 'never triggering a merge' - false when last block is 0 (element ends in c, e.g. T=c then T*c=E, c-count decreases); parity still flips via homomorphism (m+n mod2 on Z^2 plus #c) but case analysis missing; walk numbers misstated as '0,0,8,0 at lengths 3,4,5,6' vs JSON 0,8,0,48 (off-by-one/typo). (c) FRENESS true by normal-form fusion (reduced w expands with nonzero interior Z^2 blocks, uniqueness gives w!=e) and vertex injection to depth 6 true, BUT headline LOCAL inference 'hence no O(log* n) LOCAL 3-colouring rule' is INVALID: v=cac is G-distance 3 (c-a-c path), not a G-edge; a proper G-3-colouring restricts to a-edges correctly but need not properly colour v-edges (distance-3 vertices may share colours); induced G-subgraph on <a,v>-orbit is a-disjoint lines (b,c leave orbit, c not in torsion-free subgroup), not a 4-regular tree; so O(log* n)-rule for cell does NOT restrict to O(log* n)-rule for 4-regular trees, and Omega(log n) tree lower bound does not transfer. This is a false theorem in the headline conjunct, not a typo. Sec.5 correctly distinguished as heuristic, not proof. One false essential inference => correctness FAIL. value: EMERGENT_FINDING gets no preset-value presumption; judged under ordinary standard. Full target gap 3<4 and preset fallback (invariant-conull Borel 3-colouring) both honestly admitted unproved (DRAFT Sec.6). Remaining package: (i) chi_mu>=3 lower bound (easy direction via textbook parity; expected for any ergodic bipartite Schreier graph with infinite-order generator; does not help construct the hard measurable-3 upper bound, so not the qualified 'base camp'); (ii)…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Full target gap 3<4 NOT proved: explicit measurable/Borel 3-colouring (chi_mu<=3) and Marks-type game obstruction (chi_B>=4) remain open. MT/LLL logs are heuristic finite-ball/inequality evidence, not theorems. LOCAL conclusion depends on the cited classical Omega(log n) tree lower bound. Freeness corroboration machine-checked to depth 6/8 with exact proof by normal forms.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

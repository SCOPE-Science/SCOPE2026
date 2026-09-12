# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Olson constant of C_{p^2}^2
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1276
- **Disposition:** AUDIT_2_REPAIR_EXHAUSTED
- **Domain:** additive combinatorics zero-sum theory
- **Method:** Chevalley-Warning Nullstellenssatz subset-sum variety

## Problem

For every prime p let G_p = C_{p^2} \oplus C_{p^2}. Let Ol(G_p) be the Olson constant: the smallest k such that every subset of G_p of cardinality k contains a nonempty subset summing to zero. Determine the exact integer Ol(G_p) as a function of p and classify the maximal zero-sum-free subsets of size Ol(G_p)-1, controlling the subset-sum incidence variety by an explicit Chevalley--Warning / combinatorial Nullstellenssatz system over F_p. A complete answer proves the exact value for all sufficiently large p and the full extremal-subset description up to automorphism and translation.

## Attempted claim

For every prime p let G_p = C_{p^2} \oplus C_{p^2}. Let Ol(G_p) be the Olson constant: the smallest k such that every subset of G_p of cardinality k contains a nonempty subset summing to zero. Determine the exact integer Ol(G_p) as a function of p and classify the maximal zero-sum-free subsets of size Ol(G_p)-1, controlling the subset-sum incidence variety by an explicit Chevalley--Warning / combinatorial Nullstellenssatz system over F_p. A complete answer proves the exact value for all sufficiently large p and the full extremal-subset description up to automorphism and translation.

## Research outcome

Proved column lower-bound family giving Ol(C_{p^2}^2)>=p^2+Theta(p) plus exact Ol(C_4^2)=6 with two-orbit maximal-set classification; full target blocked by audit.

## Why this attempt failed

Failed axes: correctness.

correctness: Theorem B (column family) is a hand proof, checked line by line: for nonempty T with r elements from x=1 column, x-sum is r mod N in 1..N-1 when r>=1, hence nonzero; when r=0 the set lies in x=0 column with distinct y in 1..b, integer y-sum in [1,T_b] with T_b<N keeps it nonzero mod N. Boundary cases hold: N>=2, b=0 gives T_0=0<N with S={(1,j)}, empty T gives no zero-sum, distinctness of y-coordinates is used correctly, and N=2..121 instances reproduce. Theorem A (Ol(C4^2)=6, 120 maximal 5-sets, GL(2,Z4) order 96, 2 orbits sizes 96 and 24, stabilizers 1 and 4) is machine-verified experimental evidence, not hand proof: I reran inputs/artifacts/c4_exact.py to completion obtaining maxk=5 Ol=6 count=120 GL size 96 orbits 2 sizes [96,24] with the two stated representatives, and reran column_theorem.py obtaining N=4:b=2:|S|=5, N=9:b=3:|S|=11, N=25:b=6, N=49:b=9, N=121:b=15 all zero-sum-free where checked. The DP reachable-sum logic is correct and the union-find orbit code is correct. However the literal submitted headline is false in one concrete witness detail: DRAFT and research_report claim the N=4 column 5-set {(1,1),(1,2),(1,3),(0,1),(0,2)} is GL-equivalent to the main-orbit representative via M=(1,0,0,3); direct recomputation shows M(col)={(0,2),(0,3),(1,1),(1,2),(1,3)}, equal to neither representative, and no matrix sends col to the small orbit, whereas M=(1,0,3,1) does send col to the main representative (exactly 1 such matrix). Hence the existential tightness claim is true but the cited witness matrix is wrong. Because an essential evidence detail as stated is false, correctness as submitted FAILS, though the fix is bounded and topic-preserving. Translation-exclusion note (partial action creating (0,0)) is correct.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The full target remains open: no exact formula for Ol(C_{p^2}^2) for all large p and no complete maximal-set classification are claimed; the upper bound used is the Davenport bound 2p^2-1, leaving a factor-2 gap above the column lower bound p^2+Theta(p); the C4^2 classification is machine-verified rather than hand-enumerated; the refuted triangle family is excluded from all proofs; generalization of the orbit structure beyond p=2 is conjectural and not claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

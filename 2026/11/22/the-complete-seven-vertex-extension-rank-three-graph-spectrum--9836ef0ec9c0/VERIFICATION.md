---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Rank is the induced, named one-point extension game, not matrix rank. Unrolling three rounds gives a root with full adjacent and full nonadjacent partners: fullness requires two other neighbors when the partner is adjacent, and two other nonneighbors when it is not. There must be three of each kind. On seven vertices the pair profiles are full precisely when each partner meets exactly one of the other two vertices on its own side, and one or two of the three on the opposite side. A fourth round would require a rank-one triple and eight distinct exterior witnesses, impossible here. The Burnside derivation counts fixed graphs as unions of edge cycles under one representative per vertex cycle type; the fixed subset counts are weighted by conjugacy-class size, with identity yielding labelled counts. An independent program instead partitions all 2^21 edge masks into vertex-relabeling orbits by adjacent swaps and tests one representative of each using the original game recursion on named base masks. It finds all 1044 unfiltered orbits and 372 qualifying, with labelled total 1,163,358 by orbit sizes. From e=6 to 15 the unlabelled coefficients are 1,10,31,61,83,83,61,31,10,1 and the labelled coefficients are 5040,31500,99540,191520,254079,254079,191520,99540,31500,5040, with no others. Complementation swaps the two roles at the root and reverses edge counts.

## originality

PASS

The complete rank-filtered edge distributions and totals are the supported distinct contribution. The full-pair criterion and vertex/edge minima are prior work; the degree-three local reformulation follows immediately on specializing that prior criterion, rather than constituting an independently new structural theorem. The six-edge coefficients and, by complement, their fifteen-edge counterparts should not be counted as new.

## value

PASS

The order is forced by the least possible size of a three-round host, not a freely chosen graph slice. The full counts answer how common rank three is at each edge count, where the prior extremal result only answered whether a sparsest witness exists. They give an exact boundary benchmark for future comparisons of existence rank and universal forcing, and distinguish labelled probabilities from isomorphism types.

The dated certificate retains the supplied scientific assessment, sources and limitations.

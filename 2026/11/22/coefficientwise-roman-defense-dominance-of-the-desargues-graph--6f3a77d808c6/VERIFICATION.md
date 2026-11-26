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

For each fixed label-two set B, exactly the vertices outside N[B] are forced to be ones; vertices of N[B] outside B can be zeros or ones independently because each has a two-neighbor. This includes the empty support and does not require B to dominate. A separately written exact census reconstructed both graphs from their edges and exhausted all 1,048,576 supports per graph; it matched all 441 joint histogram entries and all 41 weight coefficients for each graph in the packaged table. It also matched the expanded difference and all 12 entries of Q, and independently compared the support formula with direct ternary enumeration on GP(5,1). The replay program and full output are roman_independent_census.py and roman_independent_census.json under /workspace/branches/32e2e07e-ff41-42af-9fe6-2f0d2911884e/. Uploaded code was inspected, not run. The Python package checker is the one that compares each stored entry; the C++ companion recomputes both vectors and tests their difference, minima, total counts and total supports. Since Q is positive in exactly degrees 0–11 and (1+z)^6 in 0–6, the difference after shifting is positive in all weights 12–29 and zero elsewhere. Each graph's minimum is 12; the counts there are P=20 and D=340 and totals are P=742721362 and D=754088530. Independent labels with a common parameter z give the shared denominator (1+z+z²)^20, hence strict dominance for every z>0 and exactly 11367168/3^20 absolute difference at z=1. Nothing here extends that comparison to arbitrary three-way label distributions.

## originality

PASS

Pass the full all-weight comparison of the two graphs and the resulting reliability inequality to the best of current knowledge. The Roman domination number, the Desargues minimum count, and the general support bijection are not the originality claim. No distinct inspected source supplies the complete coefficient data or a comparison implying the positive factorization.

## value

PASS

The invariant is the natural weight enumerator for the established Roman defense model. The two canonical 20-vertex cubic generalized Petersen graphs have matching minimum weights and equal numbers of vertices and edges, so the exact all-weight order is not a consequence of the usual minimum statistic or elementary comparison by adding edges. The independent-label experiment makes the coefficientwise result useful as a uniform success-probability ordering, and the complete census preserves the exact finite data for later comparisons. The result is valuable on this particular pair without claiming a general Petersen-family principle.

The dated certificate retains the supplied scientific assessment, sources and limitations.

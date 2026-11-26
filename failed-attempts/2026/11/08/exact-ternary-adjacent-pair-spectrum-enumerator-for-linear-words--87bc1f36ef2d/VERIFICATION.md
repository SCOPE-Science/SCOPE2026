---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A nonzero adjacent-pair matrix admits a word if and only if it is the arc-multiplicity matrix of a directed Euler trail. The divergence distinguishes balance from each of six oriented endpoint pairs and, together with weak connectivity on active vertices, is sufficient by adding the terminal-to-initial arc when necessary. With off-diagonal signed differences, the balanced cost is 3|p| and the representative imbalanced cost is |p|+2|p−1|. For the latter, p<=0 gives costs 2+3k and p>=1 gives 1+3k, k>=0. Each of the three pair slacks contributes 1/(1−z²); loops are independent before enforcing connectivity. A disconnected support either has only loops (keep zero and single-site loop supports) or has exactly one joined pair and a loop-positive isolated third vertex; the latter gives precisely the 3z³ and 6z² forbidden numerators over (1−z)^3(1−z²). This yields the exact rational series. Its largest pole is at 1 with coefficient 7/12 on (1−z)^(−7), giving 7m^6/8640; the other poles are strictly lower order. A code chooses one representative of each observation class. Independently growing all reachable matrices by word extension with only the current terminal symbol retained for extension, then taking their union, agreed with the exact denominator convolution for m=0..20 (python3 /workspace/audit_evidence/spectra.py). The claim is for linear ternary words, overlapping ordered pairs, and no side information.

## originality

FAIL

The distinct indexed result f0497779133f gives the exact same rational series for m>=1, the same leading constant, the same endpoint-free observation model and the same code-size interpretation. It also explicitly states that there is one empty multiset for source length one. Denote the common denominator by D; the frozen numerator minus the comparator's numerator is exactly D, so adding the already stated length-one term makes the rational functions identical. The decision rests on exact mathematical coverage, not index dates or access to the 2012 paper.

## value

FAIL

The profile count is a natural information-theoretic invariant, but its exact series, leading term and interpretation are already available for the same alphabet and word model. Incorporating the previously stated empty observation as the constant monomial is a trivial boundary re-encoding, not a distinct worthwhile mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.

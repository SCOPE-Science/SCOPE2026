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

Two queries in a row cannot both be true. For distinct rows, the all-positive pattern and coordinatewise downward closure imply that filling unqueried rows with ones is valid, so the sorted queried targets must obey j_(r)≤n−s+r. At s=n an all-positive witness requires at least one target 1; declaring exactly the target-1 queries false would then leave no preference equal to 1. Conversely for s≤n−1 the partial thresholds are all at least 2, so replacing every target 1 by 2 preserves the sorted partial criterion. Fill unused rows with ones; a true query receives its target, and a false query receives 1 for target >1 or 2 for target 1. This is coordinatewise bounded by the valid clamped tuple and realizes every bit pattern. For n=1 the construction on queries is vacuous and only the empty support survives. For each chosen row set, empty spots in circular parking with n+1 spots give (n+1−s)(n+1)^(s−1) by rotation symmetry; a distinguished vacant spot is never preferred or traversed and cuts the circle into the successful linear case. Binomial summation and removal of s=n yield the closed face polynomial. Appending a new row at target 1 preserves the old thresholds at their shifted indices, so all facets have size n−1. The s=n−1 coefficient and negative evaluation at −1 give the stated facet and reduced Euler numbers. The provided exchange witness is valid: adding one element repeats a row and adding the other gives two targets n. The rank-zero n=1 and uniform rank-one n=2 exceptions follow directly.

## originality

PASS

The partial-parking criterion and count are established inputs, not new enumerative results. The checked passages do not give the mixed positive/negative Boolean support criterion for the one-hot embedding of classical parking functions. Exact catalogue self-matches are not independent prior results; the closest distinct shattering records concern other concepts and query ground sets. The supported addition is the full trace characterization and its complex consequences.

## value

PASS

The theorem identifies every shattered support in a natural Boolean encoding, rather than just bounding the dimension or counting positive completions. In particular it explains the exact obstruction at full size and separates purity from the matroid property. The complete face data and sharp classification are useful for comparison with other preference-based concept classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.

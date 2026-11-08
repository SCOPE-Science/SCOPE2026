---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

Run `python3 checker.py` in a clean directory with Python 3.9+ and its standard library. The checker produces `BURNSIDE_SERIES_OK`, six `DIRECT_PARTITION_ORBITS_OK` lines, and `COMMUTING_EQUIVALENCE_CENSUS_OK` on success.

It computes the Burnside cycle-type sums over all matrix dimensions with at most twelve cells and applies the formal multiset transform using exact rational coefficients. It independently tests every ordered pair of set partitions on \(n=1,\dots,6\) worlds (44,168 inputs), canonicalizes the positive intersection matrices, and confirms the first six isomorphism totals, published labelled counts and vertex-transitive counts. The exact set-partition enumeration is exhaustive only for these six sizes; the formal proof establishes all coefficients and all sizes. Nothing in the finite computation certifies historical novelty, and an independent mathematical audit has not been performed.

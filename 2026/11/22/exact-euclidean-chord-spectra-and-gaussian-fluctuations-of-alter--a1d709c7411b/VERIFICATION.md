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

# Verification record

The statement is proved for all integers \(r\ge1\) through the exhaustive local-state bijection, the explicit matrix product, characteristic-polynomial reduction, exact coefficient recurrence, and analytic Perron-eigenvalue expansion. The second-shell count is asserted only for \(r\ge2\).

The standalone `verify.py` enumerates all matching supports without consulting the transfer matrix and evaluates each squared chord by integer XOR popcount. Its exact comparisons cover every ordered pair for \(1\le r\le7\), totalling 435,664 pairs, and check polynomial recurrence consequences through \(r=16\). Actual successful output:

```
ALTERNATING_SHARD_CHORD_PASS checked_ordered_pairs=435664 max_r=16
```

Exact symbolic checks were separately performed for the transfer characteristic factorization and the first two logarithmic derivatives of the dominant cubic root. Numerical or finite checks alone do not certify the all-rank theorem; the symbolic proof supplies that step.

The proof relies on the published identification of the shard-polytope vertices with alternating-matching characteristic vectors; it does not establish a result for other affine realizations, all shard arcs, or volume-sampled point pairs. Historical novelty searches were bounded, and independent validation has not been performed.

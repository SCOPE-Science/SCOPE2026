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

# Reproducible checking

Extract `verify_tripod.py` from the same finding package and run `python3 verify_tripod.py` with Python 3.11 or later. No installed packages, symbolic computer algebra, external files, or network access are needed.

The checker has two separate implementations of the objective: (1) the exact tripod first-leader and distal-path dynamic program using `fractions.Fraction`; (2) direct grounded-Laplacian construction, Gaussian inversion, and exhaustive size-\(k\) leader subsets for small cases. It tests all arm lengths in \(\{1,2,3\}\) with total length at most six, edge conductances in \(\{1,2\}\), and all admissible \(k\), as well as asymmetric weights and fractional conductances. It explicitly checks the non-nested optimal sets for the seven-vertex unit-weight tripod.

Observed output:

```
EXACT_TRIPOD_MATCH 4560 cases; root modes ['center', 'center-follower']
NON_NESTED_WITNESS 11 13/3 [(3,)] [(0, 5)]
VERIFICATION_OK 4577 total exact comparisons
```

These checks provide a finite regression test, not exhaustive evidence for arbitrary real weights or arbitrary graph size. The general result is established by the series/parallel resistor identities, the grounded-component partition, the exact shortest-path recurrence, and the exhaustive three-first-leader case split in `RESULT.md`.

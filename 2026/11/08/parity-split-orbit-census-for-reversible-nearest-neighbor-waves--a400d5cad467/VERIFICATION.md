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

# Reproducibility and boundaries

The full mathematical proof is contained in `RESULT.md`. The reproducibility files use the Python 3 standard library only. From a folder containing the distributed files, run:

```sh
python3 check_matrix.py
python3 check_enumeration.py
python3 check_orbits.py
```

The captured results are `check_matrix.out`, `check_enumeration.out` and `check_orbits.out`. The matrix program performs 1,254 exact binary nullity comparisons for ring lengths 3–35; independent tuple-state exhaustive dynamics covers 87,360 binary states for lengths 3–8; integer Möbius-inversion consistency tests run for lengths 3–60 and characteristic-two field sizes 2 and 4. Each program raises an exception on a mismatch. The checks passed when run with the distributed source.

All finite computations serve as falsification checks, not as infinite-family proofs. The proof uses an explicit traveling-wave coordinate change for odd ring lengths, and complete local Jordan analysis for even lengths. The scope excludes fields of odd characteristic, nonlinear rules, and boundary conditions other than cyclic.

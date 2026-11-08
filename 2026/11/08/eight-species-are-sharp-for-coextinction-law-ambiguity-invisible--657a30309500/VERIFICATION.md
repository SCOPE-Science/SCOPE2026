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

# Verification of the sharp eight-species coextinction moment threshold

Run the two stand-alone standard-library Python programs from the same directory:

```bash
python3 verify.py
python3 crosscheck.py
```

Each program must end with `PASS`; a failed exact identity or finite-count assertion raises an exception. `verify.py` constructs plant partner-set degrees and pairwise unions, enumerates all pollinator extinction subsets, directly checks the witness and verifies the 2,161 labelled four-plant/three-pollinator lower-bound matrices and their 42 isomorphism classes. It enumerates 150 connected four-by-four and 76 connected five-by-three classes and lists all five moment-equivalent, distribution-inequivalent pairs. `crosscheck.py` independently iterates every binary incidence matrix in those two connected eight-species cases and computes moment Bernstein coefficients from direct survival outcomes instead of degree/union formulas.

Both scripts enumerate complete finite domains under their explicitly coded constraints. The analytic small-guild arguments extend the seven-species impossibility beyond these finite enumerations. The independent pollinator-extinction assumption is essential. The decimal probability gap is not part of any certificate: the difference is exactly \(q^3(1-q)\), with exact maximum \(27/256\). The verification is mathematical and same-model only; no independent external audit has been conducted.

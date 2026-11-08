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

## Reproducible checks
Execute `python verify.py` with Python 3 and its standard library. The script independently tests the coefficient formula using exact fractions for all ranks through \(n=12\); reconstructs component-size types directly from rim subsets through \(n=12\); independently enumerates the underlying partial maps and their adjacency-preservation constraints through \(n=7\); and deduplicates restrictions of ambient dihedral automorphisms through \(n=10\). Its successful terminal marker is `VERIFY_OK`.

## Proof boundary
The unrestricted enumeration follows from the cyclic path-and-gap decomposition and automorphism factorization. The large-size growth limits follow from factorial lower and upper bounds. Computational checks are finite corroboration only. No external audit has been performed, and the proof does not establish a sharp multiplicative asymptotic for the total cardinality.

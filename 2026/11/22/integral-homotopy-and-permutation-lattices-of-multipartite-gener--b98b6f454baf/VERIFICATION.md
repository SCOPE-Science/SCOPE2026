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
# Verification and scope

`verify.py` uses Python 3 standard-library operations and does not require files outside this package. Execute `python3 verify.py` from its directory. Its completed run returned:

```
VERIFY_OK cases= 112 faces_checked= 6984 primes=2,101 orientation=PASS
```

All 112 part-size vectors have 2–4 parts, each of size 1, 2, or 3, and at most 10 total vertices. For each, the program constructs shortest-path distances, compares every vertex subset to the proposed general-position face criterion, and computes reduced Betti numbers from the oriented simplicial boundary ranks over the finite fields with 2 and 101 elements. It also checks one actual part-swap and one within-part-swap sign on a fundamental cycle for the three-part two-vertex case.

Finite fields and finite enumeration do not establish the infinite assertion or integer torsion-freeness. Those assertions follow from the topological attachment proof and integral join chain modules in RESULT.md. This is not an independent scientific assessment.

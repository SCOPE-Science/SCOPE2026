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

# Verification
The proof of the exact per-simplex profile is equations (1)–(2) of `RESULT.md`. The strict universal simplex bound is (3) and the two-case maximum argument; the explicit sharpness sequence is (4); the inverse stability formula and normal estimate are (5). All quantifiers and normalization are specified there.

`python verify.py` was executed on the current package source and returned `PASS: 90 finite consistency cases; analytic proof is separate`. The program uses exact rational vertices and Gram determinants, with floating square-root evaluations for finite tests. Consequently it is a consistency check, not an exact symbolic certificate for the universal theorem, and it cannot establish novelty or historical priority. A fresh external audit has not been performed.

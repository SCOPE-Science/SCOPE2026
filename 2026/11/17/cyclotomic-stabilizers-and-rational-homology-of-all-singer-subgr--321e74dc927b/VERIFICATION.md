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

# Verification details

`verify_singer.py` is self-contained, uses Python's standard library and does not download files. Invoke `python3 verify_singer.py`. Successful checks print `ALL_CHECKS_PASSED`. The test evaluates the explicit cyclotomic and Möbius-inversion formulas for prime powers \(q\in\{2,3,4,5,7\}\), all \(4\le n\le16\), and all subgroup divisors. It checks actual binary finite-field subspace stabilizers in dimensions four and six, and independently counts quotient flag orbits for dimension four. Finite enumeration is not an infinite proof; the unrestricted theorem follows from the explicit mathematics in `RESULT.md`.

No independent mathematical audit is represented by these computational tests.

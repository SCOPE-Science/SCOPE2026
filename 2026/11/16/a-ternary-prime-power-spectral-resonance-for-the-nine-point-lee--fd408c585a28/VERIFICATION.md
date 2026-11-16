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

The all-exponent proof factors the character polynomial by the prime-power cyclotomic polynomial and compares complete three-element residue fibers. The checker exhaustively verifies the classification by integer arithmetic for cyclic moduli 3, 9 and 27, yielding kernel dimensions 32, 416 and 1568 respectively. The finite tests are not used to infer the theorem for untested moduli.

Reproduce with `python checker.py` from the same directory. Only Python 3 standard-library facilities are required. Independent mathematical audit: not performed.

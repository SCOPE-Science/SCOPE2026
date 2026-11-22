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

# Reproducible verification

Execute `python3 check.py` using the Python 3 standard library. Expected final line: `HAMMING_WIENER_EXACT_CHECKS_OK 406585`. The checker validates exact rational moment identities, nonnegative primal and dual signs, the polynomial uniform bound on every integer in the tested range, matched objective values, and the direct Fourier transform/inverse Fourier transform on small complete cubes.

All-parameter validity follows from the analytic dual-polynomial certificate and constructive optimizer in RESULT.md. The checker ranges over dimensions 2 through 100, plus all rational transition targets, and performs direct Walsh transforms for dimensions 2 through 7. No finite computation is described as an infinite proof. No external auditing was performed.

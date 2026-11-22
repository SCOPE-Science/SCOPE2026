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

Reproduce locally with `python3 check_invol.py` (Python 3 standard library only). The script performs independent direct generation of all involutions on one through nine labels, swapping adjacent one-line positions, checking every candidate for self-inversion, and building actual connected components. It compares each component with the matching signature and Fibonacci product, checks exact combinatorial component and edge formulas, and independently obtains all pairwise shortest paths for sizes through eight. The output ends `PASS`.

The mathematical argument in `RESULT.md` proves the formulas for arbitrary integer length. Finite enumeration is a consistency test only; the Poisson limit is justified separately by factorial-moment asymptotics. No independent audit or external certification has been performed.

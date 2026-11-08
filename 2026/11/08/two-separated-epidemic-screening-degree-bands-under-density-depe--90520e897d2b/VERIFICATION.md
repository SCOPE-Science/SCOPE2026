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

The accompanying `checker.py` uses exact rational arithmetic and integer-root interval enclosures. Run `python3 checker.py` in the directory containing this file and the checker. It verifies the truncated power-law conditional mixing probabilities, critical-point sign landmarks, and all 18 degree-class sufficient-threshold decisions; the final run returned 48 passed exact assertions.

For \(k\in\{3,\ldots,20\}\), the checker bounds \(t=k^{1/3}\) by rationals with denominator \(10^{12}\), then uses the monotonic denominator \(5+t^2-c/t^4\) to enclose the screening score exactly. The general all-parameter derivative classification is demonstrated in the written proof, not inferred from the finite checks.

No independence, external certification, finite-network realization, or exact epidemic-outbreak probability is claimed.

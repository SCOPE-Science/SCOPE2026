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

# Reproduction and limits

Run `python3 verify.py` using only the standard library. The checker uses rational arithmetic, independently enumerates all joint outcomes for the four-item witness, and verifies the three-item formulas on a finite rational grid. It checks the number and identity of the expected-fair partitions and the strict gain at \(\varepsilon=1/60\).

The universal three-good theorem is verified mathematically by the proof of the exact formulas \(F_{x+y}-F_x=y^2\) and \(F_{x+y}-F_y=x^2\). The four-good continuum and its single threshold follow from an explicit polynomial identity plus strict derivative bounds, not from grid sampling.

The checker is not a substitute for independent scientific review. No independent audit is claimed.

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

The standalone `verify_cm.py` (Python 3 standard library) reproduces the exact dimensionless parameter definitions, computes the quadratic center coefficient by two independent algebraic expressions, compares it with direct finite differences of the original nonlinear update, and bisects the unique transition for five test parameters. Run `python3 verify_cm.py` in the directory containing this document and script.

The output is a finite algebraic diagnostic, **not** a proof of center-manifold existence, the infinite-time limit, or historical originality. Those claims rely on the analytic argument in RESULT.md, the cited primary equations, and self-review. The equality \(p=p_*\) is outside the accepted claim.

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

# Reproduction

Run `python3 verification.py` using Python 3 and the standard library only. The program constructs a separate backward-equation finite-graph solver, verifies the local tooth continued fraction, and evaluates convergence to the double-scaling and endpoint formulas. The run at preparation passed 21 numerical checks.

The finite linear-system checks use a reflecting cutoff at \(x=-B\), which introduces a numerical boundary approximation; their tolerances are documented in the source. The asymptotic statements follow from the exact recurrence and expansions in `RESULT.md`, not from finite data. No independent external review or certification has been performed.

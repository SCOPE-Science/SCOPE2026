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

The standalone `aux_check.py` can be run with `python3 aux_check.py` using standard SymPy, SciPy, and NumPy packages. The script reconstructs the radial and angular homogeneous polynomial expressions, verifies the quartic-rational normalizer numerically at four parameter pairs, and checks the asymptotic physical-period coefficient along three positive-depinning paths and three positive small parameters.

These finite tests do not establish the infinite-time/zero-parameter limits. The proof of the sharp rotating-versus-pinned threshold follows from the exact angular polynomial and invariant rays; the radial-graph proof uses a linear ODE in angle. The occupation limit uses uniform radial equilibration, the exact physical-time change of variables, and Scheffé's lemma. No external proof certificate or independent audit is asserted.

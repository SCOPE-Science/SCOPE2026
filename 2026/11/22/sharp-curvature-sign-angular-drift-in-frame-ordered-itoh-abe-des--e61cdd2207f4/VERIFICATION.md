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

# Reproducibility and limits

`RESULT.md` contains the analytic proof, definitions and fixed-time limits. Execute `python3 verify.py` with Python 3, NumPy, SciPy and SymPy. The standalone test includes exact symbolic reductions of the Hessian transverse term and primitive, plus four mesh refinements of spherical/hyperbolic/Euclidean implicit steps, order-averaging checks and bisector radial recursion. The finite tests provide regression diagnostics only; the uniform error estimate is justified by the smooth Taylor expansion on a compact annulus and standard finite-time discrete Gronwall argument in `RESULT.md`.

The signed asymptotic law is proved for constant-curvature surfaces in the smooth squared-distance ball; its global uniqueness for arbitrary timesteps and extension to other objectives are not established. Both the base Itoh–Abe construction and its established fixed-center symmetrization are credited to the cited original literature. No external formal proof certificate or independent audit exists.

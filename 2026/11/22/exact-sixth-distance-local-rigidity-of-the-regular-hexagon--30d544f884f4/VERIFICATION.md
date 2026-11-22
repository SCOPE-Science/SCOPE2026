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

# Reproducibility and verification

The theorem's all-direction part is an exact second-derivative argument. The identity for each triangle moment is obtained from an affine simplex map and an elementary beta integral; `verify.py` applies this identity, not numerical integration, to recover the full rational Hessian.

Run `python verify.py` in this folder with Python 3.9 or newer and SymPy 1.10 or newer. This recreates `HESSIAN.json` from the given vertex list and verifies the energy, area, stationary first derivative, characteristic polynomial factorization, rank, four explicit similarity null vectors and strict positivity of all remaining eigenvalues.

Run `python crosscheck.py` in this folder with NumPy 1.23 or newer. The independent floating-point Gauss product rule computes each of the two integrals over triangle fans, checks the base energy, and compares twelve deterministic random directions to the exact Hessian. Five Gauss nodes in each simplex parameter are sufficient for the polynomial integrands, though floating arithmetic limits the strength of this diagnostic.

Both commands passed with these exact delivered scripts. The mathematical conclusion follows from the exact moment formula and rational polynomial factorization, not from finite sampling. The scope is restricted to a neighborhood of a regular hexagon, with a fixed cyclic vertex ordering. Global optimality is not established. Independent audit has not been performed.

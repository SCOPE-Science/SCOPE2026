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

Run `python verify.py` in a Python environment with SymPy, NumPy and SciPy. The checker constructs all three stochastic orthogonal-projection contact matrices from the path incidence vectors. It checks projection identities, preservation of constants, the exact two-draw product, reflection decomposition, invariant spectral blocks, endpoint derivatives, the characteristic sextic, the one-round optimum, and the positive eigenvalues of the three-vertex minimality remainder. It then tests 300 reproducible independently sampled probability triples through explicit matrix products and compares their exact numerical spectral norms to the algebraic optimum.

The analytic proof in `RESULT.md`, not random trials or numerical root-finding, certifies the quantification over all probability triples and the unique optimizer. Floating-point root values are display approximations; the isolating interval and derivative equation give the exact optimizer. No independent mathematical validation or priority certification has been performed.

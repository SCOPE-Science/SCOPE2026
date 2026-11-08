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

The included `verify.py` reconstructs the stationary occupation-integral matrix and checks the exact Lyapunov equation symbolically. It also verifies both isolated zero-flux endpoints, the half-flux dark-sector identities, and rate-optimality substitutions. Independently, it builds the original complex four-site Hamiltonian directly from Peierls phases, then compares numerical Lyapunov integrals with the analytic formulas for 11 fluxes and four positive sink rates, performing 88 scalar and matrix-residual assertions.

Run `python verify.py` with Python 3, SymPy, NumPy, and SciPy. The checker uses no external data and does not depend on previous packages. The exact finite-dimensional matrix calculation is combined with the spectral reachability proof in `RESULT.md`; numerical samples alone would not establish the infinite-time or all-parameter statements.

The sink model has one quantum jump out of the single-excitation space. The projective first-detection protocol and elapsed-time moments under additional dephasing are not tested or claimed. Independent scientific validation has not been performed.

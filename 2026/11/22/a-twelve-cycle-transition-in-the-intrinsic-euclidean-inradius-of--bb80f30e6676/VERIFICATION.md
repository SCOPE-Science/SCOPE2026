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

The analytic proof is in `RESULT.md`. The independent finite checker `CHECK.py` uses Python 3 with NumPy and SciPy; execute `python3 CHECK.py` in the extracted directory. It enumerates all \(n^2+1\) connected-subgraph inequalities directly, checks them on every canonical vertex, verifies affine dimension \(2n-1\), and solves an unrestricted \((2n+1)\)-variable Chebyshev LP for every integer \(3\le n\le15\) and for \(n=20,24\). For each case, numerical results agree with the all-dimensional formula and its asserted active facet families to tolerance \(2\cdot10^{-8}\). The observed terminal output is `CYCLE_COSMO_INBALL_INDEPENDENT_LP_PASS`.

The numerical LP is not an exact-arithmetic or infinite-dimensional certificate. The proof relies on algebraic comparisons and strict concavity for all \(n\ge3\), and on the published connected-subgraph facet theorem. No independent mathematical review has been performed.

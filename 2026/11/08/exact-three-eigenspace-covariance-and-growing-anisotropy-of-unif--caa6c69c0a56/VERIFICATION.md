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
# Mathematical verification

The distributed `verify.py` checks the *uniform vertex law* of the complete-bipartite matching polytope, not Lebesgue-uniform sampling. Executed with Python 3, NumPy and SciPy. The verifier independently enumerates every partial permutation vertex for orders 2, 3 and 4 and constructs the full covariance matrix in exact rational arithmetic. It checks every basis direction of the four Frobenius-orthogonal components, including each eigenvalue and multiplicity, as well as strict ordering. It also checks positive distinct numerical Laguerre zeros for orders 2 through 15 and finite-size normalizations at orders 1000, 5000, and 10000. Output:

`PARTIAL_PERMUTATION_VERTEX_COVARIANCE_CHECKS_PASSED`

Finite calculations are not an all-dimensional proof. The universal decomposition follows from the exact three entry-pair occupancy types; strict ordering follows from Laguerre zeros and strict concavity; the asymptotic constants follow from the cited classical complex-uniform Perron formula and derivative estimates. The last two analytic ingredients are not checked symbolically by the script. No independent audit was performed.

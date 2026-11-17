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

# Verification scope

`verify_two_cube_radial.py` is a standalone source artifact, with its exact bytes embedded alongside this document. Running with Python 3 and NumPy prints `PASS 276 exact/statistical assertions`, followed by sample exact mean, scaled variance, and conditional variance values. The 276 count comprises 256 exact fraction assertions on small part sizes, 15 seeded-sampling comparisons, two overall-variance limit comparisons, and three critical conditional-variance comparisons. The sampling tolerances are stated explicitly in the source and must not be interpreted as proof.

For exact rational checks, conditional squares have \(\mathbb E[R_n\mid T=t]=(n+2)t^2/3\) and \(\operatorname{Var}(R_n\mid T=t)=4(n-1)t^4/45\). Dirichlet factorial moments give the first and second moments of the total square-energy and conditional mean. For large dimensions, the script checks convergence of \(N\operatorname{Var}(F_N)\) and \(N^2\operatorname{Var}(C_N)\) at representative block fractions. Infinite-dimensional Gaussian and critical non-Gaussian convergence are analytical, not exhaustively machine-certified.

No independent audit or external validation has been performed.

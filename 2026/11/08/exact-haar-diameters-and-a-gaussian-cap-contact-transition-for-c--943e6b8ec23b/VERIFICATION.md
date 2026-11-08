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

The proof reduces the exact Euclidean radius to a two-component orthogonal decomposition. This geometric step is independent of numerical integration and establishes equality for every eligible subspace; the distributional theorem then uses the exact squared-Gaussian ratio and beta law.

`verify_cylinder.py` performs 90 independent numerical constrained maximizations over actual random section coordinates; 69 empirical CDF and atom comparisons based on 90,000 beta draws per case; and 18 finite-dimensional checks of the Gaussian and chi-square asymptotic formulas. All 168 checks passed with the code's stated tolerances when executed using NumPy and SciPy. Stochastic checks are reproducible because seeds are fixed. They are not proofs of universal equalities, uniqueness of atoms or weak convergence.

The key proof checks are: normalized cylinder of unit transverse radius; \(m\ge2\) for a transverse equality vector; \(B/(1-B)\) with \(B\in(0,1)\) almost surely; beta parameters \(m/2\) and \((d-m)/2\); continuity of the beta distribution in the interior; Gaussian delta-method variance \(1/[2(1-\rho)^2]\); and independent \(\chi^2_k\) scaling in fixed codimension.

An external historical or independent mathematical audit has not been performed. The complete motivating source could not be inspected; that limitation is bibliographic, not computational verification.

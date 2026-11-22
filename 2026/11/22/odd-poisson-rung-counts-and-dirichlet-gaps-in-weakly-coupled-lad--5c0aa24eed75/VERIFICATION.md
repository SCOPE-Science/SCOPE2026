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

# Reproducibility

Run `python3 verify_critical_ladder.py` in this directory using Python 3 and the standard library. The reference execution returned `VERIFY_OK: 627 exact assertions / bounded numerical checks`.

The program independently enumerates all spanning-tree edge subsets of open ladders with one through seven rungs, comparing every admissible rung-set multiplicity with the gap-product formula and checking the total coefficient by rung count. For ladder lengths up to five, it calculates exact-rational transfer-current matrices at conductances \(1/2,1,3/2,3\), and compares all \(2^n\) inclusion events against independently weighted enumerations. Further bounded numerical diagnostics compare the finite weighted rung law with odd-conditioned Poisson probabilities, compare its mean with the finite spectral Bernoulli sum, and check the two-rung Dirichlet-gap second moment. These computations are finite cross-checks, not an exhaustive proof of asymptotic convergence.

The all-size evidence is the proof in `RESULT.md`: selected-rung cycle deletion; exact weighted enumeration; factorial dominated convergence and discrete total-variation convergence; conditional Riemann-sum convergence and independent cut marks; discrete path-Laplacian spectral convergence with a uniform summable tail; and extreme-scale separation from the finite determinantal eigenvalues. The continuum kernel is trace class, with an eigenvalue equal to one, so the limiting count is always positive. No external mathematics certification has been performed.

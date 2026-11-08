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

Run `python CHECK.py` using Python 3.10+ with assertions enabled. The standard-library script enumerates the full \(5^{3}2^4=2000\) signed spanning-tree family of scalar polytope vertices. Each feasible candidate determines a closed rational parameter interval, and every candidate quadratic is compared with the claimed sharp polynomial by *exact* minimization on its whole feasible interval. Therefore this finite computation is an exhaustive mathematical certificate for all real \(t\in[1,2]\), not a grid sample. The observed certificate contains 310 feasible symbolic families and 70 interior vertices in orbit sizes 20, 20, 10, 10, 10. Endpoint exact checks give respectively 20 and 10 scalar extremizers at \(t=1\) and \(t=2\).

Expected terminal line: `C5_SCALAR_CERTIFICATE_PASSED`. This diagnostic was obtained from a successful run of the included code. For Hilbert targets, reproduce the symbolic argument by checking the two chord equations for \(\alpha^2,\beta^2\), the pairwise variance identity, the five-cycle eigenvalue \((5-\sqrt5)/2\), the equality cases for the spectral inequality, and the elementary derivative signs. These steps are written in `RESULT.md`, without dependence on numerical experiments.

Scope excludes Hilbert targets of dimensions two and three below the golden-ratio threshold; it also excludes nonuniform weights and non-cyclic metrics. No independent external audit has been performed.

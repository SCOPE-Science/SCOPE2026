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

# Reproduction and limits

Execute `python verify.py` with Python 3 and no third-party dependencies. The verifier performs an exact rational identity check before imposing the tangency quadratic, high-precision checks of the positive curvature root and tangent contact, pointwise nonnegative slack tests, and deterministic random three-atomic mean-preserving global upper-bound tests. The standard-library script reports **11,188 passing assertions** and the numerical benchmark \(c=1\), \(L=10\), \(m=4\).

The unlimited probability-law theorem is justified by the analytic proof and its strict equality argument; neither 11,188 finite checks nor randomized samples alone can verify all laws. A direct symbolic calculation confirms that the difference between the supporting line and the Haldane curve factors as \((u-q)^2(L-u)\) times a strictly positive rational prefactor, once the quadratic for \(q\) is imposed.

The main primary source provides the Haldane equilibrium curve and a slow-switching approximation. This result does not derive finite-period convergence for arbitrary laws, nor optimize transient Han-model dynamics. Literature comparison identified relevant prior mathematical and photobioreactor results; historical priority requires independent review.

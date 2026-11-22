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

# Verification of the three-gap law

The proof uses established rational independence of distinct radical reciprocal scales and finite-dimensional equidistribution. A direct five-pattern phase calculation supplies the local generating function; a summable uniform tail bound upgrades finite independence to natural densities. The same-scale endpoint overlap occurs precisely at the explicitly classified scales below three, proving the pointwise threshold and positive-density exact support. All computations listed below are sanity checks, not substitutes for these infinite arguments.

## Reproducible checks

Run `python3 triple_checker.py` in Python 3 without dependencies. It independently counts and compares every triple of consecutive gap counts for \(k=2\), \(1\le n\le125\), and \(k=3\), \(1\le n\le48\). The two methods are (a) prime-exponent sieve of all positive integers below the final endpoint and (b) enumeration through the unique radical form. It tests five-pattern local phase distributions at 100,000 grid points per radical scale for \(k=2,3,4,5,8,12\), and the explicit large-\(k\) endpoint covariance correction for \(k=32,128,512,2048\). All tests pass.

Run `python3 empirical.py` for an additional sample of 150,000 square-full three-window vectors, using a direct squarefree-parameter enumeration. The observed lag-two versus lag-one raw product average is about \(0.06109\), compared with the predicted limiting-law difference \(3/(2\sqrt2)-1\approx0.06066\). This comparison does not prove empirical second-moment convergence.

## Boundaries

The script checks neither equidistribution for infinitely many scales nor the positive density of every possible triple. No external independent audit has been performed, and the source-based originality assessment has the residual risks stated in REVIEW.md.

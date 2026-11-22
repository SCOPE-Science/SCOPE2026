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

# Reproduction checks

The proof in `RESULT.md` gives analytic identities for every positive real intensity. Run `python checker.py` for directly enumerated two- and three-Poisson examples and low- and high-intensity comparisons. It uses only the Python standard library. The printed truncation remainder bounds are numerical evidence and do not constitute infinite-support certificates.

Optionally run `python verify_asymptotic.py` using the separately installable `mpmath` library for high-precision evaluation of the exact Bessel decomposition. Its output includes the ratio of the exact variance deficit to the stated sharp asymptotic equivalent as intensity increases. The high-precision numerical calculations corroborate, rather than establish, the Bessel dominated-convergence proof.

The distinct-rate identity is algebraic in `RESULT.md`. The monotone-covariance step is proved using independent-variable association; fixed-order Bessel asymptotics and their integral bound give the limit uniformly dominated by a geometric sequence. No external certification or independent mathematical audit has been performed.

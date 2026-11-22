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

# Mathematical reproducibility

Run `python3 check_collision.py` with Python 3, NumPy and SciPy. The checker tests 55 independently evaluated Bessel-Laplace, elliptic, positional collision, nearest-neighbor coherence and finite-cutoff identities. Direct site sums versus two-time overlaps agree in the two-dimensional finite numerical tests. Analytic steps that require proof beyond finite computation are the Bessel fourth-power integral bound, square-summability in dimension at least three, the disjoint-annulus divergence in dimension two, and the monotone-convergence limiting argument. These are proved in `RESULT.md` rather than extrapolated from the test grid. The critical two-dimensional leading constant is not determined.

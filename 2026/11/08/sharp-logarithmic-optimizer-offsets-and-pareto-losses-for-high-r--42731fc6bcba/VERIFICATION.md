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

# Analytical and computational verification

The analytic result follows from the explicit frame-bound equations in Section 8 of Faulhuber–Shafkulovska (arXiv:2204.02917). The proof checks their normalization, expands the hyperbolic functions uniformly at \(\eta=2\log n+s\), isolates and brackets the three critical points, and applies the cited global optimizer uniqueness to transfer local critical-point calculations into global sharp asymptotics. The positive regret coefficients follow from strictly convex profile functions with distinct minimizers. In particular, the calculations establish a theorem for all sufficiently large integer redundancies, rather than merely a finite test.

A standalone reproducibility script `check_gabor.py` uses Python 3 plus `mpmath` and runs with `python check_gabor.py`. The check covers five redundancy values, signs and locations of three critical points, Taylor errors, independently truncated doubly infinite Walnut-series values at extremizing Zak phases, and limiting regret positivity and convergence in three redundancies. Its expected successful output is `GABOR_HIGH_DENSITY_CHECKS_PASS 76`. The Walnut calculation uses finite truncation without a rigorous universal tail certificate, and the finite numerical tests do not prove the asymptotic theorem or mathematical novelty. No external independent audit has taken place.

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

# Mathematical verification and reproducibility

The principal argument is the exact rank-two secular equation for the two-hotspot next-generation matrix. Positivity and strict decreasingness of the resolvent quadratic form establish uniqueness of the root above the background spectral radius. The cyclic-ball convolution lemma proves the universal radial monotonicity; the five-cycle Fourier calculation proves the sign change at \(h=2/5\). Direct multiplication at the boundary proves the all-rate permutation statement. These are deductions for arbitrary admissible parameters, not conclusions extrapolated from computational sampling.

Run `python3 verify.py` with Python 3 and no third-party modules. The checker performs 597 exact-rational evaluations, including cyclic-ball convolution inequalities for sizes 5 through 17, movement-square and Green kernel comparisons for sizes 5 through 12, the rationalized five-cycle Fourier identity, the boundary matrix identity, and the exact threshold witness. Its output contains a `PASS` summary and reports the two opposite outbreak-threshold orderings.

No external numerical eigenvalue package is required. Computation verifies listed finite instances only; the full infinite-dimensional parameter domain is covered by the written proof rather than by enumeration. The invasion threshold is linear-local. Independent external audit has not been performed.

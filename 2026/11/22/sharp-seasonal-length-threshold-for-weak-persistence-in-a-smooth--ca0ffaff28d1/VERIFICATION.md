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

# Verification record

The following mathematical checks were performed on the enclosed standalone source files:

1. Analytically derive the reciprocal equation and compose the four exact interval maps. The ramp integrals vanish by reflection symmetry, and their positive additive terms lie between \(2\eta e^{-\eta}\) and \(2\eta e^{\eta}\).
2. Independently check the three affine-recurrence regimes: contraction when \(\delta>0\), expansion when \(\delta<0\), and divergence under positive forcing when \(\delta=0\). Monotonicity and vanishing ramps recover the full continuous-time upper/lower limits.
3. For the specified balanced calendar, verify exactly \(q_n=1\) and summability of \(b_n-4\), giving \(n p(T_n)\to1/4\).
4. Run `python3 CHECK.py`: four positive, three negative and one zero offset, with additional ramp symmetry checks for fifteen widths in each direction. The checker passed. Numerical evidence was not used to infer infinite-time behavior.

The Bohl exponents are controlled by arbitrarily long constant favorable and hostile intervals. Scientific limitations and closest prior work are described in RESULT.md and REVIEW.md. No independent scientific audit has been performed.

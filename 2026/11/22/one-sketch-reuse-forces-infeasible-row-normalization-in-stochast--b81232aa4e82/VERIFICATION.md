---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Verified the literal update and step range in RESULT.md:6–27. The selected row alone is multiplied by 1+β−βu², where β=ηn and u=√n||x_i||. Initially 0≤u≤√n by the orthogonal-projector diagonal bound. The multiplier is positive on this interval. For a nonzero row, u_next−1=(u−1)[1−βu(u+1)], and 0<βu(u+1)≤(1+1/√n)/2<1. Thus each positive amplitude stays between its current value and 1 and converges to 1 on its visitation subsequence (the only admissible positive fixed point); zero rows and directions remain unchanged. Every coordinate is visited infinitely often almost surely, proving the deterministic limit and preserving full column rank by positive diagonal scaling, even at the limit. The limiting Gram trace is s/n; matrix Cauchy–Schwarz gives both exact lower bounds, and n=p with X0=I gives equality. Direct differentiation also verifies the factor of 1/2 in the shared-sample expected-surrogate gradient; independent samples instead factor the expectation. VERIFICATION.md and verify.py were inspected, not executed. The claimed 96,768 finite checks are package-reported and do not certify the infinite-time assertion. Exact arithmetic, fixed positive step in the stated interval, and zero tangential term are essential scope boundaries.

## originality

PASS

Qualified to the exact all-frame limit and sharp Stiefel feasibility floor for forced reuse of a rank-one coordinate sketch in the two normal factors. The estimator with independently drawn factors and the general observation that reusing a stochastic factor can change its mean are not novel claims.

## value

PASS

A plausible implementation shortcut in a concrete sparse landing method changes the target, not just estimator variance. The theorem supplies an exact universal limit from feasible frames and a sharp dimension-dependent violation that cannot be removed by making the fixed step smaller. This is stronger and more actionable than a one-step bias example, without claiming independent-sketch failure or generalizing to arbitrary couplings.

The dated certificate retains the supplied scientific assessment, sources and limitations.

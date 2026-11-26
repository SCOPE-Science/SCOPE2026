---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The row KL projection is an exponential tilt, preserving √(u_-u_+)/u_0; for means ±a the same strictly increasing Q_a fixes the common endpoint total r and gives reflected rows for arbitrary strictly positive input weights. Column rescaling changes the projective invariant by T(1−r)/[(1−T)r]; row multipliers and martingale tilts persist as gauges. Entropy strict convexity and reflection identify π_T as the unique optimum, not the only feasible joint law. For z=log q the cycle derivative is a²(1−r)/[r(r−a²)] in (0,1) with limit 1 as r↓a. The map is increasing and its increment has sign T−r, giving global monotone trapping and a unique fixed point; the derivative at r=T gives the exact asymptotic ratio in both coordinates. The forward KL divergence to π_T vanishes quadratically with positive second derivative T/(T²−a²)+1/(1−T), giving the squared ratio on nonstationary trajectories only (at a stationary initialization the displayed ratio is undefined). Finally 1−λ=(T²−a²)/[T(T−a²)] gives the fixed-a boundary coefficient, not a claim about the iteration at T=a. The supporting checker was inspected but not run; these are symbolic deductions, not an extrapolation from its seeded tests.

## originality

FAIL

An inspected distinct published result covers the main scalar map and rate in reciprocal coordinates and proves a stronger boundary analysis. The differences in initialization, forward versus reverse interior KL, log-coordinate Lipschitz behavior, and writing out the strict-side Taylor coefficient do not supply a distinct scientific finding here. The coverage determination is not a priority or lineage judgment.

## value

FAIL

The smallest nontrivial martingale grid and its sharp deterioration near feasibility are intrinsically useful exact benchmarks. But relative to the covered recurrence and rate, the record's differences are gauge normalization, using the other interior KL direction, and differentiating the known rate at the boundary. None supplies a further exact invariant or boundary phenomenon beyond the inspected grid result.

The dated certificate retains the supplied scientific assessment, sources and limitations.

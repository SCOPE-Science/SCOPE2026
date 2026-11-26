---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Complex multiplication represents this normal planar A, so G_j(h)=|R_j((-a+ib)h)|². Direct expansion gives G_3''/a²=4−t²+vP(t) with the stated v,t. On [0,2] this is positive by the convex combination and the positive squared-term decomposition of 6(4−t²+P(t)). For t>2 the cubic factor of P(t) is positive and strictly increasing. Differentiating (t²−4)/P(t) gives the stated negative multiple of Q(t); in Q(2+s) the coefficients have one sign change and Q(2) and Q(3) have opposite signs. Thus there is one interior maximum, 0<v_*<1, and at the critical ratio only one curvature zero, leaving strict convexity. Jensen including infinite expectation follows from the strict supporting tangent and finite mean (mean zero forces H=0); strictly negative curvature above the ratio gives a nonempty open interval of means with symmetric two-point reversals. G_1'' and G_2'' are strictly positive as stated. Independent exact evaluation gave G_3(1/5)=746/1125, G_3(2/5)=377/1125, and G_3(3/10)=2041/4000 at a=1,b=3, giving the stated gap 401/36000. Bisection corroborated t_*=2.57584803206939 and the displayed ratio near 1.904257074337731; uniqueness comes from the polynomial argument, not the calculation. Replay: RESULT.md lines 32–71; VERIFICATION.md and verify.py were inspected, not executed.

## originality

PASS

Best-of-knowledge pass for the exact global RK3 squared-amplification curvature boundary and constructive reversal. A separate same-day result investigates the same matrix and law comparison for backward Euler, a material overlap in problem formulation but not coverage of the RK3 threshold. Neither novelty of Jensen's equivalence to convexity nor priority for fixed-mean time randomization generally is claimed.

## value

PASS

The normal damped rotation is the standard oscillatory scalar test mode. This classification pinpoints when any fixed-mean randomization makes its one-step numerical energy no smaller, and when a simple two-point law can improve damping; it distinguishes RK3 from RK1 and RK2 and includes the sharp boundary. It isolates a property not captured by absolute or strong stability, without equating energy damping over random durations to accuracy at a fixed terminal time.

The dated certificate retains the supplied scientific assessment, sources and limitations.

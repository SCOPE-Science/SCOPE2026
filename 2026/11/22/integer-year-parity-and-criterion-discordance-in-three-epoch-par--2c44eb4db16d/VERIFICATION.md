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

For independent equal-variance scalar observations with phase-registered cosine and endpoints 0,K, the endpoint-interpolation contrast cancels position and proper motion. Its parallax coefficient is cos(2πt)−1 and its normalized noise variance is 3/2+2(t−K/2)²/K². The common lower bound 3σ²/8 is attained exactly at the center for odd K; for even K the center is singular. In the even case folding each positive offset to its distance from the nearest integer preserves the cosine and strictly reduces the noise multiplier for offsets above 1/2. The derivative of log inverse variance on (0,1/2) is four times the difference of the decreasing π cot(πv) and increasing v/(3K²/2+2v²); the endpoint signs prove a unique positive optimum and reflection gives exactly two. At each positive offset the variance strictly decreases with K along even baselines; the half-integer benchmark tends to the lower bound. With δ=1/2−v, the stationarity equation first gives δ=O(K⁻²) by tan(πδ)≥πδ and then δ=1/(3π²K²)+O(K⁻⁴). The joint information determinant is proportional to K²[1−cos(2πt)]², hence all half-integers maximize it, and none is variance-optimal at even K. A fresh scalar bisection for K=2 gave v=0.492309377828065 and V/σ²=0.405769566440672, versus 0.40625 at the half-integer. Replay by bisecting the strictly decreasing stationarity difference on (0,1/2) and evaluating the contrast variance. The frozen verify.py was inspected, not executed; its assertion count is record evidence, not the universal proof.

## originality

PASS

The supported distinction is the global fixed-endpoint marginal-parallax parity law, including the strict even-baseline displacement and disjoint joint-D optima. The linear model, opposite-phase sensitivity and elementary determinant criterion are not themselves novel. No inspected distinct source states or supplies the full constrained classification; this is a bounded comparison, not a historical priority finding.

## value

PASS

In the smallest identifiable scalar design the classification separates information about one parameter from joint design quality. It gives an exact aliasing boundary and a structural counterexample to either opposite-phase or longer-baseline prescriptions for marginal precision with fixed endpoints. The small numerical gain over a half-year excursion is not the main value. This is an idealized design theorem, not a scheduling rule for real astrometric instruments.

The dated certificate retains the supplied scientific assessment, sources and limitations.

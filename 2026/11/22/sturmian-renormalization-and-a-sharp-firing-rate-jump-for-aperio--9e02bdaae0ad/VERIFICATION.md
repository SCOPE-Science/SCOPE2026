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

With r_i={iα+θ}, short gaps are exactly the phases in [1−α,1) and their successors lie in [0,α), so short gaps never touch. For c≤a every gap is used, including c=a by the ≥ convention. For a<c≤b the recursion takes one index step across a long gap and two across the isolated short-plus-long pair. The landing phases are exactly eligible in the sense r_i≥α; if the initial phase is below α, its next gap is long and its next phase is in [α,2α)⊂[α,1). For eligible phases [α,1−α) the next phase is r+α, and for [1−α,1) it is r+2α−1. Under y=(r−α)/(1−α) these are rotation by the irrational β=α/(1−α), with the two-gap interval chosen exactly for y≥1−β. This verifies half-open boundary and threshold conventions, including c=b. In either mechanical code, the sum of N symbols differs from N times the slope by a difference of two fractional parts, strictly less than one in absolute value. Multiplying by the two physical step-length differences gives the two discrepancy constants; dividing by N gives rates 1/ḡ and 1/(b+aβ)=(1−α)/ḡ. The one-interval transient does not affect the rate. A mechanical length-n factor is determined by the vector of cumulative sums floor(y+kγ), k=1,…,n, constant on each of the n+1 half-open intervals cut by distinct backward rotations of zero. Each cut increases one entry of this vector; all intervals have distinct codes and irrational forward orbits visit all interiors. This also gives exact factor complexity; telescoping implies balance and irrational frequency implies aperiodicity.

## originality

PASS

Credit the general physical projection recurrence and classical Sturmian rotation induction, factors, and discrepancy. The supported distinct claim is their physical combination: the exact two-regime rates and threshold drop, with synchronized output length and word laws on the same irregular clock. No independently identified result with this combination or a directly dominating statement was evidenced by the bounded comparison.

## value

PASS

The gap lengths themselves define the regime boundaries, so the window is not an arbitrary parameter slice. The result explains and quantifies a discontinuity in a physical firing rate on a nonperiodic clock, despite Sturmian output on both sides, and gives strict deterministic timing bounds rather than just average frequencies. That joint classification is more informative than a stand-alone exercise in rotating a shorter interval.

The dated certificate retains the supplied scientific assessment, sources and limitations.

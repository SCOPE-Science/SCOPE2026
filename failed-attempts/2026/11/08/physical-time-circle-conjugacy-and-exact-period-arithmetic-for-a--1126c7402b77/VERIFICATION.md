---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: Direct original-map substitution for x>0 gives the one-step reset when x>1/(1+r), and a two-step return when μ<x≤1/(1+r). The first-return unsigned log coordinate z=log(x/μ)/L rotates by -a and the physical roof is τ=1+1_{z≤a}, with a=log(1/r)/L∈(0,1/2). The sign flips each return. Four right-closed arcs concatenate into circle length Γ=2(1+a) with the original F translation by one; the rational rotation has prime period 2(p+q)/gcd(q,2) when a=p/q. Irrational rotation transfers Haar law, Koopman pure point spectrum and the exact telescoping return clock t_n=n(1+a)+z_n−z_0. The result applies only on the specified half-open invariant K, not the full plane. Direct rational arithmetic checked a=1/5 gives period 12 and inspected checker.py exact branch/prime-period tests for q=3..12; finite checks supplement the algebra.

## originality

FAIL

FAIL: November 2 previously published result already constructs an original-physical-one-step measurable circle conjugacy for the exact same F, not merely its return map, with circle circumference 2h where its h=2-theta equals the present 1+a. It gives the same invariant law, pure-point Koopman spectrum, exact physical reset frequency and bounded section clock discrepancy. The new rational prime-period denominator 2(p+q)/gcd(q,2) follows immediately from its exact rotation by one and an arithmetic gcd, while the half-open seam convention adds no substantive distinct classification. Strong previous coverage under identical model parameters.

## value

FAIL

FAIL: The reset clock, physical-time rotation, stationarity and spectrum are already explicit in the stronger earlier result. Computing the rational rotation order and choosing exact seam representatives are routine arithmetic consequences, not a separately valuable dynamical theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.

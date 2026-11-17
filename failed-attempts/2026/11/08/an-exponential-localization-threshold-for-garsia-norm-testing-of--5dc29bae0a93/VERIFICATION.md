---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

From the inspected RESULT.md and CHECK.py, H_{overline{z+t z^m}} has finite matrix E_00+tJ_m, with singular norm (1+sqrt(1+4t²))/2 for all m≥2. The exact Poisson-variance kernel profile is F=1−r²+t²(1−r^(2m))+2t(1−r²)r^(m−1) cos((m−1)theta). Subtracting F(0) and dividing by r² yields the quadratic −1+2t(1−r²)r^(m−3)−t²r^(2m−2). Rationalizing the smaller positive root gives t_-(r)=r^(3−m)/(1−r²+sqrt(1−2r²)). Its interior minimum for m≥4 is at sqrt(1−2r²)=2/(m−1), producing exactly T_m and the finite m−1 angular tie; m=3 instead attains the lower endpoint at r→0 and has unique radius sqrt((sqrt(1+6t)−2)/(3t)) for t>1/2. For m=2 strict concavity and implicit expansion give the claimed t⁴/2 small-amplitude gap. Rechecked numerically independently that T_m is reciprocal of an earlier C_{m,1} for m=3,4,5,8,10,18. The finite tests do not establish all m, which follows from the algebraic proof.

## originality

FAIL

FAIL: exact theorem coverage by an earlier Resultary result for general binomial symbols z^m+c z^n, all m>n≥1, published November 2, 2026. Set n=1 and c=1/t, then z+t z^m=t(z^m+(1/t)z); a positive scalar scales the operator/kernel norms without moving maximizers. Its threshold c=C_{m,1} is exactly t=1/C_{m,1}=T_m, with identical critical radius, m=3 continuity and m≥4 discontinuity. A separate November 8 published treatment directly addresses general az+bz^m with same threshold and full Hankel norm. The target degree-two Taylor deficit is a routine expansion of the already characterized quadratic kernel problem and does not establish a distinct original theorem.

## value

FAIL

FAIL for distinct contribution, not for mathematical interest of the subject: the phase transition, optimizer multiplicity, critical radii and operator norm are entirely covered by the November 2 broader result and a November 8 same-family result. The remaining degree-two small-t expansion and reciprocal coefficient parametrization are elementary algebraic consequences, not a separately motivated structural boundary that changes the known picture.

The dated certificate retains the supplied scientific assessment, sources and limitations.

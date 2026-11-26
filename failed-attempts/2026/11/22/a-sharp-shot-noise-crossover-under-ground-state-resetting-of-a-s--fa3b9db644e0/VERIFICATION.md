---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Each counted jump regenerates the process at G and the waiting times have exponential tails. Let f(z) be their Laplace transform and T=γ+p+s+u+2r. A first-step calculation gives 1/f(z)−1=z(H+Tz+z²)/[γp(q+z)], with q=u+r. Its coefficients through cubic order are A₁=H/(γpq), A₂=(q²−ps)/(γpq²), and A₃=(1/q−T/q²+H/q³)/(γp), using qT−H=q²−ps. For the analytic cumulant-growth exponent λ(k), 1/f(λ(k))−1=e^k−1, so J=1/A₁ and F=1−2A₂J². At equality A₂=0 and A₃=1/(γpq), giving the third normalized cumulant 1−6A₃J³=1−6γ²p²q²/H³. This also verifies the boundary at r=0 and the signs since q is strictly increasing. The waiting-time transform decays as z⁻² at large positive z, incompatible with exponential renewal intervals. The rational example is consistent (H*=24/5); the bundled symbolic checker was inspected, not executed.

## originality

FAIL

Verified exact mathematical coverage by the distinct catalogue theorem 6951e3b15413 for multiple arbitrary dark dwell laws with the same reset mechanism. Its original proof yields the exact rate, Fano formula, crossing and exact normalized third-cumulant deficit, not merely a qualitative analogue. One exponential dark dwell is an immediate specialization; the r=0 endpoint follows from the same rational law without a new argument. Both records are dated the same day, so this establishes coverage, not chronological priority.

## value

FAIL

Radiative-rate independence and the higher-cumulant distinction are worthwhile phenomena, but for this record the stronger exact emitter theorem already answers both quantitatively by one exponential-moment substitution. The elementary square-root threshold, rational example and no-reset endpoint do not add an invariant, a new mechanism, or an independently needed boundary. This is a useful illustrative calculation, not a separate scientific finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.

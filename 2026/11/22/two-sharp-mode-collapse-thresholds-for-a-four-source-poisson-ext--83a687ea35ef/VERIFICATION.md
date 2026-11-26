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

Direct differentiation of the four Cauchy terms reproduced the sextic E in u=x² with fixed leading coefficient −2 and positive denominator at q>0, the central factor −2(q+1)(q+9)Q, and the entire parameter discriminant. The strict convexity certificates and signs of H and Q isolate one positive root each, in (1,2) and (4,5). Sturm variations at (0,+∞) are (4,1), (3,2), (2,2) at q=1,2,5, so there are 3,1,0 positive roots; a positive root can only collide at q_f or cross zero at q_c. The derivative is positive near zero for q<q_c and negative for large positive x, giving 4,2,1 maxima by sign alternation and reflection. At q_f the simple discriminant zero makes the common-factor degree of E,E_u equal to one (a rank defect of k in the resultant matrix forces at least order k); two real positive roots therefore meet at an ordinary double root. To check that these are the outer maximum and its neighboring minimum, an extra exact separator was needed: the Sturm variations at u=0,1,+∞ for q=1 are 4,3,1, and all coefficients of E(1,1+v) are negative (constant −1250), so the inner root below u=1 cannot be in the fold. The fold gives no extremum there. At q_c the zero in u is simple since H does not vanish there, and E is negative for u>0 by continuity from above and absence of any positive zero at q_c. Hence E_u(0,q_c)<0 and x=0 is a strict quartically flat maximum. Both decimal heights agree. Fresh exact replay: `python3 /workspace/branches/independent_certificates.py 4`. No claim about unequal weights or vertical/two-dimensional extrema.

## originality

PASS

The supported contribution is the exact two-boundary horizontal mode diagram for this natural equal four-point arithmetic progression. The Cauchy mixture and critical-bandwidth viewpoint are known. The closest distinct positive Cauchy records have three atoms and genuinely different modal diagrams, not merely different normalizations.

## value

PASS

Four equally spaced equal sources are a natural symmetric test of resolution under Cauchy/Poisson smoothing. An exact classification distinguishing simultaneous outer losses from central coalescence, and ruling out any three-mode phase, supplies a usable critical-bandwidth benchmark and clarifies the symmetry mechanism beyond merely finding stationary points at a few heights.

The dated certificate retains the supplied scientific assessment, sources and limitations.

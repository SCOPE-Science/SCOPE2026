---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Independently constructed the five-dimensional stage-specific companion matrices for delay schedule (1,2,3), with correct stage-wise lag assignments, and symbolically recomputed det(zI-W2W1W0)=z^2[27000z^3+(10367-28675u)z^2+(4913-7825u)z-5780u]/27000 exactly. Schur cubic inequalities reduce to u>-10773/13315, while at u=-9/10 a real eigenvalue is approximately -1.09619. Halanay inequality yields exponential decay of the continuous DDE for |u|<1, and Rouché comparison via Re(rho conj sigma)=|z-1|^4/10 confirms each frozen integer-delay method is Schur-stable. At the threshold -1 is a simple multiplier and does not decay. The claim is for one fixed grid h=1, not all switching schedules.

## originality

PASS

Rodríguez-Gutiérrez and Martín-Vaquero 2026 section 4.3 explicitly says frozen stability does not imply matrix-product stability, with general sufficient common-Lyapunov and slow-variation conditions. It does not state the exact (1,2,3) grid schedule, parameter -10773/13315, or the cubic monodromy. Thus it motivates rather than implies the sharp counterexample; O best knowledge with older IMEX literature caveat.

## value

PASS

The exact spectral counterexample shows a sharp numerical instability even when the continuously delayed equation and every frozen recurrence are stable, a motivated nontrivial boundary for delay integrators.

The dated certificate retains the supplied scientific assessment, sources and limitations.

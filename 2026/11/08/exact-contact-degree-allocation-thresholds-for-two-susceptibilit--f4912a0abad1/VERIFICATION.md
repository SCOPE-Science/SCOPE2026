---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The forward infection matrix has entries (d_i-1) beta psi_j d_j/(2K) and rank one; its nonzero eigenvalue is beta[psi_H d_H(d_H-1)+psi_L d_L(d_L-1)]/(2K). Exchanging ordered degrees reduces the objective when d_H>d_L. For d_H=K-r and d_L=K+r, the exact discrete increment F(r+1)-F(r)=2[(K+r)-rho(K-r-1)] is strictly increasing in r; its unique zero gives consecutive ratio thresholds, with no non-adjacent ties. K=2 and both endpoint inequalities included. Independence of psi_H on r=K-1 follows from d_H(d_H-1)=0. K=3 case returns 21/20 versus 1/6. Rechecked by independent exact rational enumeration K=2,...,16 around all thresholds; this finite sample corroborates the algebra, not an infinite proof.

## originality

PASS

General recipient-degree SIR branching thresholds and susceptibility-degree correlations are established; the full staircase for two positive integer class degrees at a fixed equal-class budget, isolated ties, sharp homogeneous-improvement boundary and degree-one plateau are not stated in the inspected direct model theorem or in the closest published optimization of mixing at fixed two contact classes. Priority remains bounded, with a risk that elementary convex resource-allocation work implicitly contains the staircase.

## value

PASS

The exact discrete policy transition points and susceptibility-independent boundary change whether epidemic invasion is possible with the same average number of contacts, as the explicit threshold-crossing example demonstrates. The integer allocation problem is a natural constrained design, not an arbitrary numerical slice, even though its final optimization is elementary convex algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.

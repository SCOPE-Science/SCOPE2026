---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

M^T J=JM with J=diag(I_p,-I_q) implies R=-M^-1 J symmetric and MR=R M^T=-J. Uniqueness of the stable Lyapunov solution gives S=alpha S0+beta R, current Q=alpha Q0. Expanding the positive-current trace using the Lyapunov identity yields Phi=tr(M^T D^-1 M S)+tr(M); M^T J=JM cancels mixed terms, leaving alpha^2/(Tplus*Tminus) Phi(1,1). Phi(1,1)=0 forces M symmetric, hence B=0. This reconstructs all dimensions, no commutativity A,C needed. Independently solved Lyapunov equations and EPR in twelve nontrivial cases (p,q)=(1,1),(2,1),(2,2),(3,2) under three temperature contrasts; all matched scalar factor within 2e-9. Scalar matrix proof, not these finite cases, establishes universality.

## originality

PASS

Generic OU covariance and EPR formulas are known; Kharbanda, Burnet and Sabass cover the planar special case. Their 2026 abstract reports residual dynamics and strong-coupling behavior, not an all-dimensional two-temperature scalar multiplier. Authorised full paper unavailable due VPN, so exact comparison is best-of-knowledge with named priority risk. Resultary skew chain has heterogeneous baths but no published identical scalar factor in surfaced summary.

## value

PASS

A dimension-independent factor for a constrained but natural class of coupled Gaussian networks, valid with noncommuting internal relaxations, is structurally useful: it separates architecture/drift optimization from thermal contrast and gives an exact strict dissipation penalty.

The dated certificate retains the supplied scientific assessment, sources and limitations.

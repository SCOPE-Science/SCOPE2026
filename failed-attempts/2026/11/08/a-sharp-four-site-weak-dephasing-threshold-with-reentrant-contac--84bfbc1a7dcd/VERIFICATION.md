---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The specified four-site quadratic Lindblad dynamics has an exact closed 16-real-unknown stationary Hermitian two-point equation. At γ=0 boundary observability gives invertibility; d/dγ is obtained by exact linear-system differentiation. The source F(x,y) has strictly negative y^0 term −48x(x+4)^2 and strictly positive all y>=1 coefficients for x>0, so unique positive threshold yc(x). Balancing lower/higher x gives yc/x→3/35 and xyc→48. Independent exact SymPy normalization check establishes that, when J=1 and the earlier paper uses U field step, the older Φ_G(U²)=256 F(G²/4,U²), identical threshold curve. Thus mathematical formulas are consistent, and polynomial sign reasoning is valid; source VERIFY.py was not independently run during this audit.

## originality

FAIL

FAIL: The published 2026-11-01 four-site Wannier–Stark chain theorem uses the identical Hamiltonian, reservoirs, local dephasing, and stationary-current observable. It proves the entire global dephasing monotonicity/unimodality classification and precisely the same unique onset curve. Its Φ_G(U²) equals 256 times the submitted F(G²/4,U²) identically after t=2J=2, u=2U. Therefore the newer derivative-only result and endpoint laws are strict corollaries of a stronger already published same-model theorem, without a surviving independently original component.

## value

FAIL

FAIL: Since the exact same threshold, contact endpoint asymptotics and sign classification are already a direct specialization of the complete finite-γ predecessor, the submitted derivative-only theorem does not close a separately motivated unknown gap. Its exact symbolic confirmation is useful replication, but not new mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.

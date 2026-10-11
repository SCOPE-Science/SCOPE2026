---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

A relative local z rotation removes the DM phase and gives a Bell-diagonal XXZ Hamiltonian with transverse coupling R=sqrt(J^2+D_z^2). The exact Gibbs weights yield |c_z|-|c_perp| proportional to exp(2(J_z-R)/T)-1, so the optimizer boundary follows from the published Bell-diagonal maximum-correlation rule. The small-correlation entropy expansion gives the stated T^-2 coefficients. Fresh direct diagonalization of the original Hamiltonian reproduced the two equal transverse singular values, the sign change across the boundary and exact degeneracy on it.

## originality

FAIL

The formulas are correct, but the final claim is a routine specialization of two established ingredients: Chen–Yin already give the exact XXZ+DM Gibbs state, and Lang–Caves/Luo give the complete Bell-diagonal discord optimization by the largest correlation magnitude. A local z rotation replaces J+iD_z by R=sqrt(J^2+D_z^2); subtracting the two relevant correlation magnitudes yields the boundary in one line. The high-temperature coefficient is the quadratic Taylor term of the same published Bell-diagonal formula. Exact wording was not found, but implication-level coverage is decisive.

## value

FAIL

The phase-boundary phrasing is useful for interpretation, but mathematically it is a one-step comparison inside a known exact Gibbs state using the standard Bell-diagonal optimizer theorem, followed by a routine quadratic entropy expansion. Under the common value bar this is too mechanically implied to be an independent contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.

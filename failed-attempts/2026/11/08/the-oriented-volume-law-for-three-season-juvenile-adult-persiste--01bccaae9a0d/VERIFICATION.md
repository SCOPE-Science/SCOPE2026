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

Actual proof directly multiplies 2x2 season matrices to give common determinant -mu³ product b_i s_i and traces a1a2a3+mu C±, difference mu times det[(a_i,b_i,s_i)]. Perron root is strictly monotone in trace at common negative determinant. Distinct increasing critical functions T±+mu³Q give an open fertility window of opposite growth; 1–2 seasons cyclically invariant. Independent SymPy checked the universal trace difference and exact determinant-column mapping to prior. Source exact rational witness has traces 21/32,33/32 and determinant -1/16, so signs of det(I-P) differ.

## originality

FAIL

Published stronger Nov2 population theorem proves the same determinant orientation law, Floquet spectral ordering, threshold classification and minimal period for arbitrary season matrices; the new common mu fertility factor is a special case. Exact algebraic substitution confirms prior implication.

## value

FAIL

The same three-season orientation classification, exact determinant relation, spectral/persistence thresholds and smallest season count already appear as a rigorous corollary of the Nov2 stronger saturated-model theorem. Introducing a common fertility multiplier and a new rational witness is a routine substitution and computation, not a distinct motivated mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.

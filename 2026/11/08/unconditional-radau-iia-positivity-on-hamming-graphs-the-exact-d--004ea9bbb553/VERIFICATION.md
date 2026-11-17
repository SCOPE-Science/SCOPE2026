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

Tensor projectors E0=J/q, E1=I-J/q derive radial Hamming distance kernel K_r. Positive cases d1 q<=11 and (d,q)=(2,2),(2,3),(3,2) follow exact nonnegative rational numerator certificates, including completed-square checks. Complements have explicit negative diagonal at h=8/q,6/q,3/q,4/q for d1-d4; d>=5 uses L^5_xy=-120 and fifth Taylor coefficient R^(5)=1/108 to show -10h^5/9 for distance5. Independent exact rational projector and Bernstein certificates were corroborated. No finite grid substitutes for all d,q.

## originality

PASS

Existing results already imply d=1 complete-graph, d=2 square-rook, and q=2 Boolean hypercube subfamilies. The mixed alphabet q>=3, d>=3 exclusion combined with exact boundary certificates yields a complete Hamming frontier not directly entailed by those subfamily statements.

## value

PASS

A sharp two-parameter frontier between universal positivity and failure in a standard tensor-product graph family is a useful complete classification, extending the separately known complete-graph, rook-graph and Boolean-cube slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.

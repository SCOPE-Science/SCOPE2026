---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Run `python3 CHECK.py` from the directory containing this document and the standalone checker. It uses only Python's standard library, enumerates all unlabeled tree shapes through twelve vertices, and verifies the first-two-crossings cutoff at twelve sites for the expected number of connected surviving habitat pairs.

Exact checks include canonical tree-shape counts through twelve, integer distance-profile enumeration, Möbius-transform sign-variation bounds for every pair of profiles through eleven, the sole eleven-site exceptional polynomial, both twelve-site witness profiles, the polynomial factorization, and three exact rational signed values. The finite verification proves the cutoff only because the leaf-extension generation is exhaustive and because Descartes' sign bound plus the isolated exceptional cubic rule out two strict reversals. It is not evidence for weighted, cyclic, correlated-loss, or larger-size claims. Independent audit remains unperformed.

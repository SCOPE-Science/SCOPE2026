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

## Executed checks

`python checker.py` succeeded using Python 3 standard library, with exact integer/rational arithmetic. It enumerated all feasible supports and all directed weak edges for 660 seeded lower-block-triangular systems made from one- and two-dimensional feedback components, including strong cross-component interactions, nontrivial feedback signs, and zero intrinsic rates. No directed cycles appeared in any sample. The checker also confirmed the four-dimensional diagonal Lyapunov witness and the strict three-species rock–paper–scissors cycle.

## Analytic checks and limitations

The exact theorem is justified by the written projection induction and converse zero-extension of diagonal-block cycles, not by the 660 tests. Two-species acyclicity is established by support-complete proof and invertibility arguments. The block-diagonal-stability argument uses a finite Schur-complement induction; no numerical optimization certificate is needed. A direct principal-minor calculation checks the displayed full-network witness. The graph statements are not asserted as a complete description of arbitrary singular-matrix heteroclinic dynamics. Historical originality has not been independently audited.

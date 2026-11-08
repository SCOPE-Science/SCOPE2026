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

The result is established by a finite combinatorial classification; the scripts reproduce all counts independently.

`verify_exact_cover.py` enumerates all exact covers of the \(27\) axis-lines by selected points and all exact covers of the \(27\) points by selected lines. It checks the full incidence condition for every resulting pair, computes all elementary trades, performs all-source breadth-first search, and enumerates the coordinate-group orbits. The terminal output must report twelve point choices, twenty-one line tilings, 252 code sets, 1566 trade edges, the complete distance histogram, and orbit sizes 36 and 216.

`verify_structural.py` independently builds the affine Latin point codes and the three cubes of tilings from coordinate layers. It verifies the incidence condition, the trade factors, their distances, and the convolution yielding the complete trade-graph metric. The programs use Python 3 standard library modules only.

The verified domain is one explicit finite incidence graph. The proofs do not claim infinite-dimensional extension, optimal trade length for non-code intermediate states, or independent external certification.

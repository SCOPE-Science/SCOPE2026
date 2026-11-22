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

# Reproducibility checks

Run `python3 verify.py` from the extracted package. It requires Python 3 and only the standard library. The executable regenerates the Kneser-graph description of the Petersen graph, the ordinary matching faces, every barycentric flag, and every five-label permutation action. It explicitly checks the two geometric quotient face vectors, each elementary free-face collapse, the alternating quotient's maximal tree, its actual nonabelian two-cell attaching words, and all eleven legitimate generator/two-cell eliminations.

Expected final output:

```text
S5: 125 quotient flags; 62 elementary collapses; final point
A5: 238 quotient flags; 100 elementary collapses
A5: 8 vertices, 18 edges, 12 faces; 7 tree edges contracted
A5: 11 elementary 1/2 cancellations; 1 remaining spherical 2-cell
PETERSEN_ORBIT_HOMOTOPY_OK
```

The proof depends on every finite incidence in this one specified complex being checked. It does not depend on Monte Carlo sampling, floating-point boundary ranks, a timeout criterion, or any claim that an experiment proves an infinite statement. Reproducibility of the supplied verifier is not independent scientific validation.

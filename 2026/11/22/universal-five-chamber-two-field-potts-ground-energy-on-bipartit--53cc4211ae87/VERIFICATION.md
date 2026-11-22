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

# Reproduction checks

Run `python3 verify_universal.py` in the extracted artifact directory (Python 3.10 or later, standard library only). The deterministic program builds both \(K_{3,3}\) and the cube, forms their 18-spin and 24-spin triangle-expanded graphs, generates all five graph-independent proper-edge-coloring witness configurations, and verifies their integer color populations and monochromatic bond numbers. At five rational field points in the predicted regions, it compares each witness with every branch of the claimed energy envelope using `fractions.Fraction`, and verifies the unique active branch. It also performs 1,500 pseudorandom spin checks per graph of all six universal support inequalities and the energy bound; fixed seed 1127 makes these reproducible.

The observed output is:

```
K33: 6 base sites, 18 spins, 27 bonds, five sharp witnesses, 1500 random checks
cube: 8 base sites, 24 spins, 36 bonds, five sharp witnesses, 1500 random checks
TWO_FIELD_POTTS_UNIVERSAL_CHECKS_PASSED 3010
```

**Scope of verification:** These checks are finite implementation diagnostics; the all-size proof uses only the elementary triangle inequalities, matching pigeonhole bound, degree-three recoloring bound, and existence of a proper three-edge-coloring on cubic bipartite graphs. The checks do not enumerate all colorings of the 24-spin cube, determine coexistence degeneracies, or certify that literature is exhaustive.

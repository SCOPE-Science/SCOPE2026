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

# Finite checks and logical scope

`verify_frob.py` constructs the canonical bipartite branch graph using three component-line families, the six root-labeled high-multiplicity strata and the three cross-family node strata. It checks the complete Frobenius permutation, the connected fixed graph, stabilizer orders, a bona fide Frobenius-invariant spanning tree and the non-tree edge orbit decomposition. Its 12 test instances use prime degrees 5, 7, 11 and 13 and Frobenius orders 1, 2, 4, 5, 6 and 12; the script ends with `FERMAT_INTEGRAL_PICARD_TORI_VERIFIED`.

`geometry_check.py` constructs and pairwise intersects all 75 standard quintic lines over the split field \(\mathbb F_{11}\). It checks 375 ordinary two-branch crossings and 30 ordinary five-branch crossings and independently checks all three cross-family meeting equations. It ends with `FERMAT_GEOMETRY_VERIFIED`.

The calculations are finite, reproducible, exact arithmetic checks. The uniform proof uses the general prime-degree orbit argument, an integral equivariant spanning-tree construction, normalization exact sequences and local unit structure. No independent external validation has been performed.

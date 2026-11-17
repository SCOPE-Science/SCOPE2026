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

The result is proved for every odd dimension at least five by an exact cyclic change of coordinates, boundary facet decomposition, transfer-operator volume formula, and one-variable derivative factorization. The optional numerical hull checks are diagnostics only, not a substitute for this proof.

Run `python3 verify_odd_cycle_cut.py` with standard Python 3. The exact rational simplex and facet Gram tests and the Euler permutation counts use only the standard library. For an additional independent endpoint check, install NumPy and SciPy; the script will compare reconstructed convex-hull surface areas and volumes in dimensions three, five and seven. Dimension three is included **only as an out-of-scope normalization test**.

The delivered checker was executed and returned `ODD_CYCLE_CUT_GEOMETRY_PASS cases=4 exact_simplex_facets=28`. This verifies finite data and signs at the sample dimensions, not infinite-dimensional generality. Historical priority for the metric phase diagram remains conditional on discovery of unindexed literature. Independent mathematical audit has not been performed.

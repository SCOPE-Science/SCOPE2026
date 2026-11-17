---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The graph is defined by the exact 24 edges in artifacts/verify_masks.py and independently by an upper-triangular adjacency table in verify_signatures.py. All 276 edge pairs are separated by landmark bitmask OR iff the set resolves; exhaustive choose(12,0..5) tests give no bases below five and 192 five-landmark optima. Pairwise one-vertex exchanges across all 192 bases give 1152 jump and 428 original-graph-adjacent slide edges. Complete BFS from every basis certifies connectivity and eccentricity histograms 5:192 and 6:120,7:72, as well as the slide degree distribution 2:28,3:32,4:48,5:32,6:32,7:8,8:8,10:4. Both independent implementation source files were examined and an additional local reconstruction gave the same counts. Finite exhaustive proof is sufficient because the graph and all configurations are finite.

## originality

PASS

PASS best-of-knowledge: Kelenc–Tratnik–Yero introduced edge metric dimension but do not establish these exact Chvátal optimal basis and token-slide invariants. Similar Resultary results for Heawood or Clebsch graphs concern distinct underlying graphs and basis families, and no identified general theorem implies the 192/428/diameter-seven combination. Unindexed enumerations remain possible.

## value

PASS

The twelve-vertex Chvátal graph is a canonical small triangle-free four-chromatic obstruction, and its edge-metric sensing bases are natural optima. Exact mobility under adjacency-constrained slides has mathematical content distinct from the base-size census, especially the non-frozen connected slide network; this is a motivated finite classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.

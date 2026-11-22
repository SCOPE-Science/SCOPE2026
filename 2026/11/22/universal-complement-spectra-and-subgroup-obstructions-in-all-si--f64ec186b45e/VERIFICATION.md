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

# Verification instructions and boundaries

Both exact integer checkers run using only Python 3 standard-library facilities. Execute `python check_recursive.py` and `python check_direct.py`; compare their parsed JSON results with the supplied `recursive_results.json` and `direct_results.json`. Every group result must have the same five `tile_count_by_size` and `non_subgroup_count_by_size` entries, aggregate counts, and `all_tiles_have_universal_spectrum=true`. The recursive JSON additionally records concrete representative witnesses for the subgroup obstruction.

The two algorithms examine the complete finite domains, not numerical samples. The recursive algorithm includes every complement containing the identity and every zero-containing translate of each tile, then uses the exact translation multiplicity \(16/|A|\). The direct algorithm does not use that tile normalization: it iterates all subsets \(A\), all candidate complements containing the identity, and all possible normalized frequency subsets and frequency subgroups. Pairwise Fourier character inner products vanish exactly under the opposite-coefficient test in the power-of-two cyclotomic polynomial; no numerical tolerance is used.

Verification proves the stated finite enumeration conditional only on the explicit, auditable program logic and ordinary integer arithmetic. It provides no inference for larger groups, no independent audit, and no proof of literature priority.

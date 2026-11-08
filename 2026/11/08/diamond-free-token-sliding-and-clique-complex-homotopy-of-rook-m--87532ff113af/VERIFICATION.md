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

# Reproduction

Run `python3 verify.py` with Python 3 and its standard library. The script independently enumerates the nonattacking placements and valid token slides on 41 rook-board parameter instances, comparing all clique coefficients to the theorem. It checks vertex degrees, connectedness, one-spare diameters, and four-cycle counts at double one-spare boards. In addition it enumerates all labeled simple input graphs with at most five vertices and every positive token size, checking the common-core clique-count identity and the induced-diamond implication on 5,405 input-and-token cases.

Observed output:

```text
VERIFY_OK cases=41 states=1482 nonempty_cliques=11645 clique_coefficients=PASS degrees=PASS connectivity=PASS one_spare_diameters=PASS two_spare_four_cycles=PASS general_graph_instances=5405 core_identity=PASS diamond_transfer=PASS
```

These checks are exhaustive only within the stated finite parameter ranges. They do not verify unrestricted graph orders or replace the common-core, collapse, connectivity, and permutation proofs given in RESULT.md. The star-graph diameter is prior literature, not an independently proposed result. No external or independent mathematical audit was performed.

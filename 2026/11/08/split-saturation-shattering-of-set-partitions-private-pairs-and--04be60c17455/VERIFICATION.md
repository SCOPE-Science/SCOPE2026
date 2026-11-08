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

# Verification of split-saturation shattering

Run `python3 verify_partition_splits.py` from the directory containing this file. It uses only Python 3 standard libraries and tests the complete set of Bell partitions, all unordered nontrivial splits, and every family of queries for each ground-set order from one through five. It verifies agreement of the private-pair condition with full Boolean-label trace shattering without using the condition to compute the trace. Independently generated Prüfer trees verify that every largest shattered support is a unique tree-cut family. The same script computes all maximal support-size profiles and independently checks exact Littlestone dimensions through four elements using the full decision recurrence.

Expected terminal marker: `PARTITION_SPLITS_PASS`. The observed face vectors for ground-set orders four and five are `[1,7,21,16]` and `[1,15,105,300,125]`; the observed inclusion-maximal support sizes are `{2:3,3:16}` and `{3:140,4:125}`. These finite checks establish the stated small computations and corroborate, but do not replace, the unrestricted proof.

Limitations: no exhaustive verification beyond five elements; no external independent audit or proof assistant validation; the mathematical theorem's unrestricted part rests on the explicit human-readable proof. Historical priority is not certified by any computational check.

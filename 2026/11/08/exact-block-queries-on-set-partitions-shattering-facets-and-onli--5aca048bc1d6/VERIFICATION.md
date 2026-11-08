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

# Verification

Run `python3 verify.py` in a Python 3 standard-library environment. It independently enumerates the unrestricted set partitions, computes all binary exact-block traces and compares them with the proposed disjoint-family-plus-spare-element criterion. All query supports were checked for \(n\le4\), and every support through four queries was checked at \(n=5\). The small-case face coefficients and facets are checked against separate Stirling/associated-Stirling recurrences, and exact online mistake-tree dimensions were recomputed for \(n\le4\).

Actual replay marker: `PARTITION_EXACT_BLOCK_PASS supports= 69363 all_supports_n_le_4=1 sizes_le_4_n_5=1 online_n_le_4=1`.

Boundary cases verified include \(n=1\), a fully covering family with a singleton, and fully covering families whose blocks all have size at least two. The checker does not enumerate large supports at \(n=5\) or prove the theorem for arbitrary \(n\); the proof in `RESULT.md` is unrestricted. This is a self-review; no independent audit has been carried out.

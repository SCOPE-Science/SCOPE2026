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
The `verify.py` checker uses only the Python standard library. Run `python3 verify.py` in the directory containing the file. It compares the explicit traces of all unlabeled exact-\(q\)-block partitions against the forest/cardinality theorem on all supports through \(n=5\), plus deterministic selected supports at \(n=6\). The checker also confirms the basis-exchange property of maximal shattered supports for complete query graphs through \(n=5\), and compares the contraction/chromatic signed-trace criterion with explicit partition enumeration for all disjoint signed query assignments through \(n=4\), plus a deterministic selected set at \(n=5\).

A successful execution ends with `FIXED_BLOCK_PARTITION_SHATTERING_PASS 9916 partition-support cases`. The all-parameter proof is in `RESULT.md`; finite enumeration is not a proof for unrestricted \(n\), \(q\) or arbitrary \(H\). The complexity statement uses the classical NP-completeness of 3-colorability and the explicitly proved reduction; the checker does not attempt to certify complexity lower bounds.

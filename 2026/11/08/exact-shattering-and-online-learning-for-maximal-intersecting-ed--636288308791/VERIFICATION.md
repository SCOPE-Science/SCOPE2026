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

The unrestricted proof classifies maximal intersecting edge families, constructs every possible query labeling on each allowed support, and proves the online-dimension upper bound through positive-branch sizes. The topology proof uses the nerve lemma, the fundamental-group effect of adding all triangular faces, and the two-dimensional Hurewicz/Whitehead argument.

Run `python3 check.py` from the package directory. It uses only the Python standard library. The script independently enumerates maximal families for \(n=4,5,6\), checks every support of size at most four for \(4\le n\le8\), verifies the needed two-hypothesis positive branch condition, and tests the binary homological ranks through \(n=7\). It terminates with `EKR_MAXIMAL_EDGE_SHATTERING_PASS 34089`. Enumeration beyond those finite ranges is not claimed and would not itself prove the general theorem.

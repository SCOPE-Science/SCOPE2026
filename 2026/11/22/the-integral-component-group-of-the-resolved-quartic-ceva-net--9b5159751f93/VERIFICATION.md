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

The accompanying `verify_ceva4.py` is an ordinary Python standard-library program. Run with `python3 verify_ceva4.py`. It generates the exact 31-vertex Laplacian using the three pencils and sixteen base points; checks the 60-edge incidence and row sums; computes the Smith form using unimodular row and column operations for four distinct deleted vertices; and independently checks all four spanning-tree determinants by the exact Bareiss algorithm. An independent Faddeev–LeVerrier recurrence checks the full degree-31 Laplacian characteristic polynomial. All operations use integer arithmetic without random sampling, floating point, external files or network services.

The checker executed successfully from its packaged path with output `CEVA4_RESOLVED_INTEGRAL_CRITICAL_GROUP_OK`. The finite certificate proves the stated graph computation once the geometric line-pair census is reconstructed as in RESULT.md. It does not verify historical priority, assert a prescribed arithmetic smoothing exists, or supply independent mathematical audit.

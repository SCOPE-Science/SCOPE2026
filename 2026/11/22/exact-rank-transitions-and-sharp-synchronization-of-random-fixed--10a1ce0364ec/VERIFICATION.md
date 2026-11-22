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

# Reproducibility and limits

Run `python3 verify.py` with a standard Python 3 interpreter. The script independently constructs all idempotent total transformations for \(3\le n\le5\) and \(2\le r<n\), compares directly observed rank transitions with the inclusion-exclusion kernel, and compares all actual compositions of length up to three with matrix-power predictions. The direct product enumeration additionally checks the count for each prescribed constant transformation. All six tested pairs are recorded in `verification_output.txt`; the marker `ALL TESTS PASS` indicates that the checker assertions completed.

Finite checks are not an infinite proof. The exact identity for all finite \(n,r,k\) is established by the combinatorial bijection and spectral arguments in `RESULT.md`. Larger, simultaneously growing rank/dimension limits and prescribed nonconstant products are not claimed. Independent auditing has not occurred.

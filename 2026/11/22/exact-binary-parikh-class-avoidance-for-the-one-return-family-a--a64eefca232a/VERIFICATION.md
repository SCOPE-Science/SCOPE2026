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

Using Python 3 standard library, run `python3 verify_pattern_family.py` and `python3 verify_partition.py` in the directory containing these files. Their reference output is `CHECK_OUTPUT.txt`.

The direct program reconstructs all length-at-most-14 words, evaluates actual scattered-subsequence containment for each \(a^r b a b\) with \(2\le r\le6\), and compares complete weighted avoidance polynomials with a direct positive-row construction. The partition program uses independent Ferrers-row enumeration and a Gaussian-binomial recurrence over \(0\le A,B\le8\), \(2\le r\le7\); it also checks the exact unrefined counts and one-hole boundary.

These runs establish only the enumerated cases. The separate direct bijective argument in RESULT.md proves the unrestricted theorem. No independent audit or external validation was carried out.

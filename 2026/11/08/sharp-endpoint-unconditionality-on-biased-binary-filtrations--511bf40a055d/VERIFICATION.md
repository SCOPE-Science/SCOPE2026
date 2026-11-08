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

# Verification notes

The exact-rational script `check_biased_haar.py` reconstructs every tested conditional-expectation kernel row, enumerates all ancestral sign choices and compares the maximum with an separately implemented backward recurrence. It verifies 16 level-bias configurations (including fair, strictly biased and mixed cases), 10,586 leaf/sign combinations, and 120 homogeneous rational closed-form identities through depth 29. Strict-bias unique leaf and alternating ancestral signs are also checked. Run with `python3 check_biased_haar.py` using only the Python standard library. Expected terminal line: `ALL_NONHOMOGENEOUS_HAAR_ENDPOINT_CHECKS_PASSED`.

The analytical proof in RESULT.md, rather than the finite checks, establishes all depths, all positive coordinate biases and the complete claimed optimizer characterization. The script does not test infinite dimensions, arbitrary branching trees, or every real bias. No outside independent review has been performed.

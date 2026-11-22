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

The companion `check_minimal_nilpotent_words.py` performs direct matrix multiplication of each explicitly enumerated rank-one square-zero matrix over the indicated finite fields. It independently computes target frequencies for all word lengths in eight field/dimension families and compares with the closed formula for all rank-one targets and zero; no higher-rank nonzero products can occur by rank inequality. It confirms every total number of words, including all words whose product is zero. The output `verification_output.txt` ends with `VERIFY_OK`.

The executed cases are \((n,q)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2)\) and lengths ranging from two to six where computationally feasible, detailed in `RESULT.md`. These samples do **not** certify an infinite result. The general theorem is established by the projective-path proof, whose key exact normalization and spectral identities are stated in full in `RESULT.md`. The literature comparison may be incomplete; independent historical-priority verification has not been conducted.

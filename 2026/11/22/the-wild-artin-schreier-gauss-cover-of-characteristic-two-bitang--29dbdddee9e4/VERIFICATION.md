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

## Reproducibility
Run `python3 verify_char2_gauss.py` using the embedded standalone source. The script verifies the splitting formula by direct polynomial evaluation in all projective rational tangent lines. The finite-field checks are exhaustive for \(q=2,4,8\) and sampled for \(q=16\): they cover respectively \(4,144,3136,560\) integral marked quartics. All returned \(q/2\) split and \(q/2\) nonsplit tangent lines with output `GAUSS_CONTACT_SPLITTING_VERIFIED`.

The proof for arbitrary perfect characteristic-two ground fields is the algebraic function-field calculation in RESULT.md, not a claim of computational exhaustive coverage beyond those fields. The source literature comparison is a self-review; independent verification was not performed.

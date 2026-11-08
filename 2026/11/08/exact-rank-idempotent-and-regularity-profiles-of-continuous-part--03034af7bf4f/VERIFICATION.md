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

This check requires Python 3 standard library only. Run `python3 star_mr_verify.py` beside this file.

The program constructs the face sets of the star directly. It enumerates each of the \((n+2)^{n+1}\) partial functions for \(1\le n\le5\), retaining exactly those whose inverse image of *every* vertex or edge is a face or empty. It independently counts image-rank strata and idempotents. For regularity it tests every possible section through the nonempty fibers and checks that the section is itself inverse-image continuous; this is equivalent to existence of a generalized inverse because restriction preserves continuity.

The direct counts of qualifying maps are 9, 36, 185, 1278, and 10857. For all 25 rank strata, total counts, idempotent counts, and nonregular counts match the formulas in RESULT.md. Complete run output is `verification_output.txt`; its last line begins `VERIFY_OK`.

The finite experiment does not prove the general formula. The proof in RESULT.md supplies the all-\(n\) classification. No external proof assistant or independent audit was employed.

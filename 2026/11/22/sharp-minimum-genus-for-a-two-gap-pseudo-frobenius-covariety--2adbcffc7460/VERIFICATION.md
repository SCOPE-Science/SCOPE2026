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
The proof gives the infinite statement. The included `verify.py` exhaustively enumerates the target numerical semigroups for every odd Frobenius number from 5 through 31 using multiplicity extension and explicit additive-closure tests, without invoking the structural path classification to generate candidates. It checks both the least genus and equality of the full set of minimizers with the formula. The successful program output is `EXACT_MINIMUM_GENUS_OK`.

This computation is finite and cannot certify the statement for all integers. Literature overlap assessment is subject to the access limitations documented in the review.

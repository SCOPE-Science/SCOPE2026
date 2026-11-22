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
# Verification record

The exact finite verification program is `verify.py` (Python 3, standard library only). Run `python3 verify.py` in the directory containing this file. It enumerates all local selector tables and checks exactly the one-cycle condition at binary orders two, three, four and five. It prints each complete covariance-value histogram, verifies the three negative pairs at order four, and checks the first positive pair at order five against the independent rank-two determinant construction. It also evaluates the kernel matrix exactly at orders five through sixteen.

These finite checks are not an induction argument. The proof in `RESULT.md` supplies the all-order determinant identity and suffix/prefix overlap coefficient lists, which yield the positive family for every order at least five. The finite order exclusions are genuinely exhaustive because all selector-table bitmasks are traversed and each gives exactly one successor permutation. This record does not claim independent mathematical validation.

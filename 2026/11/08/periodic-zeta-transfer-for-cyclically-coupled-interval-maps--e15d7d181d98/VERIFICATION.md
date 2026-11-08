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
# Verification of the exact fixed-point and zeta identities

The accompanying `verify.py` uses only the Python 3 standard library. Running `python3 verify.py` returned `VERIFY_OK checks=605563` in the reviewed calculation. It enumerates every tuple of finite reaction maps in the six parameter cases \((s,q,m_{\max})=(2,2,10),(2,3,8),(2,4,7),(3,2,10),(3,3,7),(4,2,9)\), checking the gcd formula for all iterate indices through each specified limit. It independently computes explicit tensor-cycle transfer matrices for small matrices and checks their traces against the formulas. These finite exercises are not exhaustive for all continuous maps, all alphabet sizes or all iterate lengths.

The mathematical proof in `RESULT.md` gives (i) a bijection between fixed-point sets of cyclically conjugate compositions, (ii) the gcd coordinate-cycle bijection for all coupled iterates, (iii) the tensor trace identity, and (iv) the signed exterior-square expansion for the two-coordinate rationality corollary. The analytical steps are essential; the finite tests are regression checks only.

Historical comparison is provisional: the full texts of one 2016 cyclic-product article and one 2014 product-zeta article could not be obtained through the checked public/authorized routes. No independent scientific audit has been performed.

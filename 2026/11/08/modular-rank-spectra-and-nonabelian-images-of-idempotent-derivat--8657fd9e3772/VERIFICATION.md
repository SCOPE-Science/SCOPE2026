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

The computational checks use the supplied self-contained `check_idempotent.py`. It reconstructs the original alternating bracket on the free class-two Lie algebra, tests the original Leibniz identity on every basis pair, tests the full operator idempotence identity on every basis vector, and computes the *full* operator rank by finite-field row reduction. For each tested pair of field and generator count, every idempotent quotient block and every possible central block was enumerated. Extension-field arithmetic for `q=4` uses the irreducible polynomial `x*x+x+1` over `GF(2)`.

Verified exhaustive cases: `(d,q)=(2,2),(2,3),(2,4),(3,2)`. The `d=2` cases are compatibility controls, not independently claimed as new. The `(3,2)` direct count is `rank0:1, rank3:1408, rank4:448`. The text labeled `FORMULA` in the output is arithmetic evaluation, not exhaustive enumeration. An additional explicit three-generator binary example takes the quotient projection of rank two and central block zero; the checker verifies a nonzero bracket of image generators outside the image, confirming both nonabelianness and failure to be an ideal. All tested direct identities and predicted exact counts passed. The symbolic proof supplies the arbitrary-dimension and arbitrary-field result; the finite tests are not a proof for infinitely many fields.

No independent audit or external certification has been performed.

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

The self-contained `verify.py` was run using Python 3 from the packaged source directory. It enumerates every prime from \(2\) through \(1777\), confirms the exact fourteen exceptional cardinalities, and verifies the eighth-power image by a second modular-exponentiation implementation. Recorded stdout is preserved in `checks.txt`.

The proof for all primes \(p\ge1783\) is mathematical, not numerical: Hasse--Weil on a smooth genus-\(21\) curve implies at least \(p-7-42\sqrt p>0\) affine solutions for each nonzero target. The finite computation covers the complementary prime range without gaps. Independent mathematical audit and verification of all possible uncatalogued prior publications have not been performed.

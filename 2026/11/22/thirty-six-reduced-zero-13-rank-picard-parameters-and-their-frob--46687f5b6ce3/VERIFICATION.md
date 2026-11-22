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

The mathematical proof uses the exact Cartier formula on a holomorphic differential basis, the discriminant nonvanishing condition, and a finite extension-field polynomial Euclidean computation. To replay the complete finite certificate, execute `python verify.py` with Python 3 and SymPy in the same directory as this file. The verifier independently expands the quartic powers modulo thirteen and checks every displayed polynomial identity and gcd, the squarefreeness and discriminant coprimality, and the Frobenius fixed-degree sequence through extension degree six.

Success is signaled by `VERIFY_OK`, together with the computed 36-point result and the degree-four/twelve splitting. This is an exact deterministic finite calculation supporting an infinite-algebraic-closure assertion, because the gcd and factorization identities are polynomial identities over a finite coefficient field. It is not a claim of independent external auditing or a determination of full Newton polygons.

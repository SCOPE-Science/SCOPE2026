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
# Verification procedure

Run `python check_biclique.py` with Python 3 and SymPy. This reconstructs all determinant and trace-difference identities symbolically and checks exact-rational finite graph inverses, pair captures, and sign patterns for several \(K_{2,n}\) values. The output reports the precise number of successful assertions. In particular, it checks formula consistency without relying on floating-point threshold comparisons. The universal proof uses strict coefficient signs and the single positive quartic root; testing finitely many sizes is not an exhaustive proof of the theorem. No independent external mathematical audit has been performed.

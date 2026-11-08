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

# Exact checks and scope

Run `python3 VERIFY_FPT.py` with Python 3 and no external packages. The checker uses sparse dictionaries of monomials with coefficients in prime fields. For every listed prime/power/variable count/level and \(\lambda=0,1\), it verifies the predicted power is nonzero in \(k[x_1,\ldots,x_n]/(x_1^{p^e},\ldots,x_n^{p^e})\) and the next power is zero. For nonzero \(\lambda\), it additionally verifies that the survivor is the unique predicted corner monomial. The checked parameter tuples are \((2,2,2,6)\), \((2,2,3,4)\), \((3,2,2,4)\), \((5,1,2,3)\), \((2,3,2,5)\). Success terminates with the exact line `CERTIFICATE_OK`.

The proof of the all-exponent, arbitrary-characteristic assertion is the Frobenius induction in RESULT.md; the limited finite enumeration cannot certify that universal quantifier. The equality of Milnor numbers follows from the leading regular sequence in the Jacobian ideal, not from the finite quotient computations. The literature comparison is nonexhaustive, and independent audit is not performed.

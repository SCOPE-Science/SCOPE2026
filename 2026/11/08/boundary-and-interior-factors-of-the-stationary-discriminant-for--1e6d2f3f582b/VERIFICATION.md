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

Exact verification uses the accompanying `verify.py`, requiring SymPy. It performs symbolic discriminant factorization for three and four distinct rational poles, checks the factor degrees and exponents, computes the scroll \(S(2,2)\) derivative-numerator discriminant using \(L(t)=1+t^2+t^4\), verifies its two quadratic and one sextic rational factors and its total homogeneous degree, and checks a nonzero four-by-four evaluation determinant. The printed terminal status is `CERTIFICATE_OK`.

These are finite symbolic consistency tests. Generic irreducibility, multiplicity one, dimension bounds and the all-scroll theorem are proved separately by the algebraic incidence argument in `RESULT.md`; finite factorization is not substituted for that proof. No claim is made for rank-constrained projector data. Independent audit is not performed.

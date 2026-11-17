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
Run `python check.py` in the extracted directory, after installing the ordinary `sympy` dependency listed in `requirements.txt` if required. The checker verifies exact polynomial identities, the full symbolic Floquet characteristic polynomial, and four cubic Jury identities, then checks twelve numerical regimes spread over the stable and unstable parameter regions. This command executed successfully when the files were prepared.

The infinite claims do not rest on those finite examples; they follow from the explicit factorization, strict positivity of the two cubic discriminants, monotonicity of the product branch, and necessary-and-sufficient Schur inequalities reproduced in `RESULT.md`. The exact neutral boundary is identified by factorization of the Floquet characteristic polynomial, not a floating-point eigenvalue tolerance. The uninspected full text of the 2002 overview remains a novelty risk. No independent audit has been performed.

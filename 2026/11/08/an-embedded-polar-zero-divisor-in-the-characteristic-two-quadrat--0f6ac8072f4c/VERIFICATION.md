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

The standalone `verification.py` depends only on Python and SymPy. Running `python verification.py` constructs the resultant by the Sylvester determinant, performs exact polynomial differentiation over characteristic two, and compares the proposed ideal generators bidirectionally with Gröbner normal forms. It also checks the local normal form and Tjurina ideal, the transverse square-ideal basis of length three, and all points of \(\mathbb P^5(\mathbb F_2)\). Its recorded output is in `verification_output.txt`. The projective primary-structure assertion and conormal identification are proved geometrically in RESULT.md and are not replaced by the finite checks. No independent external validation has been performed.

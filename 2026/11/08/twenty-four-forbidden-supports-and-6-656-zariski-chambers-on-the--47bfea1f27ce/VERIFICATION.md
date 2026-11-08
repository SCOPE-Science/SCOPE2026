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

# Verification procedure and boundaries

Run `python3 verify.py` using a Python 3 interpreter and standard library. The verifier constructs the exact negative of the fourteen-curve intersection matrix with cyclic \(I_8\), doubled \(I_2\), and four labeled torsion sections. It tests all \(2^{14}=16384\) subsets by Fraction-valued Schur complements (equivalent to Sylvester positive definiteness). It lists the twenty-four minimal failures, checks that every non-positive-definite support contains at least one, and recomputes the support polynomial from a separate inclusion--exclusion dynamic program. Its full recorded output is in `verification_output.txt`. The check concluded `ALL_EXACT_TESTS_PASSED`.

These finite checks are exhaustive for the explicit matrix. Their geometric interpretation requires the separately supplied adjunction and height-pairing argument proving the list of negative curves is exhaustive. They do not establish any claim about a different surface, or global historical uniqueness. No independent validation has been performed.

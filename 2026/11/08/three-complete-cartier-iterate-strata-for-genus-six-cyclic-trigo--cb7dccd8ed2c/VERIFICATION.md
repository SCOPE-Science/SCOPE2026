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

# Verification and limits
The proof uses a complete algebraic differential basis and symbolic semilinear Cartier relations. Its hypotheses are: algebraically closed characteristic-two ground field and monic squarefree septic with unique tame branch at infinity. Genus is exactly six. The two independent finite checks are recorded as source scripts and their execution transcript in `artifacts`.

Run `python3 artifacts/verify_rank.py` to enumerate every one of the \(4^7\) monic degree-seven polynomials over \(\mathbb F_4\), filter squarefree examples, compute Cartier matrices by direct coefficient extraction, and multiply semilinearly through degree six. Expected counts: squarefree total 12288; p-ranks 0, 2, 4 with multiplicities 768, 2304, 9216; zero rank-profile mismatches.

Run `python3 artifacts/verify_points.py` to count smooth projective points over \(\mathbb F_{2^n}\) for degrees \(n=1,\ldots,6\) on three explicit curves. Newton's identities for the zeta numerator recover the expected p-ranks 0, 2 and 4; the code checks these predictions.

Finite examples are not used to infer the general formula. The theorem does not infer full Ekedahl--Oort types or historical uniqueness from experiments or unsuccessful searches. A separate independent scientific audit has not been performed.

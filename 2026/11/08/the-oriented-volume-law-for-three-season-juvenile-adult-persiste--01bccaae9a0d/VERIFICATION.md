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

# Verification of the three-season orientation law

The proof uses a symbolic identity for \(\operatorname{tr}(B_3B_2B_1)-\operatorname{tr}(B_2B_3B_1)=\mu\Delta\), the common determinant \(-\mu^3Q\), Perron-root monotonicity at fixed negative determinant, and strict increase of the criticality polynomial. None of the finite experiments is offered as an infinite proof.

Run `python verify.py` using Python 3 and SymPy. The script tests the universal trace and determinant identities in symbolic arithmetic, checks the stated exact rational matrices and threshold signs, computes the six temporal orders independently in rational arithmetic, and exercises 1,000 generated rational instances of the orientation law. Parameter restrictions for the theorem are positive fertility and both survival coordinates strictly between zero and one.

There is no independent scientific audit or independent validation. The supplied executable is a reproducibility aid to the algebraic proof, not a certificate for the entire published mathematical literature.

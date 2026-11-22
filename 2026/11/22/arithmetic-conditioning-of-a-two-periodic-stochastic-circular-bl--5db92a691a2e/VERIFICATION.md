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

# Reproducibility and limitations

Run `python verify.py` using Python 3 with NumPy and SymPy. The script builds the periodic blur matrices directly, without using the Fourier blocks to construct them, and compares dense singular values with those computed from Fourier blocks and the closed spectral formula. It also checks direct determinants numerically and, in the rational \(lpha=1/3\) example, checks exact determinants and nullities using rational SymPy arithmetic. Approximate sharp-constant checks are performed for two irrational phases at four sample dimensions. At review, the checker printed `VERIFY_OK 242`.

The direct all-size determinant, nullity and sharp asymptotic statements are proved mathematically in RESULT.md. Testing finite sizes is not a proof of those universal quantifiers; in particular, floating-point tests cannot establish irrationality, singularity for all dimensions, or an asymptotic Diophantine lower bound. No independent mathematical audit or validation has yet been performed. Historical novelty is a best-knowledge literature assessment with the residual access risks stated in REVIEW.md.

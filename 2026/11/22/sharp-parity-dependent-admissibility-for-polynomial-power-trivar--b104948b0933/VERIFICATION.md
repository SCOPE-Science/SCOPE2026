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

# Verification and reproducibility

`check_admissibility.py` is a self-contained test program requiring SymPy and SciPy. Execute `python check_admissibility.py` in the same directory. The recorded execution passed 118 assertions, including twelve symbolic density identities and eighty supplementary three-variable optimization diagnostics across a range of exponents and shape parameters.

The mathematical proof in `RESULT.md` supplies the necessary quantifiers and all-support bounds: the derivative factorization; \(B_\theta([0,1])=[-r_\theta,1]\); the parity-sensitive exact range of \(D_m\); the unique critical root for even powers; and equivalence of density positivity to admissibility. These ingredients, not a finite grid or optimization solver, establish the theorem. The threshold \(\theta_2\approx0.1535284495278\) is a numerical approximation to a uniquely defined root, not a standalone numerical certificate. No independent audit has been carried out.

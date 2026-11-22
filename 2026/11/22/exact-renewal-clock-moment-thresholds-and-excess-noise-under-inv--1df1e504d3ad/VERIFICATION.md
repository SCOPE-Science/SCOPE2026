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

# Verification of first-reset clock moment thresholds

The exact proof is given in `RESULT.md`. The included `verify.py` computes symbolically: (i) the Neumann first-moment backward equation; (ii) the Green integral for the second moment; (iii) the variance ratio; and (iv) its negative derivative. An independently assembled finite-difference approximation of the killed backward equations on \([b,150]\) checks sample moments for \(\eta=4,5,8\), with imposed absorption at the far numerical boundary. These checks were executed successfully.

The finite-domain values systematically underestimate their infinite-domain targets and are used only as consistency evidence. For all \(m\ge1\), the infinite-domain threshold itself follows from the rigorous Brownian-scale lower bound plus positive supersolution comparison, rather than numeric computation. No evidence of independent validation is claimed.

Run `python verify.py` with SymPy, NumPy, SciPy. The script has no external data dependencies.

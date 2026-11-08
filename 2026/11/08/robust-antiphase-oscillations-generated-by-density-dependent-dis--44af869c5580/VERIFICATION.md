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

The standalone `verify.py` uses exact rational arithmetic to reconstruct the orbit, both one-step derivatives, the second-iterate derivative, the strict infinity-norm contraction, and the instability eigenvalues at the symmetric equilibrium. The output was `VERIFY_OK: exact cycle, 2-step contraction, symmetric instability, migration bounds and rational identities`.

Finite rational test points check the dispersion bounds and scalar identities only as a software cross-check. The analytic arguments in `RESULT.md` establish admissibility on the entire nonnegative half-line, global convergence with constant dispersal for all nonzero initial states, and local persistence of the nondegenerate orbit under perturbations.

The originality comparison is best-knowledge only: the full original 2024 model paper was inspected in its web-readable mathematical text; the 2018 paper on a related active/refuge system was not available in full text. There is no independent external audit.

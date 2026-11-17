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

Run `python check.py` with installed NumPy, SciPy and SymPy. The checker reconstructs the exact tangent-half-angle polynomial, asserts the coefficient formulas algebraically, finds the two neutral return-map folds by shooting from their symmetry-pinned phases for four integers \(k\in\{-2,-1,1,2\}\) and three perturbation strengths \(0.1,0.05,0.025\), and checks four pairs of reciprocal Floquet multipliers.

The observed terminal marker was `VERIFY_OK symbolic_projective=1 quadratic_coefficients=1 fold_cases=12 reciprocal_pairs=4`. For \(k=1\), the widths at perturbations \(0.1,0.05,0.025\) were approximately \(1.994004349813\), \(1.998479609051\), and \(1.999618519995\), consistent with quadratic contraction. For \(k=-1\), the corresponding widths were \(2.000552890388\), \(2.000138723015\), and \(2.000034711866\), consistent with quadratic expansion. Reciprocal multiplier products had errors below \(10^{-9}\) in the four tested cases.

These are **finite corroborative checks**, not exhaustive verification of all parameters or proof of the infinite-dimensional statements. The analytic arguments in `RESULT.md` establish the Möbius restriction, nondegenerate folds, even-parity, quadratic coefficients, and global local-amplitude locking census. The source model and historical novelty require independent mathematical review.

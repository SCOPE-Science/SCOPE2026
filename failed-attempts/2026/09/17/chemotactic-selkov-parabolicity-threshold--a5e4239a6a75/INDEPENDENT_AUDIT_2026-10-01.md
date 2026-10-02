---
audit_date: 2026-10-01
status: failed
---

# Scientific audit

## Final claim

For the chemotactic Selkov system at its positive homogeneous equilibrium, \(Q=D_1D_2-\xi_1\xi_2 b^2/(a+b^2)\) is the normal-ellipticity threshold; if \(Q<0\), one Fourier branch grows as \(c|k|^2+O(1)\), making the linearized Sobolev evolution ill-posed.

## Correctness — PASS

The principal diffusion matrix and determinant were reconstructed directly. With positive trace, \(Q<0\) forces one negative diffusion eigenvalue. Independent numerical checks of representative parameters verified that the unstable eigenvalue of \(R-|k|^2\mathcal D_*\), divided by \(|k|^2\), converges to the negative of that diffusion eigenvalue. The Sobolev unboundedness conclusion then follows from single Fourier modes.

**Evidence:** package RESULT.md; M. Karmakar and A. Basu, arXiv:2609.01159

**Residual risk:** The exact degenerate case \(Q=0\) is not a complete well-posedness classification, as the record already states.

## Originality — FAIL

The central claim is a direct specialization of standard normal-ellipticity/backward-parabolic theory to a displayed 2-by-2 diffusion matrix. The source paper itself already identifies the same finite chemotaxis threshold through divergence of the preferred wave number. Computing the determinant and observing that a negative diffusion eigenvalue yields \(+c|k|^2\) growth is a textbook implication rather than an independent original theorem under the required bar.

**Equivalent formulations.** The package's 'reclassification' is the standard principal-symbol formulation of the same high-frequency behavior.

**Broader coverage.** The final claim is mechanically implied after substituting the model coefficients.

**Exact database or table.** The decisive coverage is theorem-level, not tabular.

**Claim versus prior implication.** This implication covers the scientific headline even though the exact wording 'normal ellipticity' is absent from the source.

**Checked sources:** https://arxiv.org/abs/2609.01159; https://doi.org/10.1016/j.nonrwa.2023.104042; https://doi.org/10.1155/jama/6835155

**Residual risk:** No correctness risk was found; the rejection is scientific coverage, not transport failure.

## Value — FAIL

The computation is useful as a warning about interpretation, but the final theorem is a short standard principal-symbol/eigenvalue deduction from a threshold whose high-frequency divergence the source already reports. Under the required value bar, that is too close to a textbook rephrasing to qualify as a substantive new mathematical contribution.

**Residual risk:** A substantially new regularized-model theorem or nonlinear well-posedness boundary could be valuable, but it is not the audited final claim.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.

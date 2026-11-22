---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For m>=2, weights and Huber cutoff strictly positive, the clipped-score g_x(c) is continuous monotone with compact closed zero interval; midpoint selection is continuous, translation equivariant, piecewise affine. Unique-root chambers have gradient q_i=w_i/W_I on unsaturated I with strict signed feasibility |sum_out s_i w_i|<W_I. On flat-root chambers equal masses of positive/negative saturated residuals produce midpoint gradient (e_l+e_r)/2; a feasible two-inlier state bounds it by Q. In root-relative coordinates output matrix I-1 q^T has column sums 1+(m-2)q_j; integrate the finite piecewise-affine derivatives along segments. The maximizing feasible state has a strict finite witness with perturbed sole leaf, so sharpness attained; uniform parity and arbitrarily small even-weight increase are direct signed subset cases. Independent rational checks covered m=2..10 and weighted witnesses, not all reals. For m=2 baseline coefficient is one, so the even discontinuity is only claimed m>=4.

## originality

PASS

The exact signed subset feasibility functional Q(w), induced two-input star-variation norm 1+(m-2)Q, and discontinuity from uniform even masses to arbitrarily slightly perturbed masses survive statement-level comparisons with prior Huber M-estimation and star variation literature. Score linearization itself is standard; no unconditional global-priority guarantee.

## value

PASS

A discontinuity in an exact robust location filter operator norm at equal masses is a substantive stability boundary: it separates balanced flat-score behavior from singleton-inlier amplification and identifies attainable worst perturbations. This is not merely a derivative reparameterization or a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.

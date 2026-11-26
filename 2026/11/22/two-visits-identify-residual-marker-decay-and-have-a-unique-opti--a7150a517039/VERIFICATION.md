---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the stated latent-class model, put s=1−ψ, a=α and b=a exp(−δt). The assay outcomes are conditionally, not marginally, independent (the opening word 'independent' should be read in the sense specified in the assumptions). With U=E[q−Y0], V=E[q−Yt] and K=E[(q−Y0)(q−Yt)], conditioning gives U=s(q−a), V=s(q−b) and K=s(q−a)(q−b)>0. Thus s=UV/K and a,b,δ follow uniquely. At one fixed date even with ψ held fixed one can vary δ and keep α exp(−δt) fixed (at date 0, δ simply drops out). At q=1 the three probabilities P(Y0=0), P(Yt=0), P(00) have Jacobian determinant of magnitude s²(1−a)(1−b) in (ψ,a,b). They are unit-determinant linear coordinates on three cells; the cell-coordinate Fisher determinant is the reciprocal of the product of all four cell probabilities. The additional squared Jacobian is (tb)², giving D(t)=s t²/[ψ exp(δt)+s a²]. Its log derivative in z=δt is 2/z−1/(1+C exp(−z)), C=sa²/ψ>0, strictly decreasing from positive to negative with D vanishing at both endpoints. The root is z=2+W(2C exp(−2)); monotonicity and the rare-prevalence expansion follow from W being increasing and W+log W=log(2C exp(−2)). An independent exact moment check recovered (ψ,a,b)=(2/7,3/5,1/4) for q=7/8 and q=1; independent Newton iteration gave z=2.291275616944311 at the stated example. The frozen checker was inspected, not executed; the conclusion rests on the derivation, not finite tests or field validation.

## originality

PASS

The two-component likelihood and calibrated moment inversion are standard algebra, not independently compelling novelty. The supported distinct benchmark is the exact unique joint-information optimum and its dependence on prevalence and decay in this specific two-date experiment. The strong same-day comparator has a different constrained design and neither states nor implies this benchmark.

## value

PASS

The benchmark quantifies a real design tradeoff: visits too close give no decay leverage, and at large gaps empty-site positives become too scarce. The optimal separation is always above two decay times and grows logarithmically at rare occupancy, a parameter-sensitive answer that a fixed 'wait one decay time' rule cannot supply. It is an exact mathematical reference for the specified idealized model, not a field recommendation without calibrated q, an appropriate detection law, conditional independence and a cost model.

The dated certificate retains the supplied scientific assessment, sources and limitations.

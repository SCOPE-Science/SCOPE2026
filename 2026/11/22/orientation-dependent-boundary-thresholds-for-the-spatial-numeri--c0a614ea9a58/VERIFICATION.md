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

Taking coordinate moduli reduces each radius to the respective positive functional: the forward edge term is u_j u_(j+1)^(p−1), the backward term u_j^(p−1)u_(j+1). Weighted Young at ratio r has equality exactly when u_(j+1)=r u_j. Summing gives residual coefficients t−(p−1)/(pr) and t−1/(pr^(p−1)) on u₀^p respectively. Taking r=1 gives the plateau upper bound, matched by arbitrarily long constant blocks beyond the defect; equality would force a nonzero constant sequence in ℓ_p, including at either threshold. Above threshold choose r<1 to cancel the residual coefficient. The normalized geometric sequence gives equality and the individual nonnegative Young deficits force that same sequence of moduli for every maximizer. The positive nonzero diagonal term pins the argument of each nonzero edge term to zero in the complex triangle equality, so all phases coincide. The exponent-conjugate orientation symmetry is an independent check: mapping u_j to u_j^(p−1) takes the forward positive functional at p into the backward one at q, including normalization. Both supercritical formulas have form f(t)=t+(1−a)(a/t)^(a/(1−a)), with a the respective threshold. Then f(a)=1, f'(a)=0, and f''(a)=1/(a(1−a))=p²/(p−1). Both orderings of the thresholds and the meeting at p=2 follow. For the essential disk, translated phase-ramped normalized blocks are weakly null and give every point of the unit circle as a limit on either shift; convexity gives the disk and the unperturbed norm gives the reverse inclusion. The rank-one diagonal is compact and preserves the essential range, as supported by the inspected primary theorem.

## originality

PASS

The distinguished content is the non-Hilbert exact radius and equality/transition classification for the scalar diagonal defect. The Hilbert law and essential disk ingredients are covered, and the two orientations are dual presentations at conjugate exponents, not independent novelty claims. The off-diagonal edge theorem is not this diagonal family.

## value

PASS

The point potential is a natural test for when a compact perturbation changes the ordinary spatial radius without changing the essential range. Outside the Hilbert case the sharp threshold is orientation dependent at fixed p; exact radii, nonattainment versus a unique extremal shape, and the critical curvature quantify that effect. This is more than identifying the previously known Hilbert specialization or an upper bound from Young's inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.

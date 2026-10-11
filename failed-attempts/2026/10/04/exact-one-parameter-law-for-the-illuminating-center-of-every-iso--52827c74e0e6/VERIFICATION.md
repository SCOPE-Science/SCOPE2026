---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

O'Hara's uniqueness theorem and reflection symmetry place the center on the altitude. Finch's accessible statement of Shibata's theorem says the three central-angle/subtriangle-area ratios are equal. Since their numerators sum to \(2\pi\) and denominators to the triangle area, the base subtriangle of area fraction \(q\) must subtend angle \(2\pi q\). Direct isosceles geometry gives the same angle as \(2\arctan(1/(\lambda q))\), hence \(\lambda q\tan(\pi q)=1\). The left side is strictly increasing in q on \((0,1/2)\), and implicit differentiation and elementary tangent expansions give the monotonicity and asymptotics. A fresh bisection check over \(\lambda=10^{-3},0.1,1,10,10^3\) reproduced the defining equation and both asymptotic regimes.

## originality

FAIL

The location equation is an implication-level specialization of prior results rather than a new theorem under the audit's strict originality rule. O'Hara supplies uniqueness of the relevant center for convex bodies, so reflection forces the isosceles center onto the symmetry altitude. Finch publicly records Shibata's all-triangle characterization \(\angle APB/|APB|=\angle BPC/|BPC|=\angle CPA/|CPA|\). On an isosceles triangle, substituting the altitude coordinate and the elementary area fraction immediately yields \(\lambda q\tan(\pi q)=1\). The monotonicity and endpoint asymptotics are routine one-variable consequences of that equation. Thus absence of the formula verbatim does not preserve originality.

## value

FAIL

The isosceles family is natural and the resulting formula is a useful exposition, but after the published all-triangle angle/area characterization and uniqueness are imported, the remaining work is a symmetry substitution followed by elementary one-variable calculus. Under the common value bar this is a routine specialization rather than a separate structural gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.

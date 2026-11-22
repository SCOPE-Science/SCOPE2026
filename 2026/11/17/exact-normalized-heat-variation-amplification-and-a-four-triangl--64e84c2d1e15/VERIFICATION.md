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

For a friendship graph of m>=1 triangles with one hub and Q=D^-1 A-I, hub-vs-average and antisymmetric blade modes decay as e^(-3t/2), while blade-mean differences decay as e^(-t/2). The exact hub-relative heat values follow by solving this linear ODE. The graph coarea/layer-cake identity reduces arbitrary signed inputs to binary superlevel cuts; complementing excludes the hub and the triangle disjoint-support decomposition has additive input edge variations. Each triangle cuts either one vertex or both; the full peripheral-pair ratio exceeds singleton by ((m-1)/m)(e^(-t/2)-e^(-3t/2)), giving exact N_m(t)=2(m-1)/m e^(-t/2)-(m-2)/m e^(-3t/2), attained by a pair cut. Differentiation gives strict contraction through m=4, unique transient peak for m>=5, and limiting sharp unattained (4/3)sqrt(2/3). Own direct matrix expm and exhaustive hub-free cuts m=1..6 at three positive times match formula within 1e-10; all-size proof is analytic.

## originality

PASS

Best-of-knowledge originality after actual mathematical implication comparisons with primary literature and published Resultary corpus; no located stronger theorem implies the entire exact final claim. Distinct known antecedents and historical risks are documented.

## value

PASS

An exact all-time operator seminorm, a sharp four-blade stability boundary, explicit attained worst-case cut and a global unattained envelope for a natural irregular graph family connect normalized heat dynamics with graph BV geometry. The nonexpansivity threshold differs from neighboring graph norms and is a substantive classification useful for heat-flow stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.

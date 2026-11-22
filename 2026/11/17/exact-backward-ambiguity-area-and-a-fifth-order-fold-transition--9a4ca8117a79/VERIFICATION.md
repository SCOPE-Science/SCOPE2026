---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Solve x(2−x−y)=u, with 0<u<1, to get y=2−x−u/x on x∈[1−sqrt(1−u),1]. The target predator coordinate h_u(x)=(2−x−u/x)(A+γx) has h″=−2γ−2Au/x³<0; derivatives at left/right boundary are positive/negative, proving a unique strict interior fold maximum, hence exactly two interior antecedents iff (1−u)(A+γ)<v<h_u(x*). Parametrize fold by t=x, y_c=2(1−t)(A+γt)/A, u_c=t²(1−2γ/A+2γt/A), t∈[max(0,1−A/(2γ)),1]. Integrate (v_c−v0)du_c/dt to obtain branches (5A²−5Aγ+2γ²)/(30A) for γ≤A/2 and A²(A²−10Aγ+40γ²)/(480γ³) for γ≥A/2. Their analytic expression difference is (2γ−A)^5/(480Aγ³); first four jets match, fifth difference 64/A⁴. The double-region ratio at transition is 2/17; explicitly checked both algebraic predecessors at r=1/2,gamma=1/3. I independently differentiated and integrated the polynomial fold integrand with SymPy and numerical quadrature for parameters on both sides; the continuum concavity proof, not finite samples, establishes all fibers.

## originality

PASS

The backward-fiber target-area calculation and its fifth-order fold/boundary regularity transition are not furnished by inspected same-model forward-dynamics literature or general noninvertible-map fold analysis. The 2019 two-preimage study has genuinely different prey/predator equations; no algebraic parameter or topological implication supplies this formula.

## value

PASS

Exact noninvertibility/observational ambiguity area is a natural invariant for ecological discrete maps. The onset of an interior fold from a different boundary stratum produces a verified, nontrivial C4/not-C5 parameter transition and precise double-observation fraction even in a forward-attracting regime; these are meaningful geometric facts, not a textbook negative check.

The dated certificate retains the supplied scientific assessment, sources and limitations.

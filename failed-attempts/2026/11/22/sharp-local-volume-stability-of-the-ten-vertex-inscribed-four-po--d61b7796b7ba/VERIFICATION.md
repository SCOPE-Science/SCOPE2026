---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The 25 tetrahedral facets of the orthogonal free sum have strict slack at all nonincident vertices, so each persists with its orientation. Every ridge of these retained facets is already paired and the facet adjacency graph of a convex polytope is connected; thus there is no missing facet. The interior origin also persists, giving the sum of signed simplex determinants divided by 24. For the angular contribution, an in-plane component has angle shift t*alpha_i+O(t^3) and radius 1-t^2*||u_i||^2/2+O(t^3). Expanding adjacent wedge areas cancels the angular first-order terms and gives the five-cycle Laplacian. The mixed derivative of the first cycle is sum_i u_i wedge (a_{i+1}-a_{i-1})=2 sin(theta) sum_i u_i wedge J a_i, so only its first-harmonic projection U contributes; similarly only W contributes for the second cycle. The mixed cross sign and scale follow by expanding det([[I,tW],[tU,I]])=1-t^2 tr(UW)+O(t^4), multiplied by the product (5 sin(theta))^2. With the sphere normalization the off-plane loss is exactly the square in RESULT.md; its antisymmetric mixed directions are orbit directions. The factors 5 sin^2(theta)/48 on the angular Laplacian eigenvalues and 5 sin^2(theta)/24 and 5 sin^2(theta)/12 on residual and symmetric mixed modes give precisely the listed half-Hessian bands and multiplicities 6,4,12,4,4. After nearest-orthogonal alignment the displacement is orthogonal to the orbit tangent, so its leading sphere-chart tangent displacement is normal and its squared norm is asymptotic to D. The uniform quadratic expansion and the first angular harmonic give the lower estimate and its matching limiting ratio. These are analytic checks, independent of the recorded numerical tolerances.

## originality

FAIL

A distinct indexed record already states the central same-configuration sharp labelled-orbit coefficient 25/192 and the complete five-level 30-dimensional spectrum with the same six-dimensional rotational kernel and usual-Hessian gap 25/96. The latter gap is exactly twice the frozen half-Hessian gap. This demonstrates claim-level overlap and the frozen record establishes no distinct scientific increment over that coverage. This conclusion is about insufficient demonstrated distinctness, not a determination of chronology, authorship, or proof duplication. The full alternative spectrum table was not accessible; no claim of a verified entry-by-entry table match is needed to identify coverage of the sharp theorem and the complete spectrum of the same operator.

## value

PASS

As a mathematical result the sharp quotient and complete mode decomposition answer a natural quantitative question at a volume maximizer. They distinguish the softest angular perturbations from transverse directions and rule out other infinitesimal flat modes; qualitative uniqueness alone cannot do this. This assessment is of the mathematical content, not an assertion of additional value from republishing an overlapping result.

The dated certificate retains the supplied scientific assessment, sources and limitations.

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

For z=β exp(−r), f′=(z−c)f and f″=[(z−c)²−z]f. The larger curvature root is B(c) and the smaller is below c, giving strict concavity on the rising branch if c<β≤B(c) (including strict interior concavity at threshold). For β>B(c), N(r)=rf′(r)−f(r)+f(0) has derivative rf″(r); it grows from zero to its positive inflection-point value and decreases to f(0)−f(r*)<0 at the mode. This proves the unique positive tangent on (0,r*). The 0-to-t support line contacts f only at 0,t, and the envelope then follows the strictly concave increasing branch before joining the horizontal plateau. The Jensen bound for every finite-first-moment law is sharp: the chord's contact set forces the stated weights, including collapse to the unique point mass at t, and an interior strict-branch tangent forces a point mass. The unique pointwise maximizer forces attainment only by its point mass at the modal mean; larger exact means can approach the supremum with mass (m−r*)/(M−r*) at M→∞, but not attain it. The same argument with mode 0 gives Case I. A nondegenerate mixture requires strictly β>B(c) and 0<m<t. Inspected the finite-grid script and its limits. A separate example calculation gave t≈0.63299296892124, mixture value ≈0.03615418508760 and deterministic value ≈0.03455499616969; the proof, not this check, establishes global uniqueness and nonattainment.

## originality

PASS

Pass for the explicit phase boundary, tangency and optimizer/nonattainment classification of this specified survival curve with exact first moment and unrestricted laws. Neither concavification nor the biological concept of dimorphic dispersal is new in isolation. The strongest inspectable catalogue claims optimize different objects or objective functions, and the focused exact-form search located no matching prior. The close ecological papers were not all inspectable at theorem or equation level; that remaining risk does not establish prior coverage.

## value

PASS

The two independent hazards give a simple benchmark for a natural question: can heterogeneity improve expected establishment at the same transport budget? The answer is a sharp parameter/mean classification with the whole optimizer, not an arbitrary profitable two-point example. The nonattainment regime also identifies a meaningful difference between an exact mean and a mean cap or bounded habitat. Value is mathematical in the stipulated model; no empirical or evolutionary prediction is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.

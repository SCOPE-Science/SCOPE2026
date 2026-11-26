---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Compared all 48 payoffs and the P,I,R,C order against the source. Rechecked the endpoint symmetric tangent forms in integer scaling: the leading minors of 200H are (-50,1804,-94526), (-44,1447,-64774), (-48,1167,-45550); Sylvester's criterion and convexity give the strict tangent bound on both segments. To replay the polynomial identities without a symbolic solver, multiply each normalized candidate by its displayed denominator, scale A by 100, and test normalization, equal resident payoffs and the excluded-payoff numerator at t=-1,0,1,2,3 with integer arithmetic. The resulting identities have degree at most four, so all five exact equalities certify each identity; the excluded numerators in this scaling are 20g_a and -g_b for the respective face denominators. On [0,1] both full-candidate denominators and all nontarget numerators are negative by termwise bounds; for example the unscaled buffered I expression is at most 9+687-720=-24. The acid face denominator is at most -677 with three negative resident numerators, and buffered face denominator is at least 331 with three positive resident numerators. Both cubics have positive derivative and opposite endpoint signs. Root bisection gives 0.256901888893311 and 0.994745404575664. At and above each root the supported face satisfies the Nash inequality, with equality for the excluded phenotype only at the root. The tangent inequality guarantees unique Nash selection, not absence of other rest points on invariant boundary faces. Relative entropy on the selected support decreases at least as fast as c_t times the squared distance, giving integrability of that distance squared; bounded speed gives uniform continuity and hence convergence from every strictly positive start. Time averaging the limiting log-abundance derivative proves the claimed decay. Substitution at t=1 gives (0,250,232,195)/677 and (100,49,0,185)/334 with losses 173/3385 and 1/3340. At threshold the target is already absent from the limiting equilibrium and the positive exponential rate does not apply there. Replay references: frozen RESULT.md lines 36–129 and verify.py, inspected but not executed; no numerical trajectory is needed for the convergence proof. The parameter is held fixed during each trajectory.

## originality

PASS

The published game and strictly stable-game convergence mechanism are prior. The supported contribution is the exact support and decay classification along the two line segments defined using those published matrices, not a new general stability theorem or biological dose-response law.

## value

PASS

Straight-line continuation connects already used endpoints and compares not merely their equilibria but how long coexistence persists and when it loses one coordinate. The all-interior convergence certificate and exact exponent distinguish a robustly negative acid-path invasion gap from the very weak buffered endpoint margin without inferring either from finite run time. This is a mathematically motivated worked phase diagram of a phenomenological model, not measured pH thresholds, calibrated predictions, or a treatment recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

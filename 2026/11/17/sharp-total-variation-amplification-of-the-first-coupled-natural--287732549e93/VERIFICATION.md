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

The natural cubic interpolant on knots 0,1,2,3 has M0=M3=0 and a 2×2 interior-curvature matrix [[4,1],[1,4]] with exact right sides 6 second differences. Since the spline operator is linear and preserves constants, data differences decompose uniquely into three binary step inputs; the exact induced variation norm is maximum of their three output variations. For the central step (0,0,1,1), M1=2,M2=−2 and derivative polynomials u²−1/3,2/3+2u−2u²,(1−u)²−1/3 give total variation 1+8/(9sqrt(3)). The reflected outer steps have exact smaller gain 133/125+4sqrt(3)/135+52sqrt(39)/3375. Thus all real 4-point data satisfy the sharp inequality, central step saturates; the same norm bounds two-input differences by linearity. Independently checked rational curvatures, roots and integral variations plus 200 random rational inputs.

## originality

PASS

The first coupled natural-spline discrete-to-continuous variation constant is not stated in the inspected natural-basis estimation primary manuscript or earlier three-knot positivity-defect record. A highly relevant same-day Resultary finding about *optimal symmetric four-knot spacing* cites the equispaced baseline but does not establish chronological priority or complete statement coverage without its inaccessible full text; the original exact constant is assessed best-of-knowledge, with explicit priority risk.

## value

PASS

Four knots are the smallest natural cubic interpolation case with two coupled internal second derivatives; the precise sharp variation gain and extremal step are a motivated stability invariant used to compare interpolation schemes and mesh design, not merely a random small-instance table.

The dated certificate retains the supplied scientific assessment, sources and limitations.

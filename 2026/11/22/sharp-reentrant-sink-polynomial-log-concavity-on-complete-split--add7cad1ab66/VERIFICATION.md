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

For a prescribed independent set J of sinks, all incident edges are forced, and the number of allowed residual choices is the number of orientations of G−J (acyclic orientations of G−J in the acyclic case, since no cycle can use J). Expanding z^s=(1+(z−1))^s verifies both enumerators independently: J is either a subset of the independent class or a single clique vertex. In the acyclic case, residual counts for those two types are k!(k+1)^(r−|J|) and (k−1)!k^r; the ordered clique admits exactly one cut per choice of attachment position for an independent vertex. In the unrestricted case the residual counts are 2 to the number of residual edges. Summing gives the displayed formulas. For F=(z+A)^r+C(z−1), a₀ falls and a₁ rises relative to the scaled binomial, so only a₂²≥a₁a₃ can fail; its difference is [r(r−1)A^(r−3)/12][r(r+1)A^(r−1)−2(r−2)C]. This handles r≥3 with r=1,2 automatic. At k=6 the acyclic difference criterion factors as (r−3)(r−8)≥0; at r=3 the unrestricted condition is k≤24(1−2^(−k))², true for 2≤k≤23 and false thereafter by the stated bounds. After translation, y^r+Cy−C(A+1) is strictly increasing for odd r, and strictly convex with negative value at y=0 and positive ends for even r. Nonnegative original coefficients and the constant terms locate the real zeros as stated, including the quadratic's positive discriminant. `python /workspace/replay_checks.py 3` independently deduplicated orientations induced by topological orders and directly counted all orientations in seven finite cases; the proof covers all sizes.

## originality

PASS

Credit the sink-set expansion, the resulting routine complete-split enumerator specializations, the diamond case, and the reported claw-free theorems to existing methods or results. The supported distinct claim is the exact coefficient-shape classification, including failure and recovery of log-concavity without a corresponding recovery of real-rootedness, and the comparison between the two orientation laws. The judgement concerns that classification, not priority for the definition or general formula.

## value

PASS

A canonical chordal family separates two common coefficient properties in an exact and reusable way: for clique size six, acyclic log-concavity fails for a finite interval and returns even though real-rootedness cannot return. The two-parameter boundaries and acyclic versus unrestricted comparison are more informative than the enumerator specialization or a single counterexample alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.

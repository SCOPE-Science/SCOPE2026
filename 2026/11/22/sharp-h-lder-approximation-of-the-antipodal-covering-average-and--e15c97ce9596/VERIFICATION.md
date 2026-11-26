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

Kantorovich–Rubinstein duality and interchange of two suprema give exactly the worst fiberwise W1 distance. Each label's distance to the first tracked sheet has complementary endpoint values, so it hits the midpoint and contributes at least φ(1/2)/m in any plan. For m=2k, a minimizing assignment can be taken integral because two fractional entries in the capacity-k polytope can be perturbed. Distinct k-subsets have sums of costs adding to at least two by the antipodal triangle inequality. If every minimal cost in unnormalized units were below one, the unique minimizing subset would be constant by continuity, but it changes to its complement at the glued endpoints. The alternating single-label flips glue correctly: for odd m the stationary labels are balanced and the moving atom is split, with concavity bounding the cost by φ(1/2)/m; for even m the moving atom can fill the single vacancy for at most 1/m. This includes m=1,2. Substitution of s^α and comparison of the two exact constants give the stated threshold and the three-versus-four example.

## originality

PASS

Credit the exact linear-cost parity law and the sheet-interchange obstruction as antecedents. The supported addition is sharp dependence on the concave metric, in particular the odd constant φ(1/2) and the resulting Hölder term-count reversal. The available strongest matching statement is for arclength; it does not give the transformed odd formula. The unchanged even constant is not credited as independent novelty.

## value

PASS

For a natural nontrivial double cover, this gives exact performance of continuous equal-weight approximants in a metric-sensitive norm. It identifies a qualitative reversal that the linear metric does not exhibit: even one additional sample can worsen the best approximation, with an exact exponent threshold. That effect is meaningful only with the fixed Equal-weight constraint, and is not a claim about approximation by arbitrary convex mixtures.

The dated certificate retains the supplied scientific assessment, sources and limitations.

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

Re-audited /workspace/repairs/1/RESULT.md and its narrowed slogan. The known area identity uses the intrinsic metric of the sum-zero hyperplane and counts two opposite facets per bond. A shore's incidence-tree Gram determinant is its order, so the geometric contribution is 2 sqrt(j(n−j)) times the shore tree counts. One-bridge cuts give multiplicity ℓ, and cycle-edge pairs give one. For ℓ≥4 every cut contributes at least F1 and the concave quadratic ℓ(2n−ℓ−1) is bounded below by 4(2n−5) (endpoint check includes ℓ=n at n=5). That area bound exceeds A2 since (2n−4)F1−2(F2+F3)>0. For a triangle, the known rooted-tree minimum is attained by (n−2,1,1). A non-leaf attachment has a bridge cut of size 2 through n−3, adding at least 6(F2−F1) to the benchmark; strict concavity makes this larger than 2(F3−F1). Once all branches are leaves, the sorted triple (n−3,2,1) majorizes every remaining triple, so strict concavity gives the unique second graph, including n=5 when the largest entries coincide. Substitution gives the stated A2 and strict positive exact gap. The n=4 background values were also checked. In independent finite diagnostics, generator-subset Gram volumes (not a cut enumerator) gave first and second levels 21.320508076 and 21.856406461 for n=4; 36.898979486 and 37.797958971 for n=5; and 54.850349754 and 56.378213799 for n=6. Replay: python3 /workspace/branches/independent_checks.py (graph_check). Finite enumeration is corroboration, not the all-order proof; the supplied checker was not executed.

## originality

PASS

Pass for the repaired claim only: the second distinct surface-area level, unique graph and sharp gap over all unicyclic graphs. The frozen package presented the all-unicyclic formula as a separate finding without credit to an earlier exact equivalent, and its triangle minimum is an exact fixed-cycle specialization of that same predecessor. Those pieces do not pass as original contributions. The replacement RESULT and slogan retain these facts only as a credited benchmark and method, and restrict the new assertion to the second level. The earlier result does not classify the nonminimizers or compare their least area with all longer cycles and non-leaf attachments. This is not a correctness rejection of the frozen formulas.

## value

PASS

The repaired claim answers a natural quantitative stability question for the Euclidean area: exactly how much area must increase under departure from the globally optimal unicyclic shape, and what achieves that least departure. It separates genuinely different deformations: a cycle-length change and an attached tree both cost more than moving one leaf. This is a sharp all-order discrete rigidity threshold for zonotopes of the same generator count, and at the two extremal triangles the same intrinsic volume, not a rederivation of the first-level benchmark or a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.

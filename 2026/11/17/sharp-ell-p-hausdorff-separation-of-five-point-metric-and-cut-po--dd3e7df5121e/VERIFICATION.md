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

Laurent (1996, §4.3) supplies the requisite complete 32-vertex MET_5 classification: 16 cut vertices and 16 switching-equivalent fractional vertices a_S=(2/3)1−δ(S)/3. A maximum five-vertex cut has six edges; averaging the ten maximum-size cuts gives b_∅=(3/5)1∈CUT_5. Every cut mixture has total edge sum at most 6, while ∑a_∅=20/3; Hölder enforces distance ≥(2/3)/10^{1−1/p}=10^{1/p}/15. Residual a_∅−b_∅=1/15 on all ten coordinates attains it for all p; switching transfers to all sixteen a_S. Convexifying nearest approximants to every MET vertex supplies global upper bound. For finite p>1 strict convexity, and for p=1 opposite coordinate signs of any two distinct switched residuals, enforce precisely those sixteen farthest vertices. Support-function/Hölder duality then gives 16 normal directions c_S=10^(−1/q)(1−2δ(S)) for p<∞, with no p∞ uniqueness claim. Independently checked all 16 rational projection normal inequalities and exact squared Euclidean gap 2/45. The full vertex exhaustiveness is genuinely from Laurent 1996, not floating-point census.

## originality

PASS

The 32-vertex list, metric switchings and cut framework are fully credited to Laurent (1996). The proposed new content is exact all-ℓp distance and the complete primal/dual extremizer classification. Deza–Laurent–Poljak (1992) investigates triangle facets and cut/metric relative positioning, and Deza–Dutour Sikirić (2017) generalizes cut/metric polytopes; the full formula is not found in the material read. The max-cut relaxation alias is explicitly equivalent and not claimed as a separate novelty. Older integrality-gap literature may already imply the formula and remains a priority risk.

## value

PASS

MET_5 is the first complete-graph metric relaxation not equal to CUT_5. The all-norm sharp Hausdorff and support gaps, simultaneous nearest cut mixtures, and complete finite-p equality sets quantify a natural global max-cut/metric relaxation defect at the smallest nontrivial order. It is independently useful even though the 32-vertex classification is already known; it is not merely re-enumerating the vertices.

The dated certificate retains the supplied scientific assessment, sources and limitations.

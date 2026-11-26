---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For old distances 1, 2 and 3 the only forbidden new distance pairs are respectively {1,3}, none, and (1,1). Positive Katětov vectors are realized, determine the full type by homogeneity over the named base, and have arbitrarily many distinct realizations (add copies at mutual distance 2, consistent since all old-to-copy distances are at least 1). With S the set of distance-one sites, the graph case forces S to be a clique in G² and forces precisely its external unit-edge neighborhood to 2. Each other site independently takes 2 or 3; this proves (1) with multiplicities appropriate to named parameters. In a squared cycle n≥7, after putting a clique site at 0, the only compatible pairs among offsets −2,−1,1,2 are (−2,−1),(−1,1),(1,2), even at n=7; no triple of those offsets is compatible. Thus the five clique classes have counts 1,n,n,n,n and neighborhood sizes 0,2,2,3,2, in the displayed order, giving the full polynomial and (n+4)2^(n−2). The one-pair edit preserves triangles because side differences are at most 2 and the other two positive sides sum to at least 2. It removes only the joint-one exclusion on {0,3}. For n≥8 only 1 and 2 can join these two sites in S, and the four choices have respectively 4,3,3,2 forced 2-sites and n−6 free sites. For n=7, site 5 can join {0,3} but is incompatible with both 1 and 2; all four non-S sites are then forced to 2. This proves the exact factorized difference, including 9 additional named types at n=7. The source’s finite-enumeration code and output were inspected as supporting evidence, not executed; the proof is all-order.

## originality

PASS

Katětov admissibility and realization are established tools. Closely related records include a cap-three tree support identity and a different one-pair edit, as well as an exact graph partition function for the no-distance-three slice. None of their inspected statements gives or specializes to the capped-cycle graded defect with its exceptional boundary. This is a bounded best-of-knowledge assessment.

## value

PASS

Measuring the full distance-composition spectrum and its change when exactly one long side is relaxed is a natural sensitivity question for finite bases of the generic metric space. The cycle family provides a complete all-size graded response and a sharp exceptional size explained by wraparound geometry. That local response is useful beyond the scalar type total and is not merely a list of finite computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.

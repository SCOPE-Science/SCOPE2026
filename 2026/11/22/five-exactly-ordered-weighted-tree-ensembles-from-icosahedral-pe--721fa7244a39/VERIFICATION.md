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

I reconstructed the icosahedral graph from exact golden-ratio coordinates and verified the given two-ring labeling, then enumerated all 125 perfect matchings by unique first-edge recursion. In an independent coefficient calculation, for each matching M and each subset S of it, contracting S and deleting M minus S counts exactly the trees with T intersect M=S. Summing by |S| gives the coefficients, with parallel edges retained. Grounded Laplacian determinants modulo the prime 2147483647 are exact counts since the total edge-subset bound is 2^30. The run /workspace/branches/check2.py recovers all five factorizations and multiplicities. It verifies the common value 5184000 and derivative 11404800 at t=1 and divides the adjacent differences by (t-1)^2, leaving coefficient vectors (6876,16158,14052,5358,756), (9500,20330,15906,5422,682), (8968,15480,9914,2788,290), (5376,9472,6208,1792,192). These exact coefficients prove the strict order on the entire stated domain except 1, where all matchings tie; this is not a sample of parameter values. The symmetric difference of two perfect matchings is a union of disjoint even cycles, so size four is exactly a single alternating four-cycle flip. The independently enumerated flip-isolated matchings are exactly the P5 class.

## originality

PASS

The matching count, flip-isolated class and uniform tree baseline are known. The same-day adsorption work gives the same five classes as a partition of matchings, not just the same size multiset: the independent automorphism check finds a single graph-automorphism orbit in each polynomial class, and the adsorption probabilities are automorphism-invariant and take five distinct values. The adsorption ranking, however, is 30>10>60>20>5 by multiplicity label, in particular putting the tree-maximizing orbit last. The distinct finding is the five evaluated tree polynomials and their strict, contrast-independent ranking, not discovery of the orbit partition or of the isolated matchings. No same-day publication order is inferred.

## value

PASS

The graph, the all-vertices disjoint marking constraint and the spanning-tree partition function are natural independently of the resulting finite table. It is structurally useful that the full family has one strict order for both weakening and strengthening, with exactly the known flip-isolated orbit winning, unlike the adsorption weights on the same orbits. The evaluated polynomials provide full intersection-count statistics and a reproducible benchmark for network-design and tree-ensemble comparisons, not merely a count of matching types already known.

The dated certificate retains the supplied scientific assessment, sources and limitations.

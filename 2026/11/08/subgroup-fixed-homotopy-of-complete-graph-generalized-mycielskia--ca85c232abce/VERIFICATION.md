---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Executable and mathematical verification

Run `python3 verify.py` from the same directory with Python 3 and no third-party packages. The program directly generates the graph \(\mu_\ell(K_n)\), its labeled edge set and the fixed vertex orbits for the cyclic permutation realizing each integer partition of \(n\). It independently constructs the candidate orbit graph from the level/label formula and verifies every adjacency comparison, each neighborhood-containment prerequisite at its actual deletion stage, and the exact remaining graph after domination removals.

The checks cover all unordered integer partitions of \(n\in\{2,3,4,5,6\}\) and all \(1\le\ell\le6\), totaling 168 quotient-graph instances, 16,579 orbit-pair comparisons and 462 checked removals. For quotient graphs with at most fifteen vertices and \(\ell\le5\), a separate exhaustive face enumeration and direct mod-two boundary-rank routine confirms the asserted reduced homology. This runs over 110 instances and 9,647 total faces. The extracted and replayed program must print `ALL_FIXED_MYC_CHECKS_OK` and these counts.

The mathematical proof in `RESULT.md` establishes the all-subgroup and all-level statements. Exhaustive computations over finite parameter ranges are not claimed as proofs outside those ranges; mod-two calculations alone cannot establish integral torsion-freeness or the homotopy type. The general integral types use the exact strong collapse and the cited proven ordinary homotopy classifications.

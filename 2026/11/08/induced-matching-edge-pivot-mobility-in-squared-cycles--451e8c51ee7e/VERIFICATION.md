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
# Verification of maximum induced-matching edge-pivot mobility

The theorem is proved for all integer orders of squared cycles at least five by the cyclic-block decomposition, exact coefficient counting, and constructive legal-pivot paths. The computations below check particular finite orders only.

Use Python 3 (standard library only) to execute `python3 check_direct.py` and `python3 check_gaps.py` in the directory containing the scripts. Their expected complete outputs are `direct_results.txt` and `gap_results.txt` respectively.

`check_direct.py` independently constructs the original graph and pairwise induced-edge compatibility, enumerates all maximal compatible cliques without pre-fixing the optimum size, retains every maximum clique, and finds all incident-edge-pivot components for orders 5 through 23. A maximum clique in the compatibility graph corresponds exactly to a maximum induced matching.

`check_gaps.py` independently enumerates binary edge lengths and weak gap compositions, checks that each resulting edge set is an induced matching in the original graph, and explicitly constructs the pivot graph for orders 5 through 47. It verifies the four-residue formula and the number of components.

The original embedded output files terminate with `DIRECT_EXHAUSTIVE_OK` and `GAP_ENUMERATION_AND_PIVOT_OK` respectively. Finite checks do not establish the infinite theorem by themselves. Independent scholarly audit is not performed.

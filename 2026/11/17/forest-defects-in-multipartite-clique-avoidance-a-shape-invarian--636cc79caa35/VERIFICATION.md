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

# Verification

The source `verify_forest_clique_free.py` can be executed with standard Python 3.10 or later. `verification_output.txt` contains the exact recorded output of one completed run. All 328 forests on a three-by-three cross-shore graph were enumerated, and every corresponding three-clique-free complex was computed directly from forbidden graph cliques and checked against a separate face characterization. A simulated neighborhood-fold reduction verified 1,090 legal vertex deletions ending in the predicted matching sizes. There were 21 checks with four or five shores, three cyclic-boundary checks, and four matching-filtration stage checks. All mod-two homology ranks matched the theorem.

These are finite checks; the all-size integral statement depends on the exact suspension pushout, acyclic fold collapse, and primitive integral cycles provided in the proof. Inclusion maps in the general matching filtration are proved symbolically but not independently recomputed by this finite program. External independent audit is not performed.

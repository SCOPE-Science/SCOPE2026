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
# Reproducibility
Run `python path_extension_check.py` with standard Python 3. The checker uses rational arithmetic, enumerates complete edge-sign potential sets on the tested small paths, tests signed coefficient vectors and all critical inequalities, and counts cyclic-ballot order regions for five distinct edge counts.

Observed output:
```
EXACT_TREE_TRANSPORT_DUAL_AND_CRITICAL_FACE_PASS tested_cumulative_vectors= 11715 dual_profiles= 309
CYCLIC_BALLOT_PERMUTATIONS_PASS edges= 3 admissible= 2 positive= 1 fraction_positive=1/2
CYCLIC_BALLOT_PERMUTATIONS_PASS edges= 4 admissible= 6 positive= 1 fraction_positive=1/6
CYCLIC_BALLOT_PERMUTATIONS_PASS edges= 5 admissible= 24 positive= 1 fraction_positive=1/24
CYCLIC_BALLOT_PERMUTATIONS_PASS edges= 6 admissible= 120 positive= 1 fraction_positive=1/120
CYCLIC_BALLOT_PERMUTATIONS_PASS edges= 7 admissible= 720 positive= 1 fraction_positive=1/720
CRITICAL_FOUR_VERTEX_SIGNED_THRESHOLD_PASS
WEIGHTED_PATH_SIGNED_OPTIMAL_EXTENSION_ALL_CHECKS_PASS
```
These tests are exact only for the tested finite configurations; infinite families are established by the proof. The checker is not an external audit or formal proof certificate.

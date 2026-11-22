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

This finite result can be reproduced using only Python 3 standard-library modules. Execute `python3 verify_incidence.py` and `python3 verify_petersen.py` from the directory containing the files. The two programs independently enumerate all 38,760 size-six candidate deletions, construct the jump and slide state graphs, verify their symmetry and connectedness, and compute 2,860 breadth-first-search distance rows for each movement rule. The state-count, edge-count, eccentricity, all-pairs distance, Johnson excess, and locality excess outputs are recorded in `metrics_incidence.json` and `metrics_petersen.json`. The second script asserts exact expected histograms; the first checks the explicit incidence-to-generalized-Petersen graph isomorphism. The programs employ distinct base graph constructions and complement-forest tests.

The analytical bound on minimum deletion size is obtained from the 30-edge cubic graph: the deleted count is at least six when the remainder is a forest. The complete finite census proves exact data only for this graph, not for a parameterized family. The scalar optimum count is prior knowledge. Scientific checking here is self-review only; independent audit has not been performed.

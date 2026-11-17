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

The proof counts length-three geodesics by identifying the two nine-vertex interior layers of the Johnson exchange interval with two rook boards. It establishes their precise within-board and cross-board adjacency conditions, then gives an elementary case-by-case derivation of the complete two-variable stable-set enumerator.

The accompanying `check_geodesic.py` is standalone Python 3 and uses exact integer arithmetic. It enumerates all 262,144 subsets of the 18 internal vertices of the six-element rank-three Johnson interval, retains exactly 202 stable configurations, and independently counts every surviving length-three path from one endpoint to the other. It checks all five multiplicities and their frequencies, plus the eighteen sharp configurations.

Reproduction: `python3 check_geodesic.py`.

Limits: the script checks the universal local 18-vertex model, not every ambient rank and ground-set size. The infinite-parameter extension is established separately by the explicit interval identification and matroid construction in the proof. Independent mathematical audit has not been performed.

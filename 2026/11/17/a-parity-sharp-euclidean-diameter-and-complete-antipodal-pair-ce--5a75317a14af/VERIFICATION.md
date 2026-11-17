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
# Reproduction and scope

Run `python3 flow_diameter_checker.py` with Python 3.8 or later. The script defines independent bit indices for all \(\binom N2\) directed arcs, constructs every \(s\)-to-\(t\) path from its subset of internal nodes, and computes squared Euclidean distances as the popcount of bitwise XOR of arc sets. All unordered vertex pairs for \(3\le N\le13\) are checked against both the maximum and the complete equality criterion; 4,800 larger random cases with fixed seed check the bound to order 200.

Recorded replay: `ORDERED_FLOW_DIAMETER_PASS N=3..13 exhaustive_pairs=2794155 random_large_pairs=4800`.

Independent numerical checks are unnecessary here because arc coordinates are integral zeros and ones and the script works with exact integers. The universal conclusion requires the symbolic proof in `RESULT.md`, which does not invoke experimental extrapolation. It uses the natural arc-coordinate norm only. This file does not claim any independent scientific validation or external certification.

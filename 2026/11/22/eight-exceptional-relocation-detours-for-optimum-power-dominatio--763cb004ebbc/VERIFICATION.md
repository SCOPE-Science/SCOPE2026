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

# Reproducibility of the finite result

Python 3 with its standard library suffices to execute `verify_direct.py` and `verify_bitsets.py`. Both programs build the McGee graph from the explicit 24-vertex period-three LCF chord list, independently enumerate all minimum power-dominating configurations, reconstruct the token-jump and token-slide graphs, and calculate their distances without external input files.

The set-based checker confirms every one of the 165,600 unordered configuration-pair distances under both rules, all eight exceptional jump-distance-one/slide-distance-eight pairs, and their disjointness. The integer-bitset checker independently enumerates all 576 optima and re-evaluates every pair with bitset layer expansion. Both certify the full locality-penalty distribution and eccentricity split with assertions.

The calculation is a complete finite enumeration because there are only 24 graph vertices, 2,024 three-subsets and 165,600 unordered pairs of successful three-subsets. Its correctness depends on the published LCF graph identification, ordinary power-domination rules and the transparent finite algorithms. It does not establish any result for other graphs by sampling or extrapolation. Independent audit has not been performed.

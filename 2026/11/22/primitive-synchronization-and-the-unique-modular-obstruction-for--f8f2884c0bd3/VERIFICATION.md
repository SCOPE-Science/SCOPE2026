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

The included `distance_census.cpp` exhaustively enumerates all \(9^9\) nine-state maps, filters to rank seven, builds the cyclic-distance transition graph with vertices \(0,1,2,3,4\), and tests backwards reachability to \(0\). The included `pair_census.cpp` independently builds each rank-seven map from one of 462 kernel partitions and an injective choice of seven images, and computes backwards closure in the full \(36\)-pair graph. It also directly tests preservation of residue classes modulo \(3\). Both implementations reproduce the labeled counts and find no nonsynchronizing map without that congruence.

Reproduce with `g++ -O3 -std=c++17 distance_census.cpp -o distance_census`, `g++ -O3 -std=c++17 pair_census.cpp -o pair_census`, then run both binaries. With Python 3, run `python3 subset_crosscheck.py`; this tests the subset-based reset criterion independently for every rank-defect-two map at orders \(4\), \(5\), and \(6\), and for reproducible samples at order \(9\). Arithmetic counting of the congruence-preserving transformations is independently verified in the same script.

The two full nine-state enumerations, not the nine-state sampling, support the universal converse. The analytic count supports only the number of congruence-preserving maps unless combined with the exhaustive converse. The conclusions are finite, computationally exhaustive scientific checks; no independent audit or external proof-assistant certification is represented.

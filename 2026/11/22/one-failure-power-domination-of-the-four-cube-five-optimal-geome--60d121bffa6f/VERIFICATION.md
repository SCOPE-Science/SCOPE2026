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

# Finite computational verification

The executable proof checks are `verify_direct.cpp` and `verify_structural.py`. They use only C++17 and Python 3 standard facilities. Execute:

```
c++ -std=c++17 -O2 verify_direct.cpp -o verify_direct
./verify_direct
python3 verify_structural.py
```

The direct checker enumerates all 65,536 subsets of the sixteen binary four-cube vertices, independently runs the closed-neighborhood/unique-unobserved-neighbor closure, then tests deletion of each chosen sensor. The recovered minimum is four; 376 four-subsets succeed, with auxiliary Hamming-three induced-subgraph counts 160, 192, and 24. All 376 optima are processed for token-jump and token-slide adjacency; the checker tests 2496 undirected jump edges, no slides, and a diameter of six by BFS from every state.

The second checker does not use the first one's propagation routine. It uses the proved triple-orbit reduction to enumerate all 4-subsets with auxiliary independence number at most two. It checks the involutive isomorphism between the auxiliary distance-three graph and the ordinary four-cube, classifies all five automorphism orbits, and independently performs all-source BFS on the generated optimal jump graph. Its pair-distance distribution agrees with the direct checker.

The scripts do not purport to verify any larger cube or multiple simultaneous failures. The human-readable orbit representative table and counting proof are in `RESULT.md`. No independent external audit or validation is claimed.

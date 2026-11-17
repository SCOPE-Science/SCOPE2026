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

# Verification of four-step spatial rigidity

The certificate consists of three standalone source files and their recorded outputs. The two graph computations use the same mathematical rule but distinct implementations: direct local-time comparison in C++ and an independently computed successor-presence bitmask in Python. Both find exactly 20,340 graph edges and six cyclic strongly connected components of size four, without restricting horizontal circumference. The first also checks that all 24 cyclic graph vertices give the specified row-equal four-column patterns.

Run from the folder containing the extracted files:

```
g++ -std=c++17 -O2 verify_transfer.cpp -o verify_transfer
./verify_transfer
g++ -std=c++17 -O3 verify_direct.cpp -o verify_direct
./verify_direct
python3 verify_masks.py
```

The corresponding outputs are `transfer_output.txt`, `direct_output.txt`, and `masks_output.txt`. There are no Python package dependencies beyond its standard library. Source files and outputs were replayed after extraction from their serialized record; the outputs matched exactly.

**Logical scope.** The all-circumference theorem is proved by the exactly constructed finite transfer graph and the closed-walk correspondence. Direct enumeration for circumferences three through seven is a separate consistency check, not an infinite-width proof. The graph computation is a complete finite exhaustive certificate, not a timeout or partial search. No independent external audit has been performed.

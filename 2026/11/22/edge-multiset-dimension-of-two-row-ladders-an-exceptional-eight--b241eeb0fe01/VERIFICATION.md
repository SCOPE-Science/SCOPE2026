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

The infinite-family proof is a direct comparison of the three unordered edge-distance values for two same-rail endpoint landmarks and a third landmark at column two or three. The exceptional finite lower bounds are supported by a complete obstruction certificate, not a timeout or a sample.

Run `python3 verify_certificate.py finite_obstructions.json`, `python3 verify_bfs.py`, then compile and execute `verify_coords.cpp` with a C++17 compiler. The first finite program uses graph breadth-first-search distances, while the second uses the exact grid distance formula. These routes independently agree on the finite minimum dimensions and the four-vertex-basis counts of four, twenty and eighty in the three exceptional finite cases. The certificate checker independently validates 24 classes of indexed obstructions, covering all subsets for the first three sizes and all three-element subsets for sizes five, six, and eight.

Computational checks of larger sizes illustrate the analytic construction only; they are not an infinite proof. No independent external audit or priority certification has been performed.

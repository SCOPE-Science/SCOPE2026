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

# Reproducible checks

Run `python3 VERIFY_CYCLIC.py`. It exhaustively generates permutations, filters derangements, reconstructs every legal swap on the cyclic position graph, and checks the exact component count, excedance partition, component sizes, and isolated-state count for \(3\le n\le8\). It also compares the fixed-signature path components separately. Run `c++ -O3 -std=c++17 VERIFY_CYCLIC_INDEPENDENT.cpp -o verify_cyclic_independent && ./verify_cyclic_independent`; this independent permutation and union-find implementation checks \(3\le n\le9\).

Both programs were run from actual source files and returned PASS before packaging, including the 133496-state order-nine case. After packaging, they are extracted and executed again from the saved embedded versions. Their finite exhaustions do not establish the all-order theorem, for which the constructive proof in RESULT.md supplies the reason. No external independent scientific audit was performed.

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

# Verification instructions and observed evidence

The object is a *finite* state space, not a sampled infinite family. Each graph has 16 vertices and every configuration has a unique code in \([0,3^{16}-1]\); the local update is specified completely in `RESULT.md`. `exhaustive_graphs.cpp` enumerates all 43,046,721 successors, eliminates trees feeding directed cycles, measures primitive cycle lengths, and propagates the entry and eventual-period classes. `independent_orbits.cpp` computes the same map using separately constructed masks and follows paths from every unclassified state. Full class tables agree exactly on both graphs. `cycle_reps.cpp` independently lists all 98 or six distinct primitive four-cycle representatives. `analyze_symmetries.py` constructs, verifies and applies all graph automorphisms, whose sizes match the proven upper bounds. `check_graph_invariants.py` verifies the exact strongly regular identity and the excitation-profile counts independently.

Running `python3 verify.py` with a C++17 compiler reconstructs all embedded data. In the recorded replay, the checker printed `VERIFICATION_OK` after confirming each complete class distribution, all 40 CSV records, both automorphism partitions, every expected cycle and entry bound, and `GRAPH_INVARIANTS_OK`. Captured values appear in `verification_output.txt`; source-level assertions check array ranges, every state's eventual classification, and automorphism preservation of adjacency. `rook_A.txt`, `shri_A.txt`, `rook_B.txt`, `shri_B.txt`, the `*_reps.txt` files and `*_symmetry.txt` files contain actual calculation outputs.

These checks supply a reproducible exhaustive finite proof, not a statement of independent formal certification. The claim does not assert any property for other graph orders or alphabets. Independent audit has not been performed.

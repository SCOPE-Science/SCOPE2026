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

# Verification evidence

The package includes `verification/potential.txt` containing exactly 6,561 integers in the base-nine lexicographic state order specified in `RESULT.md`.

With Python 3, run `python3 verification/verify_potential.py`. The validator reconstructs all 48,681 legal transitions, checks the exact inequality for every transition, constructs the 6,099-edge tight digraph, and independently identifies its sole directed cyclic component of size seven. It also verifies that the resulting primitive seven-column label word is Roman feasible and has cost eight per period. This finite inequality certificate gives an all-order result because any cyclic labeling of length at least seven maps to a closed walk and the potential terms telescope.

For an independently regenerated potential, compile `verification/derive_potential.cpp` with a C++17 compiler and compare its standard output to `verification/potential.txt`. The independent C++ `verification/enumerate_small.cpp` exhaustively checks all two-label supports that could meet the optimum target for the graphs on fourteen and twenty-eight vertices, reporting seven optima at each size.

The finite automaton is not itself an exhaustive enumeration of all large Roman labelings; its checked potential inequalities and cyclic-SCC structure are the mathematical certificate extending the conclusion to all positive period counts. No other cycle lengths or other Roman-domination variants are asserted. Independent scholarly audit has not been performed.

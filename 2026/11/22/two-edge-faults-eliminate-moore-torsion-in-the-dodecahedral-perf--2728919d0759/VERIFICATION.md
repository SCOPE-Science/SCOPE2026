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

The accompanying `verify_two_fault.py` is self-contained Python 3.10+ code. Re-run using `python3 verify_two_fault.py` in the directory containing the script. It enumerates all 36 ten-edge perfect matchings without duplication and checks the full automorphism group of size 120 by vertex-bijection backtracking. All 435 unordered fault pairs form exactly eight orbits. For each representative it enumerates all simplices, checks the full directed-Hasse graph for acyclicity (all vertices visited), computes all critical cells, and calculates the integral signed Morse matrix. Exact direct simplicial homology ranks over two distinct primes provide an independent finite-chain cross-check.

The eight critical-cell profiles, matrix entries and face-poset sizes are printed in `VERIFIER_OUTPUT.txt` and are rederived, not read, by the script. No combinatorial extrapolation beyond the fully enumerated graph is used. The verifier is finite proof-supporting code and not independent external scientific validation.

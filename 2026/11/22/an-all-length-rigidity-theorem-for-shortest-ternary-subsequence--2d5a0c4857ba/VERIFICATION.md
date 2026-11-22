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

# Reproduction of the finite-state proof certificate

Run `c++ -std=c++17 -O2 certify_dfa.cpp -o certify_dfa && ./certify_dfa`. It generates all 255 relevant candidates, starts after the canonical prefix `01`, computes each candidate's exact coverage transition, and performs a complete interned state exploration of the direct product with the regex recognizer. It checks every reachable state's minimum-cover set and both legal next symbols. The reported 84,725 states and 169,450 edges are a complete finite graph, not a host-length cutoff. Its 12 ambiguity **states** are not 12 exceptional words.

Run `c++ -std=c++17 -O2 verify_independent.cpp -o verify_independent && ./verify_independent`. It enumerates every canonical runfree ternary host up to length twelve (2,047 cases), computes all positional subsequence masks and minimum covers, independently checks the language normal form, and compares against the distinct greedy earliest/latest membership test. That test is explicitly bounded; its lack of errors is not an independent proof for longer host words.

The supplied `verification_output.txt` contains both program outputs, which were independently replayed against these exact included code files before packaging. All code uses standard C++17 facilities only and exits unsuccessfully on a failed test. This is same-model reproducibility evidence, not an independent scientific audit or external certification.

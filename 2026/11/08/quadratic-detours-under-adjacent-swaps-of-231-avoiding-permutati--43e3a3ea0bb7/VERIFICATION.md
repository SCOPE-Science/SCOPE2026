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

# Reproducibility and limits

The result follows mathematically from the separation-around-the-maximum and rightmost-descent sorting lemmas. The two accompanying checkers reproduce finite instances, not an infinite certificate. Both programs were executed from their packaged source text after the candidate proof was complete.

`proof_checks/verify_bruteforce.py` uses brute-force forbidden-pattern tests on all permutations for orders \(1\) through \(8\), and constructs legal-swap neighbors only among valid states; output terminates with `BRUTEFORCE_PASS`.

`proof_checks/verify_recursive.cpp` uses independent recursive Catalan generation and breadth-first searches for orders \(2\) through \(12\); output terminates with `RECURSIVE_PASS`. Compile as `g++ -std=c++17 -O2 proof_checks/verify_recursive.cpp -o verify_recursive` and run `./verify_recursive`.

The graph's global diameter, extremal-pair uniqueness, and broader distance enumerator have not been proved. No independent scholarly audit was performed.

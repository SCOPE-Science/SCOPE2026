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

The checker `check_trimmed_mean.cpp` uses only C++17 and exact integer arithmetic; no floating-point norm comparisons, randomness, network, or external data. Compile with `g++ -O3 -std=c++17 check_trimmed_mean.cpp -o check_trimmed_mean` and execute `./check_trimmed_mean`. It exhausts all rank permutations and all binary cuts modulo complement for sizes five through nine. It also checks the sharp explicit/padded witnesses at sizes ten through eighty and the six-site overlap lemma over all \(6!\) ranks.

The finite exhaustive inference depends on the rank-chamber and layer-cake lemmas proved in `RESULT.md`. The all-dimensional bound and induction-by-padding are proved analytically and not extrapolated from the eighty-site check. Compiler output is not an independent audit.

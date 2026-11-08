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

The infinite proof appears in `RESULT.md` and derives each residue threshold by an explicit bijection, not a probabilistic or empirical inference. A separate bounded dynamic-programming implementation verifies the predicted first and second threshold for every residue of all tested parameter pairs. Its count-capping at two is valid because every tested invariant depends only on zero, one, or at least two representations. A second program constructs exact integer solutions to the original three-variable Diophantine equation by directly enumerating the first two variables and checking divisibility for the third.

Run `g++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp && ./verify_cpp` and `python3 verify_brute.py`. Both should reproduce `VERIFY_OUTPUT.txt` exactly. The dynamic-programming sample comprises 1,190 full parameter pairs and 440,895 residue checks; the direct-enumeration sample comprises 240 pairs. Neither finite sample proves claims for arbitrary parameters; that follows only from the symbolic derivation. No external independent audit has been performed.

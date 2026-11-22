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

The formal domain is the full set of \(2^{18}=262144\) labeled vertex subsets of the explicitly defined 18-vertex incidence graph. Python and C++17 independently test the exact restrained condition on every subset; neither infers a finite minimum from an interrupted search.

Run:

```sh
python3 verify_affine.py
g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_cpp.cpp -o verify_cpp
./verify_cpp
```

Both programs ran successfully on the supplied source files. Both confirm 207 restrained six-sets, the full 12-term feasible polynomial, 27 isolated optimum configurations for each move rule, one 180-state component and exact main-component diameters six and eight. The Python program additionally checks the 216 graph automorphisms and the five orbit sizes, which sum to 207.

Limits: this certificate is exact for the one graph explicitly constructed, not for an infinite family; independent expert or external formal validation has not been performed.

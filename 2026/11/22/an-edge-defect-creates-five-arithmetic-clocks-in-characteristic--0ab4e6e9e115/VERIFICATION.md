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

Run `python3 check_wave.py` and `python3 check_minpoly.py` from the directory containing this file. Only the Python standard library is required. The checker constructs the actual two-level adjacency-recurrence matrices modulo three and tests all ordered side-size pairs in the range 2 through 8. It verifies the asserted global order and checks proper prime-divisor powers are nonidentity. Independently, it computes modular ranks for every time index 1 through 40 in the doubly-two residues at side sizes 2, 5 and 8. Finally, it iterates every state on the four-vertex exceptional path, checking the exact period population.

The second checker computes the adjacency minimal polynomial directly from the full modular matrix for each of 49 ordered shore-size pairs, then verifies the symbolic temporal polynomial substitution and factorization; `minpoly_output.txt` records all 98 passed tests. The attached `check_output.txt` contains the successful invocation's printed counts: 49 global-order checks, 360 fixed-space comparisons, 6,561 states, and the period distribution \(1:1,5:80,10:6480\). This is a finite corroboration; the universal domain and characteristic-three extension-field assertions require the symbolic proof in `RESULT.md`.

No independent audit has been performed.

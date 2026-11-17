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

Run `python3 check.py` from the directory containing this file. This verifier uses only Python's standard library and exact integers. It constructs all graph edges from the stated definition, makes orbits of each permutation, excludes non-independent orbits, evaluates the signed independent-orbit polynomial, and compares the result with the closed trace formula. A second method directly visits independent simplices and computes oriented-simplex signs on the fixed faces for the smaller instances.

Expected output is exactly the text of `check_output.txt`. The tested values cover 166 orbit-graph character instances for orders 3–14 (with a reduced set of group elements above order 12), 66 direct signed-face instances for orders 3–8, and rational character averages through order 75. These finite checks do not certify all n; the infinite statement follows from the written cancellation and path/cycle orbit analysis. No independent mathematical audit has occurred.

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

# Direct verification

In the same directory, execute `python3 verify.py`. This is standalone Python standard-library code. It constructs the normalized Walsh matrix up to the common factor \(1/\sqrt8\) using Sylvester recursion; checks orthogonality and the exact dyadic-prefix Gram identity; enumerates every one of \(4^8=65{,}536\) independent length assignments; and applies integer fraction-free elimination to every leading principal minor of \(68I-5H\), with exact divisibility assertions. The set of non-positive-definite exceptions is asserted equal to the eight claimed xor-translates. Exact Faddeev–LeVerrier arithmetic checks the characteristic polynomial for each exception. Exact integer/rational evaluations of the cubic prove that the exceptional spectral radius is above the separation bound.

Passing means that these finite integer certificates and all asserted identities hold in this run; the analytical derivation of the Gram formula and Sylvester characterization is supplied in `RESULT.md`. Neither finite enumeration nor this review proves the assertion for higher binary levels or establishes historical uniqueness. Independent audit has not been performed.

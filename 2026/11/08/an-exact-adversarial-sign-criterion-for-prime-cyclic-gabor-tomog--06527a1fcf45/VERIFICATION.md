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

# Verification of the exact signing criterion

Run `python3 verify.py` from the directory containing this file. It needs only Python 3 standard-library modules. The checker computes all integer ambiguity rows and decides nonzero Fourier coefficients with the prime cyclotomic minimal polynomial, not floating-point approximations. It verifies every support/signing pair at prime orders 3, 5, 7; it also explicitly constructs destructive signings for all supports failing the overlap criterion, checks support-optimal planar examples at 7 and 13, verifies Paley overlap counts at 23 and 31, and performs a fixed-seed test over prime order 11. The success marker is `ROBUST_SIGNING_GABOR_PASS`.

The proof's infinite-prime guarantees rest on cyclotomic irreducibility and the induced path-forest construction; the finite checker only corroborates algebra and boundary cases. A positive smallest-singular-value estimate is not claimed. Independent mathematical verification is not performed.

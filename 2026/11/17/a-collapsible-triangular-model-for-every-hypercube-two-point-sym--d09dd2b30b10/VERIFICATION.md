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

# Verification methods and boundaries

Execute `python3 verify.py` using Python 3 with only the standard library. The expected standard output is exactly the included `verification_output.txt`.

The checker constructs all graph vertices and edges, all two-particle deleted-product cells, all strict face chains, and all affine signed-coordinate automorphisms for dimensions two through five. It checks quotient orbit counts, actual free-face collapses on the subdivided quotient, and the two expected effective square-stabilizer cardinalities. It does not sample an infinite family as a substitute for proof. The proof of arbitrary dimension, including the collision-free equivariant barycentric retraction, is in `RESULT.md`.

Exact expected quotient orbit-flag counts for dimensions two through five are (4,5,2), (8,15,8), (12,25,14), and (16,35,20). Their Euler characteristics are all one. In all four runs the verifier independently collapses every triangle and then every remaining edge but one vertex. No external mathematical audit has been conducted.

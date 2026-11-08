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

## Verified calculations
The tree's normalized child maps produce one root chain with weights 1,2,2,... and only constant-weight 2 chains otherwise. For the root Jacobi square, substitution of the geometric ansatz gives precisely 3 r t^2 - 6 t + 4 r = 0, so t=1 gives r=6/7 and substitution gives the closed-form isolated eigenvalue. Differentiation gives the maximum at r^2=2/3. The lower modulus of S* minus the scalar is the reciprocal of the least norm of a right inverse of S minus that scalar where surjective.

A direct finite-section numerical check was performed with an extra output row in each truncated weighted shift, avoiding artificial terminal zero singular values. Finite sections at r=0,0.1,0.3,0.6,0.8 agreed with the isolated eigenvalue branch; near the bulk edge finite sections converge from above. This does not certify infinite-dimensional statements; those rest on the displayed recurrence and orthogonal direct-sum proof. No standalone script is required by the proof. Publication priority and independent validation are not claimed.

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

The risk is twice the expected quadratic objective, so there is no hidden factor of \(1/2\). The analytic identity \(R=\|L\|_F^2-\|L(I-L)^{-1}L^{\mathsf T}\|_F^2\) follows from the exact triangular sweep update and the factorization of the Hessian. The bipartite parity rule makes the fifth-order Frobenius cross term zero. The absence of a four-cycle makes each off-diagonal overlap in \(NN^{\mathsf T}\) correspond to a unique weighted incident-edge pair. Every non-source–sink orientation has a positive fourth-order gap; finite permutations imply a shared small-coupling interval.

Run `python verification/verify.py`. `verification/output.txt` gives the actual exact-rational execution log. It checks 1590 complete finite permutation cases and small-coupling spot checks; it is not an infinite proof or an independent audit. No exact numerical value of the uniform small-coupling cutoff is asserted. The full text of a related historical arrowhead study was inaccessible; the originality comparison is qualified accordingly.

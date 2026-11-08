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

# Reproducibility

The proof is algebraic: differentiating \(e^{-|z|^2}|z^n-a|^2\) yields \((|z|^2-n)z^n=a|z|^2\) away from zero and the polynomial roots. Check the derivatives of the radial maps \((r^2-n)r^{n-2}\) and \((n-r^2)r^{n-2}\), and the strict positivity of \(-1/2+1/(n-s)\) for \(s\in(n-2,n)\). These checks work symbolically for arbitrary integer \(n\ge3\); the finite numerical values in RESULT.md are illustrations, not proof.

At \(a=A_n\), the radial stationary equation has a repeated root; it is **not** counted as a nondegenerate local maximum. The source publications establish the Fock critical-point context, not independent validation of the new statement. No external mathematical audit has been performed.

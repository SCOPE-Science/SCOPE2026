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

# Verification and scope
The exact reduction of nonzero antiphase fixed points to \(g(u)=(1-u)e^{-u}=c\), the two real Jacobian eigenvalues, all four proof ranges for \(a\ge e^2\), the strict near-fold inequalities for \(a<e^2\), and the open escape set for \(b<-1/2\) are proved in RESULT.md. For a consistency replay, run `python3 verify.py` from the extracted package root; it performs 102 numerical and analytic-identity checks using the Python standard library. The finite computations are not infinite proof or independent validation. In particular, no off-antidiagonal census, neutral-multiplier nonlinear classification or all-basin picture is established.

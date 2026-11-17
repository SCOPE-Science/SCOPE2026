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

# Verification of the mathematical claim

The identity for \((I+mA+nB_c+mnC_c)^{-1}\) is obtained analytically using the \(2\times2\) adjugate. `CHECK.py` (standard Python 3, no third-party packages) tests it at \(m,n=0,\ldots,8\) for four exact-rational matrices, including the boundary \(c=0\). The script additionally checks \(\det C_c=abc\) and the positive coefficient sum \(K_{0,c}+K_1+K_{2,c}=I\). Expected final line: `PASS: 4 rational cases x 81 exact matrix identities; c=0 boundary included`.

The singular-versus-absolutely-continuous dichotomy follows from the conditional gamma law for \(c>0\), the one-dimensional exponential curve for \(c=0\), and nonsingular two-dimensional maps for the other two components at \(c=0\). Analytic scalar covariance identities produce explicit full-variation bounds, and mutual singularity yields the exact coefficient. These are infinite assertions proved mathematically, **not** claims established by the finite script.

No independent audit or external certificate is represented or asserted.

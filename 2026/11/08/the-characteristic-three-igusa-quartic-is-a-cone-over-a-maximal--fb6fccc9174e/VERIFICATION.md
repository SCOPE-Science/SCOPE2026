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

Run `python3 verify_igusa3.py`. It implements characteristic-three arithmetic and the quadratic extension \(\mathbb F_9=\mathbb F_3[\theta]/(\theta^2+1)\) in ordinary Python, without third-party dependencies. It scans all \(40\) projective points of \(\mathbb P^3(\mathbb F_3)\) and all \(820\) projective points of \(\mathbb P^3(\mathbb F_9)\), classifying singular points by the actual gradient of the restricted equation, and checks the rank-three Hessian at each of fifteen nodes. It also checks the full cone in projective four-space over both fields.

Observed exact results: \(\#B(\mathbb F_3)=25\), \(\#B(\mathbb F_9)=145\), fifteen singular nodes over each, and cone counts \(76\) and \(1306\). The printed output from an actual execution is embedded separately in `verify_output.txt`.

**Limits.** These counts alone are finite results. The proof over all extensions uses that the base has only ordinary nodes and that the resolution is a K3 surface with all fifteen exceptional conics split. The K3 cohomology and Deligne's Weil bounds turn the \(\mathbb F_9\) count into a sharp Frobenius trace certificate and force the complete characteristic polynomial \((T-3)^{21}(T+3)\). There has been no independent scientific audit.

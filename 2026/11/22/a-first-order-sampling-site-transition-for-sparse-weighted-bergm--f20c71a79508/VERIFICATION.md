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

# Verification and reproducibility

The exact function optimized is \(F_a(x)=(1+a x^{m/2})^2(1-x)^\beta\) on \([0,1]\), with \(\beta>1\), integer \(m\ge2\), and \(a\ge0\). The analytic certificate is the radial derivative sign rule and unique zero of the strictly concave crossing function \(H(y)=(m/2)y(1-y^{\beta/2})-(\beta/2)(1-y)\). At the global crossing, the critical radius is nonzero exactly for \(m\ge3\).

Run `python check.py` with Python 3 standard library. The checker executes 428 finite evaluations of stationarity, local behavior, critical ties and selected large-order approximations. Its finite samples do not establish universal statements; the proof is included in `RESULT.md`. The checker is rerunnable and uses no third-party dependencies. Independent audit or external validation has not been performed.

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

# Reproducible checks

Run the included `check_settling.py` with Python 3 and the standard library. It verifies the exact polynomial \(F(x)=-200x^3-10903x^2+18794x-203\) from the stated symbolic derivative, its three rational sign certificates, the sinking-region inclusion \(x_b>2\), and numerical root brackets. It also evaluates additional seeded exact-rational parameter samples for agreement between two analytic derivative formulas. Such tests only supplement the analytic proof; no finite parameter grid certifies an infinite result.

# Proof-specific boundaries

The classification holds for \(a,b,c,\eta>0\), \(0<\alpha<1\), and positive-sinking \(0<x<x_b\). Equality in the sharp existential frontier \(\eta=2/(1-\alpha)\) does **not** admit two extrema. At a tangent \(H(z)=0\), there is no minimum–maximum pair. The exhibited coefficients are illustrative and do not arise from field measurements.

# Scope of review

The self-review independently checked differentiation, root sign changes, construction, and literature comparison. Historical priority remains provisional because not every potentially stronger theoretical source was fully accessible. Independent external audit has not been performed.

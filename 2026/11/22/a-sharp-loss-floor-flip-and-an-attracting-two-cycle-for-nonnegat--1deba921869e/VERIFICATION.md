---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For y=λx²/(2c) the effective normalized step is α(1+y)/(1+(1+α)y), giving x₊=x t(y), t(y)=(1+y−α)/(1+(1+α)y). The strictly increasing t lies strictly between −1 and 1 at y>0 when α≤2; a positive limit of the decreasing magnitude contradicts continuity of this strict inequality. T′(0)=1−α, and at α=1 the leading map term is λx³/(2c). At α=2, y₊=y[(1−y)/(1+3y)]² gives the reciprocal increment 8(1+y)/(1−y)². It tends to 8 on nonterminating orbits, hence ny_n→1/8, with the stated spatial and loss constants. Terminating orbits are excluded. For α>2, the origin is locally repelling and the unique equation t(y)=−1 gives y_*=(α−2)/(α+2). At that root the denominator is α²/(α+2), so differentiating T gives T′(±r)=t+2y t′=1−8/α² and the return derivative is its square, less than one, including the zero-multiplier case. At the cycle λγ=2 and excess loss is cy_*. It disproves all-start convergence but says nothing about uniqueness among non-antipodal cycles or global basins. Inspected the exact-arithmetic diagnostics in check_ngn.py and VERIFICATION.md; the upload was not executed. The rational identities and limiting argument certify the theorem independently of those diagnostics.

## originality

PASS

The NGN rule and the positive-floor scalar test problem are known, as are bounds separating boundedness from convergence. The exact all-start threshold, critical coefficient and attracting cycle on the actual positive-floor map are distinct within the examined sources. Overlap with scalar flip theorems for other adaptive updates does not give this explicit classification.

## value

PASS

The simplest strongly convex test problem used by the method's authors separates boundedness from optimization: the true additive objective floor leaves an explicit attracting obstruction at every supercritical fixed base step, while the critical orbit still converges at a different rate with a sharp constant. This is a useful exact counterexample to inferring large-step minimization from NGN's per-step stability, not just a local derivative threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.

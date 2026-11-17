---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The symmetric two-matrix linearizations hI+uX±vZ satisfy (uX±vZ)^2=q²I. Multiplying exact matrix exponentials yields trace half Xi=(u²/q²)cosh(qT)+(v²/q²)cosh(qT(2θ-1)), multiplier exp(hT+acosh Xi), and positive Perron branch. Convexity of asinh((u/q)sinh(qT/2)) proves balanced duty minimizes growth and the cutoff is unique. The exact inequality Xi<cosh(-hT) gives stated duty interval; Taylor expansion yields square-root closing. Cooperative comparison gives nonlinear IBA extinction whenever the linear Floquet exponent is negative. Independent calculation at h=-3/4,u=1/2,v=1,T=2 returns -0.171872904561 and interval (0.239703586224,0.760296413776).

## originality

FAIL

FAIL: The November 1 published rotated-symmetric-saddle theorem fully covers this linearization. After orthogonal conjugacy set p=q, damping a=-h, cos(angle)=u/q, sin(angle)=v/q, and dwell difference Δ=T(2θ-1). Its exact half-trace S=cos²(angle)cosh(pT)+sin²(angle)cosh(pΔ) is literally Xi. Its complete sharp switching cutoff, all-duty interval, square-root boundary and fixed-duty single-transition statements imply every submitted linear phase-diagram assertion. Under the paradox hypotheses h+u<0<h+q, 0<-h<q as required by that theorem. Nonlinear extinction is standard monotone SIS comparison, not a surviving original classification.

## value

FAIL

FAIL: The dominant exact Floquet boundary, threshold, and square-root law are already fully classified by the more general published symmetric-saddle result under a direct orthogonal change of basis. Naming the matrices as community contacts and attaching routine cooperative comparison provides no independent unknown structural result, despite the public-health motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

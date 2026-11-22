---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The distributional derivative representation of arbitrary BV inputs reduces the norm to the largest single-jump response. Direct differentiation gives (C_3 f_c)prime=(2 sqrt(1-c^2)/pi)Q_c, Q_c=(16c^2-4)x^2+4cx+2-4c^2. The two internal roots for c>=2/3 give explicit H(c)=(4/3)sqrt(1-u)[1+2u+(16u^2-11u+2)^(3/2)/(4u-1)^2]. Differentiation, exact squaring and a Sturm chain isolate exactly one stationary point on (4/9,1) at u*=.692..., with sign changing + to -. On c<=2/3 the finite exact integer/rational midpoint upper certificate M=128, grid c=k/12000 k<=8000, integral error <=24/M^2, |Hprime|<80 and grid allowance 40/12000 show max upper 2.4425881184680684 <49/20. Independent reimplementation of all 8001 integer midpoint enclosures reproduced this strict gap; at c=5/6 the exact radical witness exceeds 49/20. Since 2H/pi is norm, global maximizers ±sqrt(u*) are off-center. The exact discrete certificate plus analytic continuum bound, not finite sampling alone, closes the proof.

## originality

PASS

This is a precise fixed-degree exact BV operator norm; known Chebyshev approximation/error-localization bounds do not determine it. The published degree-three Legendre projection has a different weight and midpoint extremizer; Jacobi degree-two findings have different polynomial range. A complete equivalent Chebyshev BV projection formula was not found in the inspected sources, with residual risk for older projection-norm literature.

## value

PASS

The first nontrivial cubic Chebyshev truncation has a natural sharp stability constant and surprising displaced worst-case discontinuities, needed to bound variation amplification under spectral projection. A rigorous algebraic optimizer and continuum certificate make this a substantive exact operator norm rather than an arbitrary numeric instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.

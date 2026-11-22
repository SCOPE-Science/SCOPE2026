---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Orthogonalization of {1, cos(ωt)−sinc ω, sin(ωt)} in averaged L² gives V=1+sinc ω cosω−2sinc² ω>0 and K(ω)=1+2(1−sinc ω)²/V; Riesz representation determines equality vectors. SymPy independently differentiated and factored K′=2(1−s)N/(ωV²), with N as printed in RESULT.md. Analytic proof excludes 0<ω<π and 2π<ω<3π by K<3, ω≥3π by K<27/7<4 while K(3π/2)>4, and proves N>0 for π<ω<3π/2. In last quadrant 3π/2<ω<2π, N>0 at entry and N<0 once cosω≥(√3−1)/2; on the remainder the derivative bounds N_c<-158/81, N_s<43/9, c′>9/10, s′<7/50 force dN/dω<0 and unique root. Exact endpoints K(0+)=9/4, K(∞)=3; 65-digit independent root agrees ω*=4.9049244571380714153237888 and K*=4.2673035613955620568. Numeric sampling alone is not uniqueness proof.

## originality

PASS

The orthogonal three-tone evaluation kernel is known in general and the endpoint case is sharply solved, but the unique global optimum over frequency gap at the *midpoint* is different. Related local interior frequency splitting only covers the small-gap neighborhood; it does not imply the global resonant optimum. Potential earlier Christoffel/sampling inequalities remain priority risk.

## value

PASS

The exact in-domain pointwise evaluation amplification for the smallest oscillatory nontrivial Fourier space is a canonical leverage/Christoffel invariant. Optimizing over gap and proving attainment, uniqueness, and sharp separation from collision and infinite-separation limits is a complete meaningful frequency-design result rather than a textbook fixed-gap Cauchy–Schwarz application.

The dated certificate retains the supplied scientific assessment, sources and limitations.

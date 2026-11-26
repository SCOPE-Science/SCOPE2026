---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Let x=pi/(J+1) and set q_j=sin((j+1)x) with support 0 through J-1. For lag k<J, product-to-sum gives the sine-vector correlation: the sum of cos((2j+k+2)x) has central angle (J+1)x=pi and is -sin((J-k)x)/sin x. This gives precisely Ferrari's Eq. (30) after multiplying by 2(-1)^k and dividing by S=(J+1)/2. Lag one gives S cos x and agrees with -4c_2^J/(4-2c_2^J); Eq. (30) is vacuous at J=2, so the constant and first cosine coefficients already suffice there. Multiplying the spectral factor by (1-z)^2 with the normalization sin^4(theta/2)=|1-z|^4/16 yields C_J=1/[2(J+1)(1+cos x)]. The new factor P_J has strictly positive coefficients at every index 0 through J+1, including the two endpoints. Comparing the real-part cosine coefficients of the real analytic symbol with the autocorrelations proves strict alternation. Triangle equality against the positive constant and negative linear term forces z=-r on every disk of positive radius. At r=1, C_J(4 cot(x/2))^2 is the stated value. The optional mpmath script was inspected, not run; its sampled contours and finite orders do not establish the theorem. No operator-valued or general A-stable-family assertion was verified.

## originality

PASS

The distinct result is the all-order strict sign property of ordinary symbol coefficients and the exact unique maximizer at every radius. The parent paper supplies the optimized family and enough Fourier data to derive it, but leaves the unit-disk supremum explicitly open outside J=2 through 6. The autocorrelation argument closes that gap, not a separate claim on the already known endpoint value.

## value

PASS

Resolves the explicitly posed unit-disk extremum problem and gives a stronger ordinary-coefficient theorem and unique extremum on every circular contour. These are precise scalar symbol bounds for the optimized family, not claims about CQ operator convergence or numerical stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.

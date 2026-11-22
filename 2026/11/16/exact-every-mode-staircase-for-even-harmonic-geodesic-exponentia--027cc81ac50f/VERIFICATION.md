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

The exact normalized Fourier coefficient c_n=a[1-(-1)^n exp(-pi a)]/[pi(a^2+n^2)] is strictly positive for a>0. Multiplication by cos(2theta) shifts n by two, leaving parity factors identical; the ratio 2c_n/(c_(n-2)+c_(n+2)) equals R_n(t) with t=a^2. R_0,R_1>1 while high R_n<1; Fourier PSD is precisely b>=-min_(n>=2)R_n(t). Differentiating the continuous relaxation in y=n^2 gives a single positive minimizer and at most two nearest integer candidates. Independently checked the rational adjacent-difference polynomial P_n(t); its single positive roots, unimodality, monotone minimizer and ordered crossing orientation cover all t>0 with only adjacent ties. Boundary Fourier holes are finite; for every N distinct sites sufficiently many consecutive nonzero coefficients give an invertible Vandermonde form, proving strict PD. Small/large-a expansions follow algebraically. Inspected full RESULT.md at source tree and CHECK.py; independent SymPy exact algebra checked ratio and crossing identities. Finite CHECK.py experiments alone do not prove the all-frequency assertions.

## originality

PASS

Best-of-knowledge new complete second-harmonic circle spectral staircase. The closest published first-harmonic theorem gives a parity-split bound and eventually active modes, not this all-mode algebraic adjacent-transition classification; general circle Schoenberg theory supplies the Fourier criterion but not its parameter-dependent minimizer.

## value

PASS

The exact PSD boundary and every-mode adjacent-crossing staircase solve a natural covariance design question: which signed even-harmonic perturbations are admissible and which Fourier modes become critical as damping varies. The no-skips law and finite spectral-hole strictness are substantive all-parameter structural facts, not textbook restatement of the Fourier criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.

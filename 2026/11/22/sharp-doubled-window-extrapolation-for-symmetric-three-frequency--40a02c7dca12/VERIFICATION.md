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

With dt/2, the Gram matrix splits into the even 2x2 block on (1,cos(omega t)) and the sine block; nonzero gap gives positive Gram determinants D and T/2. Inversion and Cauchy–Schwarz give the stated exact E/D+O/T and kernel equality family. I independently checked F=657 DT/4−ET−OD. Using x=sqrt(u), D=(1+B)/2−(1−cos(2x))/(2u) and E=1+(B+cos(4x))/2+(sin x−sin(3x))/x, I rebuilt its Taylor coefficients as exact fractions and certified F70/u^4>1/100 by centered Taylor bounds on 36 closed intervals of width 1/4, without using the uploaded Bernstein implementation. Replay: python3 -I -B /workspace/branches/review-3-certificate.py. The cubic-and-lower coefficients vanish, and leading coefficients agree with the source. On |u|=100, the four original trig majorants follow from e<3 using sinh(10)/10, sinh(20)/20, cosh(20), cosh(40), and imply |F|<10^29. Cauchy's bound gives the certified tail <u^4/1000 for 0<u<=9, so the positivity is uniform, not sampling. For omega>=3, the exponential Gram eigenvalues are >=1/3 from absolute off-diagonal row sums <=2/omega, hence K<=9. As omega tends to zero, the rescaled basis 1,sin(omega t)/omega,2(1−cos(omega t))/omega^2 tends to 1,t,t^2 at the observation and evaluation points. The Legendre kernel then gives 1+12+5(11/2)^2=657/4 and yields a limiting extremizing family but no positive-gap equality. Reflection and unimodular modulation preserve the estimate.

## originality

PASS

The exact exterior positive-gap rigidity and sharp constant are distinct from the available endpoint and two-frequency theorems. General sparse-Fourier extrapolation controls growth rate, not this sharp finite-dimensional constant. The collision limit and the Gram-matrix method by themselves are not original.

## value

PASS

The far endpoint of the adjacent unit prediction interval is a natural test point for sparse extrapolation. The three-tone result gives an exact evaluation benchmark beyond the two-tone case and distinguishes every genuine finite gap from the confluent quadratic limit, a conclusion not available from growth-rate estimates or the limit calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

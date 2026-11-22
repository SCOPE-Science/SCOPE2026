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

Fourier inversion of the first slice makes h_0(n)=f(n)conj(g(n-x0))=C omega^(an), nonzero pointwise, so f and g have no zero coordinate. The next slice gives ratio R(n)=h1/h0=alpha omega^(un)+beta omega^(vn); the telescoping product for j shifts factors into q-Pochhammer partial product with q=omega^(-s(c-b)) order d and z=omega^((c-b)n), z^d=1. The cyclotomic full-d block equals 1-(-t)^d and is nonzero because all window ratios are nonzero. For r<d, Gaussian q-binomial coefficient factors (1-q^h) have h<d and are nonzero, and distinct z^0..z^r frequencies cannot collide. Multiplicative character pre-factor shifts frequencies only. Summing N/d complete repetitions gives N(d+1)/2. Existence: alpha=(1+(-0.7)^d)^(1/d)>0.7, beta=0.7, R(n)=alpha+beta omega^(Nn/d), whose cyclic product is 1; nonvanishing then gives consistent nonzero g and f=1/conj(g). This algebra is valid for every composite N, not numerical FFT threshold extrapolation.

## originality

PASS

Conditional neighboring-slice rigidity differs from both global STFT support minimizers and sparse window/signal support gaps. The discrete Gaussian-binomial expansion is classical; the asserted contribution is its forced all-row cyclic frequency staircase under two neighboring Fourier profiles.

## value

PASS

A local measurement of only two adjacent time slices forces the exact complete STFT support and its divisor arithmetic. This is a meaningful rigidity theorem in finite time-frequency analysis with constructive attainability, not a generic uncertainty bound or routine substitution into one such bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.

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

The stated noiseless model on the entire line gives an L1 convolution with k_v(s)=h(s/v)/v for s>=0 and zero otherwise. Its transform is C(xi)H(v xi). Both transforms have no real zeros; with a=v2/v1 in (0,1), the N-term measured ratio product at a^j omega/v1 is H(omega)/H(a^N omega). H is continuous at 0 and H(0)=1, proving the exact reconstruction including omega=0 without any branch of a logarithm or extra moment condition. Division gives C and Fourier injectivity gives uniqueness a.e. At one fixed positive speed, use distinct unit-mass exponential h1,h2 and the unit-mass Laplace g. Swapping their spatial kernels between convolution with g and the sensor leaves the same product and produces distinct admissible nonnegative sources and responses with nonzero transforms. The finite-second-moment formulas solve the two mean and variance equations of X+vU; for existing higher cumulants independence gives the analogous linear equations. An independent arithmetic replay gave a telescope error of about 1.24e-16 (1/normalization limit error 4.87e-13 at 40 factors), recovered E[U]=0.6 and variances 0.573333 and 1.28, and reproduced the one-speed alias at a frequency where the source transforms were separated by 0.222.

## originality

PASS

The supported distinction is the explicit nonparametric inverse for two full outputs of a common source through positive speed dilations of a single normalized causal L1 sensor, with one speed minimal in that class. Blind multichannel identification, convolution ambiguity and Fourier factorization are prior principles, not new here. The strongest inspected multichannel theorem relies on finite-dimensional sparse channel structure, not satisfied by the general impulse responses here. No independent covering statement was established by the bounded comparison.

## value

PASS

Two controlled traversal speeds supply a minimal sufficient experimental design within an infinite-dimensional blind model: the sensor need not first be externally calibrated, and repeating the same speed cannot substitute. The exact inverse and the one-speed indistinguishable pairs give complementary benchmarks for subsequent stability, sampling or calibration work. This goes beyond reporting a Fourier-domain product.

The dated certificate retains the supplied scientific assessment, sources and limitations.

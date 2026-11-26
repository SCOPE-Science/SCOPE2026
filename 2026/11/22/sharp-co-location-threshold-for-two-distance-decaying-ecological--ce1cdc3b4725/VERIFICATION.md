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

Conditional independence makes the integrand the sum of two single-device responses minus their product. On splitting at the device coordinates the product kernel is constant between the devices and exponential on the two outer intervals, giving the claimed exact formula, including d=0 and endpoints. At fixed gap the center derivative has the sign of ℓ/2−c because its other factor is positive even at p=1 (the two boundary exponentials have sum strictly below 2). The maximal allowed gap has only one feasible center. With the center fixed at ℓ/2 the gap derivative has the sign of p−exp(−ℓ/2)H(d) for d>0. H is strictly increasing with H(0)=1 and exp(−ℓ/2)H(ℓ)=(exp(ℓ)−1)/ℓ>1. This proves unique midpoint co-location including at equality, and one interior global maximum above threshold. H(d)=1+d+13d²/24+O(d³) gives the onset and d*/ℓ→1/2 at p=1, yielding quarters, whereas fixed p<1 yields exact midpoint placement as ℓ→0. The root logarithm 3d*/2−log d*+log(1−exp(−d*))=ℓ/2+log p first gives d*/ℓ→1/3 at fixed p>0 and then the stated logarithmic correction including the constant. At (ℓ,p)=(2,0.7) an independent bisection and composite Simpson integration of the original conditional probability on the three segments gave gap 0.626998110087, optimum 0.679671811520 and midpoint value 0.673125926750.

## originality

PASS

Credit prior centering and quarter/third geometry in the discrete certain-on-site analogue, and the co-location phenomenon in different continuous Gaussian models. The supported distinct contribution is the exact arbitrary-placement global threshold, unique positive-gap equation and its quantitative behavior in the uniform interval with exponential absolute-distance response and adjustable on-site probability. The inspected sources do not cover this combination; priority outside the bounded comparison is not established.

## value

PASS

An exact global design boundary in this naturally normalized two-device problem distinguishes when placing both devices together beats forcing them apart. It controls all placements including equality, and the singular p=1 short-length limit explains why exact on-site detection is qualitatively different from arbitrarily high but fixed imperfect detection. Together with the separation law this makes a useful benchmark against which to test different kernels, location priors or dependence models.

The dated certificate retains the supplied scientific assessment, sources and limitations.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For w=n+1/2 and f(theta)=sqrt(1+sin^2(theta/2))-sin(theta/2)-1, the defining sine-transform difference has f(0)=0, f(0)=1/4, f^(4)(0)=-7/16; odd derivatives at pi vanish by evenness near pi and cos(pi w)=0. Repeated exact integration by parts therefore gives D(n)=-1/(4pi w^3)-7/(16pi w^5)+O(w^-7), with exact reflection D(-n-1)=-D(n). Nonzero cubic coefficient gives weighted l1 convergence iff alpha<2 and two-sided omitted-tail l1~1/(4pi R^2). Convolution endpoint operator norms on l1 and l∞ equal the l1 kernel sum, with general lp upper bound by Young. Independently integrated the source Fourier formula at n=10,20,40; relative two-term expansion ratios 1.000688,1.00004378,1.00000283. All boundary normalizations are fixed at half-integer positions.

## originality

PASS

The full primary Petrov 2025 preprint, Sect. 4.2 Lemma 4.2, studies the *identical* fully discrete Hilbert kernel and its Riesz–Titchmarsh difference but gives only O(n^-2) and ordinary l1 summability. It does not give the two nonzero coefficients, exact alpha=2 weighted cutoff, or sharp 1/(4pi R^2) finite-stencil endpoint norm. Nearby published Hilbert results concern cyclic or semi-discrete transforms with different kernels. The improvement is a valid strict refinement of the primary theorem, with residual historical risk from older oscillatory Fourier analysis.

## value

PASS

The discrepancy D is a natural operator-level error between Petrov’s fully discrete boundary Hilbert transform and a canonical half-grid singular transform. The exact cubic tail reveals an unexpectedly better truncation rate, exact error constant and maximal polynomially weighted convolution space. These are directly useful to finite-stencil approximation and weighted operator estimates, unlike an arbitrary coefficient exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.

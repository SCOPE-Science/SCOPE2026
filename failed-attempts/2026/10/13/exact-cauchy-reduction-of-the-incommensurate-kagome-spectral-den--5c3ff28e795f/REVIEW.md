# Independent mathematical audit

## correctness

FAIL

The central sign reduction and density integral are correct, but the frozen Finding literally asserts the satisfying set for a non-strict inequality as a union of open intervals and omits the transition slice. For example x=1, y=r_A(1)=3 gives product zero and satisfies the inequality but belongs to neither claimed open interval. Both endpoints must be included on each side of x_0; at x=x_0 the two middle roots coincide and the satisfying set is the entire closed interval [c_-,r_A]. The discrepancy has zero measure. The product of the three tangent factors has denominator (1+x²)^2(1+y²)^2; the roots satisfy c_-<r_B<r_A and c_-<c_+<r_A, with the only crossing r_B=c_+ at x²=3/5. On a fundamental square, the irrational flow gives Haar measure and independent Cauchy tangents; boundary sets have measure zero. The arctangent sum and difference identities (c_-c_+=-3, c_-+c_+=-4x) give the stated angular lengths. The same density applies to the energy-scale probability by weighting momentum by 2k and integrating by parts; this concerns the leading band condition, not exact finite-k band edges. Independent replay: /workspace/branches/8e755b8b-4247-4184-b173-46fdbd204ee7/independent_integral.py gives 0.639080422792130 by adaptive quadrature in x and after x=tan t; these error estimates are not rigorous enclosures. The source's 0.639081 is a close numerical approximation rather than the nearest six-decimal rounding. Frozen verify.py and VERIFICATION.md were inspected, not executed. Closing the intervals would not remove the decisive originality failure.

## originality

FAIL

The distinct October 4 indexed finding gives the same leading-condition reduction to a one-dimensional Cauchy integral, the same breakpoint, and the same high-precision constant. This is not mere overlap of the decimal or source model: conditioning on the c-phase tangent and changing the other tangent by a circle rotation identifies the conditional angular measures pointwise. The simpler arctangent expressions in the frozen presentation do not make a different exact invariant or non-equivalent reduction.

## value

FAIL

The exact one-dimensional representation is intrinsically informative relative to the physics paper, but already available for precisely this model. Relative to that representation the frozen contribution is a rotation of the phase slice and shorter arctangent expressions, with the same breakpoint and numerical content, and no demonstrated mathematical need for the algebraic restatement. An endpoint correction does not leave a distinct worthwhile result to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.

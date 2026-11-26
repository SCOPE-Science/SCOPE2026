# Independent mathematical audit

## correctness

PASS

Gaussian Fourier differentiation in degrees four and two forces the quadratic part to be −ΔQ/(8π), cancels the constant transform correction exactly, and rules out Q≡0 for a nonzero eigenfunction with f(0)=0. If A=Q|_S is negative anywhere, it is uniformly negative on a smaller spherical patch and the leading term forces an infinite-volume negative cone at large radii. If A>0, the directional squared endpoint is u=((d+2)/(2π)+Δ_SA/(8πA))_+ (the later ν notation refers to the same untruncated expression defined as u in line 66). Exact polar integration and convexity of the positive-part d/2 power give the claimed inequality because spherical integration by parts gives E[Δ_SA/A]=E|∇_S log A|². This average is strictly positive unless A is constant. For nonnegative A with zeros, the perturbation Q+ε|x|⁴ changes f by εe^(−πr²)r²(r²−R₀²). Inside R₀, volume convergence follows by dominated convergence on a finite-volume ball and the null polynomial zero set; outside R₀, indicators for the strict negative set increase to the original indicator as ε decreases. A nonconstant nonnegative smooth A has a patch with A>0 and gradient bounded away from zero, producing a uniform positive angular penalty for the perturbations. Thus the limit is strictly above the radial minimum, including if it is infinite. Direct polar integration of the planar harmonic perturbation gives 2/√(1−ε²); independently computed angular quadrature at ε=0.2 and 0.8 corroborated the areas 2.0412414523 and 3.3333333333 and saturation of the planar angular bound. The nested artifacts/verify_quartic.py was inspected but not executed. Its recorded sample calculations are not a proof of the full-shell theorem.

## originality

PASS

Pass for the supported distinct theorem: the all-dimensional sharp minimum and uniqueness across the entire degree-at-most-four shell, in particular nonnegative noncoercive quartics with spherical zeros. The positive-leading quantitative formula is already identically covered by distinct record 637249742702, and the earlier planar catalog statement materially overlaps the d=2 result. Neither covers the spherical-zero extension in dimensions d≥3 in the compared evidence. The planar example is illustrative and not credited as a separate originality contribution. The two all-dimensional records share a date, which establishes neither direction of historical priority.

## value

PASS

An exact solution in the entire first nontrivial positive Fourier–Hermite shell is a useful finite-dimensional benchmark for the unrestricted definite-set problem. Closing the noncoercive boundary matters: positivity of the leading quartic was not required by the original optimization, and deleting boundary competitors without a strictness argument would not establish the unique radial minimizer. The overlapping coercive penalty and planar example provide interpretation, not the incremental value.

The dated certificate retains the supplied scientific assessment, sources and limitations.

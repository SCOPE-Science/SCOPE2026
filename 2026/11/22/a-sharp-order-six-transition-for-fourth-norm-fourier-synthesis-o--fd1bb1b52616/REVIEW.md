# Independent mathematical audit

## correctness

PASS

Unitary convolution and Parseval give ∑|f̂|⁴=N⁻¹∑|f*f|². Modulating a maximizing character to the trivial one and scaling nonzero sum to 1 produces the upper bound (N min Φ)⁻¹/⁴, with Φ the squared convolution energy. It is strictly convex on the complex vector space viewed over the reals because it is the sum of strictly convex fourth powers on the injective Fourier image. It is coercive by finite-dimensional norm equivalence. Conjugation and z→2x+3d−z preserve the affine constraint and energy, hence by uniqueness the minimizer has real weights (t,1/2−t,1/2−t,t). The convolution outputs are at 2x+kd; equality of these sites depends only on k modulo m, so no ambient-group embedding assumption is needed (the original support is a coset, not necessarily the subgroup). Squaring and collecting the seven coefficients leaves only the 4, 5, 6 and ≥7 quartics. The first two derivatives have unique real zero 1/4, and the latter cubics have positive quadratic derivatives by their negative discriminants and strictly opposite signs at 1/4 and 1/2. Thus all weights of the optimal profile are positive, which ensures the trivial character really maximizes the Fourier absolute value and the upper bound is attained. Reversing normalization gives all complex equality cases. Independent bisection and convolution give t₆=0.2748888295956773677… and t∞=0.3104604169623260244…, with relative ratio gains over the indicator of 0.22572947…% and 1.25649476…%, respectively. Replay: RESULT.md Proof §§1–5, including coefficient aggregation at lines 54–58; packaged verification script inspected as text only. Scope: four consecutive distinct sites with step order m≥4 and counting-measure Fourier norms, not all four-point sets or other norm quotients.

## originality

PASS

The supported distinct claim is the explicit nonuniform optimal Fourier-evaluation profile at m=6 and m≥7 and its arithmetic transition, not the affine-transitive cases m=4,5 or the use of strict convexity. Strongest same-objective overlaps concern line supports; strongest same-support overlap has a different normalization and objective.

## value

PASS

This exactly resolves a canonical four-site family for a motivated sharp synthesis constant beyond the affine-transitive case. The significance is the change from uniform weights to a unique endpoint-heavy profile at the first relevant collision order and its stabilization, including full complex equality classification, rather than the small percentage gain alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

Stable two-step scalar affine recurrence has unique fixed two-cycle p=[a(1-eta b)u+bv]/D and q=[au+b(1-eta a)v]/D with D=a+b-ab eta>0. Their arithmetic center satisfies (p+q)/2-x* =ab eta(a-b)(u-v)/[2(a+b)D]. Squaring under F=(a+b)/2 yields exact excess. At fixed cycle, a(p-u)+b(q-v)=0 by cancellation of consecutive steps, hence (a p+b q)/(a+b)=(au+bv)/(a+b)=x*. Independent SymPy symbolic cancellation and numeric example reproduce identities for stable parameters. This proves only constant-step deterministic scalar two-component quadratic limit, not random-order SGD.

## originality

FAIL

FAIL under the claim-versus-prior implication test: classical incremental-gradient theory already gives the constant-step cyclic limit-cycle framework, even for linear least-squares, and its exact within-cycle balance x_next=x-eta sum_i ∇f_i(phase_i). Specializing that general balance to two scalar quadratics immediately yields the advertised curvature-weighted center; solving the two-by-two affine map gives the bias and gap via textbook substitutions. The formula may not be printed verbatim in SWA papers, but it is mechanically covered by the known general fixed-cycle identity with no new structural obstacle. No credible independent principle beyond this direct specialization remains.

## value

FAIL

FAIL independently of correctness: the entire analysis is the elementary fixed point of two scalar affine contractions, with objective gap its square. The existence of constant-step cyclic gradient bias and phase oscillations is classical and already emphasized for linear least squares; the two-phase average does not demonstrate a new learning guarantee or a nonroutine boundary for SWA as deployed in the primary deep-learning setting. Its correction requires known a,b and is an immediate cycle-stationarity identity. This is a useful instructional example, but the intrinsic claimed research-level mathematical increment is too thin.

The dated certificate retains the supplied scientific assessment, sources and limitations.

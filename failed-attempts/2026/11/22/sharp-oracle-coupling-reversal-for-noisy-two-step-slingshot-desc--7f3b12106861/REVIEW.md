# Independent mathematical audit

## correctness

PASS

The two signed descent/ascent steps act respectively by I−rS and I+rS, with noise signs −h,+h. Thus the pair endpoint is a z+h[ξ₁−(I+rS)ξ₀], with a=1−r². Centering and independent pairs give the exact sum of innovation second moments, with geometric ratio a²; the horizon and invariant-risk optima reduce to the same positive multiple of the one-pair cost. In the two swap eigendirections the marginal variances are v and Cauchy–Schwarz gives cost at least v(|1±r|−1)² per coordinate. Nonzero multipliers force equality or sign reversal almost surely; isotropy makes both equalities feasible together. At r=1 the plus equality remains necessary, and one can take an independent minus output with the prescribed marginal. Consequently the optimizer is unique off r=1 among arbitrary joint laws, as claimed. Division by 1−a²=r²(2−r²) gives the stationary formulas; independent noise has total pair cost v(4+2r²), and identical reuse has 2vr². The finite-horizon and small-r limits follow. The conditional-unbiasedness caveat concerns conditioning on the full information after the first call; with that requirement the cross term is zero. Bounded exact reproduction checked multipliers and several horizons, including R*=18/41 at r=3/5 and swap/reuse/independent risks 26/7,36/7,86/7 at r=6/5 with σ=v=1.

## originality

FAIL

No distinct retrieved source was shown to print this exact GDA formula. The core claim is nevertheless mechanically covered: take the known signed GDA update matrix for the second call and use it as the argument of the classical squared Gaussian transport/orthogonal Procrustes problem. The optimizer is its polar factor; its sole sign change is read directly from 1−r. The rest is a scalar geometric series or elementary second moments. The rejection is based on this exact implication, not on inaccessible primary text or a matching title.

## value

FAIL

The benchmark is well posed and can illustrate coupling versus fresh calls. But its only optimizing decision is the sign of one known propagator eigenvalue in the standard polar alignment problem. The horizon risks and comparators then follow by routine substitutions; neither the singular point nor the stationary limit resolves an additional research obstacle beyond that established implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.

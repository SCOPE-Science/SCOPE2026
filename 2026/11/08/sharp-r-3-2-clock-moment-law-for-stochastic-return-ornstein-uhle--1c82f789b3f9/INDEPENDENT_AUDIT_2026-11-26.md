# Independent mathematical audit

## correctness

PASS

Both phases have generator d²/dx²−k_j x d/dx and the target stays absorbing. For U(x)=∫_x^1 K, direct differentiation gives L₂U=−1 and 1+L₁U=(k₁−k₂)xK(x); the natural left-boundary behavior of U is logarithmic (Gaussian Mills bound). The return solves the scale-function problem on (0,1), and a return from x≤0 cannot reach 1 without first reaching 0. The mean duration of a full cycle is therefore p_r U(0)+(k₁−k₂)A_r by stopped Dynkin, including U(1)=0 on either success path. The independent clock can be revealed at time zero; ties have probability zero even for clock atoms because the search hitting time has no atoms. Each cycle has finite mean and positive success probability. The exact ratio follows by renewal. Locally xK(x)=K(0)x+x²+O(x³); a smooth cutoff, the centered Gaussian OU law and symmetry give g(t)=2t+O(t²). The absorbing-boundary error is exponential in 1/t by the OU time change to Brownian motion and reflection. H(x)~x₊/S₂ gives h(t)~√t/(S₂√π). Boundedness on x<1 gives global bounds |g(t)|≤Ct, h(t)≤C√t, and the reflection estimate gives P(τ≤t)≤Ct². Thus r²A_r→E[W²] and √r p_r→E[√W]/(S₂√π) by dominated convergence. Dividing gives the displayed signed coefficient and both clock examples; equal stiffness is exact. This is pointwise in fixed k₁≥0, k₂>0 and the independent positive finite-second-moment clock law. Independent finite corroboration: /workspace/fast_clock_replay.py uses direct cycle-time/success quadrature at k₁=0,k₂=2, not the defect identity. At r=25600 the deterministic and two-point scaled corrections are −5.1852355 and −6.7104213 against −5.1849654 and −6.7098390. The frozen checker was inspected, not run; no finite test establishes the general limit.

## originality

PASS

Pass for the sharp arbitrary-finite-second-moment clock law, not for renewal, the Poisson model or its limiting mean, or the pathwise equal-stiffness observation in isolation. The closest earlier exact formula is Poisson only; the generic arbitrary-clock formula needs a new small-clock numerator cancellation and success expansion to yield the moment ratio. The stronger transform-level SCOPE result is explicitly later and credits the frozen mean law.

## value

PASS

The limiting pure-return MFPT was known in the Poisson model, but is insensitive to how often search is interrupted. The leading signed correction distinguishes clocks of the same mean and quantifies which features of their shape survive rapid resetting. The precise exponent, explicit coefficient and stiffness sign are useful for designing and comparing high-rate benchmarks; no finite-rate ordering is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.

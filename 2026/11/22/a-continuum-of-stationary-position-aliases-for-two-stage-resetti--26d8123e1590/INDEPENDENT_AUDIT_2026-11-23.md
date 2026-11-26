# Independent mathematical audit

## correctness

PASS

Write the Erlang clock as two independent exponential stages. Brownian increments over the two stages are independent and have the same Laplace density kappa exp(−kappa|x|)/2; its self-convolution is the displayed endpoint law. Per unit mean exploration time the two stages contribute with equal weight, the first occupation law being Laplace and the second its self-convolution; this yields the exploration density and b_D=1/4. For a return endpoint y, integrating dt=du/(c u^alpha) up to |y| and applying Tonelli yields the return occupation for either sign of x. Substituting the endpoint density and using Gamma(2−alpha)=(1−alpha)Gamma(1−alpha) gives b_R=1/(3−alpha) and finite mean return duration Gamma(1−alpha) kappa^(alpha−1)(3−alpha)/(2c). The chosen immediate departure rules out waiting at u=0, and the cycle law is regenerative with finite mean and nonarithmetic duration (condition on the clock; the absolute Brownian endpoint has a density and its duration map is strictly increasing). No origin atom occurs. Normalizing cycle rewards gives the stated weight and full equilibrium law. At fixed D,r, c maps bijectively to 0<w<1, so the strict attainable interval at fixed alpha, the union, the analytic fibers and exclusion of both overall endpoints follow; equality of densities is equivalent to equality of b (varying kappa would additionally require matching the exponential decay rate). The example gives (w,b)=(2/5,3/10) and (2/3,3/10), and u=c²s²/4 at alpha=1/2 yields acceleration c²/2. Integrating the radial density gives the CDF and moments. Its signed difference has a unique radial crossing at one, and the positive area of exp(−z)(z−1) is 1/e, giving TV. Phase labels invert the return moment and the odds w/(1−w). Independently replayed /workspace/reviews/evidence/2-return-clock.py, using stage characteristic functions and quadrature of return cycle rewards at four frequencies for four parameter sets, including alpha=0.999 and both examples; the normalization and normalized return second moments also passed. This bounded check is not the continuum proof.

## originality

PASS

Qualified to the complete cross-exponent stationary inverse-fiber result for the fixed Erlang-two clock. General renewal occupations, acceleration and invariance in the exponential-clock case, and the Erlang constant-speed specialization are prior results, not standalone novelty. No inspected primary statement establishes this nontrivial compensation between return shape and speed under a nonmemoryless clock.

## value

PASS

The first nonmemoryless Erlang clock provides a natural inverse problem: the usual fixed-speed-shape family is identifiable in speed yet the full unlabelled law cannot tell ballistic motion from constant acceleration or select from a continuum of protocols. The formulas classify all observable shape values and quantify exactly what a phase-labelled measurement adds. This is a structural identifiability result, not a numerical collision or statistical guarantee at finite sampling noise.

The dated certificate retains the supplied scientific assessment, sources and limitations.

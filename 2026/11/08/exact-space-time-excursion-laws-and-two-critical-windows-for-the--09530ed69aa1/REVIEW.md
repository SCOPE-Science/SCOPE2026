# Independent mathematical audit

## correctness

PASS

Conditional uniformity on each affine itinerary yields transition cutoff levels 1,1,1,2,j-1 for j>=5. The normalized four-level weights give the stated departure probability alpha and a geometric initial height H given departure. The outside steps have iid increments K-1 with K geometric on the nonnegative integers. Strong Markov at each downcrossing gives r^h and r=z(1-lambda)/(1-lambda r); the unconditional defective PGF simplifies to (1-alpha)z+alpha r^2. For n>=2 Lagrange inversion gives alpha (2/n) binom(2n-3,n-2)(1-lambda)^n lambda^(n-2), verifying the critical formula; r(1)=min(1,q) gives escape alpha(1-q^2) when q<1, and r'(1) gives the subcritical mean. For maximum height the harmonic q^h and memoryless exit overshoot with E q^overshoot=q yield (q^h-1)/(q^(L+1)-1) for starts below L. Exit is a.s. for fixed L (a block of L downward steps suffices), with integrable upper-exit overshoot; the initial geometric H also has the same overshoot conditional on H>=L. Averaging gives numerator E q^H-1=q^2-1; q=1 is the continuous limit. Positive-drift escape is unbounded by the law of large numbers, and the other phases return a.s. At lambda_N, the finite masses divided by their critical values equal (alpha_lambda/alpha_1/2)(2lambda)^(-2)[4lambda(1-lambda)]^n for n>=2. Critical masses are bounded by a constant times n^(-3/2), justifying the temporal Riemann sum on n>N with truncation error O(R^(-1/2)) beyond RN. Its limit is alpha_1/2/pi^(1/2) times the integral over [1,infinity) of t^(-3/2) exp(-4u^2 t); the scaled escape atom adds 8 alpha_1/2 max(u,0). Evaluating the integral gives the advertised erfc crossover. The height crossover follows from log q=-4u/L+O(L^(-2)) and the critical formula at u=0. Ran python3 /workspace/review_replay.py (section 2) for exact independent affine-image return masses through step 18 at three rational parameters and escape algebra; that bounded check does not establish either limiting law. Inspected the original verifier without executing it.

## originality

PASS

Distinct contribution on current evidence is the all-parameter height distribution for the four-level Lebesgue return experiment and the explicit joint presentation of its L^(-1) height window and the defective time-tail crossover. Substantial prior coverage applies to the time kernel, time-scale width, and critical height component, and the return-law contribution is an explicit change of base using known bulk PGFs, not a new skip-free theorem.

## value

PASS

Time and maximum height are natural observables on the same explicitly sampled excursion. The exact spatial formula, including the escaping mass, and the contrast between L^(-1) and N^(-1/2) windows offer a quantitative benchmark beyond detecting a conservative/dissipative phase change. The critical and off-critical comparisons tell a researcher how to scale two competing finite thresholds, without confusing this clock or map with that of the original dynamical family.

The dated certificate retains the supplied scientific assessment, sources and limitations.

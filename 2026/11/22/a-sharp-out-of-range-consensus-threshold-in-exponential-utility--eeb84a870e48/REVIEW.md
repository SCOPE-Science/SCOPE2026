# Independent mathematical audit

## correctness

PASS

For the stated synchronous exponential rule, the gap is (1−2μ)^t d and the mean increment is μd r^t tanh(ar^t), with a=κd/2 and r=|1−2μ|. The gap retains admissibility and the increments sum absolutely. For μ≤1/2 the updates are convex combinations; for μ>1/2 the crossing function μ Σ r^j tanh(ar^j) increases strictly and continuously from tanh(a)/2 to infinity. At crossing the weak-gradient tanh bounds leave 1−μ_c between a(1−a²/3)/2 and a/2. The zeroth term in the strong-gradient equation bounds μ_c−1/2 by 1/(e^(2a)−1); the rest is O(ae^(−4a)), giving the claimed equivalent. Monotone sum–integral comparison at mesh −log(2μ−1) gives the stated divergence coefficient and bounded remainder. Independent bisection and series evaluation recover μ_c=0.764874065819… and L_0.9=1.691149330027… for κ=d=1 and x_0=0. One strictness sign in the mean-increment proof should be non-strict for t≥1 at μ=1/2, when the first update already gives consensus. The source's Eq. (1) directly uses 2μ; its algebra agrees at N=2, but it does not support attributing a general μN/(N−1) normalization to that equation. Neither issue changes the stated two-agent theorem. The supplied checker was inspected, not executed.

## originality

PASS

Credit the originating utility rule, real-valued opinion space, admissible high learning rates, and geometric gap contraction to the preprint. Pass only the unique deterministic exponential-utility hull-exit threshold, its endpoint asymptotics and its quantitative consensus divergence. The inspected comparisons do not already decide these claims.

## value

PASS

An exact boundary between in-range and out-of-range agreement is useful here because the source rule permits over-relaxation, yet its disagreement contracts at every fixed admissible learning rate. The unique boundary and its opposite-end asymptotics distinguish this structural effect from an isolated overshoot example. The result is limited to synchronous noiseless pairs and unclipped opinions, and is not a claim about larger or stochastic populations.

The dated certificate retains the supplied scientific assessment, sources and limitations.

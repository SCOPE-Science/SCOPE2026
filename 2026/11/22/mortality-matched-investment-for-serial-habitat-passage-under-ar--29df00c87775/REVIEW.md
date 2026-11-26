# Independent mathematical audit

## correctness

PASS

For the abstract serial continuous-time chain, the joint success subdensity has factor uv and exponents a=u+d_1, b=v+d_2. Integrating on x+y=s gives uv·s·exp(−(a+b)s/2)·sinhc((a−b)s/2), continuously at a=b. Swapping u and v keeps uv and a+b fixed. If d_1>d_2 and u>v the squared absolute exit-rate difference strictly increases by 4(u−v)(d_1−d_2) over the swapped value, giving strict improvement for all weights in scope (bounded nonnegative Borel, positive on a positive-measure set). The positive derivative of sinhc at a positive argument also gives J_w'(C/2)>0, so balance cannot be optimal. The other ordering follows by interchanging indices; the objective is continuous on [0,C], positive inside and zero at both endpoints. Equal losses give success probability uv/(uv+dC+d²), strictly maximal at balance. The conditional exponential-sum survival function with fixed mean exit-rate parameter m is e^(−mt)[cosh(ηt)+m sinh(ηt)/η], increasing with rate imbalance η, so a nonincreasing reward and strict success comparison imply unique balance. For small T, integrating the analytic series gives 2J_T/T²=uv[1−KT/3+(K²/16+δ²/48)T²+O(T³)] uniformly through two u derivatives, with K=a+b and δ=a−b. Strict concavity follows. The stationarity equation first gives displacement O(T²) and then C²(d_1−d_2)T²/96+O(T³). For large T the exponentially bounded derivative tails imply uniform C² convergence. The eventual-success log has strictly negative second derivative; at its root the ratio satisfies (u/v)²=d_1(C+d_2)/[d_2(C+d_1)]. Uniform convergence localizes all finite-deadline optimizers to this root and then local strict concavity gives eventual uniqueness. Equality at intermediate deadlines is not asserted either way. I inspected the packaged SciPy checker without running it. A separate decimal evaluation of uv[(1−e^(−bT))/b−(1−e^(−aT))/a]/(a−b) and numerical stationarity for the frozen example gave u≈1.89630479, J≈0.294939543, and J at balance≈0.278364504, supporting the illustration but not certifying intermediate-horizon uniqueness.

## originality

PASS

The distinct mathematical result is the all-reward strict allocation ordering for the two-stage irreversible fixed-rate-budget model, together with the hard-deadline optimizer asymptotics. The convolution formula, the conditional stochastic comparison used at equal losses, and the individual exponential clocks are not credited as new. The closest checked fixed-budget and serial-passage results optimize different quantities or compare different route types. The Bon–Păltănea primary text could not be recovered; potential overlap with a stronger stochastic order is expressly not ruled out by a search miss.

## value

PASS

In a simple absorbing Markov chain, the sign of the optimal departure from balance is invariant under arbitrary admissible reward windows, and not just under eventual success or monotone deadlines. This is a substantive structural comparison of objectives; the short-horizon bias and explicit limiting split quantify two different deadline regimes rather than merely reparametrizing the clocks. Its significance is as an exact benchmark for independent exponential hazards and a linear rate budget, not empirical or operational guidance. No general uniqueness, calibration, correlated-hazard or larger-network conclusion is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.

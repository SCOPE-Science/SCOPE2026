# Independent mathematical audit

## correctness

PASS

Conditioned on the observed value, the left and right bridge pieces are independent; reflection gives their respective crossing probabilities q_t and q_b below the barrier, yielding g=q_b+q_t-q_b q_t. The midpoint squares to three exponential terms with coefficients 4,-4,1; Gaussian tilting of the truncated integrals and addition of the upper tail give the exact coefficients 5,-4,1 in the Finding. Away from the midpoint, the tilt by q_b squared shifts the observed mean to 4ht. Below t=1/4 the shifted observation is linearly below h, and at equality the retained half-Gaussian still has h(h-Y) diverging almost surely under a fixed centered coupling; in both cases g/q_b tends to one in the truncated tilt, with bound 2. This gives the interior saddle equivalent and the boundary factor 1/2. Above t=1/4 the change u=h(h-Y) has an integrable rescaled envelope since 4t-1>0. Its six term integrals, divided by v, are 1/(4b-1), 1/(4t-1), 1/3, 2, -2/(2b+1), -2/(2t+1); the Gaussian upper tail adds 1. The decay exponents are all strictly below 4 at fixed interior times, so subtraction of the squared mean is negligible. At the midpoint C=10/3 and the exponent is uniquely smallest by monotonicity on the half-interval and symmetry. Endpoints are deterministic, and neither a moving-time limit nor a finite-h global optimum follows. A fresh bounded midpoint diagnostic using composite Simpson quadrature, 60000 subintervals on each side of h over [-8,8] and on [z,20] for each standard-normal tail at z=2h,4h,6h, matched the exact second moment to relative error below 2e-14 at h=0.35,1,1.9. The supplied script was inspected, not run; finite diagnostics do not certify the limit.

## originality

PASS

Best-of-knowledge pass for the explicit fixed-time large-barrier equivalents and leading constants of the one-observation explained variance, not for the classical reflection identity, Gaussian tilting, or any general claim of sampling-time optimality. The closest distinct indexed problem changes the bridge, the observation protocol and the optimization question. No available evidence establishes coverage of the three fixed-time regimes.

## value

PASS

This quantifies how much one real-valued observation of a canonical pinned diffusion can explain about a rare exceedance. The exact prefactors distinguish the interior, critical, and boundary-dominated regimes; even the best fixed time on the exponential scale explains only order 1/h of the target variance. This is useful for fixed-sample rare-event estimation benchmarks and goes beyond routine evaluation of one reflection probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.

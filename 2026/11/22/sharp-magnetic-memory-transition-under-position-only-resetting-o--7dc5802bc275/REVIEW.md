# Independent mathematical audit

## correctness

PASS

A two-sided stationary OU velocity and independent Poisson clock give the stationary position by integration from the last reset. The exponential age and finite OU second moments justify the integrations; the positive damping and occurrence of resets remove dependence on initial data. For an independent derivation put z=-gamma+i*omega and K(u)=Theta Re exp(z*u) at u>=0. The age integral gives S=C(0)=(2/r) integral_0^infty exp(-ru)K(u)du. The mixed correlation with future velocity at v>=0 is integral_0^infty exp(-ra)K(v+a)da=Theta Re[exp(z*v)/(r-z)]. The part of X_1(0) retained in X_1(t) gives exp(-rt)S; each future velocity increment at v is retained exactly when there is no reset on (v,t], an event independent of the clock before zero and of the entire velocity process. Integrating the mixed correlation with this survival factor gives the stated resolvent. The coefficient of exp(-rt) has numerator Theta[(r-gamma)(r-2gamma)(r+gamma)+(r+2gamma)omega^2] over the stated positive denominator. For r<gamma it is strictly positive and dominates; analyticity precludes compact-interval accumulation of zeros. For r>gamma the nonzero e^{-gamma*t} harmonic dominates and alternates strictly at arbitrarily large times. At r=gamma the covariance is a positive damping factor times 3+cos(omega*t)+(2gamma/omega)sin(omega*t), whose minimum is 3-sqrt(1+4gamma^2/omega^2). At equality the minima are isolated tangencies, not sign reversals. This checks both directions of the claimed classification and the thermal-intensity independence. The supplied check.py and verification notes were inspected, not run. The separate /workspace/branches/review-replay.py checked the survival-integral and resolvent representations by bounded quadrature; the sign theorem does not depend on numerical tests.

## originality

PASS

Position-only inertial resetting, magnetic or active reset models, and several stationary covariance sign boundaries have prior coverage. Credit none of those ingredients, nor generic linear resolvent methods, as new. The supported distinct result is the exact stationary Cartesian lag-sign transition for a freely moving planar thermal magnetic OU velocity retained at complete spatial resets, including the offset-amplitude threshold and tangential boundary on the resonant line. The comparison is limited to the statements and models actually inspected.

## value

PASS

The survival of velocity memory under complete position erasure makes the stationary position autocovariance a natural observable. The calculation identifies not merely a crossover of two decay scales but exactly when arbitrarily late negative covariance remains possible, including a separate nonnegative tangency boundary. This distinguishes true reversals from zeros and shows why faster spatial resets do not remove the slowly decaying cyclotron contribution. The result does not count transient negative bands for r<gamma or assert measurable amplitudes at late times.

The dated certificate retains the supplied scientific assessment, sources and limitations.

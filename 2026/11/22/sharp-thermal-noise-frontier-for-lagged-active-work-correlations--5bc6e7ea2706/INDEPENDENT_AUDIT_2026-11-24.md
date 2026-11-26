# Independent mathematical audit

## correctness

PASS

Independently split the stationary position into the response to V and the centered thermal OU position, independent of V. The two resulting work integrals have zero cross covariance by conditioning on V. The thermal OU position covariance is (D/kappa) exp(-kappa |t|); its mixed time derivative is 2D delta_0 - D kappa exp(-kappa |t|). Multiplication by the independent propulsion covariance gives exactly the negative regular thermal term and the contact term in RESULT.md:48–66. For the active part write Y=V-kappa X_active, y=exp(-t), x=exp(-kappa t), and b=(y-x)/(kappa-1), or b=t y at resonance. The stationary identities Cov(Y,X_active)=0 and Cov(Y,V)=A/(kappa+1) give Cov(Y_0,V_t)=Ay/(kappa+1), Cov(Y_0,Y_t)=A(y-kappa b)/(kappa+1), and Cov(V_0,Y_t)=A(y-kappa b)-kappa A x/(kappa+1). Pairing V_0 Y_0 with V_t Y_t by Wick gives precisely the two exponential terms and the resonant limit, continuously at all separated lags; averaging this kernel over the two disjoint increment intervals proves the defining limit. The initial regular value A² kappa(d_c-d), the monotonic single-exponential bracket on each side of kappa=1, and the linear resonant bracket verify the sign classification including strict negativity at positive lag on the frontier. Differentiating the crossing and d_c verifies both monotonicities; direct integration gives the stated variance rate. For kappa=2, A=1, D=1/10 the crossing is log(41/30); at kappa=A=1, D=1/2 it is 1/4. Inspected VERIFICATION.md and check.py; did not execute the frozen script. Its finite diagnostics are not needed to extend the proof to all parameters.

## originality

PASS

The supported distinct claim is the full finite-lag sign frontier and crossing law for stationary separated work increments, not the model, the integrated work large deviations, the Wick identity, or asymptotic variance. The closest distinct evidence concerns other observables or long-time rather than lag-resolved fluctuations; no inspected statement supplies the stationary finite-time variance or equivalent kernel that would cover this result. This decision is limited by explicitly identified full-text access gaps.

## value

PASS

The frontier determines when nearby separated work increments switch from correlated to anticorrelated and when they are anticorrelated at every positive lag. The stochastic thermal cross term is essential, and the result distinguishes a negative regular covariance from a positive contact term and variance. Neither the threshold with equality nor the lag transition can be read from the long-time variance alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.

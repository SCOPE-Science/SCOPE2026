# Independent mathematical audit

## correctness

PASS

The causal factorization C_t=D(I−tS)^−1 proves compactness; pointwise order on positive matrices gives increasing norms (strict for 0<t<1, by testing on a nonnegative compact norm maximizer). In the inverse quotient, expanding the zero-extended difference squares gives t times the free gradient energy plus (1−t)^2 times the unweighted mass. The ground-state substitution v_n=sqrt(n+1)f_n gives conductance sqrt(n(n+1)) and diagonal Hardy excess (n+1)r_n, with r_0=7/4−sqrt(2)>0 and r_n nonnegative and of order (n+1)^−4 for n>=1. The sine test on the shortened logarithmic interval has mass a/2+O(1), gradient energy at most π²/(2a)+O(a^−2), summable Hardy excess O(a^−2), and exponentially small confining term. For the liminf, normalize discrete mass to L; O(1/L) excess gives vanishing f_0, bounded local H^1 of the interpolant at x_n=log(n+1)/L, and exponentially small mass on x>=1+δ for every δ>0. The mass comparison on [0,R] is with the sum truncated to x_n<=R: replacing 1/(n+1) by log((n+2)/(n+1)) costs O(1)/L on compacts, and max mesh width is O(1/L). For R>1, the tail bound recovers the full discrete mass. Thus the normalized limit lies in H_0^1(0,1), and on intervals away from zero the conductance tends to the continuum coefficient one. Sharp Dirichlet Poincaré yields π² in the reciprocal-squared norm gap, and differentiation of E^−1/2 at E=1/4 gives the stated 4π². The independent finite-section sandwich under originality also proves the main limit without this mesh argument. Read VERIFICATION.md and check.py; did not execute the uploaded code.

## originality

FAIL

The frozen coefficient is mechanically implied by the known sharp finite Hardy constant, via positivity and a causal finite-section comparison with errors smaller than the main gap. The different parameter and the different standalone proof do not make the exact norm invariant distinct.

## value

FAIL

The operator is natural and the log-coordinate proof is mathematically useful, but the frozen contribution is the single scalar invariant and does not state an additional result about singular-vector profiles, higher modes, or improved error. The invariant is mechanically inherited from the finite Hardy asymptotic, so it does not survive as an independent exact finding under the standard. No repair is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

The stable affine OU/free-diffusion recurrence defines the stationary event-indexed chain; its random coefficient contracts in L^4 and the innovations have finite fourth moment. For an independent derivation, write the conditional start variance as Q+R given past durations and put M=exp(-2kT). The conditional release variance is Q+MR and the next excess variance is MR+2DS. Thus E[R]=L/(1-a) and E[R^2]=(2aL E[R]+H/3)/(1-b). Conditional Gaussian square products give G=2(a-1)Q^2+(1-a)Q E[R]+3(a-b)E[R^2]-L(Q+a E[R]), which simplifies to the recorded expression. The affine conditional second moment propagates the next-cycle covariance by a at each additional lag, giving strictly positive prefactors multiplying G for all j>=1. Substitution independently reproduces the three rational functions; the third numerator polynomial has one sign change and a positive root bracketed by 11.141522 and 11.141523. The weak and strong limits give the claimed endpoint signs for all fixed m>=3, not uniqueness beyond m=3. The deterministic variance recursion gives the stated negative formula, and A-B=L gives the identical mean work kD/q. Replay via RESULT.md lines 40–113 or the variance recursion above. The supplied verification script was inspected, not executed; the conclusions are exact, not simulation estimates.

## originality

PASS

The distinctive result is the exact stationary cycle-indexed switching-work covariance for renewal trapping, with all positive lags sharing the sign and a minimal three-stage matched Erlang clock for negative covariance. Inspected annual-catalogue and literature results overlap in model, work statistics, or correlation transitions, but the compared statements do not imply this sign classification.

## value

PASS

Changing the dwell-time shape at fixed mean changes an experimentally interpretable cycle-memory statistic while leaving mean injected work unchanged. The exact minimal-stage boundary and common sign at every positive lag are sharper than observing a numerical sign change or a physical-time variance trend. The result supplies a testable benchmark for linear renewal-driven energetics; it does not claim a laboratory-time sign law or uniqueness for all Erlang shapes.

The dated certificate retains the supplied scientific assessment, sources and limitations.

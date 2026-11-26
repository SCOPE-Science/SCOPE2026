# Independent mathematical audit

## correctness

PASS

The first-order ODE gives Q_j=C(X^j-Z^j) by integrating over [t0,t1], with X=e^(-k(T-t1)) and Z=e^(-k(T-t0)). The ratios fix s=X+Z and delta^2=4Q3/Q1-3s^2=(X-Z)^2. A feasible interior triple is exactly Q1>0, delta>0 and e^(-kT)<(s-delta)/2<(s+delta)/2<1. Ordered roots, C=Q1/delta and the logarithmic endpoints reconstruct the readings uniquely. For either pair i<j of the three channels, set rho=Z/X and keep Q_j/Q_i fixed. The equation X^(j-i)=(Q_j/Q_i)(1-rho^i)/(1-rho^j) gives a continuous family for rho near its physical value, with C=Q_i/[X^i(1-rho^i)] fixing the common scale. All strict physical inequalities persist. Holding Q1,Q2 fixed gives dC/dQ3=-2/delta^3; normalization produces 2(1+rho+rho^2)/(1-rho)^2. The exact 6 follows from rho=e^(-kh) and 1-rho~kh. Direct factorization gives the frozen signed Jacobian in (C,X,Z), -C^2 delta^4; changing to (C,t0,t1) multiplies by -k^2 XZ. At the rational witness X=1/2,Z=1/4,C=4, delta=1/4 and Q3=7/16 give the relative sensitivity 14 exactly. The uploaded test was inspected but not run; these analytic checks suffice. All assertions are for calibrated exact data and a positive single interior rectangular pulse; no finite-noise or minimax claim follows.

## originality

FAIL

The decisive overlap is the established one-pulse equations in the distinct twin-pulse record, not the matching title, the date, or an inaccessible citation. Its Proof §1 gives the identical first three normalized observations in sum-product form. All of the exact single-pulse inverse, feasibility and conditioning calculations follow mechanically from those equations, including from their first three channels alone. The publications' within-day priority is not determined. The two documents are not identical (the other main finding is a four-channel discriminator), but the single-pulse mathematics considered here is covered by its explicit proof-level identities.

## value

FAIL

The motivating question is useful: a physically feasible inverse can still be very ill-conditioned for short pulses. Here, however, the exact inverse and its duration-only derivative are mechanical readings of the already explicit quadratic in the same data, with the constant 6 from a first-order exponential expansion. No distinct useful unknown invariant, independent bound, or design consequence survives the overlap. The one-model local derivative cannot be promoted to a general practical noise bound to supply that missing contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.

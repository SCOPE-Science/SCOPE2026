# Independent mathematical audit

## correctness

PASS

The stationary convolution is well defined by positive on-state occupation. For integer n>=1 the killed two-state generator Q-2n*kappa*diag(0,1) has negative trace and positive determinant; the L^n norm of the exponential integrand of the conditional variance thus decays exponentially with lag. Minkowski integration gives finite variance-mixture moments of every finite order, and synchronous coupling contracts since the integrated on-time diverges. The stationary state-resolved moments solve a nonsingular 2-by-2 system with M1=D/kappa and M0=(2D*pi0+beta M1)/alpha. The lagged generator has characteristic polynomial p(z)=z^2-(kappa+T)z+alpha*kappa with p(0)>0 and p(kappa)<0. C(0)=V and C'(0+)=-D fix the two displayed residues. At s=D/V<kappa, p(s) has the sign of H by the exact factorization, so A+ has the opposite sign while A->0. A negative fast coefficient violates high-order alternating derivative signs, since lambda+>lambda-. Twice differentiating or using the lag generator gives C''(0+)=D*kappa*(alpha-beta)/T; dividing C''(t) by the positive slow exponential reduces it to a constant plus a single decaying term. This validates all three curvature cases including alpha=beta and the strict crossing for alpha<beta. For H=0 the remaining mode has rate T/2 and variance 2D/T. The fourth moment equations give N1=3DV/kappa, N0=(12DM0+beta N1)/alpha and hence the positive fourth cumulant and standardized excess in the frozen claim. The independent script python3 /workspace/review_replay.py (section 5) corroborates the exact stationary moment and phase identities on 21 rational cases. The frozen checker was inspected but not executed; it applies five lag comparisons to 1,029 grid cases, then 21 extra cancellation checks, not five lag comparisons for all 1,050. This does not affect the proof.

## originality

FAIL

The central exact covariance-cancellation and fourth-cumulant finding is mechanically covered by the nonsingular zero-stiffness boundary of the earlier broad Resultary result 8f817ade8710. Its proof also supplies the full covariance ODE and exactly the factor determining the sign phase. This is positive evidence of implication, not failure based on an inaccessible source. The audited theorem is not false, nor is its boundary literally in the earlier theorem's strict-positive wording; the actual identities settle coverage.

## value

FAIL

An unconfined phase is a natural physical boundary, and the interpretation of OU covariance with a non-Gaussian marginal is useful. But as a standalone research contribution, the main camouflage classification and its diagnostic reduce to the existing regular two-stiffness formulas, and the residual sign and curvature observations are obtained by evaluating the same known two-mode ODE and comparing its two exponential terms. No new diagnostic, exact invariant beyond the existing solution, or singular-boundary obstruction giving independent mathematical value was established. No substantive repair is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.

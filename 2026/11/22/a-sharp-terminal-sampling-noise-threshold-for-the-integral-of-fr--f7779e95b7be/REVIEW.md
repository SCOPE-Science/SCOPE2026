# Independent mathematical audit

## correctness

PASS

For standard H=3/4 fBm and independent Gaussian noise, Gaussian projection gives Var(J)=2/7 and information c(t)^2/(t^(3/2)+η), where c(t)=Cov(J,B_t). An independent global check at η=1/2: set g=2c and d=1−t^(3/2). Integration of g′ gives g=1−d/3−e, where e is the integral from t to 1 of (1−s)s^(1/2)+(1−s)^(3/2). Since 1−s≥(2/3)(1−s^(3/2)), e≥2d²/9. The difference 1−d/3−sqrt(1−2d/3) is (d²/9)/(1−d/3+sqrt(1−2d/3))≤d²/6. Thus 0≤g<sqrt(1−2d/3) for t<1, proving strict terminal superiority including at the threshold. Comparing cross-multiplied informations, the endpoint advantage increases with η since c(t)<c(1)=1/2. The endpoint derivative of information has sign η−1/2; below the threshold continuity, including the zero-information limit at t=0 even without noise, gives an interior maximizer. The terminal risk and the general-H necessary condition follow by substitution and differentiation; no interior uniqueness or general-H sufficiency is shown. Frozen replay references: RESULT.md lines 20–52, VERIFICATION.md and verify.py inspected, not executed.

## originality

PASS

Distinct on the inspected evidence: the nearest scalar-integral endpoint theorem is for a different Gaussian kernel; the nearest standard-fBm one-site theorem optimizes a different loss with noiseless samples. Credit classical Gaussian conditioning and integrated-fBm moments, not the strict global switch as a consequence of either alone.

## value

PASS

A canonical scalar-area sensing problem with a single reading has an exact noise level separating interior sensing from strictly terminal sensing. The global comparison at equality goes materially beyond the local derivative barrier and gives a useful calibration case for Gaussian quadrature design. It is not a general classification in H.

The dated certificate retains the supplied scientific assessment, sources and limitations.

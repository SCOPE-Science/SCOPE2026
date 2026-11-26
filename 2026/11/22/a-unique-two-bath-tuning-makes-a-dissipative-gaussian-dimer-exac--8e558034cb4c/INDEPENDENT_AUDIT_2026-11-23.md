# Independent mathematical audit

## correctness

PASS

In normalized sum/difference coordinates the drift rates are a-k and a+k. The transformed noise matrix has diagonal entries (T1+T2)/2 and off-diagonal entry (T1-T2)/2; dividing twice these entries by the sums of their two drift rates gives the stationary covariance in that basis. Projecting back yields exactly the two stated residues, with b_- strictly positive. For positive lags s,t the stationary Gaussian Markov covariance defect factors as b_- b_+ (exp(-(a-k)s)-exp(-(a+k)s))(exp(-(a-k)t)-exp(-(a+k)t)). Thus the fast coefficient must vanish, uniquely at T2/T1=(2a+k)/k. At that positive calibration the scalar covariance, mean, and continuity give the complete stationary OU law, with no claim of equality for the full hidden filtration, preparation, or forced response. Independently, Stratonovich heat into bath one is (A S A)11-aT1, which gives k^2(T2-T1)/(2a); potential-energy stationarity gives J2=-J1. The entropy rate and its strictly positive derivative at fixed visible lambda,T1 follow as stated, with endpoint rates 0 and +infinity. The forced mean response has both modes, so is strictly smaller than the passive-law inferred response at every positive lag. Read the source and verification files including verify.py without executing it. Independent high-precision integration of 2 exp(-At)D exp(-At) at (a,k,T1,T2)=(2,1,1,5) gave S=(1,1;1,3); computing the Stratonovich expression and the lag-0.73 covariance reproduced J1=1, sigma=0.8 and exp(-0.73). These checks do not replace the all-parameter proof or establish experimental realizability.

## originality

PASS

The standard Gaussian projection criterion and general OU covariance, response and entropy machinery are not original. The supported addition is the explicit unique positive calibration and fixed complete scalar-path-law dissipation range in this nondegenerately coupled, two-diagonal-bath model. Prior bounded comparisons did not supply that joint claim; general formulas substantially shorten its derivation.

## value

PASS

The calibrated family shows a sharp identifiability failure without appending an independent hidden dissipater: the hidden coordinate genuinely drives the observed one, yet even complete passive path data give no finite upper bound on entropy production in the stated model. The unique temperature condition distinguishes the exact failure from a marginal or single-lag coincidence, and force response provides a precise way to distinguish the models in principle. This does not assert that arbitrarily large dissipation is physically attainable in an overdamped laboratory regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.

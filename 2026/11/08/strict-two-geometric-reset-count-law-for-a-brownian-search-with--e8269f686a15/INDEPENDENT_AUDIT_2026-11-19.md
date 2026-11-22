# Independent mathematical audit

## correctness

PASS

For generator D*dxx, the gate-killed backward ODE system has two explicit positive decaying modes and reflecting/absorbing endpoint conditions H0'(0)=0, H1(0)=1; those uniquely give h0=p(Au-v)/B and h1=(pAu+qv)/B for strictly positive parameters. Gate resolvent U=r(rI-Q)^(-1) and strong Markov plus reset-clock memorylessness give K=U-h*U[1,:] for gate persistence. K is positive substochastic with row sums 1-h_i and det K=z(1-h1)>0; direct independent symbolic reduction verifies det(sI-K)=-pquv/(AB^2)<0 where s=pi K 1. This strictly interlaces s between two positive subunit eigenvalues for all positive physical parameters, making the two spectral weights strictly positive. Cayley-Hamilton yields P(N>=n)=pi K^n1=w+lambda+^n+w-lambda-^n for all n>=0. Positive distinct weights prove strict discrete tail log-convexity/decreasing hazard, and total variance yields strict excess 2w+w-(m+-m-)^2 over the geometric same-mean variance. This is an analytical proof; fresh symbolic checks and 9018 numerical comparisons support the identities only.

## originality

PASS

Best-of-knowledge PASS, qualified by an important generic Markov-renewal/phase-type derivability risk. The exact same persistent closed-reflecting/open-absorbing gated Brownian model was developed in Mercado-Vásquez–Boyer (2021), but inspected results give absorption-time transforms and first moments rather than the count-marked two-geometric pmf and strict positive weights. Sunil et al. (2023) supply general count-and-cost renewal transforms for scalar renewal resetting; their renewal Eq. (3) assumes full process renewal after a reset, not a persistent gate. Bressloff (2020) reinitializes the gate; Bressloff (2023) obtains ungated scalar-geometric count. A later 2025/2026 blinking-target paper has a transparent rather than reflecting closed gate and does not state the count law. The claimed novel content is the positive spectral mixing and strict hazard/variance assertions in the fully persistent gate model, not first discovery of gate-persistent Brownian resetting or phase-type matrices. Semantic published-record search found no distinct covering prior, but a literature search is not a novelty proof.

## value

PASS

A persistent switching absorber is a natural stochastic search model where position resetting does not erase environmental memory. The count N is an operationally meaningful number of interventions, not merely mean absorption time. Exact positive mixture scales, strictly decreasing conditional absorption hazard, and strict excess dispersion distinguish the persistent gate quantitatively from ordinary renewal resetting and give an all-positive-parameter classification. The core sign identity is a motivated nontrivial structural statement rather than one arbitrary parameter experiment. Boundaries: excludes nonstationary initial gate, singular rates, drift, multiple gates, non-exponential reset clocks.

The dated certificate retains the supplied scientific assessment, sources and limitations.

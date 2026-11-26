# Independent mathematical audit

## correctness

PASS

The corrected RESULT.md uses floor(n^t), giving genuine right-continuous paths in D[0,1] with J1. The frozen ceiling version is not D-valued: for n>=2 the right limit at t=0 uses K_2 instead of K_1, with a positive probability of a different second label because multiple weights are positive. Floor and ceiling counts differ uniformly by at most one, so the target limit and normalization are unchanged; the corrected proof works directly with floors. To check it, weights lie between delta*exp(-S_{j-1}) and exp(-S_{j-1}), and successive S values are separated by d>0. Each early label needs only floor(exp(S_{j-1}+h+1)) observations to have exponentially small nonappearance probability, and outside the early-box cutoff the residual mass is at most exp(-i-h-1) on the unit log grid. Union bounds give a uniform O_P(log log n) count error, summably in n=ceil(exp(k)); the ergodic inverse law and monotonicity yield the all-integer strong law. The finite-state Poisson equation leaves a bounded remainder to a bounded-difference martingale, with limiting bracket equal to the absolute Green–Kubo sum by geometric covariance decay and stationarity. For M the count of S_{j-1}<=Lt, the error S_M-Lt lies between zero and the maximal increment, and M/L tends uniformly to t/mu. Substitution in the partial-sum functional CLT gives -s B(t/mu)/mu, equal in law to the stated s B(t)/mu^(3/2), including the variance-zero case. For two states the centered observable lies in the eigenvalue-lambda eigenspace, so the geometric covariance sum gives (1+lambda)/(1-lambda) times the one-step variance and the example coefficient 51/250. The frozen exact-rational checker was inspected, not executed, and does not test the process topology.

## originality

PASS

The corrected floor formulation makes a topological repair, not a claim of novelty in the choice of interpolation. The supported distinct contribution is the nested-sample functional and almost-sure limit in a bounded finite-state Markov stick environment, with explicit dependence-sensitive covariance scaling. Model construction, iid scalar limits, and fixed-size occupancy-threshold process transfers are prior work; the strongest inspected statements do not give the needed nested-sample process.

## value

PASS

The theorem isolates a concrete statistical effect in a natural dependent extension of stick breaking: the leading logarithmic growth only knows the stationary break law, but the path-scale fluctuations can be changed arbitrarily, at fixed two-state marginals, through correlations. The uniform nested-sample comparison justifies the process statement and the strong law; neither a mere reformulation of a prior iid number nor the change to floors is the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.

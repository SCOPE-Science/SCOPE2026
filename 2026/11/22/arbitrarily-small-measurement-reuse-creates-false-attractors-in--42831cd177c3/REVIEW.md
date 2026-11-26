# Independent mathematical audit

## correctness

PASS

For x>0 the singleton winner is negative only on the all-negative candidate outcome; reflection gives the negative half-line and uniform ties give mean zero at x=0. Conditioning on the common stored winner makes queries independent with means pS and variances 1-p². Thus different queries have unconditional covariance p² Var(S|x), which gives exactly the claimed average variance and the nonzero limiting floor. On x>0 and x<0, the mean update contracts to the respective ±μ without crossing zero for fixed 0<η≤1; zero also remains a mean equilibrium by the tie rule. For the pathwise claim let τ be first entry into the nonpositive half-line. The squared distance from μ, stopped at τ, satisfies the stated conditional drift because (1−η)²≤1−η and the centered bounded response has conditional variance ≤1, including the crossing step. At a crossing the stopped squared distance is ≥μ², whereas its expected value is bounded by the accumulated squares of the steps. This gives P(τ<∞)≤π²/96. Adding the tail sum of squared steps gives a nonnegative supermartingale with summable expected accumulated drift. On no exit the squared error has a limit, and divergence of the step sum forces it to be zero. The same argument without stopping proves the p=0 case. The positive-reuse bound requires the stated start and p-dependent schedule; it is not an all-starts or exact-basin assertion. Read RESULT.md §§1–4 of the proof, VERIFICATION.md, and verify.py as text. The supplied finite rational checks cover moments, not the infinite pathwise conclusion; the latter was checked analytically.

## originality

PASS

Credit prior qualitative selection bias, independent refresh, and exact scalar cached/fresh endpoints. The supported distinction is the common-winner mixed-reuse conditional law for every stated batch size and the explicit high-probability wrong limit for arbitrarily small positive reuse, neither covered by the compared models or their theorems. No within-day priority or universal novelty is inferred.

## value

PASS

This is a useful sharply controlled independence counterexample: a shared screened response gives a residual variance even as the query batch becomes large, and the mean bias yields a wrong stochastic limit with uniformly positive, quantified probability under a valid decreasing-step schedule. It shows a failure of consistency, not just an error bound or a biased single update. The exact frontier is specific to a scalar dense-noise winner oracle and the pathwise statement does not transfer to standard streaming quantile Kaczmarz.

The dated certificate retains the supplied scientific assessment, sources and limitations.

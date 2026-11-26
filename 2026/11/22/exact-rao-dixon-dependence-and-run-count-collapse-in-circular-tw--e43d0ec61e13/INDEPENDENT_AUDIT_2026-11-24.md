# Independent mathematical audit

## correctness

PASS

For the independent samples under the common atomless null, anchoring a named first-sample point yields equally likely assignments of the other first-sample label positions. These positions and the weak gap compositions are in bijection. Samplewise, the zeros are the only negative deviations when n/m<=1, so R=2nZ/m. Each occupied gap contributes one second-sample run, matched by one first-sample run, proving the stated affine equivalence, with matched tie treatment. The null has P(S1=0)=(m-1)/(m+n-1), P(S1=S2=0)=(m-1)(m-2)/((m+n-1)(m+n-2)), including m=2. The factorial generating identities give E Q=n+2n(n-1)/(m+1) and its zero-conditioned version by replacing m with m-1. For Var Q, if P_k is the ratio of falling n of order k to rising m of order k, expansion gives (24m+4m(m-1))P_4+24mP_3+4mP_2-(2mP_2)^2, which factors as in the source. The covariance follows from the mean shift multiplied by m P(S1=0); both variances and covariance are positive. Verified the denominator-minus-numerator factor and balanced successive-difference factor; the cubic is positive at 2 and has positive derivative for s>=2. Counting positive compositions gives the balanced vacancy law; leading powers give both limiting statements. Independent exact replay python3 -B /workspace/evidence/check_2.py checks separator configurations for 28 pairs with 2<=n<=m<=8. All-parameter correctness uses the moment proof, not these finite checks. This is dependence in second moments and optimal linear prediction, not a full joint law or incremental power theorem.

## originality

PASS

For the exact finite mixed covariance/correlation and its balanced behavior, best of inspected evidence. Do not credit Rao's vacancy/run reduction separately as new mathematics: it follows immediately from the 2021 published positive-part identity and identifying circular blocks. The vacancy marginal at balance is also a direct composition count. The strongest inspected sources give definitions, marginal calibration, the common occupancy law, or exact entries for other occupancy/spacing covariances; they do not give the evaluated mixed rational dependence and its monotonicity.

## value

PASS

Two used circular two-sample procedures have an exact finite dependence that is not visible from separate critical values or asymptotic marginal normality. The rational correlation discriminates two-observation degeneracy, sparse versus balanced behavior, and the exact monotone loss of linear predictability at balance. The simple run identity has practical interpretive value but is not the standalone research contribution; neither piece establishes power improvements.

The dated certificate retains the supplied scientific assessment, sources and limitations.

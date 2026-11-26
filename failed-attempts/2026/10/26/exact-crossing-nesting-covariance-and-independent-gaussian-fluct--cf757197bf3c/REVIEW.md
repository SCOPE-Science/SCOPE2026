# Independent mathematical audit

## correctness

PASS

Ranking n labeled independent uniform endpoint pairs gives exactly 2^n n! equally likely rank assignments for each matching. For the two centered order-two kernels, write the three gaps (u,v-u,1-v) as (l,b,r), which is Dirichlet(1,1,1). The conditional probabilities are 2b(1-b) and b²+2lr. The simplex moment formula E[l^i b^j r^k]=2 i!j!k!/(i+j+k+2)! gives mean 1/3 for each, raw second moments 2/15, and raw mixed moment 1/9. Consequently their first-projection covariance is I/45. For the same chord pair the indicators are exclusive, with covariance −1/9; the canonical remainder per pair has marginal variance 8/45. Its distinct pair terms are uncorrelated, also when sharing one endpoint index, by conditional centering. Thus the C,N variances are n(n−1)(n+3)/45 and their covariance −n(n−1)/18, giving the claimed correlation and the stated matrix by A=binomial(n,2)−C−N. The n=2 matrix agrees with a uniform one-hot vector. The canonical remainder has second moment O(n²), so multivariate iid CLT on the first projections and the deterministic alignment identity give the asserted singular trivariate limit. A separate exact enumeration checked all nine entries and means for n=2,3,4,5; the frozen script was read, not executed. The recorded verification is finite corroboration, not an asymptotic proof or formal verification.

## originality

FAIL

Two distinct Resultary statements already materially cover the bivariate theorem in the identical uniform matching model, including the October 18 record's same orthogonality mechanism. The explicit third row/column and third limit coordinate are linear consequences of the previously stated bivariate theorem and the published pair-count identity. This is a statement-level coverage decision, not a claim of historical authorship or priority.

## value

FAIL

The contrast between finite negative correlation and limiting independence is a meaningful question, and orthogonal projections explain it. But those are already present together in a matched result. The only apparent extension is to a deterministic third coordinate, which requires neither a new estimate nor a new phenomenon. A pedagogical restatement and explicit matrix are insufficient as a surviving distinct finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.

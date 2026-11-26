# Independent mathematical audit

## correctness

PASS

Equation (4) and Algorithm 2 of arXiv:2609.11751v1 use independently sampled evaluation and update losses and projected feedback-gradient descent; the null step is only for the other branch. The ratio here is (B/A)(1−AP)², so the affine gain update is a strict convex combination with 1/A and preserves the interior. The four slopes lie in (0,1−2η], not the open-upper interval in RESULT.md line 57 (equality at A=B=1); the contraction bound in the actual proof is unchanged. The common contraction yields the unique stationary marginal. Centering at p*=1/μ gives a zero-mean innovation independent of the old centered gain, though not of the fresh slope; the mixed second-moment term vanishes from the old gain's zero mean. Its variance is 4η²νs²/μ² and the squared-slope expectation is 1−4ημ²+4η²ν². Solving gives the stated V; conditional linear regression gives the geometric correlation. Then M=s²/(μ²−ην²), with positive denominator, and M>1 iff η>b/ν² since μ²−s²=b. The admissible open window is nonempty iff (1+b²)²>8b³, and the quartic has just one root above one by the sign of 4b(b²−6b+1). Bisection gives 7.739425778114425627…; the rational example gives 18225/17024. For an independent pathwise check, summing the conditional linear gain recursion and applying the bounded martingale-difference strong law gives time-average P→1/μ. For each fixed ε>0, the bounded observations log(|1−AₖPₖ|+ε) differ in time average from their conditional means by a vanishing martingale average. Those means are a concave sum of logs of the positive affine factors 1−p+ε and bp−1+ε, so Jensen bounds the limsup by their value at 1/μ. Letting ε decrease to zero gives the asserted negative upper bound, agreeing with the frozen stationary-coupling proof. Replay: RESULT.md Proof §§1–4 plus arXiv:2609.11751v1 §3.1, Eq. (4) and Algorithm 2; packaged checker read as text only. The multiplier concerns a fresh test at an invariant marginal, not the expectation growth rate of the actual iterate, and the almost-sure bound is not an exact Lyapunov exponent.

## originality

PASS

The supported distinction is the exact gain/curvature region for fresh-test amplification from the invariant learned stepsize of the specified OSGM ratio branch, together with an all-admissible-gain bound on the actual typical trajectory. The algorithm, the fixed population target, generic random affine stationarity, and the general notion of a pathwise-versus-moment distinction are not new claims.

## value

PASS

The exact region identifies when variance in a genuinely online learned step changes the sign of an independent squared-error diagnostic, although the population target remains squared contractive and actual optimizer paths decay. The natural diagnostic and coupled-path comparison justify the scalar model; there is no claim of actual coupled mean-square divergence, field-scale optimizer performance, or general conditioning guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.

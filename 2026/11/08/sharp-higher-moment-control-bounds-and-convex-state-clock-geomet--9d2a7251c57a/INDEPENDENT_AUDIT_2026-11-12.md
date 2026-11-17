# Independent mathematical audit

## correctness

PASS

For a finite killed continuous-time Markov chain with certain absorption, the Green matrix G=(-Q)^{-1} is entrywise nonnegative and U_m=m! e_a^T G^m 1 for every integer m>=1. Multiplying any group of edges with one source by t>0 changes one row of -Q affinely; the determinant and each cofactor are affine in t. Positivity on all t>0 forces their two coefficients nonnegative. Each positive Green entry has log-rate elasticity between -1 and 1; a positive sum of products of m Green entries has elasticity in [-m,m]. Uniform scaling of all edges gives the -m budget exactly. The single-step exponential attains -m; two transient states A->B (rate a), A->C (t), C->A (b) yield G=[[b,t],[b,a+t]]/(ab) and asymptotically attain +m. Full state-clock factors give a finite positive exponential sum indexed by m state occupancies, with gradient -E N and covariance Hessian. Independent symbolic checks for m=1..6 verify the two-state upper asymptotic. Hypotheses include positive graph-preserving rates, finite state space, and integer raw moments; no arbitrary multi-source bound or variance bound follows.

## originality

PASS

Best-of-knowledge surviving novelty concerns m>=2 sharp architecture-independent same-source bounds, matching positive extremals, and simultaneous log-state-clock convexity. The mean m=1 control budget and general moment formulas are explicitly prior; no stronger primary statement establishing this whole control law was identified. Caswell 2011 complete text remains inaccessible, a genuine priority risk.

## value

PASS

Higher raw moments quantify the long passage-time tail, a distinct engineering/statistical objective from the mean. The 2026 mean-budget work motivates the higher-moment question. The result gives tight rate-independent bounds for a whole class of same-source kinetic controls and a globally convex simultaneous state-clock geometry, useful for robust network rate-design rather than an arbitrary finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

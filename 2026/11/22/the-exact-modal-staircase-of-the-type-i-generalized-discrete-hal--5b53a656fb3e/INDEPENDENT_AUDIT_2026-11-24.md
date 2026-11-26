# Independent mathematical audit

## correctness

PASS

The PMF telescopes to one and is the unit-bin floor law, with a_0=0. For alpha<=1 the positive parent density strictly decreases, giving strict mass decrease. For alpha>=1 both the log-sech-squared term and the nonnegative multiple of log-tanh give a strictly concave log density. In RESULT.md:57–65, the two interior arguments are strictly inside the same outer interval and their sum equals the sum of the extremes; strict concavity therefore survives integration over both offsets and gives strict discrete log-concavity. The increasing likelihood ratio f_beta/f_alpha integrated over neighboring bins makes each successive mass ratio strictly increasing in alpha, from below 1 at alpha=1 to infinity. Log-concavity then orders the crossings strictly. Independently, for k>=1 divide the crossing by a_{k+2}^alpha: the equation is 1-2r+r^v=0 with r=(a_{k+1}/a_{k+2})^alpha and v=(log a_{k+2}-log a_k)/(log a_{k+2}-log a_{k+1}). The expansion log a_j=-2q^j+O(q^{3j}) gives v=1+1/q+O_theta(q^{2k}) and q^{-k}log(a_{k+2}/a_{k+1})=2q(1-q)+O_theta(q^{2k}). The nontrivial root of the limiting strictly convex function is simple since the function is negative just below 1 and positive at 0. Smooth dependence near that root yields the stated C_q and error. Divergence of the ordered thresholds now gives the complete global mode and tie classification. The supplied checker was read, not run; separate bounded floating-point evaluations reproduced the four theta=1 displayed numbers. Neither the numerics nor the proof assert rate-uniformity.

## originality

PASS

Credit the PMF, its one-parameter shape and the known first-tie example to Barbiero–Hitaj, and the general ordering tools to standard theory. The supported distinct claim is the complete strict all-index classification for this bin law together with the explicit and quantified tail crossing. No covering statement was found in available material; historical priority is not certified.

## value

PASS

Which count value is most probable is a natural shape question for this named PMF. A complete no-skip and adjacent-tie rule determines it for all parameters, while the fixed-rate limit locates the large-index boundaries on the exponential scale more precisely than a continuous mode approximation. This goes materially beyond the known isolated tie and does not claim estimation, hazard, or uniform-rate consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.

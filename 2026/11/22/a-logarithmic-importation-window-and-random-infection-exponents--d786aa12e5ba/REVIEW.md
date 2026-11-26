# Independent mathematical audit

## correctness

PASS

Detailed balance on the count chain with rates (n-k)(k+a)/n and k gives the weights (a)_k R_{n,k}/k!, with R_{n,k}=product_{j<k}(1-j/n). Independently, the uncut cumulative weight S_m=sum_{k<=m}(a)_k/k! is product_{j=1}^m(1+a/j) by telescoping, so log S_m=a H_m+O(a^2) uniformly in m for 0<a<=1. On k<=n^(1/2-delta) the collision factor is 1+o(1) uniformly, and on k>=n^(1/2+delta) the entire sum is bounded by n exp(-k_min(k_min-1)/(2n)), since the uncut weights are at most one. The two truncations sandwich Z_n between limits exp(c(1/2-delta)) and exp(c(1/2+delta)); let delta decrease to zero. The exact interior CDF cutoff is floor(n^y-1), not floor(n^y) as used in the proof sketch; both give the same interior limit by the product estimate, and yield the same upper bounds. The zero atom follows directly from pi_0=1/Z_n; the interior CDF tends to one as y increases to 1/2, ruling out an endpoint atom by monotonicity. When a log n diverges with a tending to zero, compare the exact interior partial sum to a lower cutoff at n^(1/2-delta) with y<1/2-delta: the log ratio is at most -a log n(1/2-delta-y)+o(1); y=0 follows from Z_n diverging, negative y is trivial and the upper Gaussian tail still vanishes. Only concentration of the logarithmic exponent is established, not concentration of K_n/sqrt(n). The slogan's density is the unconditional continuous component; the density conditional on a positive count in the limiting law divides it by 1-exp(-c/2). Read the supplied finite detailed-balance and rising-factorial checks without executing them; the limit is analytic.

## originality

PASS

The full finite stationary law and the critical harmonic cutoff in a closely related modified model are prior. The distinct claim is the finite-positive-source triangular array: a parameter-dependent exponential tilt of logarithmic size, with a nonzero mass at the zero state, and the higher-source collapse of the exponent. No equivalent theorem or dominating asymptotic result was found in the inspected material; this is not a priority certification.

## value

PASS

A positive atom at zero and a continuous spread over polynomial count scales coexist at equilibrium; neither the mean nor the assertion of a sqrt(n) cutoff describes this. The singular parameter window and its departure regime form a usable benchmark for complete-graph count models. The result does not estimate mixing, transient dynamics, finite-size convergence rates or behavior on heterogeneous graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.

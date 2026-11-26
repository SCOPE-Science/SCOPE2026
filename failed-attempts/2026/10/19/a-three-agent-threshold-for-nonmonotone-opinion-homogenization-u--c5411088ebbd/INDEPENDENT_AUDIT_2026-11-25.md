# Independent mathematical audit

## correctness

PASS

For the triangle, P=(3I+J)/6 where J is all ones. The row sums of PB are at most 5/6 with the third platform susceptibility zero, so the fixed point is attracting even at z=1. Solving the two active equations, then the third, gives y=(1-b)(8-5z,2,2-z)/D, D=12-8b-8z+5bz>=1. The three pairwise squared differences divided by 9 give population variance about its own mean. Its derivative has sign of (12-11b)z-12(1-b), giving the claimed unique interior minimum and strict sign change. Substitution confirms the minimum and both endpoint gaps; for example the frozen increase at b=3/4 is exactly 1/1274. The two-agent centered eigenvalue of P is 1-2alpha; writing y=P u and solving the two anchor equations gives the absolute gap coefficient |1-2alpha|/[1+alpha(b/(1-b)+c/(1-c))]. Squaring and dividing by 4 confirms coordinatewise nonincrease. If one susceptibility is 1 the other anchors a consensus; both 1 allow multiple equilibria, all consensuses, and the variance remains zero. One agent has variance zero. This establishes sharpness in the stated class, not with arbitrary prediction/peer rules. Inspected RESULT.md lines 27–95, verify.py, VERIFICATION.md and requirements.txt; the optional SymPy checker (>=1.12,<2) was not executed, and neither exact symbolic checking nor its finite rational regressions replace the sign and domain arguments.

## originality

FAIL

The pivotal optimization is a mechanical complete-graph specialization of a distinct indexed one-vertex FJ theorem, not just a similar path example. At a predictive fixed point write y=P u and u=(I-B)x*+BPu. On the frozen triangle L=I-P=(I-J/3)/2 is a symmetric weighted Laplacian, and the equation for u is the static FJ equation (L+K)u=Kx*, where K_ii=(1-beta_i)/beta_i; zero susceptibility pins u_i=x_i^*. The indexed combined objective becomes a positive constant multiple of the frozen pure variance because L is proportional to the centering projector, and P acts as 1/2 on that subspace. The indexed rank-one optimizer applies with the third vertex pinned by the explicit infinite-stubbornness limit and gives exactly z_b and the frozen bowl; details below. The one- and two-agent boundary in this setting is an elementary anchored opinion-gap computation, not a distinct surviving theorem of comparable scope. This decision credits indexed mathematical coverage, not chronological priority or dependence; the dates of the entries alone do not adjudicate those questions.

## value

PASS

As a mathematical example the family tests a natural boundary of homogeneous-platform monotonicity, with a minimal network and a robust interval of the reverse behavior rather than an arbitrary numerical anomaly. That counterexample is useful for interpreting the predictive-loop hypothesis even though its exact equilibrium optimization is already covered by the broader indexed result. There is no supported independent originality in the submitted claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.

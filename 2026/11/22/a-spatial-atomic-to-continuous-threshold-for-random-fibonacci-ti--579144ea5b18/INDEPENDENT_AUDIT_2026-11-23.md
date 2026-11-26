# Independent mathematical audit

## correctness

PASS

The sampling is over the lattice distances in one coordinate's first-feasible annulus; the placement flips have already been averaged out. There are exactly w[m-1] sampled distances. The absent top bit always fails. With the top bit present, the initial plateau has length w[m-1]-W[m-1], and the plateau at rank t>=1 has length s[t]-s[t-1]=g[v2(t)] by binary carry. This also handles m=1 and the strict inequality at the right endpoint. Averaging the upper-half contribution over lower subset sums yields W[m-1]/(4w[m-1]) above 1/2. Eventual geometric domination gives W[n]/w[n] -> 1/(Q-1); for Q>2 the fixed-rank dyadic masses converge with total limiting mass one, proving TV convergence. At Q=2 the reversed coefficient sequence converges in l1 to the fair binary coefficients; the limiting CDF is continuous so CDF convergence is uniform, and the independent rescaled lattice threshold tends to uniform on [0,1]. This proves the asserted weak limit; TV distance to the continuous limit is one under the event-supremum convention. For Fibonacci weights, F[n+d]=F[n+d-1]+F[n]>2F[n] on the sampled subsequence, and the primitive recurrence has dominant root rho_d. The identity rho_d^d-1=1/(rho_d-1) gives the claimed atom and mean. Independently enumerated the order-two phase w=(2,5,13,34,89): the sixteen plateau lengths start 35,2,3,2,6,2,3,2,14, agree with the carry formula and sum to 89. The packaged check.py was inspected, not executed; its enumeration and finite diagnostics are not proofs of the limits.

## originality

PASS

Pass for the spatially sampled finite rank-frequency law together with the asymptotic ratio classification, not for Fibonacci tiling, binary ranking, fixed-target failure probabilities, or the plateau geometry of classical self-similar Cantor CDFs. The closest fixed-target and occupation results do not average this observable over the feasibility annulus.

## value

PASS

Uniform annular sampling is a natural way to turn pointwise tiling risk into spatial frequency. The complete finite law plus the sharp ratio boundary identifies when risk is carried by dense atoms with explicit masses and when it is continuously spread; the largest Fibonacci atom gives a direct dimension-dependent frequency. This is more than a list of attainable risks and requires neither a multidimensional coverage interpretation nor a priority claim for Cantor distributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.

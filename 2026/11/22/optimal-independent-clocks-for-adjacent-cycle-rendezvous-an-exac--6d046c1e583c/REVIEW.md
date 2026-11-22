# Scientific review: adjacent-cycle rendezvous clocks

## Correctness — PASS

The relative-position walk has Fourier eigenvalues \(\lambda_k=(1-p+p\cos(2\pi k/n))^2\). Solving the Dirichlet Poisson equation gives \(H_n(p)=\sum_{k=1}^{n-1}[p(2-p(1-\cos(2\pi k/n)))]^{-1}\) at distance one. The Poisson-kernel expansion sums this exactly. Every reciprocal summand is strictly convex; the boundary analysis establishes unique interior optima, including odd cycles. Uniform differentiable geometric-error bounds near \(p=2/3\) give the first-order optimizer correction. Wald's identity gives the move count, and its derivative is strictly positive. The independent finite killed-chain checker passed 193 assertions. The experiments are corroboration, not a substitute for the full proof.

## Originality — PASS, with material source-access risk

This is **not** a first proof of symmetric Markovian cycle meeting optimization or of the relative-chain construction. Alpern (1995) and Alpern–Gal (2003, Section 15.4.1) treat that classical problem for random initial placements, and Zhang–Tan–Krishnamachari (2014) furnish a Fourier/eigenvalue framework for uniformly started independent walkers. The 2022 treatment also includes the three-vertex optimum. The claim distinguished here is an *adjacent-start*, all-size exact formula together with the \(n^{-1}\) correction to its common-clock optimal rate and the opposite optimization criterion when actual moves are counted. These are not entailed merely by the quoted uniform-start expected value or finite small-graph optimizers without fresh asymptotic analysis. The 1995 original's full text was inaccessible, while the 2003 retrospective chapter was materially read; historical priority remains unverified and a broader implication could be missed. published-finding corpus searches compared collision, reset, and rendezvous aliases with no exact matching published result in the retrieved items.

## Value — PASS

Adjacent initial separation is a natural local encounter experiment, unlike random-start rendezvous whose mean is quadratic in cycle length. Its clock-time mean grows linearly in size, so identifying the sharp universal interior time optimum and the sign-reversed actual-motion cost is a meaningful efficiency distinction: faster ticks and fewer mechanical moves optimize incompatible objectives. The finite-size correction is relevant to calibrating moderate cycles; it is not only a textbook restatement of a known return-time formula.

## Limitations

No all-start, unequal-clock, adaptive-clock, edge-crossing or general-graph assertion is made. Older rendezvous research could contain an earlier exact all-size adjacent-start calculation not indexed here. Finite checks cover only the specified cases and do not establish infinite claims; the proof addresses the general case. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.

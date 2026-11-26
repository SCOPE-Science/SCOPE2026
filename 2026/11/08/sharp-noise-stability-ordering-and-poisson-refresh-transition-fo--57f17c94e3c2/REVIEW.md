# Independent mathematical audit

## correctness

PASS

Deleting one maximum edge on each cactus cycle yields the MST, with all bridges retained. Given r refreshed indices, the overall maximum among the n+r independent samples falls on a retained edge with probability (n−r)/(n+r), guaranteeing concurrence. Otherwise, conditional on its label, the other sample's n candidate ranks are exchangeable, so its maximum has the same edge label with probability 1/n. This independently yields the stated conditional probability, including r=0 and r=n. Independence across edge-disjoint cycles gives the Bernoulli product. For shape, the copula value Z has a decreasing density: the common-value component changes variables by t=(1−ε)y+εy², while in either off-diagonal triangle, with x<y, t=x[(1−ε)+εy] and the x-Jacobian is 1/[(1−ε)+εy]. Both density terms decrease, with strict decrease from the off-diagonal part. At ε=1 the density is −log t. Integration by parts in n E[Z^(n−1)] has zero lower boundary for n≥1; the resulting positive moment measure is nondegenerate, proving strict decrease and strict log-convexity (with s₁=1). Strict convex discrete differences give the two unique length multisets, and each is realizable by cycles joined at one vertex. Binomial size-bias of the conditional failure formula gives 2(n−1)ε E[1/(n+1+Bin(n−1,ε))]; subtract from λₙε and use the mean of the binomial for the uniform quadratic error. Its full support range gives the lower bound, so union and exponential product bounds give the extreme regimes. The uniform error and Le Cam bound give total variation in the stated Poisson regime, trivially including α=0.

## originality

PASS

The generic finite-sample concurrence identity and independent-refresh model are known. The distinct supported result is the explicit partial-refresh cycle law together with strict shape in cycle length, the sharp fixed-budget cactus profiles, and a uniform estimate giving the many-cycle transition. The closest inspected comparables do not imply this combination. No claim of worldwide priority is made.

## value

PASS

Exact identity retention is a natural MST-noise observable. Strict shape is stronger than independent cycle decomposition: with the same graph cycle budget and number of cycles it decides which length profiles are most and least stable. The uniform single-cycle estimate determines the Poisson mean even for heterogeneous cycles whose lengths vary with cycle count; these are concrete uses of the sharp law.

The dated certificate retains the supplied scientific assessment, sources and limitations.

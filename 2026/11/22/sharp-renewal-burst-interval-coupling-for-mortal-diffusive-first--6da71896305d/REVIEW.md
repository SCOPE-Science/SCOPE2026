# Independent mathematical audit

## correctness

PASS

The original main rate and endpoint order are correct. Its limitations incorrectly said the optimal coupling may be non-unique for atomic or degenerate marginals. The complete corrected RESULT.md in /workspace/repairs/3/ fixes this, verifies equality at both endpoints, and clarifies the exponential upper bound used for general delay laws. Independent proof reconstruction: killed hitting has success probability exp(-x_0 sqrt(d/D)), and a<=q(u)<=a+exp(-du). Given all arrival/mark pairs the survival product is exact. Relative to the product of eventual failure probabilities the logarithm of their ratio is bounded by (j_+/a)/(1-exp(-d w_-)), even at an arrival time or when no batch has arrived. H(s)=E[exp(sW)a^J] is finite, strictly increasing, starts below one, and diverges. At its root, exp(theta S_n)a^(sum J_i) is a mean-one martingale. Stop at K=N(t)+1, bounded by floor(t/w_-)+1, rather than at N(t). With t<S_K<=t+w_+ and a^j_+<=a^J_K<=1, this gives e^-theta(t+w_+)<=F(t)<=a^-j_+ e^-theta t. This proves the exact limit for Q without nonlattice assumptions. For each s>0, use E[XY]=integral of P(X>x,Y>y) with X=exp(sW), Y=a^J. The two Fréchet tail bounds are pointwise attained by opposite and same order matching of X,Y, respectively; since Y decreases with J, this makes comonotone W,J minimize H and countermonotone W,J maximize H. Increasing roots reverse this order. Equality of rates forces equality of integrals at that positive root. The nonnegative integrand gap must vanish almost everywhere, hence at every threshold by right-continuity from above. The joint tail determines the joint law, and both transforms are injective. Atoms allow nonunique representations, not nonunique laws; a degenerate marginal gives a single law for both extrema. Recomputed the three quadratics in exp(theta) with the respective matching weights: y^2+2y=8, y^2+y=16/3, and 2y^2+y=8. Their positive roots give rates 0.6931471805599453, 0.6221386073711349, 0.5684704336385026 and ratio 1.2193196682604011. Throughput is E[J]/E[W]=1 in each case by the iid renewal reward ratio, and x_0=log 2 for D=d=1 gives the stated a. The added equality argument is analytical; no supporting numeric file needed a change.

## originality

PASS

Credit the physical, delayed-search, sharp fixed-marginal burst–interval exponent comparison, not the classical rearrangement bounds (including their joint-law equality) or the renewal-reward root as a general transform mechanism. Proven prior coverage includes the one-searcher renewal root exactly. Neither that result nor the inspected dependent-renewal abstract establishes the model's fixed-marginal interval–batch envelope. Changing the equality-limitations sentence does not make generic rearrangement an originality claim. This is a bounded, best-of-knowledge verdict.

## value

PASS

The effect is a controlled design comparison: the interval law, batch-size law, production rate and throughput all stay fixed, while the sharp delayed first-reaction exponent changes. The exact upper/lower bound for all joint laws, with an explicit realizable separation between extrema and equality at the quantile couplings, supplies useful information not captured by tuning the mean or one marginal. Its value is in that physical rate characterization and constrained comparison, not in recomputing the example's roots or classical dependence bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.

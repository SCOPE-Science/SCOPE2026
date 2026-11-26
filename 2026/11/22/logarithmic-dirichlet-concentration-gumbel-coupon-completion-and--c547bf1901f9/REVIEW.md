# Independent mathematical audit

## correctness

PASS

The total mass of a fixed r-label set has Beta(ra_q,(q−r)a_q) law; its avoidance probability is the stated rising-factorial ratio. Counting ordered r-tuples gives the exact factorial moment. For fixed r the integral approximation to ∑ a_q/(qa_q+j) has error at most 1/q, and the full infinite sum of squared summands is at most 1/q²+a_q/q. Thus the logarithmic error is o(1), uniformly even before restricting to the window. For m=floor(b_q+s_q x), the floor error in 1+m/(qa_q) is O(1/(qa_q)); taking a_q times its logarithm gives log q+x+o(1). All fixed factorial moments converge to e^(−rx), giving the Poisson law and the Gumbel probability at zero. The centering and scale use the actual a_q and have the stated leading limits. Conditioning on a designated label being unseen tilts its Beta marginal by (1−P_i)^m, giving Beta(a_q,(q−1)a_q+m); the normalized conditional mean tends to e^(−1/κ) and variance is O(1/a_q). Since the expected number of unseen labels is bounded at each fixed window location, the probability of any atypical unseen mass at m=floor(b_q−Ls_q) tends to zero for fixed L. The last label lies in that set unless completion is already observed, whose limiting probability exp(−e^L) vanishes as L grows. This proves the last-label convergence and the joint statement without assuming independence between time and the latent mark. The unconditioned normalized marginal has mean one and vanishing variance. No integer-shape assumption, quenched limit or tail-moment convergence is required. verify.py was inspected, not executed; its finite checks are ancillary.

## originality

PASS

The model, finite avoidance probabilities and unmarked extreme-value tools are established. The supported distinct conclusion is the logarithmic-shape completion window together with localization of the last label's latent mass at e^(−1/κ)/q. Existing exact probabilities and deterministic coupon criteria give direct routes to the unmarked limits after checking the intensity, but those comparisons do not identify the latent mass of the winner. The closest indexed reinforced-urn and marked-coupon findings were checked at statement level and distinguish different limits or different marks.

## value

PASS

The logarithmic regime is a natural scale where an individual rate concentrates about the uniform rate while the extreme discovery process still selects a label with an order-one relative mass bias. The actual-shape centering resolves the fluctuations at scale q, which need not be captured by the leading q log q equivalent alone, and the terminal-mass limit quantifies a phenomenon invisible in a Gumbel marginal. The conclusions are useful without suggesting a quenched theorem or extending beyond the specified window.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

Proposition 2.1 of the v1 Dyck pattern poset paper gives the distinct lower-cover count, not the number of position pairs. With X the sum of products of sizes of two different components, the count is n²/4−X/4+epsilon. Conditional on component sizes, the internal Dyck words are independent; each nontrivial size-f component has the Narayana peak law at f−1 with mean f/2, and the size-one adjustment is bounded. Narayana is hypergeometric (population 2m, m successes, m+1 draws at semilength m), so variance is O(m), the fourth centered moment O(m²), and the centered sqrt(m)-scale limit has variance 1/8. Applied to the total peaks and the conditional components, these bounds give E epsilon=O(n) and E epsilon²=O(n³); the local pattern correction is O(n). Marking the two component pairs for X² gives one coincident-pair term and six ordered edge-pair choices on either three or four marked components. With s=sqrt(1−4z), A1~1/(4s), A2~1/(8s³), and C~2, the first and second moment series have leading terms (1/2)s^−2 and (1/8)s^−6. Coefficient extraction and division by C_n give EX=(sqrt(pi)/2)n^(3/2)+O(n) and EX²=(sqrt(pi)/16)n^(7/2)+O(n³). The squared mean and the remainder are smaller; Cauchy–Schwarz gives a mixed error O(n^(13/4)), so Var(L_n)~(sqrt(pi)/256)n^(7/2). The largest-component remainder is tight since the fixed-residual limits 4^(−r−1)[z^r]C² sum to one. Hence all peak cross-products between components are O_P(n), leaving the total-peak square, whose Gaussian limit is centered at n²/4; true-mean centering shifts the limit by +sqrt(pi)/8. For the rare-split mechanism, the leading marked-pair coefficients can also be localized: with pair sizes i,j and remaining size k, the exponentially renormalized h-th pair weight (h=1 or 2) is bounded by a constant times i^(h−3/2) j^(h−3/2)(k+1)^−3/2. For k≤n/2 and min(i,j)≤δn, δ<1/4, summing gives O(δ^(h−1/2)n^(2h−2)); k>n/2 contributes O(n^(2h−5/2)). Thus the leading moment contributions come from two macroscopic components in the limit δ→0, with overlap and disjoint-pair terms subleading for the second moment.

## originality

PASS

The per-word lower-cover identity is known. A same-day insertion-deficit result treats exactly the component interaction X and covers the leading deletion mean correction by double counting consecutive-level cover edges. It does not supply a second moment of the deficit or distribution of the lower-cover degree; first moments dualize but second moments count ordered pairs of edges sharing different endpoints. The joint conclusion of a sharp n^(7/2) variance and a Gaussian n^(3/2)-scale distributional limit (with its mean-centering shift) is not thereby covered. The decision rests on that stochastic scale separation, not on reinvention of the cover formula or a priority claim for the mean alone.

## value

PASS

The exact variance gives a statistic of a natural full level of the Dyck poset that is not predicted by its weak limit. For the same valid-output diversity observable, typical peak fluctuations are Gaussian but two macroscopic components, on a vanishing-probability subset, determine the leading second moment and shift the mean relative to the typical center. The explicit constant and failure of uniform integrability distinguish risk from typical behavior, beyond a pointwise count or a weak-limit calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

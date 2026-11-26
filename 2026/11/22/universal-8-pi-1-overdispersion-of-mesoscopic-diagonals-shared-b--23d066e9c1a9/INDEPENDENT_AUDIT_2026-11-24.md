# Independent mathematical audit

## correctness

PASS

Let r count strictly intermediate vertices on the shorter arc, as in the Finding. The one-diagonal cut gives p=C_r C_{n-r-2}/C_{n-2}, with n choices of the short arc for the band under review. For fixed arcs of indices r,s, a disjoint pair may meet at an endpoint: the second start runs from r+1 to n−s−1 inclusive, giving n−r−s−1 placements per first arc. A nested pair with d=r−s has d+1 placements and the three cell factors are C_s,C_d,C_{n-r-2}; crossing pairs have joint probability zero. Squaring the single-triangulation probabilities and doubling the ordered nested contribution gives the exact first and factorial second moment. Uniform Stirling asymptotics show n p² is the Riemann-sum weight for dx/(π x³) and disjoint pairs converge to the product of first moments. For nested pairs, C_{r−d}/C_r→4^{-d} at fixed d, uniformly in a fixed positive rescaled band, and is bounded by a constant times 4^{-d} whenever both indices are in the band. Thus (d+1)C_d²/16^d=O(d^{-2}) gives summable domination. The beta integral gives 1+K=4/π for this sum including d=0, so after subtracting the product of means, the diagonal and nested terms give 1+2K=8/π−1. The same argument applies to the two orderings of f and g: for fixed d the index difference vanishes on the rescaled axis and the weights tend to f(x)g(x); fixed-width endpoint regions of an interval have vanishing total weight. Independent enumeration of noncrossing diagonal sets and of ordered pairs of triangulations confirmed the cut counts and exact rational moments for n=5 through 9, including all 14 admissible bands.

## originality

PASS

The Catalan cut identities and generating functions for the unmarked total are established antecedents. The reviewed contribution is the mesoscopic length-resolved covariance for two independent triangulations, with the specific universal factor from near-nested compatible pairs. None of the strongest inspected statements identifies that moment or its scale.

## value

PASS

At the natural length scale where shared diagonals have order-one expected count, rare occurrence alone does not predict the variance. The result pinpoints the extra near-nested contribution, gives a band-independent variance-to-mean ratio greater than one, and gives a covariance functional that applies to separated or overlapping length windows. That is useful quantitative information for the natural common-diagonal statistic, not a finite enumeration or routine feasibility check.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

On the connected symmetric stochastic domain, trace inverse of M=I−P+J/N minus 1 is the stated zero-target Kemeny constant, including periodic kernels. Its strict convexity follows by conjugating the second derivative by M^(−1/2); a nonzero symmetric perturbation has a strictly positive weighted square. Disconnected boundary points have divergent objective. Averaging over within-part permutations is sufficient to get the three edge classes, even when additional automorphisms merge classes. On the three normalized part indicators, the quotient Laplacian has trace S and principal minors Q/(ab), Q/(bc), Q/(ca); this and the vertex-contrast eigenvalues give the stated F. For c<a+b, all three capacities are tight and the capacity multipliers have the stated cyclic formula. In the potentially negative regime, bc=Q+Y² and a=X+Z give the displayed bound Q²−bc(XZ−2aY)>0, whereas singleton parts have 2aY>XZ directly. For c≥a+b, the negative gradient at (0,b,a) is (2,f,f) with f>1 (the numerator at c=a+b is (a+b)²(2(a+b)−3) and increases thereafter). The nonnegativity multiplier 2f−2 and the two capacity multipliers f give KKT stationarity, including equality when the third capacity is tight but its multiplier is zero. This certifies the global unique kernel. Substitution gives the values, both equal to N−3/2 at c=a+b. Read VERIFICATION.md and check.py without executing the uploaded code. Independently checked the inverse trace on full matrices for eight triples spanning singleton, balanced, equality, and imbalanced cases, with agreement to within 4×10⁻¹⁵. The finite check is not needed for the KKT conclusion.

## originality

PASS

The novelty supported here is the explicit active-set law for arbitrary positive tripartite part sizes, not the general convex optimization formulation, strict convexity, or the complete-split intersection. In particular the exact intersection K_{1,1,c}, c≥2, is also covered by a distinct complete-split result; the shared record date gives no historical order.

## value

PASS

The classification gives an exact, nontrivial support boundary in a standard graph family for a natural Markov objective; the optimal walk deletes a whole permitted edge class even at a no-holding boundary. It certifies uniqueness against asymmetric edge assignments and provides solved instances for the general optimization framework. The value lies in general tripartite sizes, not in repeating the split overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.

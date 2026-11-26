# Independent mathematical audit

## correctness

PASS

The mixing density puts weights 1-q and q on gamma shapes one and three; Poissonization gives the stated mixture with common NB parameter q and normalizes at one. Complex-root factorization shows b_n=q^n[3-2 Re(u^n)]>0 with summable b_n/n. For the analytic pgf, thinning at c approaching one forces each b_n-b_(n+1)>=0 by expanding the quotient to first order in 1-c. Conversely, if those differences are nonnegative, integrate (v-1)(log G)'(v)=sum_n (b_n-b_(n+1))(v^n-1) along v=1-s+sz for c<=s<=1 with weight ds/s; the logarithm of the quotient has nonnegative summable positive-degree coefficients. This verifies the criterion independently in this setting. Directly using Re(u) and Re(u²) gives b_1-b_2=q(1-q)P(q)/(1+d)^2. Substitution q=(1+theta)^(-1) gives the quartic, strictly increasing for positive theta; the signs at q=7/10 and 71/100 locate the unique boundary. For every n>=2 the conjugate term is bounded by |u|^n |1-qu| and yields the sufficient strict inequality 9(1-q)(1+q(1-q))³>4, which holds for 0<=q<=71/100 by the derivative's one interior maximum and exact endpoint bounds. Thus all later comparisons are strict everywhere in the surviving region, including the first-term tie at the boundary. At theta=2/5, b_1-b_2=-2390/170569 while p_(n+1)-p_n=-8q^n(5(n-1)²+4)/16807<0 for every n>=0. Independent exact checks and output: branches/1733d608-ca72-4d03-9d19-fc070f81b70c/independent_check.py and independent_check.log; the frozen checker was inspected, not executed.

## originality

PASS

The distinct geometric/shape-three mixture record 669cf2e9718e is exact broader coverage of the compound-Poisson baseline, not of the pointwise thinning frontier or the decreasing-mass witness. Its theorem is uniform over q at a fixed mixture weight. The xgamma specialization instead follows a curve of changing mixture weights p=1-q, and the surviving sharp boundary is outside its uniform guarantee. Credit the compound-Poisson formula as overlapping context, not an independent new claim. The quartic frontier and the full-support witness survive the comparison.

## value

PASS

For this applied count family, the result reduces an infinite marginal-feasibility test to a single sharp parameter boundary with its equality structure, and the exact monotonically decreasing PMF on the excluded side shows why elementary shape and ordinary compound-Poisson structure do not suffice. The improvement over a sufficient uniform-in-rate region is a pointwise classification, not a numerical refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.

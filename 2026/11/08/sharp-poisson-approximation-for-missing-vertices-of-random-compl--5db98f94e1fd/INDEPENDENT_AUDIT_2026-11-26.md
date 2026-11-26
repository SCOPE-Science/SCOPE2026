# Independent mathematical audit

## correctness

PASS

The coefficient counts sum spanning trees on each retained vertex set (the singletons must be included), not equally weighted vertex sets. In the balanced case the log coefficient correction in units of 1/m is 3k/2-(i-j)^2: the two binomial falling factorials contribute -(i(i-1)+j(j-1))/2, and the retained-size powers contribute i(j+1)+j(i+1)-(i²+j²)/2. At fixed k the binomial weights average (i-j)^2 to k, leaving k/2, precisely the first-order correction of θ^k. The log remainders and exponentiation cost O((k+1)^4/m²) uniformly up to m^(1/9). The analogous proportional-size log remainder is O((k+1)^2/N) without a second-order match. Re-expanding the three balanced terms in R₂-θ²/2 gives second-order coefficients (-2/3,35/6,-2×5/6) in units e^(-2)/m², totaling 7/2. For unequal proportional sides let A and B be the two contributions to θ. The same-side terms divided by A²/2, B²/2 are respectively 1-N/a²+O(N^-2), 1-N/b²+O(N^-2); the cross term divided by AB is 1+N/(ab)+O(N^-2). This gives -N(A/a-B/b)^2/2 to first order and the claimed squared limiting constant; equality of the two limit terms would require log(a/b)+a/b-b/a=0 in the limit, possible only at balance. The extension/leaf-deletion double count gives factorial domination up to half the minimum degree; every smaller tree extends up to that cutoff, and a larger tree has at most one subtree per fixed subset of its vertices, giving a super-polynomial remaining tail. Summed coefficient error controls the normalization, and the Poisson-vanishing statistic p₂/p₀-(p₁/p₀)^2/2 supplies the matching lower bound since both zeroth masses stay bounded below. Replay: frozen RESULT.md lines 35–102 (all-scale estimates) and verify.py (inspected only; finite checks are not a proof of the TV orders). The result does not give a uniform transition for near-balanced unequal parts or extreme imbalance.

## originality

PASS

The tree enumeration, spanning-probability limit and prelimit-parameter Poisson framework have prior coverage. The checked claims do not supply the sharp rates or the second-coefficient residuals, and the refinement is supported by model-specific higher-order cancellation and a lower bound.

## value

PASS

Improves an already established Poisson phenomenon in a natural structural family: balanced parts remove an entire leading order, unlike fixed unequal proportions, and a residual diagnostic gives real distribution-level sharpness and explains the sign change. This is more than recomputing limiting masses. The comparison specified is to θ=R₁, not a fixed limiting law or a claim of an exactly optimal TV parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.

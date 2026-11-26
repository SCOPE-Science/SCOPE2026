# Independent mathematical audit

## correctness

PASS

For each real p>0 and for the separate p=0 negative log pseudodeterminant, the scalar eigenvalue loss is strictly convex on (0,infinity). Its trace Hessian on the centered positive-definite restriction has strictly positive coefficients (divided differences of the derivative, or the second derivative at repeated eigenvalues). The conductance-to-restricted-Laplacian map is injective from the distinct off-diagonal entries and the known constant kernel. Existence follows from the compact budget simplex, feasible connected designs, and divergence approaching disconnection; for the log objective all other eigenvalues are bounded above on this simplex so they cannot cancel that divergence. Strict convexity gives uniqueness before imposing any symmetry. Hub swaps and page permutations then force common positive spokes x and a spine y>=0. Page differences, the symmetric hub/page contrast, and the antisymmetric hubs give (2x)^(multiplicity m-1), (m+2)x, and mx+2y as eigenvalues (first notation indicates multiplicity, not a power). Independently vary x in (0,B/(2m)] with hub eigenvalue d=2B/c + m(1-4/c)x. For p>0 the scalar objective is A x^(-p)+d^(-p); its derivative divided by p is -A/x^(p+1)+m(4-c)/(c d^(p+1)). For p=0 use the same derivative expression with A=m and no division by p. Convexity gives positive y exactly when the right-boundary derivative is positive, equivalent to c<4/(1+m^p A); equality gives y=0. Solving the derivative equation with d/x=m+2t recovers the stated allocation. For m=2 the denominator is 2+2^(-p). For m>=3 its p-derivative is at least 2 log(3/2)+log(3/5)>0 and the denominator diverges. Dividing the same expression by m^(p+1)/2^p verifies the large-m formula. For m=2 let g=log((4-c)/c)-log(1+2^(-p)); active t=exp(g/(p+1))-1, and the derivative sign is N=(p+1)g'-g. On c<2, N strictly decreases from (3/2)log 2-log((4-c)/c) to -log((4-c)/c), giving the sharp peak threshold and single root. At any activation g=0 and N>0, so that root is strictly in the active region; the budget share strictly increases with t. The limiting g gives the claimed high-order equivalent; c>=2 is always inactive. This analytical check covers ties and all stated real orders and budgets. The supplied numerical script was inspected, not treated as a universal proof.

## originality

PASS

Credit the exact p=0 determinant cutoff for m>=3 and p=1 resistance cutoff for m>=2 as known on the identical graph and prices. The distinct claim is the all-real-order solution with opposite threshold monotonicities by page count and a sharp unique B2 spending peak. Same-day spectral-moment allocation results on other graph families are substantial analogues, not precedence evidence or coverage of the book theorem.

## value

PASS

The optional short link in a book network creates an interpretable design decision across statistical and diffusion objectives sharing the same budget. The opposite full-order support behavior of B2 versus larger books, and the nonmonotone yet unique two-page spending peak, distinguish edge presence from edge expenditure in an exact unrestricted design. These are structural results for the whole natural priced family, not simply recomputed endpoint values.

The dated certificate retains the supplied scientific assessment, sources and limitations.

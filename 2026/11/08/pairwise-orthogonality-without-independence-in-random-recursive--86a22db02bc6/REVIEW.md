# Scientific review

## Correctness — PASS
The mixed moment \(\mathbb E[S_i(n)S_j(n)]=n^2/(ij)\) follows from a conditional product recurrence and the exact ancestry probability \(1/i\); the result holds for every \(n\ge2\) and \(i<j\). A separate parent-choice telescoping calculation proves the strict negative covariance of singleton-subtree indicators for every \(2\le i<j<n\). One-label variances follow from the two-color Pólya urn. Summation reconstructs the classical total-path-length variance without relying on finite experiments. An exhaustive, exact-rational checker independently verifies 336 assertions across all 46,233 trees of orders 2–9. Main risk: inadvertent convention changes between inclusive subtree size and descendants excluding the root, explicitly prevented by the definitions.

## Originality — PASS, with bounded historical-priority risk
Kuba–Panholzer (2006), read in full, derives one-label descendant distributions and factorial moments, not the two-label mixed moments. The examined full text of Feng–Mahmoud (2010) concerns unlabelled fringe-shape counts; its two-piece decomposition does not assert pairwise birth-label orthogonality. Mahmoud–Smythe (1991) treats a single marked rooted subtree; full text was not accessible in this review and remains a named residual risk. Existing nearby research on direct-child count versus a labeled subtree and on the special vertex-2 subtree size versus an aggregate fringe profile addresses different random variables. Neither its statements nor the classical total path-length variance, considered alone, implies the individually zero covariances without further calculation. Search and reading do not prove historical uniqueness; some earlier multivariate-urn treatment may cover the formula implicitly.

## Value — PASS
It is not evident from the marginal beta-binomial laws that all distinct birth-labelled subtree sizes have exactly diagonal covariance, especially since their descendant sets are nested or disjoint depending on the random ancestry relation. The theorem explains an exact cancellation between competition and ancestor nesting, demonstrates that this orthogonality coexists with strict dependence for every nonconstant pair, and gives a natural diagonal decomposition of the global total-path-length fluctuation. These are structurally useful joint properties of an established random-tree model, not a replacement for an already known variance identity.

## Scope and independent review
The proof does not establish independence or conclusions for preferential attachment and nonuniform growing trees. The cited 1991 article and possible broader joint urn representations retain residual priority uncertainty.

Self-review: passed. Independent audit: not yet performed.

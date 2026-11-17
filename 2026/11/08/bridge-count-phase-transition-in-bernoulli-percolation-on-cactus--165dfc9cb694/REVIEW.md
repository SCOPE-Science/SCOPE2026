# Independent mathematical audit

## correctness

PASS

For cactus cycles C_j each retained cycle is either entirely present and has zero bridges within C_j, or is incomplete and every retained cycle-edge is a bridge; noncycle original bridges remain bridges. Thus B=X−Σ c_j I_j with independent edge blocks, giving the exact joint PGF and Cov(X,B)=p(1−p)(m−Σ c_j²p^{c_j−1}). Strictly increasing Σ c_j²p^{c_j−1} gives the unique interior sign change iff Σ c_j²>m. Conditioning X=e makes the edge set a uniform e-subset: f(e)=e−Σ c_j(e)_c_j/(m)_c_j; its second difference is −Σ c_j²(c_j−1)(e)_(c_j−2)/(m)_c_j≤0, with correct endpoint first differences. Tree case, m≥1 and p=0,1 boundaries separately handled. Independent rational enumeration of triangle with 0,1,6,7 pendant edges at p=2/5 reproduced covariance exactly; the original source finite checker was inspected, not treated as an infinite proof.

## originality

PASS

Best-of-knowledge comparison of the exact observable (joint count of retained edges and surviving bridges) finds earlier general component-size algorithms and edgewise bridge-probability methods, and cactus connectivity correlations, but not the closed all-cactus bivariate PGF or its sharp sign criterion and fixed-budget concavity. This is an explicit conditional judgment; all general connectivity algorithms could encode the observable only via additional work.

## value

PASS

The exact bivariate law simultaneously determines arbitrary bridge-count mixed moments and the sharply characterized positive-to-negative covariance boundary across all finite cacti. Fixed-edge-budget concavity and at most two adjacent optimizers link Bernoulli and uniform-subset models. These are motivated structural and phase-boundary facts for a natural graph family, not merely a renamed known table or tiny unmotivated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

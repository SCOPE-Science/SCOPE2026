# Scientific review of entropy-optimal bidirectional Hardy averaging

## Correctness — PASS

The distributional-BV signed-measure representation reduces the operator defect to the explicitly calculated kernel \(K_\alpha(x,s)\). Its \(L^1\) norm is exactly \(E_\alpha(s)\), which is strictly concave in the jump coordinate and therefore has a unique optimizer. A single jump realizes the upper bound; uniqueness of the maximizing coordinate proves all interior-weight equality cases. Evaluation at the midpoint establishes the global mixture lower bound and its unique optimality. The entropy second-derivative estimate proves the uniform quadratic stability inequality, and near-midpoint jumps establish sharpness of the stability coefficient. The standalone checker passed all documented numerical tests. No finite test is used as an infinite proof.

## Originality — PASS with historical risk

The directly inspected primary papers are Nekvinda–Pick (2011), Soria (2010), and Lu–Yan–Zhao (2013). They study optimal Hardy source/target spaces, one-sided identity defects on decreasing-function cones in Lorentz settings, and higher-dimensional \(L^p\) Hardy estimates, respectively. These statements do not imply the all-real-BV, unweighted integrated error for a convex family of *forward and reflection-conjugate* Hardy averages, its uniquely minimizing symmetric mixture or its sharp quadratic location bound. The reflected average is not the Copson integral adjoint, and a superposition of two operators is not their convex sum. Electronic searches did not reveal an exact equivalent; searches cannot establish a priority theorem. Unindexed historical work and other terminology remain residual risks.

## Value — PASS

The precise mathematical choice is whether to average all observations left of a location, all observations right of it, or to mix both while retaining constants. The optimal \(BV\)-normalized integrated approximation error is not furnished by either one-sided norm alone: directional averaging has sharp constant \(e^{-1}\), while the unique optimally balanced design has the smaller exact constant \((\log2)/2\). The new stability inequality bounds *how the entire variation measure must localize* when the worst-case error is nearly attained; it is sharp even for infinitesimal displacement of a single discontinuity. Thus the exact coefficient and rigidity identify an intrinsic design tradeoff for prefix/suffix smoothing of discontinuities, beyond a generic boundedness estimate.

## Sources and limitations

Primary full-text materials: https://ems.press/content/serial-article-files/35810 ; https://www.impan.pl/shop/en/publication/transaction/download/product/89912 ; https://link.springer.com/article/10.1186/1029-242X-2013-148 . No assertion is made for nonconvex or position-dependent weights, other norms or dimensions. Historical priority and independent mathematical verification remain open.

Self-review: passed. Independent audit: not yet performed.

# Review: sharp geodesic widths at tree-zonotope local minima

## Correctness — PASS
The result specifies finite simple unweighted trees and the zero-sum Euclidean unit sphere. The edge-difference maps form a basis because a tree has no cycles. For any candidate direction with two or more active differences, restricting to the open sign region of the corresponding linear subspace excludes a local minimum. For a one-edge cut, strict cut-covariance inequalities make the one-sided tangent variation positive. Projecting the other centered cut indicators produces an exact \(\ell^1\)-to-Euclidean comparison, with equality on an explicitly signed single projected cut. Positivity of the distinguished edge difference over the explicit angular interval gives the attained finite-angle formula. Direct Gram substitution checks the path and star corollaries. The supplied exact checker reproduced its claimed finite counts.

## Originality — PASS (historical priority provisional)
Padrol–Pilaud–Poullot (arXiv:2111.12422, full HTML article read) characterize graphical-zonotope deformation cones, rather than the sphere-wide local width minima or angular profiles. Feld–Aujol–Gilboa–Papadakis (2019, indexed abstract inspected) study general one-homogeneous Rayleigh quotient flows, specifically graph total variation on an \(\ell^1\) sphere, not this explicit Euclidean tree classification. Kolmogorov–Pock–Rolinek (2016, abstract inspected) treat total-variation minimization with unary terms on trees. Known global inradius results are stronger for global cut minima only, but do not logically yield all nonglobal local minima or the exact attained geodesic coefficients. Complete text of some relevant optimization literature was not available, so an equivalent earlier statement remains possible.

## Mathematical value — PASS
The Euclidean width function is a natural nonsmooth, nonconvex optimization landscape attached to a well-studied family of zonotopes. The theorem describes every strict local well, gives its exact finite-angle stability profile for any tree, and distinguishes leaf-edge profiles of combinatorially equivalent path and star parallelotopes by an unbounded ratio \(n-2\), despite equal width at the compared directions. Its contribution is a complete geometric stability classification, not a restatement of the known global inradius or a finite numerical catalogue.

## Scientific limitations
The current proof does not classify local maxima, weighted trees, non-tree graphs, or angles outside the explicit interval. Exact rational computations on finitely many labeled trees do not establish an infinite theorem. Independent mathematical review and exhaustive historical-priority confirmation remain outstanding.

Self-review: passed. Independent audit: not yet performed.

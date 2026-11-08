# Central-witness convexification thresholds for every skeleton of a product of simplices

## Finding

Let \(P=\Delta_{d_1}\times\cdots\times\Delta_{d_r}\) be a Cartesian product of \(r\ge1\) nondegenerate simplices, with \(d_i\ge1\) and \(D=\sum_i d_i\ge2\). Let \(S_k(P)\) be the **closed** union of its faces of dimension at most \(k\), where \(0\le k<D\). Let \(c_P\) be its vertex centroid (equivalently, the product of the individual simplex centroids). For every real \(t\ge0\),

\[
S_k(P)+tP=(1+t)P
\quad\Longleftrightarrow\quad
\sum_{i=1}^r\left\lceil\frac{d_i+1}{1+t}\right\rceil\le k+r
\quad\Longleftrightarrow\quad
(1+t)c_P\in S_k(P)+tP.
\]

Consequently the exact polytope-relative Schneider convexification index is

\[
\boxed{\displaystyle
c^{(P)}(S_k(P))=
\min_{\substack{1\le s_i\le d_i+1\\\sum_i(s_i-1)\le k}}
\max_{1\le i\le r}\left(\frac{d_i+1}{s_i}-1\right).}
\]

The minimum is attained, is rational, and is independent of simplex shape. This is both an exact threshold and a **single-point nonconvexity witness theorem**: whenever the Minkowski sum fails to be convex, it omits the scaled centroid.

## Assumptions and scope

All simplices are full-dimensional in their factor affine spans; they need not be regular, lattice, or congruent. Minkowski addition and dilation use ambient Euclidean affine coordinates with a fixed origin. By affine equivariance, the statements are independent of the origins and of nonsingular affine changes of coordinates. The closed skeleton includes the full relative boundaries of its faces. In the displayed threshold, \(t\ge0\) and \(k\in\{0,\ldots,D-1\}\). The displayed optimization uses integer support bounds \(s_i\). Since \(\operatorname{conv} S_k(P)=P\), the Minkowski sum is convex if and only if it equals \((1+t)P\).

## Proof

**1. Barycentric model of faces.** In factor \(i\), write barycentric coordinates with \(n_i=d_i+1\) nonnegative entries summing to one. For any \(a=(a^{(1)},\ldots,a^{(r)})\in P\), let \(q_i(a)\) be the number of strictly positive coordinates in factor \(i\). The minimal product face containing \(a\) has dimension

\[
\sum_{i=1}^r(q_i(a)-1).
\]

Thus \(a\in S_k(P)\) precisely when this sum is at most \(k\).

**2. An exact capacity criterion.** For any \(y\in(1+t)P\), denote its barycentric blocks by \(Y^{(i)}\), each nonnegative and summing to \(1+t\). A representation \(y=a+tb\) with \(a,b\in P\) is equivalent to finding for each factor a nonnegative probability vector \(A^{(i)}\le Y^{(i)}\) coordinatewise. For \(t>0\), take \(B^{(i)}=(Y^{(i)}-A^{(i)})/t\); at \(t=0\), choose \(b\in P\) arbitrarily. A probability vector \(A^{(i)}\le Y^{(i)}\) with support size at most \(s\) exists if and only if the sum of the \(s\) largest coordinates of \(Y^{(i)}\) is at least one. Necessity is immediate. Sufficiency follows by greedily filling unit mass in those \(s\) coordinates without exceeding their available masses. Consequently \(y\in S_k(P)+tP\) if and only if there are integers \(s_i\in\{1,\ldots,n_i\}\), \(\sum_i(s_i-1)\le k\), for which each block's largest \(s_i\) coordinates total at least one.

**3. Centroid extremality.** For every nonnegative block with \(n_i\) entries and total \(1+t\), its \(s\) largest entries sum to at least \(s(1+t)/n_i\). Thus the sufficient support allowance

\[
s_i(t)=\left\lceil\frac{n_i}{1+t}\right\rceil
\]

works for **every** target \(y\). If \(\sum_i(s_i(t)-1)\le k\), Step 2 constructs a decomposition for every \(y\in(1+t)P\). Conversely, at the factorwise centroid all the entries are equal to \((1+t)/n_i\), so a probability vector dominated by that block must have at least \(s_i(t)\) nonzero entries. If the budget inequality fails, Step 2 excludes \((1+t)c_P\). This proves the three-way equivalence, including the ceiling boundary and \(t=0\).

**4. Exact threshold.** For a prescribed integer support allowance \(s_i\), the centroid capacity inequality is \(t\ge n_i/s_i-1\). Hence a support-allocation tuple with \(\sum_i(s_i-1)\le k\) works exactly at and above the maximum of these rational bounds. Minimizing over finitely many allowable tuples proves the index formula; its infimum is achieved because the inequalities are closed and there are finitely many allocations. \(\square\)

Three useful exact consequences: for vertex sets \(k=0\), the index is \(\max_i d_i\); for the boundary \(k=D-1\), the index is \(1/\max_i d_i\). For the one-skeleton in dimension four, \(\Delta_2\times\Delta_2\) has index \(2\), while a four-simplex has index \(3/2\). The product family therefore exhibits a genuine combinatorial dependence not determined by ambient dimension and skeleton order alone.

## Verification

The accompanying `verify.py` uses exact rational arithmetic and independently enumerates all coordinate-subset choices needed to dominate a unit-mass vector. For varied small products, skeleton dimensions, and dilation parameters, it compares this independent feasibility search against the ceiling criterion, checks the sharp centroid obstruction, and evaluates the separate finite minimum over support budgets. Run `python verify.py` from the extracted package directory. It reports `VERIFY_OK 1380 exact rational instances; 350 centroid witness checks; support allocations and index minimizations`. The exhaustive support tests in these finite cases are supplementary only; the capacity argument and averaging inequality above prove the arbitrary-dimensional theorem.

## Relationship to prior work

Meyer (2026) develops general necessary-and-sufficient exposed-set criteria for when the Minkowski sum of a nonconvex set and a dilated convex body becomes convex, including a specialized polytope criterion. The work motivates the quantitative question, but the inspected text does not supply an exact ceiling formula for every skeleton of a product of simplices or the single-centroid equivalence above. Schneider (1975) introduced the corresponding finite convexification index; the boundary and vertex cases agree with the classical index framework, but do not imply the intermediate-skeleton product classification.

A separate published result, *Sharp finite convexification thresholds for every skeleton of a simplex* (2026), analyzes **equal-weight Minkowski averages of multiple copies of a nonconvex simplex skeleton**. It proves a threshold on the number of skeleton summands. Our statement instead adds **one copy of a scaled convex product** and identifies a threshold for that different operation, with several simplex factors. In particular, the self-summation result supplies neither the displayed product support-allocation formula nor the all-scale centroid test. Related broad Shapley–Folkman-type convexification statements concern convergence or approximate convexity and do not by themselves give this exact finite equality.

## Limitations

The hypothesis that the convexifier is the same product of simplices is essential to the coordinatewise capacity reduction; no corresponding universal center-witness assertion is claimed for arbitrary polytopes. The formula is an exact finite-dimensional assertion, not an asymptotic statement. The supplementary verifier cannot exclude previous independent discovery. Absolute historical priority has not been established, and no generalization to arbitrary convexifiers is claimed.

## References

1. Mark Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744v1, first public 2026-10-19, https://arxiv.org/abs/2610.26744 .
2. Rolf Schneider, *A measure of convexity for compact sets*, Pacific Journal of Mathematics **58** (1975), 617–625, https://doi.org/10.2140/pjm.1975.58.617 .
3. *Sharp finite convexification thresholds for every skeleton of a simplex*, published research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-finite-convexification-thresholds-for-every-skeleton-of-a--92b027220722 .
4. Matthieu Fradelizi, Mokshay Madiman, Arnaud Marsiglietti, Artem Zvavitch, *The convexification effect of Minkowski summation*, arXiv:1704.05486v1, 2017, https://arxiv.org/abs/1704.05486 .

# Sharp diagonal-metric coordinatewise sensitivity of strict permutahedral projection

## Finding

Let \(n\ge 3\), let \(c_1>c_2>\cdots>c_n\) be arbitrary real numbers, and let \(\mathcal P(c)\subset\mathbb R^n\) be their permutation polytope. For fixed positive \(w_1,\ldots,w_n\), define the weighted nearest-point map
\[
Q_w(y)=\operatorname*{argmin}_{z\in\mathcal P(c)}\frac12\sum_{i=1}^n w_i(z_i-y_i)^2.
\]
Put \(a_i=1/w_i\), let \(A=\max_i a_i\), and sort the remaining \(n-1\) inverse weights (with one occurrence of \(A\) removed) as \(0<b_1\le\cdots\le b_{n-1}\). Then the **exact global input/output coordinate-maximum Lipschitz constant** is
\[
\boxed{\operatorname{Lip}_{\infty\to\infty}(Q_w)=1+\max_{2\le r\le n-1}\frac{(r-1)A}{A+\sum_{j=1}^r b_j}.}
\]
It is attained by a pair of distinct finite input vectors. The constant is independent of the particular strictly decreasing generating vector \(c\), and requires only sorting and a prefix scan to evaluate.

The smallest possible constant over diagonal weights is \(2-2/n\), reached precisely when all weights agree (up to a common factor). The supremum over positive diagonal metrics is \(n-1\), not attained for any finite strictly positive weights. A proper face, rather than the full relative interior of the permutahedron, can determine the worst case: for \(n=5\) and inverse weights \((100,100,1,1,1)\), the sharp coefficient is \(303/103\), realized by a four-coordinate block, whereas the full-dimensional affine piece has coefficient \(503/203\).

## Assumptions and scope

All spaces and parameters are real. The generating entries must be pairwise distinct; no positivity or spacing assumptions on them are required. The metric is the squared quadratic distance with the *fixed diagonal* matrix \(W=\operatorname{diag}(w_1,\ldots,w_n)\); the norm used to measure input and output errors is the ordinary unweighted \(\ell_\infty\) norm. The problem is not Euclidean projection in that error norm, nor a statement about non-diagonal positive definite metrics.

For each \(y\in\mathbb R^n\), strict convexity gives a unique minimizer. The global coefficient is the supremum over \(y\ne y'\) of \(\|Q_w(y)-Q_w(y')\|_\infty/\|y-y'\|_\infty\).

## Proof

**Face structure.** An exposed face of \(\mathcal P(c)\) is indexed by an ordered partition \(B_1,\ldots,B_t\) of \(\{1,\ldots,n\}\), obtained by grouping equal coefficients of an exposing linear functional. Rearrangement assigns to each block a consecutive portion of the distinct values \(c_i\). Its face is the Cartesian product (in the corresponding coordinate blocks) of the permutahedra of those portions. Because all \(c_i\) are distinct, its affine hull consists exactly of the independent equations \(\sum_{i\in B_j}z_i=\gamma_j\) for fixed block sums \(\gamma_j\). Conversely, every ordered partition is exposed by taking distinct exposing values on its blocks. In particular, every nonempty coordinate subset can occur as a block of a face, with all remaining coordinates singleton blocks.

**Active-face linear pieces.** Let \(q\) belong to the relative interior of a face \(F\). At any input \(y\) for which \(W(y-q)\) belongs to the relative interior of the normal cone of \(F\), weighted projection onto \(\mathcal P(c)\) agrees, locally, with weighted projection onto the affine hull of \(F\). Indeed the weighted first-order condition is \(W(y-q)\in N_{\mathcal P(c)}(q)\), and the relative interiors of both the face and its normal cone persist under sufficiently small perturbations of the input. There are finitely many such polyhedral affine cells; continuity of the weighted projection extends piecewise-affine bounds across their boundaries.

For a face block \(B\) of size \(s\), put \(A_B=\sum_{k\in B}a_k\). Minimizing the diagonal quadratic subject to the block-sum equality gives the local formula
\[
(Q_w(y))_i=y_i-\frac{a_i}{A_B}\left(\sum_{j\in B}y_j-\gamma_B\right),\qquad i\in B.
\]
Thus its Jacobian block is \(J_{ij}=\mathbf 1_{\{i=j\}}-a_i/A_B\) for \(i,j\in B\), with zeros outside the block. For \(s=1\) its only row is zero. For \(s\ge2\), the absolute row sum for \(i\in B\) is exactly
\[
\sum_{j\in B}|J_{ij}|=1+\frac{(s-2)a_i}{A_B}.
\]
Because a continuous piecewise-affine map has a global Lipschitz coefficient equal to the maximum induced norm of its affine pieces, and because every face has an open nonempty projection cell in which its Jacobian is attained, the required coefficient equals
\[
\max\left\{1,\max_{B\subseteq\{1,\ldots,n\},\ |B|\ge3}\ \max_{i\in B}\left(1+\frac{(|B|-2)a_i}{\sum_{j\in B}a_j}\right)\right\}.
\]
This also proves attainment by distinct inputs: select a point in an open cell of a maximizing face and perturb it a sufficiently small nonzero distance in a coordinate-sign direction attaining the induced row norm. The entire short segment remains in the same affine cell.

**Optimize over face blocks.** Fix a maximizing subset \(B\), its size \(r+1\), and its maximizing row \(i\). That row must have the largest inverse weight within \(B\). If a global maximum inverse weight \(A\) is outside \(B\), replacing \(i\) by an index carrying \(A\) strictly improves or preserves the ratio \(a_i/(a_i+\sum_{j\in B\setminus\{i\}}a_j)\). Hence one can always use an index of weight \(A\). For fixed \(r\), retaining that index and choosing the other \(r\) indices with the smallest inverse weights minimizes the denominator. Maximization over \(2\le r\le n-1\) yields the stated formula.

**Extremal metric consequences.** The choice \(r=n-1\) gives \(\operatorname{Lip}_\infty(Q_w)\ge 1+(n-2)A/\sum_i a_i\ge2-2/n\). Equality forces every inverse weight equal, and equal inverse weights attain equality because \((r-1)/(r+1)\) increases with \(r\). Every positive metric has \(\operatorname{Lip}_\infty(Q_w)<n-1\), because each fraction in the formula is strictly below \(r-1\le n-2\). Taking one inverse weight to infinity with all others fixed forces the \(r=n-1\) term toward \(n-1\).

**A genuinely proper-face maximizer.** For inverse weights \((100,100,1,1,1)\), the candidates for \(r=2,3,4\) are respectively \(1+100/102\), \(1+200/103\), and \(1+300/203\). The middle is strictly the largest, giving \(303/103\). The full-affine-piece norm is only \(503/203\). In particular, examining only the affine hull of the whole polytope misses the sharp coefficient.

## Verification

Run `python3 checker.py` using only the Python standard library. The script performs 600 independent rational-parameter comparisons of the sorted formula against exhaustive subset/row maximization for dimensions three through seven. It also checks two explicitly constructed rational input/projection pairs on the standard five-coordinate permutahedron: all subset facets and the first-order optimality inequality against all 120 permutation vertices are checked exactly, and the achieved finite ratio is \(303/103\). The program verifies finite instances; the preceding arguments establish the statement for all admissible dimensions and real parameters.

## Relationship to prior work

Lim and Wright's 2016 paper develops algorithms for permutahedral projection under *uniformly separable* Bregman divergences. Its identical per-coordinate divergence restriction does not cover the nonuniform diagonal quadratic metrics considered here. Moondra, Mortagy, and Gupta (public preprint of June 22, 2021) analyze repeated projections onto submodular base polytopes and the behavior of their active faces; their Euclidean perturbation treatment and uniformly separable projection algorithms do not state this anisotropic sharp coordinatewise formula. Padrol, Pilaud, and Poullot (2023 online publication) describe the ordered-partition normal-fan geometry of graphical zonotopes, a structural ingredient compatible with the face argument here, not a metric-sensitivity theorem. The formula can also be viewed as a sharp weighted operator norm among the block-centering projectors arising on permutahedral faces; it is not a statement about entropy-regularized soft ranking, ordinary Euclidean simplex score maps, or uniform-metric \(\ell_p\) projections.

## Limitations

This is a same-model mathematical argument with supplementary exact-rational checks, not an independently audited result. No claim is made for generating vectors with repeated entries, general positive-definite non-diagonal metrics, other endpoint norms, or nonlinear Bregman divergences. The priority review cannot exclude a differently phrased older theorem on weighted quadratic projections or generalized-permutahedron perturbation bounds. Computational tests do not prove the infinite parameter family independently of the analytic proof.

## References

1. J. Moondra, H. Mortagy, S. Gupta, *Reusing Combinatorial Structure: Faster Iterative Projections over Submodular Base Polytopes*, first public arXiv posting 2021-06-22, https://arxiv.org/abs/2106.11943 .
2. C. H. Lim, S. J. Wright, *Efficient Bregman Projections onto the Permutahedron and Related Polytopes*, AISTATS/PMLR 51 (2016), https://proceedings.mlr.press/v51/lim16.html .
3. A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, first online 2023-10-13, https://doi.org/10.1007/s00454-023-00586-x .

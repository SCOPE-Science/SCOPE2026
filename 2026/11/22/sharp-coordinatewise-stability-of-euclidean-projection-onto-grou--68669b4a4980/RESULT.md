# Sharp coordinatewise stability of Euclidean projection onto group-maximum balls

## Finding

For any partition of a finite coordinate set into \(m\ge1\) nonempty blocks \(G_1,\dots,G_m\), write \(d_i=|G_i|\). Given \(R>0\), let \(P_R\) be Euclidean nearest-point projection onto
\[
K_R=\left\{x:\sum_{i=1}^{m}\|x_{G_i}\|_\infty\le R\right\}.
\]
Every vector norm used to quantify perturbations below is **coordinatewise** \(\ell_\infty\), not the block maximum/sum norm defining the ball. Let \(d_{(1)}\ge\cdots\ge d_{(m)}\) be the sorted block sizes. Then
\[
\operatorname{Lip}_\infty(P_R)=
\begin{cases}
1,&m\le2,\\
\displaystyle 1+\max_{2\le k\le m-1}\frac{k-1}{1+\sum_{j=1}^{k}d_{(j)}^{-1}},&m\ge3.
\end{cases}
\]
This constant is **attained** by a pair of distinct finite inputs on a common open affine region. Thus \(P_R\) is coordinatewise nonexpansive if and only if \(m\le2\). Computing its sharp conditioning requires sorting the \(m\) block sizes and then a linear prefix scan: \(O(m\log m)\) arithmetic comparisons/operations. In particular, for \(m\ge3\) equally sized blocks of cardinality \(q\),
\[
\operatorname{Lip}_\infty(P_R)=1+\frac{q(m-2)}{q+m-1}.
\]
For singleton blocks the value specializes to \(2-2/m\), and for fixed \(m\ge3\) the equal-block coefficient approaches \(m-1\) as \(q\to\infty\). The radius \(R>0\) does not enter the coefficient.

## Assumptions and scope

The ambient dimension is the positive integer \(n=\sum_i d_i\). All groups are nonempty, mutually disjoint, and cover the coordinates. The input, output and projection are real; projection means minimizing squared Euclidean distance, uniquely, over the closed convex group-maximum ball. The theorem excludes the degenerate radius \(R=0\), for which projection is the zero map and has Lipschitz coefficient zero. The strict open-cell attainability statement concerns pairs of sufficiently close but unequal inputs, not arbitrary input pairs.

## Proof

**1. Clipping optimality.** By invariance under coordinatewise sign changes, consider nonnegative inputs \(y\). If \(\sum_i\|y_{G_i}\|_\infty\le R\), the projection is \(y\), contributing Jacobian norm one. Otherwise introduce cap variables \(t_i\ge0\), \(\sum_i t_i=R\). Given the caps, the optimal output is \(x_{ij}=\min\{y_{ij},t_i\}\), and the remaining convex problem minimizes
\[
\frac12\sum_{i=1}^{m}\sum_{j\in G_i}(y_{ij}-t_i)_+^2
\quad\text{subject to }t_i\ge0,\ \sum_i t_i=R.
\]
The Lagrange multiplier \(\lambda\) for the sum constraint is positive at every nontrivial active clipping cell.

**2. Differentiating an open cell.** Let \(A\) be the active group set (\(t_i>0\)) and, for \(i\in A\), let \(S_i=\{j\in G_i:y_{ij}>t_i\}\), \(k_i=|S_i|\ge1\). Choose a cell with all clipping and group-activity inequalities strict. The stationarity equations and cap sum yield, with \(H=\sum_{i\in A}k_i^{-1}\),
\[
k_it_i=\sum_{j\in S_i}y_{ij}-\lambda,
\quad
\lambda=\frac{\sum_{i\in A}k_i^{-1}\sum_{j\in S_i}y_{ij}-R}{H}.
\]
Thus for a clipped output coordinate of group \(i\in A\), the derivative with respect to a clipped input in group \(h\in A\) is
\[
\frac{\mathbf1_{h=i}}{k_i}-\frac1{k_i k_hH}.
\]
Unclipped outputs have the corresponding identity row; inactive-group outputs have zero rows. Each clipped row has total absolute coefficient sum
\[
\left(1-\frac1{k_iH}\right)+\frac{|A|-1}{k_iH}
=1+\frac{|A|-2}{k_iH}
\quad (|A|\ge2).
\]
For \(|A|=1\), clipped rows are zero. Sign changes conjugate the cell Jacobian by coordinate sign matrices and therefore preserve these absolute row sums.

**3. Optimizing face patterns.** If \(r=|A|\le2\), all cell row norms are at most one. For \(r\ge3\), fix the group \(i\) of the output row. The quantity to be minimized in the denominator is
\[
k_iH=1+\sum_{h\in A\setminus\{i\}}\frac{k_i}{k_h}.
\]
Subject to \(1\le k_h\le d_h\), it is minimized by \(k_i=1\) and \(k_h=d_h\) for all other active groups. If there are \(k=r-1\) such other groups, the sum of their reciprocal sizes is minimized by taking the \(k\) largest block sizes, leaving one distinct group for the output row; the restriction \(k\le m-1\) guarantees one remains. The resulting value is
\[
1+\frac{k-1}{1+\sum_{j=1}^{k}d_{(j)}^{-1}}.
\]
The ambient projector is a continuous piecewise-affine map because \(K_R\) is polyhedral. On every affine region its maximum-norm operator norm is bounded by this finite maximum. Splitting a line segment into its finitely many affine-cell intersections proves the same bound globally, including all nondifferentiable boundaries.

**4. Sharpness by a strictly realizable face.** Pick any \(k\in\{2,\ldots,m-1\}\) and designate the \(k\) largest groups as the other active groups, with an additional distinct target group \(i\). Let \(r=k+1\), choose \(\lambda>0\), and set every active cap to \(t_h=R/r\). In target group \(i\), take one coordinate with input \(t_i+\lambda\) and every other coordinate zero, so \(k_i=1\). In each of the \(k\) other active groups \(h\), set every input coordinate to \(t_h+\lambda/d_h\), so \(k_h=d_h\). Set all other groups' inputs to zero. These choices satisfy the stationarity system and have strictly positive margins between clipped/unclipped coordinates, between active/inactive groups, and between the positive multiplier and zero. Consequently they lie in an open full-dimensional affine region with precisely this face pattern. Choose a sufficiently small input perturbation that is positive on the target clipped coordinate, negative on every other active clipped coordinate, and zero elsewhere. Its maximum norm is its amplitude, and the target output increases by exactly that amplitude times the row's absolute coefficient sum, not merely in a differential limit. This proves a pair of **finite distinct** inputs attains each candidate constant and hence the maximizing one. For \(m\le2\) an open interior region has identity projection, attaining one.

**5. Consequences.** The candidate fraction is positive as soon as \(m\ge3\), proving the nonexpansivity classification. With \(d_i=q\), the candidate \(1+q(k-1)/(q+k)\) is strictly increasing in \(k\ge2\), so its maximum occurs at \(k=m-1\) and simplifies to the stated homogeneous-block value. With \(q=1\), this reduces to \(2-2/m\) for \(m\ge2\). No asymptotic statement assumes uniformity across changing \(m\).

## Verification

The accompanying `checker.py` is a standalone reproducibility program (Python 3 plus NumPy). From its extracted directory, run `python checker.py`. It exhaustively compares the exact rational closed formula against every strict-cell pattern for all \(340\) block-size tuples with one through four blocks, each size one through four. It also runs \(120\) constructed near-cell finite sharp-pair tests and \(120\) random two-input tests against an independent bisection-based Euclidean projection routine. The computation is supplementary: only the arguments in the Proof establish the universal statements. The large numerical examples \((1,100,100)\) and \((1,100,100,100)\) approach respectively \(101/51\) and \(303/103\) in the finite-pair check; the analytic formula establishes these numbers exactly.

## Relationship to prior work

This is the standard Euclidean projection onto a mixed \(\ell_{1,\infty}\) ball (sum of block maxima); group ordering conventions may reverse the two norm subscripts. Quattoni–Carreras–Collins–Darrell (2009), Chau–Wohlberg–Rodriguez (2018), Chu–Zhang–Sun–Tao (2020), and Perez–Condat–Barlaud (2023) derive efficient algorithms and clipping/KKT descriptions for the same projection; those descriptions are used as **prior** facts here. Béjar–Dokmanić–Vidal (2019) study its dual proximal counterpart. Perez–Barlaud (2024) study a multilevel *non-Euclidean* projection rule, not the exact Euclidean nearest-point map. The new assertion is a sharp **global coordinate-maximum-norm** modulus depending only on block cardinalities, together with a complete nonexpansivity dichotomy and actual finite-pair attainment. These assertions are not automatic from Euclidean firm nonexpansivity, which controls the Euclidean norm only. In the special case of singleton blocks, the formula agrees with the familiar cross-polytope projection modulus. Literature and mathematical-record comparisons found no precise covering result, but this is not an exhaustive historical novelty certification.

## Limitations

The formula assumes unweighted block maxima, unweighted Euclidean distance, finite-dimensional real coordinates, and positive radius. It makes no assertion about arbitrary overlapping groups, other input/output norms, or the complexity of computing the projection itself. A historical-priority uncertainty remains for older group-projection sensitivity literature and other formulations of the same norm. No independent proof audit has been performed.

## References

- A. Quattoni, X. Carreras, M. Collins, T. Darrell, *An Efficient Projection for \(\ell_{1,\infty}\) Regularization*, ICML (2009), DOI: 10.1145/1553374.1553484. Author manuscript: https://dspace.mit.edu/entities/publication/28ba4c03-2baf-4d6a-a5b0-323056c0ed25
- D. Chau, B. Wohlberg, P. Rodriguez, *A Fast Projection Method for the \(\ell_{1,\infty}\) Norm Ball*, arXiv:1806.10041 (first public posting 2018-06-26), https://arxiv.org/abs/1806.10041
- J. Béjar, I. Dokmanić, R. Vidal, *The Fastest \(\ell_{1,\infty}\) Prox in the West*, arXiv:1910.03749, https://arxiv.org/abs/1910.03749
- C. Chu, H. Zhang, J. Sun, R. Tao, *A Semismooth Newton Algorithm for Efficient Projections onto \(\ell_{1,\infty}\)-Norm Ball*, PMLR 119 (2020), https://proceedings.mlr.press/v119/chu20b.html
- G. Perez, L. Condat, M. Barlaud, *Efficient Projection Algorithms onto the \(\ell_{1,\infty}\)-Norm Ball*, arXiv:2307.09836, https://arxiv.org/abs/2307.09836
- G. Perez, M. Barlaud, *Multi-level projection with exponential parallel speedup*, arXiv:2405.02086, https://arxiv.org/abs/2405.02086

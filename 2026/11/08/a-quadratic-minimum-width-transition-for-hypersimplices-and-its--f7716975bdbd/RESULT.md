# Intrinsic Euclidean width of every positively diagonally scaled hypersimplex

## Finding and scope

For integers \(n\ge2\), \(1\le k<n\), and arbitrary positive real numbers \(s_1,\ldots,s_n\), define the *scaled hypersimplex*
\[
K_s=\operatorname{diag}(s_1,\ldots,s_n)\Delta_{n,k},\qquad
\Delta_{n,k}=\{x\in[0,1]^n:\sum_i x_i=k\}.
\]
Its affine-direction space, used throughout for *intrinsic* Euclidean width, is \(L_s=\{v:\sum_i v_i/s_i=0\}\). Set \(w_i=s_i^{-2}\), \(T=\sum_iw_i\), and for each nonempty proper \(S\subsetneq[n]\) set
\[
A_S=\sum_{i\in S}w_i,\quad B_S=T-A_S,\quad
m(S)=\min\{|S|,n-|S|,k,n-k\}.
\]
Then the **exact minimum intrinsic directional width**, for every positive anisotropic diagonal scaling, is
\[
\boxed{\min_{v\in L_s,\ \|v\|_2=1}
 \Big(\max_{x\in K_s}\langle v,x\rangle-\min_{x\in K_s}\langle v,x\rangle\Big)
 =\min_{\varnothing\ne S\subsetneq[n]}m(S)\sqrt{\frac{T}{A_SB_S}}.}
\]
**All** minimizing unit normals, with no others, are precisely the vectors \(\pm v^S\) for subsets attaining the minimum, where
\[
v_i^S=\begin{cases}
 s_i^{-1}\sqrt{B_S/(A_ST)},&i\in S,\\
 -s_i^{-1}\sqrt{A_S/(B_ST)},&i\notin S.
\end{cases}
\]
The formula is a finite subset minimization, not an asserted polynomial-time algorithm. If all scales are equal it reduces to the known hypersimplex width theorem and its rank-dependent threshold. **The unweighted width formula, all unweighted minimizing directions, and the threshold \(n=4\min(k,n-k)^2-1\) were already published (2026-10-18 and 2026-10-25); they are cited here solely as a previously known specialization, not a new finding.** The distinct claim is the complete anisotropically scaled theorem with its exhaustive equality classification.

## Proof

Write \(q=\min(k,n-k)\). Given an intrinsic vector \(v\in L_s\), put \(y_i=s_iv_i\). Thus \(\sum_iw_iy_i=0\) and \(\|v\|_2^2=\sum_iw_iy_i^2\). The width is
\[
W(y)=\sum_{\mathrm{top}\ q}y_i-\sum_{\mathrm{bottom}\ q}y_i.
\]
Indeed the support function of a hypersimplex selects the largest \(k\) entries, and subtracting the smallest \(k\) entries agrees with the expression for \(q=n-k\) by complementary sums. This support-width expression is invariant under adding a constant to every \(y_i\).

Fix a weak ordering of all \(n\) coordinates and relabel them in nonincreasing order. Define \(A_j=\sum_{i\le j}w_i\) and weighted-mean-zero step vectors
\[
\rho_j=\mathbf1_{\{1,\ldots,j\}}-\frac{A_j}{T}\mathbf1,
\qquad 1\le j<n.
\]
Every \(y\) in this ordered cone has the unique representation
\[
y=\sum_{j=1}^{n-1}d_j\rho_j,\qquad d_j=y_j-y_{j+1}\ge0.
\]
The differences fix all coordinates up to a common additive constant, which the weighted-mean-zero condition fixes uniquely. The width functional \(W\) is *linear within this cone*; moreover,
\[
W(\rho_j)=\min\{j,n-j,q\},\qquad
\|\rho_j\|_w^2=\sum_iw_i\rho_{j,i}^2=\frac{A_j(T-A_j)}T.
\]
Let \(c\) be the least ratio \(W(\rho_j)/\|\rho_j\|_w\) over the step rays in this chamber. Linearity followed by the norm triangle inequality gives
\[
W(y)=\sum_jd_jW(\rho_j)\ge c\sum_jd_j\|\rho_j\|_w
\ge c\|y\|_w.
\]
Since all weights are strictly positive, the weighted Euclidean norm is strictly convex; any two distinct step rays have their nonzero gaps at distinct positions and are not positive collinear. If two coefficients \(d_j\) are positive, the last triangle inequality is strict. **Consequently, every global minimizer must be a single two-level step ray** in one of the ordered chambers; no mixture of tied rays can minimize. Conversely each normalized step ray attains its own ratio. Varying the ordering exhausts all subsets \(S\), and yields the displayed minimum and no additional directions.

For a general subset \(S\), the unnormalized centered step equals \(B_S/T\) on \(S\) and \(-A_S/T\) on its complement. It has squared weighted norm \(A_SB_S/T\), hence normalizing \(v_i=y_i/s_i\) gives exactly \(v^S\). The proof covers all ranks \(1\le k<n\), ties, and all positive scales without appealing to finite experiments. \(\square\)

## Interpretation and verification limits

The formula determines the least metric thickness and all thinnest projections of any coordinate-anisotropic realization of a uniform-matroid base polytope. The threshold phenomenon in the unscaled specialization was known; anisotropic weights can break all its coordinate-permutation symmetries and select non-cardinality-determined subsets. For example, with inverse squared scales \(w=(1,2,3,5)\), rank \(k=2\), the optimum is obtained by evaluating the displayed rational squared-width ratios \(m(S)^2T/(A_SB_S)\) over the fourteen proper nonempty subsets. An independent exact-rational small-grid check of this example corroborates, but does not replace, the proof.

The argument does not extend directly to non-diagonal linear maps, non-Euclidean norms, or arbitrary matroid base polytopes. Strictly positive scales and intrinsic rather than ambient Euclidean width are essential. Historical priority of the weighted formula remains best-of-knowledge; a differently titled earlier weighted base-polytope theorem is a residual risk.

## Relation to earlier work

1. *Euclidean thickness and a two-orbit phase transition for hypersimplices* (2026-10-18), https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-euclidean-thickness-and-a-two-orbit-phase-transition-for-hypersi--bde72189e441 . Earlier exact all-rank **unweighted** width, equality directions and quadratic transition.
2. *Exact minimum Euclidean width and a quadratic phase transition for hypersimplices* (2026-10-25), https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-exact-minimum-euclidean-width-and-a-quadratic-phase-transition-f--f678b57db834 . Earlier independent statement and proof of the same unweighted specialization.
3. *Minimum Euclidean width of diagonally scaled polymatroid independence polytopes* (2026-11-08), https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-minimum-euclidean-width-of-diagonally-scaled-polymatroid-indepen--8ee77a677514 . This studies the *full-dimensional down-closed independence polytope* and its ambient normals, not the rank-equality base polytope or its intrinsic weighted-mean-zero normals; its minimization formula is different and does not imply the result here.
4. S. Har-Peled and E. W. Robson, *On the Width of the Regular n-Simplex*, arXiv:2301.02616 (2023), https://arxiv.org/abs/2301.02616 ; the rank-one case is classical.
5. L. Martínez-Sandoval and A. Padrol, *The convex dimension of hypergraphs and the hypersimplicial Van Kampen-Flores Theorem*, arXiv:1909.01189 (2019), https://arxiv.org/abs/1909.01189 ; hypersimplex projection-skeleton rather than weighted metric-width classification.

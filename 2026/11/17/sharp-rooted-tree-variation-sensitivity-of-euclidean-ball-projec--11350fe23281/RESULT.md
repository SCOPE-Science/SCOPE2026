# Sharp rooted-tree variation sensitivity of Euclidean ball projection

## Finding

Let \(T=(V,E)\) be a finite unweighted tree with \(n=|V|\ge2\), let \(r\) be a designated root, and write \(d_v\) for the number of children of vertex \(v\). On real vertex signals define the *anchored tree-variation norm*
\[
\|h\|_{T,r}=|h_r|+\sum_{v\ne r}|h_v-h_{p(v)}|,
\]
where \(p(v)\) denotes the parent of \(v\). Let \(P_R\) be Euclidean nearest-point projection onto the Euclidean ball of radius \(R>0\) centered at zero. Its exact sharp global two-input Lipschitz constant, in the same anchored norm on input and output, is
\[
\boxed{L(T,r)=\sup_{x\ne y}\frac{\|P_R(x)-P_R(y)\|_{T,r}}{\|x-y\|_{T,r}}=\frac{1+\sqrt{n\sum_{v\in V}(1+d_v)^2}}2.}
\]
The coefficient is independent of \(R\), is strictly greater than one, and is a strict supremum: no two distinct finite inputs attain equality. A boundary-approaching explicit family witnesses sharpness.

Among all rooted trees on the same \(n\ge2\) vertices,
\[
\frac{1+\sqrt{n(4n-3)}}2\le L(T,r)\le\frac{1+\sqrt{n(n^2+n-1)}}2.
\]
The lower equality holds exactly for a path rooted at an endpoint, and the upper equality exactly for a star rooted at its center (with the usual coinciding descriptions for \(n=2\)). The lower and upper coefficients grow, respectively, like \(n\) and \(n^{3/2}/2\), revealing a branching-dependent change of stability scale.

## Assumptions and scope

The vertex signal space is \(\mathbb R^V\), with the standard *unweighted* Euclidean inner product for the projection and the anchored tree-variation norm for the Lipschitz ratio. Edges are unweighted, each parent-child edge appears exactly once, and \(r\) is fixed. The ball has center zero and fixed radius \(R>0\). The projection is the elementary radial map
\[
P_R(x)=\begin{cases}x,&\|x\|_2\le R,\\R x/\|x\|_2,&\|x\|_2>R.\end{cases}
\]
The statement concerns the exact operator's global two-input modulus, not one-input output variation or projection in the anchored norm. The root term is essential: without it, the edge variation alone is a seminorm and radial projection does not in general preserve its constant-vector kernel.

## Proof

**1. The anchored difference matrix.** Enumerate the root first and every parent before its children. Let \(D\) be the invertible matrix whose root row is coordinate evaluation at \(r\) and whose row at each nonroot \(v\) is \(e_v^\top-e_{p(v)}^\top\). Then \(\|h\|_{T,r}=\|Dh\|_1\). If \(h^{(v)}=D^{-1}e_v\), then \(h^{(v)}\) is the indicator of the full descendant subtree \(T_v\), so \(\|h^{(v)}\|_2=\sqrt{|T_v|}\). In particular, \(h^{(r)}=\mathbf 1\) and \(|T_r|=n\).

**2. A rank-one tangent norm identity.** Outside the Euclidean ball, at \(x\) with \(u=x/\|x\|_2\), the derivative is
\[
DP_R(x)=\frac R{\|x\|_2}(I-uu^\top).
\]
The induced anchored norm of \(I-uu^\top\) is the maximum of the \(\ell_1\) column norms of \(D(I-uu^\top)D^{-1}\). For each vertex \(v\), duality of \(\ell_1\) and \(\ell_\infty\) gives
\[
\|D(I-uu^\top)h^{(v)}\|_1
=\max_{s\in\{-1,1\}^{V}}\left(s_v-(D^\top s\cdot u)(h^{(v)}\cdot u)\right).
\]
For any two real vectors \(a,b\) in dimension at least two, the minimum over Euclidean unit vectors \(u\) of \((a\cdot u)(b\cdot u)\) is \((a\cdot b-\|a\|_2\|b\|_2)/2\): these are the smaller eigenvalue and Rayleigh minimum of \((ab^\top+ba^\top)/2\). Taking \(a=D^\top s\), \(b=h^{(v)}\), and using \(a\cdot b=s_v\), yields the exact identity
\[
\sup_{\|u\|_2=1}\|I-uu^\top\|_{T,r\to T,r}
=\frac12\max_{v\in V}\max_{s\in\{-1,1\}^V}
\left(s_v+\sqrt{|T_v|}\,\|D^\top s\|_2\right).
\]
There is no exchange-of-limits issue: these are finite maxima over compact sets.

**3. Sharp sign and subtree bounds.** With \(s_v\) the row-sign at vertex \(v\),
\[
(D^\top s)_v=s_v-\sum_{w\text{ child of }v}s_w.
\]
Thus every sign vector satisfies
\[
\|D^\top s\|_2^2\le\sum_{v\in V}(1+d_v)^2=:S(T,r).
\]
Choose \(s_v=(-1)^{\operatorname{depth}(v)}\), so \(s_r=1\). Every child has opposite sign from its parent, yielding equality in every squared-coordinate bound. Take \(v=r\), whose subtree has size \(n\). The maximum is therefore exactly \((1+\sqrt{nS(T,r)})/2\).

**4. Passage from derivatives to the global coefficient.** On the ball's interior, the derivative has anchored norm one. At exterior points, the derivative norm is strictly below the sharp tangent norm because \(R/\|x\|_2<1\). A nondegenerate straight segment intersects the boundary sphere in at most two points. Integrating the derivative along such a segment gives the global Lipschitz upper bound. Since \(n\ge2\), the sharp tangent norm exceeds one and the derivative norm is strictly smaller than that value almost everywhere on each nondegenerate segment; hence no finite distinct pair attains equality.

To approach sharpness explicitly, choose alternating signs \(s\), set \(a=D^\top s\), \(b=\mathbf1\), and let
\[
u=\frac{a/\|a\|_2-b/\|b\|_2}{\|a/\|a\|_2-b/\|b\|_2\|_2}.
\]
The smaller-eigenvalue calculation in step 2 gives \(\|D(I-uu^\top)b\|_1=(1+\sqrt{nS(T,r)})/2\). Take \(x=(R+\delta)u\) and \(y=x+\varepsilon b\) with \(\delta>0\), and let first \(\varepsilon\downarrow0\) then \(\delta\downarrow0\). Both inputs lie outside for sufficiently small \(\varepsilon\), and their ratio tends to the stated constant. Homogeneity \(P_R(x)=R P_1(x/R)\) shows independence of \(R\).

**5. Extremal rooted trees.** Since \(\sum_v d_v=n-1\),
\[
S(T,r)=\sum_v(1+d_v)^2=3n-2+\sum_vd_v^2.
\]
For nonnegative integer child counts summing to \(n-1\), \(n-1\le\sum_vd_v^2\le(n-1)^2\). Equality in the first inequality requires each \(d_v\in\{0,1\}\), forcing an endpoint-rooted path; equality in the second requires one vertex to have all \(n-1\) children, forcing a center-rooted star. Substitution gives the two bounds and the stated growth orders.

## Verification

The accompanying standard-library Python program `verify.py` exhaustively checks the sign extremum and subtree-step identities on all \(1441\) rooted labelled trees obtained from Prüfer sequences with \(2\le n\le6\) and root fixed at vertex zero. It independently checks the exact path/star child-count expressions for \(2\le n\le70\), and tests the tangent vector and near-boundary finite-input ratios on five dissimilar rooted trees. Expected final line: `ALL_ROOTED_TREE_RADIAL_BV_DIAGNOSTICS_PASS`. These finite diagnostics do **not** establish the unrestricted theorem; steps 1–5 are its proof.

## Relationship to prior work

The 2015 preprint by Kolmogorov, Pock and Rolínek develops optimization for tree total-variation energies; its full accessible article treats tree TV minimization rather than the mixed-norm Lipschitz coefficient of a Euclidean radial projector. The classical studies of radial projection by de Figueiredo–Karlovitz (1967) and Thele (1974) concern the Lipschitz constant when the radial ball and the stability metric are generated by the **same** Banach norm; those results do not directly cover a Euclidean ball measured in a different anchored tree-variation norm. Work on mixed-norm Euclidean disk projection establishes constants for planar coordinate \(\ell_p\) norms, not the all-tree branching formula. These comparisons do not constitute a proof of historical priority.

## Limitations

The theorem does not cover arbitrary weighted edge variation, non-tree graphs, nonzero ball centers, unequal Euclidean vertex masses, or projections onto arbitrary convex bodies. Sharpness is by a limiting pair, not by a finite attained pair. The old radial-projection papers could not all be inspected in full, so historical priority remains subject to archival review. The norm's root anchor is part of the theorem and should not be silently dropped.

## References

1. V. Kolmogorov, T. Pock and M. Rolínek, *Total variation on a tree*, arXiv:1502.07770, first public version 26 February 2015, https://arxiv.org/abs/1502.07770.
2. D. G. de Figueiredo and L. A. Karlovitz, *On the radial projection in normed spaces*, Bulletin of the American Mathematical Society 73 (1967), 364–368, https://doi.org/10.1090/S0002-9904-1967-11753-1.
3. R. L. Thele, *Some results on the radial projection in Banach spaces*, Proceedings of the American Mathematical Society 42 (1974), 483–486, https://doi.org/10.1090/S0002-9939-1974-0328550-1.
4. Ya. I. Alber, *Metric and Generalized Projection Operators in Banach Spaces: Properties and Applications*, arXiv:funct-an/9311001, https://arxiv.org/abs/funct-an/9311001.

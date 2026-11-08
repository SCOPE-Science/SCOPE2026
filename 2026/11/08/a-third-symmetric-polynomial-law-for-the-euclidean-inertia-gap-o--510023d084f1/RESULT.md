# A third-symmetric-polynomial law for the Euclidean inertia gap of order and chain polytopes

## Finding

Let \(k\ge1\) and let \(m_1,\ldots,m_k\) be positive integers with \(N=\sum_{g=1}^k m_g\). Let \(P=A_{m_1}\oplus\cdots\oplus A_{m_k}\) be the ordinal sum of antichains, so every element of an earlier layer precedes every element of a later layer. In the standard coordinate Euclidean realization, let \(\mathcal O(P)\) and \(\mathcal C(P)\) be its order and chain polytopes.

For any full-dimensional convex body \(K\subset\mathbb R^N\), let \(X_K\) be uniformly distributed by volume on \(K\) and define its normalized Euclidean inertia about its centroid by
\[
J(K)=\mathbb E\|X_K-\mathbb E X_K\|_2^2=\operatorname{tr}\operatorname{Cov}(X_K).
\]
Then the **exact inertia gap** is
\[
\boxed{\quad J(\mathcal O(P))-J(\mathcal C(P))
=\frac{e_3(m_1,\ldots,m_k)}{(N+1)^2(N+2)},\quad
 e_3(m_1,\ldots,m_k)=\sum_{1\le a<b<c\le k}m_am_bm_c.\quad}
\]
In particular this difference is unchanged by permuting the layer sizes, despite the fact that the order of layers can affect the individual polytopes.

For each layer \(g\), write \(s_g=\sum_{h<g}m_h\). If \(i,j\) are any two coordinate labels in layer \(g\), including \(i=j\), then the stronger covariance identity holds:
\[
\boxed{\quad\operatorname{Cov}(X_{\mathcal O,i},X_{\mathcal O,j})
-\operatorname{Cov}(X_{\mathcal C,i},X_{\mathcal C,j})
=\frac{s_g(N-s_g-m_g)}{(N+1)^2(N+2)}.\quad}
\]
Consequently the difference of the full covariance matrices has rank at most \(k\); on each within-layer coordinate-contrast subspace the two covariance operators agree.

For \(N\ge3\), the gap is zero exactly when \(k\le2\). The two polytopes are Euclidean-congruent exactly when \(k\le2\): for two layers, reflect all coordinates in the second layer about \(1/2\); for three or more layers, their positive inertia difference precludes a Euclidean congruence.

The sharp all-compositions bounds, for fixed \(N\ge3\), are
\[
0\le J(\mathcal O(P))-J(\mathcal C(P))\le
\frac{\binom N3}{(N+1)^2(N+2)},
\]
with left equality exactly for at most two layers and right equality exactly for the \(N\)-element chain (all layer sizes one). For fixed \(N\) and \(3\le k\le N\), the gap is maximized precisely by layer sizes differing by at most one and minimized precisely by the layer-size multiset \(\{N-k+1,1,\ldots,1\}\). Permutations of the extremizing multiset have equal gap. The formulas include the degenerate case \(N=k\), when both extrema coincide.

Equivalently, for independent uniform points \(X_K,X_K'\) in the indicated polytope, the difference of the expected squared interpoint Euclidean distances is exactly twice the displayed inertia gap.

## Assumptions and scope

All coordinates have their unweighted standard orthonormal Euclidean metric. The order polytope consists of \(0\le x_v\le1\) with \(x_u\le x_v\) whenever \(u<v\) in \(P\). The chain polytope consists of \(y_v\ge0\) satisfying \(\sum_{v\in C}y_v\le1\) for every chain \(C\). For an ordinal sum of antichains, its maximal-chain inequalities are equivalently \(\sum_g\max_{v\in A_{m_g}}y_v\le1\).

The statements concern volume-uniform interior points, not uniformly selected vertices. The metric is not invariant under arbitrary affine or unimodular changes of coordinates. All layer sizes are positive integers, so no empty layers are included. The moment and congruence formulas hold in every dimension allowed by these assumptions.

## Proof

**1. An explicit measure-preserving transfer.** For a point \(x\in\mathcal O(P)\), put \(M_{g-1}(x)=\max_{v\in A_{m_{g-1}}}x_v\) and set \(M_0(x)=0\). Define \(y_v=x_v-M_{g-1}(x)\) for every coordinate \(v\) in layer \(g\). Because \(P\) is an ordinal sum, each \(y_v\ge0\). The sum of the layer maxima of \(y\) is the maximum coordinate in the last layer of \(x\), hence is at most one; thus \(y\in\mathcal C(P)\). Conversely, set \(S_0=0\), \(S_g=\sum_{h\le g}\max_{v\in A_{m_h}}y_v\), and let \(x_v=S_{g-1}+y_v\) in layer \(g\). This gives an inverse map into \(\mathcal O(P)\). On each chamber where the maximum in every layer has a fixed label, these maps are triangular affine with diagonal entries one and hence absolute Jacobian one. They therefore transport uniform volume measure between the two polytopes.

**2. Exact coupling by uniform order statistics.** Let \(U_{(1)}<\cdots<U_{(N)}\) be the order statistics of \(N\) independent uniform variables on \((0,1)\), with \(U_{(0)}=0\). Uniform volume on \(\mathcal O(P)\) is obtained by assigning the first \(m_1\) ranks uniformly to the first layer, the next \(m_2\) ranks uniformly to the second layer, and so forth, independently permuting the labels within each layer. Indeed all such simplicial chambers have equal coordinate volume \(1/N!\). For a fixed coordinate in layer \(g\), its local rank \(T\) is uniform on \(\{1,\ldots,m_g\}\); writing \(s=s_g\), the coupled order- and chain-polytope coordinates are
\[
X=U_{(s+T)},\qquad Y=U_{(s+T)}-U_{(s)}.
\]
The \(N+1\) gaps between zero, the order statistics and one have the \(\operatorname{Dirichlet}(1,\ldots,1)\) law. Consequently the sum of any \(t\) consecutive gaps has first moment \(t/(N+1)\) and second moment \(t(t+1)/((N+1)(N+2))\).

**3. The diagonal variance identity.** Put \(m=m_g\), \(\mu=(m+1)/2\), and \(Q=(N+1)(N+2)\). Conditioning on \(T\) and applying the spacing moments yields
\[
\mathbb E X=(s+\mu)/(N+1),\qquad \mathbb E Y=\mu/(N+1),
\]
\[
\mathbb E X^2-\mathbb E Y^2
=\frac{s(s+m+2)}{Q}.
\]
Subtracting the squared means gives, with no asymptotic approximation,
\[
\operatorname{Var}(X)-\operatorname{Var}(Y)
=\frac{s(N-s-m)}{(N+1)^2(N+2)}.
\]
This applies to every coordinate of the layer, including the first and last layers where it vanishes.

**4. The complete within-layer covariance identity.** For local ranks \(t,u\in\{1,\ldots,m\}\), the same Dirichlet calculation gives
\[
\mathbb E[U_{(s+t)}U_{(s+u)}]
-\mathbb E[(U_{(s+t)}-U_{(s)})(U_{(s+u)}-U_{(s)})]
=\frac{s(s+t+u+1)}{Q}.
\]
For two fixed coordinate labels in one layer, their local ranks are either equal (one label) or a uniformly drawn distinct pair (different labels). In both cases the expected sum of their ranks is \(m+1\). Their uncentered mixed-moment difference is therefore \(s(s+m+2)/Q\), while the product-of-means difference is \(s(s+m+1)/(N+1)^2\). This proves the stated within-layer covariance formula. The within-layer blocks of the covariance difference are constant matrices; independent coordinate-permutation symmetry also makes every off-diagonal block constant. Hence the full covariance difference annihilates the \((N-k)\)-dimensional direct sum of within-layer contrast spaces and has rank at most \(k\).

**5. Summation and symmetry.** Summing the variance identity from Step 3 over the \(m_g\) coordinates in each layer gives
\[
J(\mathcal O(P))-J(\mathcal C(P))
=\frac{\sum_{g=1}^k m_g(\sum_{a<g}m_a)(\sum_{c>g}m_c)}{(N+1)^2(N+2)}.
\]
Every choice of three distinct layers \(a<g<c\) occurs exactly once in this sum, with multiplicity \(m_am_gm_c\). Thus the numerator is exactly \(e_3(m_1,\ldots,m_k)\). This proves the law and its invariance under permutations of the layer sizes.

**6. Congruence and extremizers.** If \(k=1\), both polytopes are the unit cube. If \(k=2\), the coordinate reflection \(x_v\mapsto1-x_v\) on the second layer maps the order inequalities \(x_u\le x_v\) into the chain inequalities \(x_u+y_v\le1\), giving an isometry. If \(k\ge3\), every layer size is positive and \(e_3>0\); inertia is preserved by any Euclidean isometry, hence the two polytopes cannot be congruent.

The integer \(e_3(m_1,\ldots,m_k)\) counts triples of elements belonging to three *different* layers. It is therefore at most \(\binom N3\), with equality (for \(N\ge3\)) exactly when every layer has size one, and is zero exactly when there are fewer than three layers. For fixed \(N,k\ge3\), replace unequal layer sizes \(a>b+1\) by \(a-1,b+1\). The elementary-symmetric numerator increases by exactly \((a-b-1)\) times the sum of the remaining \(k-2\) layer sizes, which is strictly positive. Repeating this balancing step proves the maximum and its equality class. Reversing such transfers until all excess elements reside in a single layer proves the minimum and its equality class. Finally, independence gives \(\mathbb E\|X_K-X_K'\|_2^2=2J(K)\), proving the squared-interpoint-distance interpretation.

## Verification

The standalone file `check_inertia.py` uses exact rational arithmetic and an independently implemented simplex-moment integral. For every positive composition of every \(N\le7\), it enumerates all within-layer permutations, builds every order-polytope simplex, maps its vertices to the corresponding chain-polytope simplex, and evaluates its centroid and second-moment matrix using the uniform-simplex barycentric formula. It does **not** use the proposed Dirichlet variance identity to calculate these moments. The checker then compares the resulting full covariance blocks with the theorem and checks the inertia difference against the symmetric-polynomial expression.

The actual executed result was `ORDER_CHAIN_DIRICHLET_SIMPLEX_CHECKS_PASSED 127 1813 1981 21`: 127 complete compositions, 1,813 exact within-layer covariance-entry comparisons, 1,981 fixed-height equality-profile checks, and 21 two-layer vertex-set reflection checks. These finite tests are checks, not an exhaustive proof for unbounded dimension; Steps 1–6 provide that proof.

## Relationship to prior work

Stanley's order/chain polytope theory supplies their definitions, equal-volume triangulations and the transfer map. Hibi and Li classify unimodular equivalence and characterize differences in facet structure; such statements neither determine nor imply the displayed interior quadratic moments. Ahmad, Fourier and Joswig investigate maximal ranked posets with exactly the layer structure used here and prove face-number comparisons across chain-order interpolations. Freij-Hollanti and Lundström develop face-enumerator inequalities under ordinal sums. These sources make the family and the missing metric comparison mathematically natural, but their inspected arguments do not state a volume-uniform inertia law or the third-symmetric-polynomial formula.

The exact gap also differs from previously investigated directional mean widths of three equally sized layers: mean width is a boundary support-function functional, whereas the present invariant is the centered second moment of *interior uniform volume*. Neither measure determines the other. The named source materials and textual searches did not identify an earlier equivalent identity. Historical priority remains provisional; an unlocated equivalent moment formula or a consequence of an uninspected source remains possible.

## Limitations

The theorem is restricted to ordinal sums of nonempty antichains in the standard Euclidean embedding. It does not establish an inertia comparison for arbitrary finite posets, general marked chain-order interpolants, weighted coordinate metrics, or nonuniform densities. The covariance difference is not asserted to be positive semidefinite: the theorem concerns its trace and its precisely identified blocks. The exact computer checks are finite and independent mathematical audit has not been performed.

## References

1. I. Ahmad, G. Fourier, M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626, first submitted 2023-09-04, especially §§1–2 and Theorem 4.1. https://arxiv.org/abs/2309.01626
2. R. Freij-Hollanti, T. Lundström, *\(f\)-vector inequalities for order and chain polytopes*, arXiv:2312.13890, submitted 2023-12-21, especially §§2,4–6. https://arxiv.org/abs/2312.13890
3. T. Hibi, N. Li, *Unimodular equivalence of order and chain polytopes*, arXiv:1208.4029, first submitted 2012-08-20, §§1–2. https://arxiv.org/abs/1208.4029
4. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, DOI:10.1007/BF02187680.

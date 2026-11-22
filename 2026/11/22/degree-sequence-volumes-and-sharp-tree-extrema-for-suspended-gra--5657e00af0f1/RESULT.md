# Degree-sequence volumes and sharp tree extrema for suspended graph elliptopes

## Finding

Let \(T\) be any finite tree on \(n\ge2\) vertices, with degrees \(d_1,\ldots,d_n\), and let \(G=K_1\vee T\) be the graph obtained by adjoining a new universal vertex. Its projected graph elliptope \(\mathcal I(G)\) is defined in standard \([0,1]\) edge-correlation coordinates (see below); its ambient dimension is \(2n-1\). Define
\[
J_d=\int_{-1}^{1}(1-t^2)^{d/2}\,dt
=\frac{\sqrt\pi\,\Gamma(1+d/2)}{\Gamma(3/2+d/2)}\quad(d\ge0).
\]
Then its exact ordinary coordinate volume is
\[
\boxed{\operatorname{vol}_{2n-1}\mathcal I(K_1\vee T)
=2^{-n}\prod_{i=1}^{n}J_{d_i}.}
\]
In particular, *any two trees with the same degree multiset have exactly the same suspended-elliptope volume*, regardless of their other graph structure.

For fixed \(n\ge4\), among all trees on \(n\) vertices the unique volume minimizer (up to graph isomorphism) is the path \(P_n\), while the unique maximizer is the star \(K_{1,n-1}\). In fact,
\[
\boxed{\operatorname{vol}\mathcal I(K_1\vee P_n)
=2^{-n}\left(\frac\pi2\right)^2\left(\frac43\right)^{n-2},}
\]
\[
\boxed{\operatorname{vol}\mathcal I(K_1\vee K_{1,n-1})
=2^{-n}J_{n-1}\left(\frac\pi2\right)^{n-1}.}
\]
Their sharp ratio grows exponentially:
\[
\boxed{\frac{\operatorname{vol}\mathcal I(K_1\vee K_{1,n-1})}
{\operatorname{vol}\mathcal I(K_1\vee P_n)}
\sim\sqrt{\frac8{\pi n}}\left(\frac{3\pi}{8}\right)^{n-2}.}
\]
For \(n=2,3\), the star and path descriptions coincide; the inequalities are equalities for every tree of that order. The star-family formula is already available separately in the triangular-book case; the statement here is the all-tree degree invariant and its sharp global extrema.

## Assumptions and scope

For a finite simple graph \(G=(V,E)\), define \(\mathcal I(G)\subset[0,1]^E\) by
\[
\mathcal I(G)=\bigl\{((1-\langle z_u,z_v\rangle)/2)_{uv\in E}:
 z_v\text{ unit vectors in some common real Euclidean space}\bigr\}.
\]
No fixed rank constraint is imposed. Each \(T\) is an unweighted simple undirected connected acyclic graph, with no isolated vertices for \(n\ge2\). The measure is ordinary Lebesgue volume in the displayed edge coordinates, not a quotient by graph automorphisms and not volume in the full space of symmetric matrices. The graph \(K_1\vee T\) has exactly \(2n-1\) edges, and its elliptope is full-dimensional. Graph isomorphism is the only equivalence in the uniqueness assertions. The only limit is along integers \(n\to\infty\).

## Proof

**1. All local triangle constraints are jointly sufficient.** Work initially in correlation coordinates \([-1,1]^E\). Denote the correlation between the universal vertex and tree vertex \(i\) by \(x_i\), and the correlation of tree edge \(ij\) by \(y_{ij}\). Necessity of positive semidefiniteness of each three-by-three triangle Gram matrix gives
\[
|y_{ij}-x_ix_j|\le\sqrt{(1-x_i^2)(1-x_j^2)}.
\]
Conversely, suppose all these inequalities hold. Apart from measure-zero endpoints \(x_i=\pm1\), write \(s_i=\sqrt{1-x_i^2}\) and \(c_{ij}=(y_{ij}-x_ix_j)/(s_is_j)\), so \(|c_{ij}|\le1\). Root the tree at vertex \(1\); take a unit vector \(w_1\), and recursively construct for each child \(j\) of \(i\)
\[
w_j=c_{ij}w_i+\sqrt{1-c_{ij}^2}\,e_j,
\]
where \(e_j\) is a fresh unit basis vector orthogonal to all ancestor directions and to directions already introduced. As the underlying graph is a tree, no compatibility equation closes a cycle; every \(w_j\) is a unit vector and \(\langle w_i,w_j\rangle=c_{ij}\) on its parent edge. Choose a further unit vector \(e_0\) orthogonal to all the \(w_i\), set the universal vertex vector equal to \(e_0\), and take \(z_i=x_i e_0+s_iw_i\). Then all \(z_i\) are unit vectors and realize every \(x_i,y_{ij}\). Limits cover the endpoint sections. This constructs a global Gram completion explicitly, without assuming a rank bound or appealing only to an abstract chordal-graph theorem.

**2. Exact volume.** For fixed \(x=(x_1,\ldots,x_n)\), every tree-edge coordinate \(y_{ij}\) varies independently over an interval of length \(2\sqrt{(1-x_i^2)(1-x_j^2)}\), by Step 1. There are \(n-1\) tree edges. Fubini's theorem gives the correlation-coordinate volume
\[
2^{n-1}\int_{[-1,1]^n}\prod_{ij\in E(T)}
\sqrt{(1-x_i^2)(1-x_j^2)}\,dx
=2^{n-1}\prod_iJ_{d_i}.
\]
Passing to cut coordinates \(h_e=(1-r_e)/2\) for all \(2n-1\) edge correlations \(r_e\) has Jacobian magnitude \(2^{-(2n-1)}\), yielding the claimed \(2^{-n}\prod_iJ_{d_i}\). Since every \(J_d>0\), the elliptope is full-dimensional. This establishes degree-multiset invariance, rather than an assertion of its converse.

**3. Sharp path and star extrema.** The function \(f(t)=\log J_t\) for real \(t\ge0\) is strictly convex: \(J_t\) is the exponential moment of the nonconstant function \(\tfrac12\log(1-x^2)\) under Lebesgue measure on \((-1,1)\), and strict Hölder inequality gives strict log convexity. For any \(n\)-vertex tree the integers \(a_i=d_i-1\) are nonnegative with sum \(n-2\). Its sorted degree vector is therefore majorized above by \((n-1,1,\ldots,1)\), and majorizes \((2,\ldots,2,1,1)\). The latter vector has \(n-2\) entries equal to \(2\). Karamata's inequality applied to the strictly convex \(f\) yields the path/star volume bounds, with equality only for the corresponding degree multisets. A tree with all degrees at most two is a path; a tree with one degree \(n-1\) is a star. This proves uniqueness up to isomorphism for \(n\ge4\).

Finally \(J_1=\pi/2\), \(J_2=4/3\), and \(J_{n-1}\sim\sqrt{2\pi/n}\) by the gamma-ratio asymptotic. Substitution into the exact extremal formulas gives the stated sharp ratio, including its leading constant.

## Verification

The fully self-contained `verify.py` (Python standard library) reconstructs explicit global Gram vectors from locally feasible triangle data on randomly generated trees; checks the beta integral identities against independent numerical quadrature; enumerates **all 280,392 labeled trees of orders two through eight** using Prüfer sequences and tests the sharp inequalities and equality criteria; and compares the previously published triangular-book formula with the star specialization at thirty orders. It also checks the first-order asymptotic at larger orders. It finished with `TREE_ELLIPTOPE_DEGREE_VOLUME_PASS`. These finite checks supplement rather than replace the all-orders Gram and strict-convexity proofs.

For example, at order four the path has volume \(\pi^2/36\), whereas the star has volume \(3\pi^4/1024\). At order five the corresponding values are \(\pi^2/54\) and \(\pi^4/480\). These are \([0,1]\)-coordinate, dimension-seven and dimension-nine volumes respectively.

## Relationship to prior work

Lee and Skipper (first posted 4 March 2017) computed volumes of Boolean-quadric polytopes and linear relaxations for sparse graphs, notably stars and paths, and related them to cut polytopes of their suspensions. Their objects are polyhedral cut/Boolean models, not the positive-semidefinite elliptope; their results do not supply the all-tree PSD degree product. Avis, Devroye and Deza (2026) compare projected cut and elliptope volumes and prove an exact elliptope-volume formula for cycles; their graph-elliptope product law applies to graphs sharing at most one vertex, not to the triangles of a general suspension that share varying edges. The previously published *Exact edge-gluing volumes for triangular-book graph elliptopes* establishes the \(T=K_{1,n-1}\) star specialization, and that already-known case is expressly excluded from the novelty claim. The shared triangular-fiber method is acknowledged; the general tree factorization and its sharp extremal principle require the acyclic joint-completion argument and degree majorization. They are not implied merely by the special book case or by the linear Boolean-quadric volumes. Search and source comparisons do not establish unconditional historical uniqueness.

## Limitations

The result requires that deleting the universal vertex leaves a tree. For cyclic residual graphs the triangle constraints need not be jointly sufficient; in particular this theorem gives no formula for arbitrary chordal, series-parallel or complete graph elliptopes. The volume is coordinate-dependent under non-orthogonal affine changes and is not a graph-isomorphism-complete invariant: identical degree multisets suffice for equality but a converse is not proved. The star formula alone was previously known. Exact local PSD completion and the general majorization argument are the infinite proofs; finite enumeration and numerical integration do not certify all orders. Independent mathematical validation has not been performed.

## References

1. J. Lee, D. Skipper, *Volume computation for sparse boolean quadric relaxations*, arXiv:1703.02444, first posted 4 March 2017, https://arxiv.org/abs/1703.02444. Especially the introduction and Sections 2–4, and the cut-polytope suspension correspondence.
2. D. Avis, L. Devroye, A. Deza, *On the volumes of the elliptope, metric polytope, and cut polytope*, arXiv:2604.16735, first posted 17 April 2026, https://arxiv.org/abs/2604.16735. Especially Section 3, Proposition 3.7, Theorems 3.8–3.9 and Table 2.
3. *Exact edge-gluing volumes for triangular-book graph elliptopes*, published 17 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-edge-gluing-volumes-for-triangular-book-graph-elliptopes--2a5bf42a51de. The full star-family case and its beta-integral proof.

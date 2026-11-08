# The first two intrinsic-volume extremizers among rooted-tree order polytopes

## Finding

Let \(n\ge4\), and let \(T\) range over rooted trees with \(n\) vertices. Equip the associated order polytope
\[
\mathcal O(T)=\{x\in[0,1]^{V(T)}:x_u\le x_v\text{ whenever }u\text{ is the parent of }v\}
\]
with its canonical coordinate Euclidean metric. Write \(V_j\) for the conventional intrinsic volumes, \(1\le j\le n\), with \(V_n\) equal to volume and \(2V_{n-1}\) equal to Euclidean boundary area.

Define four rooted trees: \(C_n\), a path rooted at an endpoint; \(F_n\), a path on \(n-2\) vertices rooted at an endpoint, with two terminal children at its other endpoint; \(B_n\), a star with one spoke subdivided, rooted at the original center; and \(S_n\), a star rooted at its center. For every \(j\in\{1,\ldots,n\}\) and every rooted tree \(T\) that is neither \(C_n\) nor \(S_n\),
\[
V_j(\mathcal O(C_n))<V_j(\mathcal O(F_n))\le V_j(\mathcal O(T))\le V_j(\mathcal O(B_n))<V_j(\mathcal O(S_n)).
\]
Equality at the left non-strict inequality occurs only when \(T\cong F_n\), and equality at the right non-strict inequality occurs only when \(T\cong B_n\), as rooted trees. In particular, the same unique first and second extremizers simultaneously govern every nontrivial intrinsic volume.

Let \(A(T)=\mathcal H^{n-1}(\partial\mathcal O(T))\). The exact four boundary areas, in increasing order, are
\[
\begin{aligned}
A(C_n)&=\frac{2+(n-1)\sqrt2}{(n-1)!},\\
A(F_n)&=\frac{4+2(n-2)\sqrt2}{(n-1)!},\\
A(B_n)&=1+\frac{n+1}{2(n-1)}\sqrt2,\\
A(S_n)&=2+\sqrt2.
\end{aligned}
\]
The sharp first gap above the minimum and below the maximum therefore equals, respectively,
\[
\frac{2+(n-3)\sqrt2}{(n-1)!},\qquad 1+\frac{n-3}{2(n-1)}\sqrt2.
\]
The former decreases factorially with dimension while the latter tends to \(1+1/\sqrt2\).

More generally, if \(h(v)\) is the number of vertices in the descendant subtree of \(v\), then, with \(Q(T)=\prod_{v\in V(T)}h(v)^{-1}\),
\[
A(T)=nQ(T)+\sum_{v\text{ leaf}}Q(T-v)+\sqrt2\sum_{e\in E(T)}Q(T/e),
\]
where deletion of a leaf retains the root, and contraction of an edge identifies its endpoints and retains the natural root. This supplies an exact area formula for every rooted tree, not merely the four extremizers.

## Assumptions and scope

Trees are finite, simple, connected, with a distinguished root, all edges directed from parent to child. A leaf is a maximal element of the rooted-tree poset (not the root); \(T-v\) means deleting a leaf, and \(T/e\) means contracting an edge as a rooted tree. All volumes use standard, unweighted coordinate Euclidean geometry in \(\mathbb R^n\); the polytope is full dimensional. Intrinsic volumes employ the classical Steiner/Kubota normalization, so \(A=2V_{n-1}\). No other embeddings or weighted orders are claimed.

## Proof

**1. Volume and facets.** The standard triangulation of an order polytope into unit simplices indexed by linear extensions gives
\[
\operatorname{vol}_n\mathcal O(T)=\frac{e(T)}{n!}=Q(T).
\]
The last equality is the rooted-tree hook formula: an increasing labeling is formed by choosing the root first and interleaving increasing labelings of its child subtrees. An induction gives \(e(T)=n!/\prod_v h(v)\).

The irredundant facets of \(\mathcal O(T)\) are exactly \(x_r=0\), \(x_v=1\) for each leaf \(v\), and \(x_u=x_v\) for every parent-child edge \(uv\). For the root facet, the remaining coordinates form the product of child-subtree order polytopes; its area is \(nQ(T)\). A leaf-upper facet is isometric to \(\mathcal O(T-v)\), hence has area \(Q(T-v)\). On an edge-equality facet, the two coordinate slots are identified. Deleting one duplicate identifies its parameter domain with \(\mathcal O(T/e)\), but the induced Euclidean Gram determinant is \(2\), so the actual facet area is \(\sqrt2\,Q(T/e)\). Summing yields the asserted area formula. No other facets contribute.

**2. Strict monotonicity of intrinsic volumes.** If \(K\subsetneq L\) are full-dimensional convex bodies in \(\mathbb R^n\), then \(V_j(K)<V_j(L)\) for every \(1\le j\le n\). For \(j=n\) this follows from strict volume inclusion. For smaller \(j\), Kubota's formula averages the \(j\)-dimensional volumes of orthogonal projections. A strict supporting-hyperplane separation between \(K\) and a point of \(L\setminus K\) persists after projections onto an open, positive-measure family of \(j\)-planes, so the integral inequality is strict. Intrinsic volumes are invariant under coordinate permutation.

**3. Universal four-level comparison.** In every rooted tree the root lies below every other element, so all its inequalities include the star-poset inequalities and \(\mathcal O(T)\subseteq\mathcal O(S_n)\), after relabeling. If \(T\) is not the rooted star, it has comparable nonroot vertices \(u<v\). The rooted broom order with root below everyone and this one extra relation has fewer order relations than \(T\). Hence \(\mathcal O(T)\subseteq\mathcal O(B_n)\). Equality of these two full-dimensional order polytopes requires their comparability relations to agree, which forces \(T\cong B_n\).

Every rooted tree admits a linear extension. Imposing the total order of one such extension gives \(\mathcal O(C_n)\subseteq\mathcal O(T)\). If \(T\) is not a chain, it has at least two leaves \(u,v\). First linearly order the other \(n-2\) elements, and place \(u,v\) above that ordered chain but incomparable with each other. This rooted fork order extends all relations of \(T\) and gives \(\mathcal O(F_n)\subseteq\mathcal O(T)\). Equality forces \(T\cong F_n\). Proper inclusion and step 2 give every strict inequality and its unique equality case, simultaneously for all intrinsic volumes.

**4. Four areas and gaps.** Applying the facet formula of step 1 to \(C_n\), its two coordinate facets each contribute \(1/(n-1)!\) and its \(n-1\) equality facets contribute \(\sqrt2/(n-1)!\) each. For \(F_n\), the root and both leaf facets together contribute \(4/(n-1)!\), while its \(n-3\) spine-edge contractions yield twice the path of length \(n-1\) in linear-extension count and its two terminal-edge contractions yield one each, giving \(2(n-2)\sqrt2/(n-1)!\). For \(S_n\), the root facet is a unit cube, the leaf-upper facets total \(1\), and the edge facets total \(\sqrt2\). For \(B_n\), the root facet and all leaf-upper facets each total \(1/2\); its two exceptional edge contractions are stars with \(n-1\) vertices and its remaining \(n-3\) contractions are brooms with \(n-1\) vertices. Their combined coefficient is \((n+1)/(2(n-1))\). The four displayed areas and their sharp gaps follow by subtraction.

## Verification

The included `checker.py` evaluates the hook/facet expression exactly as \(a+b\sqrt2\), enumerates every nonisomorphic unrooted tree with every root through \(n=10\), and checks the four area levels, their unique rooted-tree profiles, and the four closed formulas. It independently constructs the \(0/1\) upper-ideal vertices and obtains Euclidean boundary area using SciPy convex hulls through \(n=6\). A recorded execution checked 1,803 rooted profiles, 59 independent convex hulls and 28 level comparisons, returning `ROOTED_TREE_ORDER_POLYTOPE_CHECKS_PASSED 1803 59 28`. These are finite corroborations; the comparison for all \(n\) and all \(j\) is proved analytically in steps 2–4. To replay, run `python checker.py` with `networkx`, `numpy`, and `scipy` installed.

## Relationship to prior work

Stanley's foundational order-polytope paper supplies the facet and unimodular-triangulation descriptions used in step 1; its linear-extension volume formula is not a claim of novelty here. Ahmad, Fourier, and Joswig (2023) compare face vectors of chain-order polytopes for maximal ranked posets, not Euclidean surface areas or the four rooted-tree extremizers. Von Bell and collaborators (2021/2022) study order-polytope triangulations and volume extremizers for generalized snake posets, rather than rooted-tree intrinsic-volume first/second levels. The present combination of an all-rooted-tree Euclidean area identity, simultaneous intrinsic-volume first/second extremizers, and exact opposite-end gap formulas was not located in inspected sources or targeted mathematical-record searches. This is not an assertion of exhaustive historical priority.

## Limitations

The result is restricted to rooted-tree posets, canonical coordinate Euclidean geometry and standard intrinsic volumes. It does not order the third or further interior surface-area levels, nor does it give closed formulas for every intermediate intrinsic volume. Literature searches cannot establish uniqueness of historical priority; terminology from convex-geometric order bodies or tree-poset enumerations could hide equivalent results. The only independent checks are finite numerical/algorithmic checks, not independent mathematical audits.

## References

1. R. P. Stanley, *Two Poset Polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, DOI:10.1007/BF02187680; author-hosted version: https://math.mit.edu/~rstan/pubs/pubfiles/66.pdf.
2. I. Ahmad, G. Fourier, M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626v1, publicly posted 2023-09-04, https://arxiv.org/abs/2309.01626.
3. M. von Bell, B. Braun, D. Hanely, K. Serhiyenko, J. Vega, A. Vindas-Meléndez, M. Yip, *Triangulations, order polytopes, and generalized snake posets*, arXiv:2102.11306v1, publicly posted 2021-02-22, https://arxiv.org/abs/2102.11306.

# Exact beta moment factorization and covariance signs for rooted-forest chain polytopes

## Finding
Let \(P\) be any finite nonempty poset whose Hasse diagram is a rooted forest, with every root minimal and all edges directed away from roots. For each element \(v\), let \(s_v\) be the number of vertices in the descendant subtree rooted at \(v\), including \(v\). Write \(\mathcal C(P)\) for the ordinary chain polytope in its standard nonnegative coordinates, and let \(X\) be uniformly distributed in \(\mathcal C(P)\) with respect to full-dimensional Euclidean volume. The following statements form one joint distribution-and-sign theorem.

**Exact factorization and moments.** Take mutually independent random variables \(B_v\sim\operatorname{Beta}(1,s_v)\), and set
\[
X_v=B_v\prod_{u\prec v}(1-B_u),
\]
where \(u\prec v\) means that \(u\) is a strict ancestor of \(v\). This gives exactly the uniform distribution on \(\mathcal C(P)\), not merely a distribution on its boundary or its vertices. For every multiindex \(\alpha=(\alpha_v)_{v\in P}\in\mathbb Z_{\ge0}^{P}\), writing \(D_v=\sum_{w\succ v}\alpha_w\) for the strict-descendant exponent total, all polynomial moments satisfy
\[
\boxed{\mathbb E\prod_{v\in P}X_v^{\alpha_v}
=\prod_{v\in P}\frac{\alpha_v!\,(s_v)_{D_v}}{(s_v+1)_{\alpha_v+D_v}}.}
\]
Here \((a)_j=a(a+1)\cdots(a+j-1)\) is the rising factorial and \((a)_0=1\). The Euclidean volume is \(\operatorname{Vol}(\mathcal C(P))=\prod_v s_v^{-1}\).

**Exact covariance-sign trichotomy.** For any two distinct vertices \(v,w\), the sign of \(\operatorname{Cov}(X_v,X_w)\) identifies their rooted-forest relationship:
\[
\boxed{\begin{cases}
\operatorname{Cov}(X_v,X_w)<0,&v,w\text{ are comparable};\\
\operatorname{Cov}(X_v,X_w)>0,&v,w\text{ incomparable in the same tree};\\
\operatorname{Cov}(X_v,X_w)=0,&v,w\text{ lie in different trees}.
\end{cases}}
\]
Thus the strict sign pattern recovers the comparability relation and the partition into rooted-tree components (but does not generally recover the orientation of the order).

## Assumptions and scope
A rooted forest here is a poset in which every nonminimal element covers exactly one element; each connected component is consequently a rooted tree. All strict ancestors of a given vertex form a chain. The \(s_v\) are positive integers. The chain polytope has inequalities \(x_v\ge0\) and \(\sum_{v\in C}x_v\le1\) for every maximal chain \(C\), equivalent here to root-to-leaf paths. No regularity, bounded degree, equisized branches, or prescribed number of components is assumed. Uniformity means Lebesgue volume on the entire \(|P|\)-dimensional body.

## Proof
**1. A global coordinate parameterization.** For \(b\in(0,1)^P\), define \(x_v=b_v\prod_{u\prec v}(1-b_u)\). Along each root-to-leaf path, the partial sum telescopes to \(1-\prod_{v\in C}(1-b_v)<1\). Therefore \(x\) lies in the interior of \(\mathcal C(P)\). Conversely, given an interior \(x\), recursively put
\[
b_v=\frac{x_v}{1-\sum_{u\prec v}x_u}.
\]
The strict path inequalities make every denominator positive and every resulting \(b_v\) strictly between zero and one. These maps are mutually inverse. Order the coordinates so that parents precede children; the Jacobian of \(b\mapsto x\) is triangular with diagonal entries \(\prod_{u\prec v}(1-b_u)\). Consequently
\[
\left|\frac{\partial x}{\partial b}\right|=\prod_{u\in P}(1-b_u)^{s_u-1}.
\]
Integration of this Jacobian over the open unit cube gives \(\operatorname{Vol}(\mathcal C(P))=\prod_u 1/s_u\). Dividing by the volume gives exactly the product density \(\prod_u s_u(1-b_u)^{s_u-1}\). Thus the \(B_u\) are independent \(\operatorname{Beta}(1,s_u)\) under the uniform-volume law.

**2. All mixed moments.** In the product \(\prod_vX_v^{\alpha_v}\), the factor belonging to \(B_u\) is \(B_u^{\alpha_u}(1-B_u)^{D_u}\). Independence and the elementary beta integral yield
\[
\mathbb E[B_u^p(1-B_u)^q]
=s_u\int_0^1b^p(1-b)^{s_u+q-1}\,db
=\frac{p!\,(s_u)_q}{(s_u+1)_{p+q}}.
\]
Multiplying with \(p=\alpha_u\), \(q=D_u\) gives the asserted formula for every nonnegative integral multiindex.

**3. Signs of all pairwise covariances.** Write \(\mu_v=\mathbb EX_v>0\). For an integer \(s\ge1\) put
\[
F(s)=\frac{\mathbb E(1-B)^2}{(\mathbb E(1-B))^2}
=\frac{(s+1)^2}{s(s+2)}=1+\frac{1}{s(s+2)}>1,
\quad
G(s)=\frac{\mathbb E[B(1-B)]}{\mathbb EB\,\mathbb E(1-B)}
=\frac{s+1}{s+2}<1,
\]
where \(B\sim\operatorname{Beta}(1,s)\). These are exact ratios, with no assumed independence between the chain coordinates.

If \(v,w\) are incomparable, their coordinates have common random factors only at their common strict ancestors, and hence
\[
\frac{\mathbb E[X_vX_w]}{\mu_v\mu_w}
=\prod_{u\prec v,\,u\prec w}F(s_u).
\]
When they belong to the same tree, their least common ancestor appears in this product, which is therefore strictly greater than one. For vertices in different trees the product is empty, equal to one; in fact all their underlying beta factors are disjoint.

If \(v\prec w\), the shared ancestor factors again contribute \(F\), while at \(v\) the joint product contains \(B_v(1-B_v)\). Thus
\[
\frac{\mathbb E[X_vX_w]}{\mu_v\mu_w}
=G(s_v)\prod_{u\prec v}F(s_u).
\]
List the \(h\) strict ancestors of \(v\) from its parent upward as \(u_1,\ldots,u_h\). Since \(s_{u_j}\ge s_v+j\), and \(F\) decreases strictly on the positive integers,
\[
G(s_v)\prod_{j=1}^{h}F(s_{u_j})
\le G(s_v)\prod_{j=1}^{h}F(s_v+j)
=\frac{s_v+h+1}{s_v+h+2}<1.
\]
This also covers \(h=0\) with the empty product. Interchanging \(v,w\) gives all comparable cases and proves the trichotomy.

## Verification
The accompanying pure-standard-library checker `rooted_forest_chain_moments_checker.py` reconstructs polynomial moments independently using Stanley's canonical triangulation of the order polytope, transported by the linear parent-difference transfer for a rooted forest. Within each simplex, the ordered-coordinate spacings have a uniform Dirichlet law; the checker integrates the first and second chain-coordinate moments exactly as rational numbers and compares them with the claimed beta product. Across every increasing-label rooted forest of sizes \(1\) through \(6\), it verifies the volume hook product, every first and second moment, and all pairwise covariance signs. Output from its executed test was `ROOTED_FOREST_CHAIN_MOMENTS_EXACT_PASSED 873 59602 34406 24328`, denoting forests, canonical simplices, moment comparisons, and sign comparisons. These checks do not constitute an exhaustive proof for arbitrary orders; the Jacobian and ratio arguments above provide the infinite proof.

For illustration, in the three-element rooted star (one root and two leaves), the root-to-leaf covariances equal \(-3/160\), while the leaf-to-leaf covariance is \(3/320\). This contrasts with a single three-element chain, where all distinct-coordinate covariances are \(-1/80\).

## Relationship to prior work
Stanley's construction and transfer map give the general order/chain-polytope framework. Okada and Tsuchiya, *Two enriched poset polytopes* (arXiv:2003.12271, first public March 27, 2020), present that general transfer theorem alongside enriched analogues and unimodular triangulations. Ohsugi and Tsuchiya, *Enriched chain polytopes* (arXiv:1812.02097, first public December 5, 2018), concentrate on Ehrhart and toric properties of an enriched polytope. The separate work of von Bell et al. (arXiv:2102.11306) treats volume and triangulations of generalized snake-poset order polytopes. The current result concerns a distinct quantitative feature: the complete continuous interior mixed-moment law and strict covariance-sign classification on ordinary rooted-forest chain polytopes. The hook-length volume identity, a consequence of classical linear-extension enumeration, is stated here as a check and normalization, not as a new theorem in isolation.

An earlier complete-moment formula for stable-set polytopes of complete multipartite graphs applies to some special rooted forests, notably chains and height-two rooted stars, but not to all rooted forests: a rooted tree with relations \(r<a<b\) and \(r<c\) has a comparability graph whose nonadjacency is not an equivalence relation, so it is not complete multipartite. No priority claim is made over the known transfer map, hook-length formula, or the overlapping special cases.

## Limitations
The statement requires each nonminimal element to have exactly one immediate predecessor. In a general poset, multiple predecessor chains cause the inverse denominator and Jacobian to involve maxima, and this beta product factorization and covariance-sign trichotomy are not established. The sign matrix recovers comparability and tree-component membership, not in general the rooted orientation or a uniquely labeled poset. Literature priority has not been independently adjudicated; equivalent formulations in continuous order-preserving-labeling or Dirichlet-tree probability literature are a residual risk. The finite checker does not address orders beyond six directly.

## References
1. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, DOI:10.1007/BF02187680.
2. S. Okada and A. Tsuchiya, *Two enriched poset polytopes*, arXiv:2003.12271 (first public 2020-03-27); Annals of Combinatorics 28 (2024), 257–282.
3. H. Ohsugi and A. Tsuchiya, *Enriched chain polytopes*, arXiv:1812.02097 (first public 2018-12-05); Israel Journal of Mathematics 237 (2020), 485–500.
4. M. von Bell, B. Braun, D. Hanely, K. Serhiyenko, J. Vega, A. R. Vindas-Meléndez, and M. Yip, *Triangulations, order polytopes, and generalized snake posets*, arXiv:2102.11306 (first public 2021-02-22); Combinatorial Theory 2 (2022), #10.

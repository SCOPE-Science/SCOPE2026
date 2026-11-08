# The complete diametral graph of the symmetric Stanley–Cayley lift

## Finding
Let \(P\) be a nonempty finite poset on \([d]\), let \(\mathcal L(P)\) be its linear extensions, and write \(k=|\mathcal L(P)|\). For each extension \(\sigma\), let \(\Delta_\sigma\subseteq[0,1]^d\) be Stanley's staircase simplex, and give the alternatives **equal Euclidean treatment** by forming the full one-hot Cayley lift
\[
\widehat D(P)=\operatorname{conv}\{(x,e_\sigma):x\in\Delta_\sigma,\ \sigma\in\mathcal L(P)\}\subseteq\mathbb R^{d+k}.
\]
Here \(e_\sigma\) are all \(k\) standard unit vectors; distances are the induced Euclidean distances in the affine hyperplane \(\sum_\sigma z_\sigma=1\). This orthogonal indicator model is **not** the same metric as dropping an indicator coordinate.

If \(k=1\) (equivalently, \(P\) is a chain), then \(\operatorname{diam}_2(\widehat D(P))^2=d\), with exactly one unordered diametral pair. If \(k\ge2\), then
\[
\boxed{\operatorname{diam}_2(\widehat D(P))^2=d+2.}
\]
Moreover, **every** diametral pair consists of two distinct-color lifted vertices \((\mathbf1_I,e_\sigma)\) and \((\mathbf1_{I^c},e_\tau)\), where \(\sigma\ne\tau\) and \(I\) is a union of connected components of the undirected comparability graph of \(P\); the two indicated indicator vectors must be respective staircase-simplex vertices. Conversely, all such pairs are diametral.

For every component union \(I\subseteq[d]\), put
\[
 a(I)=e(P|_I)e(P|_{I^c}),\qquad e(Q)=|\mathcal L(Q)|,\qquad e(\varnothing)=1.
\]
Then for \(k\ge2\) the exact number of unordered diametral pairs is
\[
\boxed{N(P)=k(k-1)+\frac12\sum_{\substack{I\text{ a union of comparability components}\\\varnothing\ne I\ne[d]}}a(I)^2.}
\]
The full diameter graph splits into one copy of the complete bipartite graph \(K_{k,k}\) with one perfect matching removed, and, for each unordered nontrivial complementary component-union pair \(\{I,I^c\}\), one complete bipartite graph \(K_{a(I),a(I)}\). In particular, if \(P\) is connected and not a chain, then \(N(P)=k(k-1)\); disconnectedness is detected by the presence of additional diameter-graph components. For the \(d\)-element antichain,
\[
N(P)=d!(d!-1)+\frac{(d!)^2}{2}\sum_{j=1}^{d-1}\binom dj^{-1}.
\]

## Assumptions and scope
An extension \(\sigma=(\sigma_1,\ldots,\sigma_d)\) orders smaller elements before larger ones. Its simplex is \(\Delta_\sigma=\{0\le x_{\sigma_1}\le\cdots\le x_{\sigma_d}\le1\}\), with vertices \(\mathbf1_{\{\sigma_{r+1},\ldots,\sigma_d\}}\), \(0\le r\le d\). A comparability component is a connected component of the undirected graph joining comparable elements; both empty and full unions are allowed. All posets are finite, labeled, and nonempty. The Cayley lift uses a full orthogonal indicator vector, not an arbitrary affine coordinate compression. The diameter graph has the lifted vertices as nodes and edges joining exactly diameter-attaining pairs.

## Proof
**Step 1: Vertices and sharp ambient bound.** Every lifted generating point \((\mathbf1_S,e_\sigma)\), with \(S\) a suffix of \(\sigma\), is a vertex: it is a vertex within the exposed color face \(z=e_\sigma\). These are all the vertices, since the lift is their convex hull. For any two vertices, the squared Euclidean distance is
\[
\|\mathbf1_S-\mathbf1_T\|_2^2+\|e_\sigma-e_\tau\|_2^2
=|S\triangle T|+2\mathbf1_{\sigma\ne\tau}\le d+2.
\]
If \(k\ge2\), the empty and full suffix occur in **every** simplex. Choosing the empty suffix in one color and the full suffix in another attains \(d+2\). If \(k=1\), the only color distance is zero, and the empty/full suffix attain \(d\). Strict convexity of the squared Euclidean norm implies that neither endpoint of a diametral pair can be a nonvertex: for a nontrivial convex combination, the squared distance to any fixed point is strictly below the corresponding convex combination of squared distances. Thus it suffices to classify equality among these vertices.

**Step 2: Complementarity and components.** For \(k\ge2\), equality requires \(\sigma\ne\tau\) and \(S\triangle T=[d]\), equivalently \(T=S^c\). A set is a suffix of an extension exactly when it is an upper order ideal of \(P\). If both \(S\) and \(S^c\) are upper order ideals, neither can contain one endpoint of a comparable pair without the other: if \(u<v\) and \(u\in S\), upward closure forces \(v\in S\); if \(v\in S\) and \(u\notin S\), upward closure of the complement forces \(v\notin S\). Therefore membership is constant across comparability edges and their connected components. Conversely every component union and its complement are upper order ideals, so each appears as a suffix in some linear extensions.

**Step 3: Exact count and graph.** If \(I\) is a component union, the extensions with suffix \(I\) are exactly a linear extension of \(P|_{I^c}\) followed by a linear extension of \(P|_I\); there are \(a(I)\) such choices. For \(I=\varnothing\) or \([d]\), both suffixes appear in all \(k\) extensions, and distinct colors leave precisely \(k(k-1)\) unordered pairs joining the empty and full vertices. For a nonempty proper \(I\), no extension can simultaneously have \(I\) and \(I^c\) as suffixes. Thus all \(a(I)^2\) cross pairs are valid. A pair is indexed twice, by \(I\) and \(I^c\), giving the half-sum. Distinct complementary subset pairs give disjoint vertex classes, establishing the asserted graph decomposition. For an antichain every subset is a component union and \(a(I)=|I|!(d-|I|)!\); substituting and using \(|I|!(d-|I|)!=d!/\binom d{|I|}\) yields the displayed reciprocal-binomial formula. If \(k=1\), the single chain simplex has only one complementary suffix pair, empty/full, and the squared diameter is \(d\). This proves all assertions. \(\square\)

## Verification
Run `python3 verify.py` using Python 3 and the standard library. It enumerates all 407 naturally labeled posets on at most five elements, constructs every lifted vertex, directly computes **2,996,310** squared vertex-pair distances with integer arithmetic, compares the actual diameter-pair counts with the component-extension formula, and independently checks the antichain specialization through seven elements. The exhaustive finite replay is an error check, not the proof of the all-poset theorem.

## Relationship to prior work
Qu and Lee (arXiv:2610.35668v1, first publicly submitted 2026-10-26) construct the Cayley polytope of Stanley's triangulation and determine its facet-normal lifting and compatibility behavior. The source uses an affine coordinate reduction in which one indicator is zero. The present work instead uses the fully symmetric one-hot Euclidean metric, and studies a distinct geometric invariant: the entire diameter graph. Their facet results do not imply the Euclidean distance or complement-component multiplicity formula via any stated metric-preserving transformation. Standard order-polytope facts provide the staircase-simplex vertices and the characterization of upper ideals. The pre-existing *linear extension diameter* studied by Felsner–Reuter and Brightwell–Massow is Kendall inversion distance between permutations and is a different invariant. Related published results about Euclidean diameters of partial permutohedra and preorder polytopes concern distinct vertex families.

## Limitations
The result is **metric-specific**: dropping an indicator coordinate produces an affinely equivalent Cayley polytope, but not an isometric one, and its Euclidean diameter need not equal the formula here. The diameter graph is a graph of Euclidean diameter-attaining vertex pairs, not the one-skeleton graph or the inversion metric on linear extensions. A formula in terms of numbers of linear extensions is exact but can be computationally expensive for general posets. The proof gives neither the facet description nor arbitrary weighted-color distances. Comprehensive historical priority and independent mathematical validation have not been established.

## References
1. Y. Qu and J. Lee, *On the facets of the Cayley polytope of Stanley's triangulation*, arXiv:2610.35668v1 (2026-10-26), revised v2 (2026-10-27); especially §§1–2 and the facet theorems. https://arxiv.org/abs/2610.35668
2. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23 (staircase triangulation and order ideals).
3. S. Felsner and K. Reuter, *The linear extension diameter of a poset*, SIAM J. Discrete Math. 12 (1999), 360–373 (a different permutation-inversion metric).
4. G. Brightwell and M. Massow, *Diametral pairs of linear extensions*, SIAM J. Discrete Math. 27 (2013), 634–649 (a different permutation-inversion metric).

# Four-point reconstruction from the rank spectrum of biclique partial-automorphism inverse monoids

## Finding
Let \(a,b\ge 2\), let \(G=K_{a,b}\) be the finite simple complete bipartite graph, and let \(P(G)\) be the inverse monoid of all partial bijections between vertex-induced subgraphs of \(G\) that preserve both adjacency and nonadjacency. Define \(c_k(G)\) to be the number of elements with domain size \(k\), including the empty map.

**Sharp four-point reconstruction theorem.** The three integers \(c_1(G),c_2(G),c_4(G)\) determine the unordered pair \(\{a,b\}\), hence the isomorphism type of \(G\). In contrast, \(c_3(G)\) is already determined by \(c_1(G)\) and \(c_2(G)\), and for each integer \(h\ge2\), the nonisomorphic graphs
\[
K_{h^2,h^2}\quad\text{and}\quad K_{h^2-h,h^2+h}
\]
have identical counts \(c_k\) for \(0\le k\le3\), but different \(c_4\). Thus the threshold of rank four is sharp for this family of inverse monoids.

More explicitly, write \(n=a+b\), \(m=ab\), \(K=\binom n2\), \(t=m-K/2\). Then
\[
\begin{aligned}
c_0&=1,\quad c_1=n^2,\\
c_2&=K^2+4t^2,\\
c_3&=\frac{(n-2)^2}{2}\left(c_2-\frac23K^2\right).
\end{aligned}
\]
For any two candidate products \(m\) and \(K-m\) associated with actual bipartitions of the same \(n\),
\[
c_4(n,m)-c_4(n,K-m)
=\frac23(n-2)t\left(8t^2-n(n-1)\right).
\]
The right-hand side is nonzero whenever the two candidate products differ. Accordingly \(c_4\) resolves the only ambiguity left by \(c_2\).

For all \(2\le k\le n\), the complete rank spectrum is given by
\[
\begin{aligned}
c_k={}&k!U_k^2+
\sum_{\substack{1\le i<j\\i+j=k}}
i!j!V_{ij}^2
+\mathbf1_{2\mid k}\,2\bigl((k/2)!\bigr)^2 W_{k/2}^2,\\
U_k={}&\binom ak+\binom bk,\\
V_{ij}={}&\binom ai\binom bj+\binom aj\binom bi,\\
W_i={}&\binom ai\binom bi.
\end{aligned}
\]
Here binomial coefficients are zero outside their usual range; \(c_0=1\) and \(c_1=n^2\) are stated separately.

## Assumptions and scope
All graphs are finite, undirected, simple and uncoloured, and the bipartition is **not** marked. A partial automorphism means an induced-subgraph isomorphism, not merely an injective graph homomorphism, and its rank is its domain cardinality. The result applies to integers \(a,b\ge2\); no group action or distinguished side is supplied to the reconstruction. It concerns *numbers* of partial automorphisms by rank, not knowledge of the partial automorphisms themselves. Inverse-monoid composition and inversion are the usual operations on partial bijections.

## Proof
**1. Exact rank enumeration.** Each induced subgraph on \(k\ge2\) vertices is either an independent set or a complete bipartite graph with both sides nonempty. There are \(U_k\) induced independent \(k\)-sets. All such sets are mutually isomorphic and their induced automorphism group has order \(k!\), giving \(k!U_k^2\) partial isomorphisms. When the nonempty side sizes are distinct, \(i<j\), there are \(V_{ij}\) induced copies of \(K_{i,j}\); its automorphism group has order \(i!j!\), giving the middle summand. For equal positive side sizes \(i=j\) there are \(W_i\) induced copies and the automorphism group has order \(2(i!)^2\), giving the final summand. The induced-subgraph types are disjoint, so the sum is exact. The empty map and arbitrary singleton-to-singleton maps give \(c_0=1\), \(c_1=n^2\).

**2. What ranks two and three see.** Put \(K=\binom n2\) and \(m=ab\). Exactly \(m\) unordered pairs are edges and \(K-m\) are nonedges. Both two-vertex induced graphs have automorphism order two, so \(c_2=2(m^2+(K-m)^2)=K^2+4(m-K/2)^2\). Hence \(c_1\) gives the integer \(n\), while \(c_2\) gives \(m\) only up to reflection about \(K/2\).

There are \(T=m(n-2)/2\) induced three-vertex paths and \(E=\binom n3-T\) independent triples. Their automorphism-group orders are two and six, respectively. Thus \(c_3=2T^2+6E^2\), which simplifies to the displayed expression depending only on \(n\) and \(c_2\). In particular, rank three cannot break the rank-two ambiguity.

**3. Rank-four separation.** The three induced four-vertex types are an independent set, a star with one vertex on one side and three on the other, and a four-cycle with two vertices on each side. Their respective induced automorphism-group orders are \(24,6,8\). Their counts as functions of \(n,m\) are
\[
\begin{aligned}
U_4(n,m)&=\frac{n^4-6n^3+11n^2-6n-4mn^2+18mn-22m+2m^2}{24},\\
V_{13}(n,m)&=\frac{m(n^2-3n+4-2m)}{6},\\
W_2(n,m)&=\frac{m(m-n+1)}4.
\end{aligned}
\]
Therefore \(c_4(n,m)=24U_4(n,m)^2+6V_{13}(n,m)^2+8W_2(n,m)^2\). Direct polynomial expansion and factoring gives
\[
c_4(n,m)-c_4(n,K-m)=\frac{2}{3}(n-2)t\left(8t^2-n(n-1)\right),\qquad t=m-K/2.
\]
Suppose both \(m\) and its reflected candidate \(K-m\) arise as products of two nonnegative integers summing to \(n\). Both products are at most \(n^2/4\); their average is \(K/2=n(n-1)/4\). Therefore \(|t|\le n/4\). As \(n\ge4\),
\[
8t^2\le n^2/2<n(n-1),
\]
and the quadratic factor cannot vanish. The difference can be zero only when \(t=0\), in which case both candidate products already coincide. Thus \(c_4\) distinguishes every genuinely different candidate product. From the resulting \(m\), the pair \(\{a,b\}\) consists of the integer roots of \(X^2-nX+m=0\).

**4. Infinite sharpness.** Let \(h\ge2\) and put \(n=2h^2\). The products for the pairs \((h^2,h^2)\) and \((h^2-h,h^2+h)\) are \(h^4\) and \(h^4-h^2\), respectively, whose sum is \(\binom n2\). Rank-two counts agree by reflection, rank-three counts agree by Step 2, and ranks zero and one depend only on \(n\). But the two products differ, so Step 3 makes the rank-four counts unequal. These graphs are nonisomorphic because their bipartition sizes differ. This proves sharpness.

## Verification
The accompanying Python 3 program `verify_partial_biclique.py` uses only the standard library. It directly enumerates every induced-subgraph isomorphism of domain rank at most four for five small bicliques, without using the classification formula for its enumeration; it separately computes the formula and compares the results. It also certifies the rank-three and rank-four polynomial identities by exact rational evaluation on interpolation grids whose dimensions exceed their coordinate degrees. It checks the infinite sharpness-family formula numerically for integer parameters \(2\le h<20\), and checks rank-one/two/four reconstruction for all \(4\le n<100\), subject to \(a,b\ge2\). These finite tests support, but do not replace, the symbolic proof.

As a worked instance, \(K_{4,4}\) and \(K_{2,6}\) both have ranks-zero-through-three counts \((1,64,800,4992)\). Their rank-four counts are \(16608\) and \(16800\), respectively.

## Relationship to prior work
Jajcay, Jajcayová, Szakács and Szendrei (2018, revised 2020) introduce the inverse monoid of graph partial automorphisms and show that the *actual maps* of rank at most two determine the entire monoid inside a fixed symmetric inverse monoid. Their result does not say that the mere **cardinalities** of the rank-one and rank-two strata determine the graph: the sharpness family above shows the distinction. Their groupoid/Green-class connection between induced subgraph types and partial automorphisms underlies the rank enumeration here.

Separate published work on homogeneous-graph partial-automorphism rank spectra includes balanced disjoint-union-of-cliques cases, while work on multipartite partial isometries counts square-zero or nilpotent submonoids. The present statement concerns the *unrestricted* inverse monoid of each (including unbalanced) biclique, and the sharp threshold for inverse reconstruction from three rank cardinalities. The publicly indexed descriptions of the latter works were checked but their full repository texts could not be retrieved for a conclusive whole-document exclusion.

## Limitations
The theorem does not assert reconstruction of arbitrary graphs, arbitrary multipartite graphs, or an unlabelled inverse monoid from arbitrary finite numerical summaries. It uses the known prior assumption that the object is a complete bipartite graph with both sides of size at least two. It is a same-model mathematical argument corroborated by finite tests, not independently audited. The search for prior equivalent formulations is necessarily incomplete, particularly for relevant repository materials whose full texts were not accessible.

## References
1. R. Jajcay, T. Jajcayová, N. Szakács, M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422, first version 2018-09-12, revised 2020-02-11, published *Journal of Algebraic Combinatorics* **53** (2021), 829–849. https://arxiv.org/abs/1809.04422
2. *Rank spectra and Gaussian deficiency laws for finite homogeneous graph partial automorphisms*, published repository record, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-rank-spectra-and-gaussian-deficiency-laws-for-finite-homogeneous--cd9dfc7a9f4c
3. *The complete square-zero rank distribution of multipartite partial-isometry monoids*, published repository record, 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-the-complete-square-zero-rank-distribution-of-multipartite-parti--aab2f4eae4e5
